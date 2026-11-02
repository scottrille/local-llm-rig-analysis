# Sources

Grouped by topic. All were consulted between 28 August and 1 November 2026.
Figures from these sources are cited, not reproduced wholesale; check the
original before quoting numbers.

## Benchmarks: measured performance

- [Performance of llama.cpp on NVIDIA DGX Spark](https://github.com/ggml-org/llama.cpp/discussions/16578) — the primary Spark source, including the depth curve (gpt-oss-120b tg32 from 60.57 at depth 0 to 40.55 at 32K, pp2048 from 1,956 to 1,027)
- [Local LLM benchmarks on RTX PRO 6000 Blackwell](https://www.vaditaslim.com/blog/ai/local-llm-benchmarks-rtx-pro-6000) — eight models, pp512 and tg128
- [sglang LLM inference: RTX Pro 6000 vs DGX Spark](https://github.com/casualcomputer/rtx_pro_6000_vs_dgx_spark) — six architectures, batch sizes 1 to 32
- [Apple M5 Max for local LLMs: first benchmarks](https://www.hardware-corner.net/m5-max-local-llm-benchmarks-20261233/) — the M5 Max basis for the M5 Ultra extrapolations
- [gpt-oss-120b on M5 Ultra (80c), oMLX benchmark](https://omlx.ai/benchmarks/performance/dx5x4yhw) — 110.1 tok/s decode on a 256 GB machine, 24 Sep 2026
- [Apple silicon LLM benchmarks, LLMCheck](https://llmcheck.net/benchmarks) — collected M5 Ultra measurements, including gpt-oss-120b at 120 tok/s (96 at 32K) and gpt-oss-20b at 184
- [M5 Ultra LLM benchmarks, fireside-labs](https://github.com/fireside-labs/m5-ultra-llm-benchmarks) — an owner's 30-core CPU / 64-core GPU, 256 GB machine, which confirms that the bin is sold at 256 GB
- [LLM tokens/sec benchmarks 2026: RTX 4090 vs 3090](https://mustafa.net/llm-tokens-per-second-benchmarks/) — RTX 3090 dense figures
- [Why DGX Spark runs 70B LLMs at 2.7 tokens/s](https://www.mayhemcode.com/2026/08/why-dgx-spark-runs-70b-llms-at-27.html)
- [Strix Halo guide: benchmarks, hogeheer499-commits](https://github.com/hogeheer499-commits/strix-halo-guide/blob/main/BENCHMARKS.md) — gpt-oss-120b MXFP4 on Vulkan at 55.6 tok/s, and prefill from 729 tok/s on a 2K prompt to 478 on a 32K prompt (Beelink GTR9 Pro, 128 GB)
- [Strix Halo LLM performance, visorcraft](https://github.com/visorcraft/strix-halo-llm-perf) — Llama 3.1 70B Q4 at 5.1 tok/s, Qwen2.5 32B at 11.3, 14B at 24.5, 7B at 47.3, and Qwen3 235B at Q3_K_M at 17.2
- [Strix Halo GPU LLM performance tests, Framework community](https://community.frame.work/t/amd-strix-halo-ryzen-ai-max-395-gpu-llm-performance-tests/72521) — gpt-oss-20b at 77.3 tok/s and gpt-oss-120b at 54.8 on Vulkan
- [Strix Halo LLM inference notes, Level1Techs](https://forum.level1techs.com/t/strix-halo-llm-inference-notes/249466) — ROCm versus Vulkan on gpt-oss and a 70B dense model
- [Radeon AI PRO R9700 for local AI in 2026](https://runaihome.com/blog/amd-radeon-ai-pro-r9700-local-ai-hardware-guide-2026/) — R9700 measured llama.cpp results and street pricing
- [AMD Radeon AI PRO R9700 dual-GPU AI inference performance, Puget Systems](https://www.pugetsystems.com/labs/articles/amd-radeon-ai-pro-r9700-dual-gpu-ai-inference-performance/)
- [AMD Radeon AI PRO R9700 Linux performance, Phoronix](https://www.phoronix.com/review/amd-radeon-ai-pro-r9700)

## Architecture

- [Analyzing Nvidia GB10's GPU, Chips and Cheese](https://chipsandcheese.com/p/analyzing-nvidia-gb10s-gpu) — 48 SMs, 24 MB L2, compute capability 12.1, and the measured bandwidth picture
- [NVIDIA dissects GB10 Superchip, TechPowerUp](https://www.techpowerup.com/340385/nvidia-dissects-gb10-superchip-soc-with-20-cpu-cores-and-6-144-cuda-gpu-cores)
- [RTX PRO 6000 Blackwell Workstation Edition, NVIDIA](https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000/)
- [Mac Studio technical specifications, Apple](https://www.apple.com/mac-studio/specs/) — confirms both M5 Ultra GPU bins run at 1,200 GB/s
- [Radeon AI PRO R9700 specifications, fitmyllm](https://www.fitmyllm.com/gpu/radeon-ai-pro-r9700)

## Clustering

- [RDMA over Thunderbolt 5 for Mac clusters, AppleInsider](https://appleinsider.com/articles/25/12/20/ai-calculations-on-mac-cluster-gets-a-big-boost-from-new-rdma-support-on-thunderbolt-5) — the four-node EXO vs llama.cpp scaling figures
- [Explore distributed inference and training with MLX, WWDC26](https://developer.apple.com/videos/play/wwdc2026/233/)
- [Running DeepSeek V3 671B on a Mac cluster, EXO Labs](https://blog.exolabs.net/day-2/)
- [exo, exo-explore on GitHub](https://github.com/exo-explore/exo) — maintainer, Apache 2.0 license, tensor parallelism over RDMA, MLX backend
- [1.5 TB of VRAM on Mac Studio: RDMA over Thunderbolt 5, Jeff Geerling](https://jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5) — EXO versus llama.cpp RPC, and the RDMA latency drop from ~300 to under 50 microseconds
- [Apple's MLX turns four Macs into a trillion-parameter cluster, AlphaSignal](https://alphasignal.ai/news/apple-s-mlx-turns-four-macs-into-a-trillion-parameter-cluster) — JACCL at 50–60 Gb/s over Thunderbolt 5
- [vLLM 0.17.0 MXFP4 patches for DGX Spark, NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/vllm-0-17-0-mxfp4-patches-for-dgx-spark-qwen3-5-35b-a3b-70-tok-s-gpt-oss-120b-80-tok-s-tp-2/362824) — gpt-oss-120b on two Sparks with TP=2: 51.82 tok/s stock, 80.88 patched
- [Running gpt-oss-120b on a single DGX Spark, Conselara](https://conselara.dev/notes/gpt-oss-120b-single-dgx-spark/) — one Spark at 37–39 tok/s on the stock NGC vLLM, 59–63 with a community fork
- [Two DGX Sparks linked: setup and measured speeds](https://eurokommerz.at/blog/dgx-spark-two-nodes-and-beyond-llms/) — NVIDIA's Qwen3 235B NVFP4 TensorRT-LLM figure (11.73 tok/s, TP=2) and the ~190 Gb/s RDMA link test
- [Two NVIDIA DGX Sparks, three open models, Techstrong.ai](https://techstrong.ai/features/two-nvidia-dgx-sparks-three-open-models-and-the-benchmark-that-misled-us/) — 1.71x single-stream scaling with TP=2 (model not stated), and ConnectX-7 throughput

## Software stacks

- [llama.cpp vs MLX vs Ollama vs vLLM on Apple Silicon 2026](https://contracollective.com/blog/llama-cpp-vs-mlx-ollama-vllm-apple-silicon-2026) — the 20–40% MLX advantage over llama.cpp, and the feature-gap matrix
- [mlx-lm, ml-explore](https://github.com/ml-explore/mlx-lm) — conversion, serving, `mx.distributed`
- [vllm-mlx](https://github.com/waybarrios/vllm-mlx) — continuous batching, paged KV cache, prefix caching, and an Anthropic `/v1/messages` endpoint on Apple silicon
- [Apple's MLX framework gains CUDA backend support](https://biggo.com/news/202507150712_MLX_CUDA_Backend_Support)
- [Strix Halo software status, llm-tracker.info](https://llm-tracker.info/_TOORG/Strix-Halo) — the Vulkan-beats-ROCm finding on `gfx1151`
- [AMD Strix Halo system optimization, ROCm docs](https://rocmdocs.amd.com/en/develop/how-to/system-optimization/strixhalo.html)
- [DGX Spark + vLLM playbook](https://vlaicu.io/posts/dgx-vllm-playbook/) — the Marlin MoE fallback and KV pool behavior
- [Run models with llama.cpp on DGX Spark](https://build.nvidia.com/spark/llama-cpp)
- [Set up local network access, DGX Spark](https://build.nvidia.com/spark/connect-to-your-spark)
- [Nvidia says it's more than doubled the DGX Spark's performance since launch, The Register](https://www.theregister.com/2026/01/05/nvidia_dgx_spark_speed/) — 2.5x software gains, concentrated in prefill

## Pricing

- [NVIDIA GPU price report, August 2026](https://www.buysellram.com/blog/nvidia-consumer-gpu-price-report-august-2026/)
- [NVIDIA consumer GPU market update, October 2026](https://www.buysellram.com/blog/nvidia-consumer-gpu-market-update/) — the 60–64% RTX 5090 rise and used-above-new inversion
- [Nvidia doubles RTX PRO 6000 Blackwell's MSRP to $16,000, Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year)
- [NVIDIA RTX PRO 6000 Blackwell pricing, Thunder Compute](https://www.thundercompute.com/blog/nvidia-rtx-pro-6000-pricing)
- [DGX Spark gets $700 price hike as memory shortages bite, Tom's Hardware](https://www.tomshardware.com/desktops/mini-pcs/nvidia-dgx-spark-gets-18-percent-price-increase-as-memory-shortages-bite-founders-edition-now-usd4-699-up-from-usd3-999)
- [DGX Spark 64GB launched and big 128GB GB10 price increases, ServeTheHome](https://www.servethehome.com/nvidia-dgx-spark-64gb-launched-and-big-128gb-gb10-price-increases/)
- [DGX Spark 64GB arrives at $4,999 as the 128GB model jumps to $6,950, Hardware Busters](https://hwbusters.com/news/nvidia-dgx-spark-64gb-arrives-at-4999-as-the-128gb-model-jumps-to-6950/)
- [Apple announces the M5 Ultra Mac Studio, Macworld](https://www.macworld.com/article/3220024/apple-announces-the-m5-ultra-mac-studio-with-up-to-512gb-of-ram.html)
- [Apple isn't taking pre-orders for every M5 Ultra configuration, AppleInsider](https://appleinsider.com/articles/26/08/25/you-can-spend-18299-on-a-mac-studio-today-or-more-in-october) — the configuration ladder
- [Mac Studio with M5 Ultra now available with 512GB RAM for $22,299, MacRumors](https://www.macrumors.com/2026/10/28/mac-studio-m5-ultra-512gb-ram/)
- [Apple's 512GB Mac Studio RAM upgrade now costs $15,500, iDrop News](https://www.idropnews.com/news/apple-512gb-m5-ultra-mac-studio-upgrade-cost/270296)
- [AMD officially prices Radeon AI PRO R9700 at $1,299, WCCFtech](https://wccftech.com/amd-officially-launches-radeon-ai-pro-r9700-at-1299/)
- [Used Radeon AI PRO R9700 listings, GPUpoet](https://gpupoet.com/gpu/shop/amd-radeon-ai-pro-r9700)
- [Ryzen AI Max+ 395 mini PC comparison, ComputingForGeeks](https://computingforgeeks.com/ryzen-ai-max-395-mini-pc-comparison/) — 128 GB Strix Halo mini PCs at $3,449 to $3,649 in October 2026
- [GMKtec EVO-X2 (128GB) price and specs, AI Gear Watch](https://aigearwatch.com/hardware/gmktec-evo-x2-128gb/)
- [AMD's Ryzen AI Halo launches with 128GB at $3,999, TweakTown](https://www.tweaktown.com/news/112183/amds-ryzen-ai-halo-ai-mini-pc-launches-in-the-us-with-128gb-memory-and-a-dollars3999-price-tag/index.html)
- [Ryzen AI Halo with Max+ PRO 495 launches at $7,299 with 192GB, VideoCardz](https://videocardz.com/newz/amd-ryzen-ai-halo-with-ryzen-ai-max-pro-495-launches-at-7299-with-192gb-memory)
- [AMD Gorgon Halo PCs span $6,799 to $9,249, Shattered](https://shattered.io/amd-gorgon-halo-pcs-pricing-6799-9249-2026/)
- [Increasing the VRAM allocation on AMD AI APUs under Linux, Jeff Geerling](https://www.jeffgeerling.com/blog/2025/increasing-vram-allocation-on-amd-ai-apus-under-linux/)
- [SSD price index](https://cheapestssd.com/ssd-price-index/) — NAND trend and $/TB, as of August 2026

## Roadmap

- [Nvidia CEO confirms GB10 and N1/N1X are identical silicon, Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/nvidia-ceo-huang-says-upcoming-dgx-spark-systems-are-powered-by-n1-silicon-confirms-gb10-superchip-and-n1-n1x-socs-are-identical)
- [N1X/N1 laptops this quarter, N2 in Q3 2027, VideoCardz](https://videocardz.com/newz/nvidia-n1x-n1-laptops-to-debut-this-quarter-n2-series-in-q3-2027)
- [Ryzen AI Max 400 'Gorgon Halo' packs up to 192GB, Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/amd-ryzen-ai-max-400-gorgon-halo-packs-up-to-192gb-of-unified-memory-refreshed-apu-uses-zen-5-and-rdna-3-5-and-can-clock-up-to-5-2-ghz)
- [AMD's Medusa Halo APUs could use LPDDR6, Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/amds-future-medusa-halo-apus-could-use-lpddr6-ram-new-leak-suggests-ryzen-ai-max-500-series-could-have-80-percent-more-memory-bandwidth) — 461 to 691 GB/s, leaked and unconfirmed
- [Apple overhauls chip roadmap, ditches M6 Pro and Max for M7, TechRepublic](https://www.techrepublic.com/article/news-apple-m6-m7-ai-mac-roadmap/) — M7 Ultra Mac Studio not expected until 2028

## Model landscape

- [LLM Releases tracker](https://www.llm-releases.com/)
- [Every open-weight AI model worth running in 2026](https://joshuaschultz.com/cheatsheets/open-weight-models-2026/) — total vs active parameter counts
- [Scaling RL: 2025 roundup and 2026 lookout](https://charlottexia.substack.com/p/scaling-rl-2025-roundup-and-2026)

## Storage

- [Best Thunderbolt 5 SSD enclosures: DIY vs prebuilt](https://fixoryhq.com/en/best-thunderbolt5-ssd-enclosures-guide/) — enclosure models, the JHL9480 controller, and the Gen 5 warning
- [OWC Thunderbolt 5 storage solutions](https://www.owc.com/solutions/thunderbolt-5)
