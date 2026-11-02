# Methodology

## The bandwidth model

Decode (token generation) is memory-bandwidth-bound: each token requires reading
the active weights out of memory once. So:

```
tokens/sec ≈ (bandwidth × efficiency) / bytes read per token
```

Efficiency is the fraction of theoretical bandwidth actually achieved. On the DGX
Spark it measures at roughly 60%, and that calibration reproduces published
results closely:

| Model | Active params | Bytes/token | Predicted | Measured |
|---|---|---|---|---|
| gpt-oss-20b MXFP4 | ~3.6B | ~1.9 GB | 86 | 86.2 |
| gpt-oss-120b MXFP4 | ~5.1B | ~2.7 GB | 61 | 60.6 |
| Qwen 32B dense Q4 | 32B | ~16.5 GB | 10 | ~8 |
| Llama 70B dense Q4 | 70B | ~36 GB | 4.6 | 2.7–5 |

**Where the model fails.** It overestimates very large MoE models. Measured EXO
figures on M3 Ultra hardware imply a single M5 Ultra runs DeepSeek 671B at about
31 tok/s and Qwen3 235B at about 29, where the bandwidth arithmetic alone
predicted 48 and 50 to 80. The likely cause is that expert routing scatters
memory access in a way sequential weight reads do not. Large-MoE figures in the
page are measurement-derived, not model-derived.

## Active versus total parameters

This is the single most important distinction in the analysis.

A dense model reads all its parameters per token. A mixture-of-experts model
replaces each layer's feed-forward network with N parallel copies plus a router,
and activates only k of them per token, per layer. Attention, embeddings, norms,
and the routers themselves always run.

So an MoE's resource profile is:

- **Capacity** proportional to *total* parameters (all experts must be resident,
  because routing is dynamic per token and cannot be predicted ahead)
- **Bandwidth** proportional to *active* parameters

gpt-oss-120b is 117B total and 5.1B active, a sparsity ratio of 23x. This is why
it runs faster than a 32B dense model on the same hardware, and why
capacity-rich, bandwidth-poor machines suit it.

Note that `8x7B`-style naming is misleading: Mixtral 8x7B has 46.7B parameters,
not 56B, because only the FFN is replicated and attention is shared.

## Context depth

Every headline tokens/sec figure is a depth-zero figure. Context imposes three
separate costs:

1. **KV cache memory.** Computed from published architectures as
   `2 × layers × KV heads × head dim × bytes`. Roughly 0.32 MB/token for a
   Llama-class 70B and 0.26 MB for a 32B. gpt-oss-120b needs only about
   0.036 MB/token: it uses grouped-query attention, and only half of its 36
   layers use full attention. The other half keep a 128-token sliding window,
   so their cache does not grow with context
2. **Prefill time.** Context ÷ prefill rate at that depth
3. **Decode decay.** Attention reads the entire cache on every token generated

The Spark's depth curve is measured: 60.57 tok/s decode at depth 0 falling to
40.55 at 32K, and 1,956 tok/s prefill falling to 1,027. Other columns apply the
same shape, because the decay is a property of the KV-to-weights ratio rather
than of the machine.

**MoE models slow down more with context than dense models do**, because the
cache adds to a small number: the *active* parameters. gpt-oss-120b reads
~2.7 GB of weights per token and ~1.2 GB of cache at 32K, so its memory traffic
per token rises about 45%. That predicts a decode loss of about 31%, close to
the 33% measured on the Spark. A dense 70B reads ~36 GB of weights and ~10.5 GB
of cache at 32K, a rise of about 29%, so it loses about a fifth of its speed.

## Which figures are measured

**Measured:**

- DGX Spark gpt-oss figures, from the llama.cpp benchmark discussion
- RTX 3090 and RTX PRO 6000 figures, from published llama.cpp and Ollama runs
- M5 Max figures at 614 GB/s, including gpt-oss-120b Q8 at 87.9 tok/s decode and
  1,325 tok/s prefill
- Mac cluster scaling on four M3 Ultra Studios at 819 GB/s
- Radeon AI PRO R9700 single-card llama.cpp results

**Derived:**

- All M5 Ultra figures, scaled from M5 Max by the 1.95x bandwidth ratio (the
  Ultra is two Max dies). Apple's claimed 4.3x AI compute over M3 Ultra suggests
  prefill could beat these estimates
- RTX 5090 figures, taken from RTX PRO 6000 measurements, since both use the
  GB202 die at the full 1,792 GB/s
- Two-Spark cluster throughput, inferred from the interconnect rather than
  benchmarked (see below)
- R9700 dual-card figures, assuming layer splitting

## Structural caveats

**Dual-GPU speeds assume llama.cpp layer splitting**, where cards work
sequentially and effective bandwidth stays at a single card's rate. You buy
capacity, not speed. vLLM tensor parallelism reaches roughly 1.4 to 1.6x that,
with a more fragile setup.

**Two-Spark figures are an assumption, not a measurement.** Under pipeline
parallelism each layer still executes once, which yields capacity without
throughput. NVIDIA has published nothing comparable to Apple's four-node numbers.
Since EXO gains on Macs specifically by distributing expert weights so each node
reads less memory per token, a Spark cluster running comparable expert
parallelism over RDMA could plausibly do the same. Treat the flat figure as
conservative and untested.

**Multi-Mac figures require specific software.** macOS Tahoe 26.2 for the
Thunderbolt 5 RDMA driver, and EXO as the runtime. They do not apply to
llama.cpp, which scales negatively across nodes.

**Apple-silicon batching and prefix caching** assume the community `vllm-mlx`
server rather than `mlx-lm` or llama.cpp.

## Prices

Delivered cost, meaning street price plus about 11% sales tax, applied to every
configuration so that they compare fairly. Substitute your own rate.

GPU configurations also include a host PC, priced before tax at about $500 for a
single-card build, $600 for a dual-card build and $1,500 for the RTX PRO 6000
workstation. Unified-memory machines (Spark, Mac) need no host.

These are asking prices, not completed sales, and they were wrong twice during
this analysis. The lesson recorded in `corrections.md`: do not extrapolate a
vendor's published memory-upgrade rate linearly. Apple charges $25/GB for the
first 160 GB above its base configuration and $45/GB for the next 256 GB.
