# How this analysis was built

A reconstruction of the question-by-question thread the page came from, written
from the working session rather than exported verbatim. It is a record of the
reasoning path, not a transcript.

The original question was narrow: how do you wire a DGX Spark into a Windows 11
plus WSL2 development setup? The scope grew every time an answer turned out to
depend on something that had not been checked.

---

## 1. Setup and networking

**Q:** How do I configure a DGX Spark to serve models to both Claude Desktop on
Windows and Claude Code in WSL2? Network, vLLM or llama.cpp, model loading.

Treat the Spark as a headless Linux server on the LAN. The useful finding was a
WSL2-specific trap: default NAT networking cannot resolve mDNS, so `spark.local`
resolves from PowerShell and fails in WSL2. Fixing it globally:

```ini
# %USERPROFILE%\.wslconfig
[wsl2]
networkingMode=mirrored
dnsTunneling=true
autoProxy=true
```

Mirrored mode makes WSL2 share the Windows network stack, so `.local` names, LAN
IPs, and localhost forwarding behave identically on both sides.

Ports: 10GbE RJ45 for the LAN. The two QSFP 200GbE ConnectX-7 ports are for
Spark-to-Spark RDMA, not for talking to a workstation.

Two GB10-specific traps worth recording: FP4 lacks native compute on `sm_121`, so
NVFP4 MoE layers fall back to Marlin (confirm `Using 'MARLIN' NvFp4 MoE backend`
in the logs or output is literal `!!!!`); and vLLM preallocates one KV pool out of
the shared 128 GB, so `--gpu-memory-utilization 0.85` takes ~76 GB from the CPU
side.

---

## 2. GB10 versus RTX PRO 6000

**Q:** How does a GB10 compare to what's in an RTX PRO 6000?

Same architecture generation, roughly 4x apart in GPU scale and 6.5x in
bandwidth. GB10 is 48 SMs and 6,144 CUDA cores at 273 GB/s; GB202 is 188 SMs and
24,064 cores at 1,792 GB/s. Different compute capabilities (`sm_121` vs `sm_120`),
which matters for prebuilt wheels.

---

## 3. Perceived throughput

**Q:** Quantitatively, what tok/s? Qualitatively, what does the difference feel
like?

The framing that mattered: in agentic work you are not reading the stream. The
model emits reasoning, tool calls, and diffs, and you wait for the whole turn. A
3,000-token response at 20 tok/s is 150 seconds; at 150 tok/s it is 20. Across
20 to 30 turns that is 45 minutes against 6.

---

## 4. Why the Spark looked backwards

**Q:** Re-explain why the Spark handles larger models better than smaller ones.

It does not, and the premise needed dismantling. See `corrections.md` #11. The
real content: decode speed tracks *active* parameters, MoE models have few, and
unified memory removes the offload cliff rather than adding speed.

---

## 5. MoE versus dense

**Q:** Is an MoE really a bunch of smaller models packed together, one of which
answers the prompt?

Wrong at three levels, and the corrections are the useful part:

- **Not model-level.** Only the feed-forward sublayer is replicated. Attention,
  embeddings, and norms are shared. Mixtral 8x7B has 46.7B parameters, not 56B.
- **Not one expert, not per prompt.** Routing is top-k (4 of 128 for
  gpt-oss-120b) and happens independently at every layer for every token. A
  36-layer model makes 36 routing decisions per token.
- **Experts are not topic specialists.** Routing is learned end to end with no
  supervision; what emerges clusters around token-level and syntactic patterns.
  The name is inherited from a 1991 paper and is misleading.

---

## 6. Industry direction

**Q:** Dense or MoE? Larger, or better-trained?

MoE has won at the frontier and is getting sparser: Mixtral 8x7B was 3.6x sparse
in early 2024; Kimi K2.5 is 31x. Dense survives below about 30B, where
decoupling capacity from compute stops paying.

Three axes move at different speeds: total parameters still growing, **active
parameters roughly flat at 13–40B for two years**, and training compute per
parameter sharply up. The marginal compute dollar moved to post-training RL and
to inference-time compute.

The consequence for hardware: flat active parameters mean decode speed for a
given model class will not get worse, but the shift to inference-time scaling
penalizes low-bandwidth machines, because reasoning models emit thousands of
thinking tokens before answering.

---

## 7. Software stacks

**Q:** What are the stack differences, and do they change the hardware choice?

Four worlds: CUDA x86, CUDA aarch64, Metal/MLX, ROCm. The reassuring constant is
that all of them expose an OpenAI-compatible HTTP endpoint, so the client side is
identical regardless of what you buy. The stack determines what runs on the box,
not how you reach it.

Three conclusions changed the ranking: the Spark's CUDA claim is narrower than it
sounds (`corrections.md` #10), the Mac is an excellent inference appliance and a
poor development platform, and AMD's software was weaker than its specs — later
partially corrected (`corrections.md` #6).

---

## 8. A reader correction on MLX portability

**Q:** Does "MLX is Apple-only" mean I can't use Python MLX libraries from WSL2 to
talk to the Mac?

No, and the question exposed a conflation worth recording. MLX is a compute
framework that executes where it runs; it is not a client library. You reach a
Mac the same way you reach a Spark: `pip install openai` and a base URL. The
article's point was about portability of MLX *code* to GPU servers, and MLX has
since gained a CUDA backend anyway.

The weights conversion is also less of an obstacle than it reads: `mlx_lm.convert`
is one command, and `mlx-community` hosts thousands of pre-converted models. The
real constraint is architecture support, not file format, which is the same class
of problem as llama.cpp needing a PR for a novel architecture.

---

## 9. Reader corrections on price

**Three separate rounds**, each one catching figures that were wrong:

1. Launch-era MSRPs instead of street prices (`corrections.md` #1)
2. Base-bin pre-tax Mac pricing against a real configurator session
   (`corrections.md` #4)
3. An October repricing wave that moved several conclusions

The habit that came out of it: a single delivered-cost basis, with change-since
columns, and explicit "measured / derived / assumed" labels.

---

## 10. Context as a first-class criterion

**Q:** Context matters across all of these. Add it to the evaluation.

This produced the most useful section in the page. One vague "long-context
headroom" row became three measured costs: KV cache capacity, time to first
token, and permanent decode decay. See `methodology.md`.

---

## 11. A reader correction on table structure

**Q:** Your clustering table mixes apples and oranges.

Correct, and the fix generalized. See `corrections.md` #9. The principle carried
forward: hold the conditions fixed within a table, vary one thing, and put
inferred numbers somewhere that says they are inferred.

This is also why the AMD card later got its own comparison table against the
other discrete GPUs rather than a column in the main matrix.

---

## 12. Repricing and additions

Later rounds added the 256 GB and 512 GB M5 Ultra configurations, their dual-Mac
clusters, the DGX Spark 64 GB SKU, and the Radeon AI PRO R9700, and repriced
everything twice as the shortage deepened.

The clustering research turned up the single most surprising measurement in the
project: on identical Mac hardware over the same interconnect, EXO with RDMA
gains 34% on two nodes while llama.cpp loses 16%. The runtime decides whether a
second machine helps at all.
