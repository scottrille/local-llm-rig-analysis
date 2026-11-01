# Sources

Grouped by topic. All were consulted between 28 August and 1 November 2026.
Figures from these sources are cited, not reproduced wholesale; check the
original before quoting numbers.

## Benchmarks: measured performance

- [Performance of llama.cpp on NVIDIA DGX Spark](https://github.com/ggml-org/llama.cpp/discussions/16578) — the primary Spark source, including the depth curve (gpt-oss-120b tg32 from 60.57 at depth 0 to 40.55 at 32K, pp2048 from 1,956 to 1,027)
- [Local LLM benchmarks on RTX PRO 6000 Blackwell](https://www.vaditaslim.com/blog/local-llm-benchmarks-rtx-pro-6000) — eight models, pp512 and tg128
- [sglang LLM inference: RTX Pro 6000 vs DGX Spark](https://github.com/casualcomputer/rtx_pro_6000_vs_dgx_spark) — six architectures, batch sizes 1 to 32
- [Apple M5 Max for local LLMs: first benchmarks](https://www.hardware-corner.net/m5-max-local-llm-benchmarks-20261233/) — the M5 Max basis for all M5 Ultra extrapolations
- [LLM tokens/sec benchmarks 2026: RTX 4090 vs 3090](https://mustafa.net/llm-tokens-per-second-benchmarks/) — RTX 3090 dense figures
- [Why DGX Spark runs 70B LLMs at 2.7 tokens/s](https://www.mayhemcode.com/2026/08/why-dgx-spark-runs-70b-llms-at-27.html)
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
- [SSD price tracker, August 2026](https://cheapestssd.com/ssd-price-tracker/) — NAND trend and $/TB

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
