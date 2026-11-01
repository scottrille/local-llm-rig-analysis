# Corrections

Every claim in this analysis that turned out wrong, what replaced it, and why it
was wrong. Kept because the failure modes are more transferable than the
conclusions, and because the conclusions have a short shelf life.

---

## 1. Prices answered from priors rather than checked

**Claimed (August, first pass):** RTX 3090 ~$900 used, RTX 5090 ~$2,200, DGX
Spark $3,999, RTX PRO 6000 ~$8,500.

**Actual:** $1,095–$1,181, $4,288–$4,381, $4,699, $13,998–$15,499.

**Why:** These were launch-era MSRPs recalled rather than looked up. A DRAM
contract-price spike of roughly 80% in Q1 2026 had repriced everything with a
lot of memory, and NVIDIA had raised the PRO 6000 MSRP from $8,435 to $16,000.

**Lesson:** Prices are never a knowledge question. Neither are availability,
current office-holders, or anything else with a clock on it.

---

## 2. A recommendation built on a stale price

**Claimed:** "At $8,100 for two Sparks you're close to an RTX PRO 6000 build,"
and therefore two Sparks were hard to justify.

**Actual:** Two Sparks were ~$10,000 and a PRO 6000 build ~$16,500. The
alternative cost 65% more, not slightly more.

**Why:** The entire argument rested on the bad PRO 6000 figure. One wrong input
invalidated a verdict, not just a number.

**Lesson:** When a price is wrong, re-derive the conclusions that leaned on it
rather than just patching the figure.

---

## 3. External storage cost

**Claimed:** External NVMe runs about $150/TB, so take the small internal SSD.

**Actual:** $175–$255/TB all-in for practical sizes. Gen 4 NVMe averaged $90/TB
in August, up from $75 in April, with specific drives at $105–$130/TB.

**Why:** NAND is in the same shortage as DRAM. Fabs are prioritizing AI and
data-center orders.

**Note:** The recommendation survived (Apple charges $500/TB), but at 2x to 3.5x
better rather than the 3x to 5x implied.

---

## 4. Mac pricing quoted on an inconsistent basis

**Claimed:** M5 Ultra 256GB at $9,499.

**Actual:** ~$12,000 delivered. $9,499 was the base 30/64 GPU bin, pre-tax, and
Apple's configurator appears to pair 256 GB only with the 36/80 bin, making it
$10,799 pre-tax.

**Why two errors compounded:** the cheaper bin was quoted without checking
availability, and the Mac was quoted pre-tax while tax was discussed separately,
which skewed every comparison against the machines whose prices already included
a build.

**Fix:** Everything moved to a single delivered-cost basis, street price plus
~11% sales tax applied uniformly.

---

## 5. "No continuous batching or prefix caching on Apple silicon"

**Claimed:** The Mac has no vLLM, therefore no continuous batching and no
automatic prefix caching, and this was called disqualifying.

**Actual:** True of `mlx-lm` and llama.cpp, false of the ecosystem. The community
`vllm-mlx` project provides continuous batching, a paged KV cache, prefix
caching, and an Anthropic-format `/v1/messages` endpoint that Claude Code can be
pointed at directly.

**Why:** Checked whether upstream vLLM supported Metal, concluded the capability
did not exist, and stopped there.

**What does hold:** the fine-tuning toolchain. PEFT, TRL, Unsloth, and Axolotl
are CUDA projects; MLX has its own LoRA implementation and its own recipes.

---

## 6. Blanket dismissal of AMD

**Claimed:** AMD's memory advantage does not survive contact with its software.
Vulkan beats AMD's own ROCm by 2.5x on prompt processing, PyTorch needs community
wheels, no official support.

**Actual for the card in question:** that evidence was from Strix Halo
(`gfx1151`, integrated). The discrete Radeon AI PRO R9700 is `gfx1201`, and ROCm
7.2 lists it as officially supported on Linux and Windows with precompiled
kernels and no `HSA_OVERRIDE` workaround.

**Why:** Generalized from an integrated part to a vendor.

**What still holds:** the fastest measured llama.cpp result on the R9700 was on
Vulkan rather than ROCm, Ollama ships ROCm 6.x libraries with no `gfx1201`
kernels and falls back to CPU until `OLLAMA_VULKAN=1` is set, and prefill runs
3.44x slower than an RTX 5090 at 32K context.

---

## 7. The bandwidth model overestimates very large MoE

**Claimed:** M5 Ultra at ~48 tok/s on DeepSeek 671B and 50–80 on Qwen3 235B.

**Actual:** Measured EXO figures on M3 Ultra, scaled by bandwidth, give ~31 and
~29.

**Why:** The formula assumes bytes-read-per-token is the only constraint. At very
high sparsity, expert routing scatters memory access and the effective efficiency
drops well below the 60–75% that mid-size models achieve.

**Note:** The model held up well on gpt-oss-120b and on dense models. It fails at
the sparse extreme, in the optimistic direction.

---

## 8. The M5 Ultra 512GB price estimate

**Claimed:** ~$16,000 pre-tax, extrapolated from Apple's own 96 to 256 GB rate.

**Actual:** $22,299. The memory option alone is $15,500.

**Why:** Linear extrapolation. Apple charges $25/GB for the first 160 GB above
its 96 GB base and $45/GB for the next 256 GB. The ladder escalates at the top
tier.

**What it changed:** two conclusions reversed. The 512 GB tier turned out to
offer no better memory value than the 256 GB ($52/GB either way), and two 256 GB
machines became $750 *cheaper* than one 512 GB machine rather than $6,400 more
expensive. The earlier verdict that the pair was "hard to justify" was an
artifact of the estimate, not of Apple's pricing.

**Lesson:** Treat a vendor's published rate as a floor, not a slope. This
estimate was flagged as the page's biggest unknown, which was right, but the
magnitude was still understated.

---

## 9. A table that mixed two kinds of thing

**Problem:** The cluster-scaling table had three rows of (model × runtime)
measured on M3 Ultra Macs, then a fourth row for a different platform, with a
different model, and a number that was inferred rather than measured.

**Fix:** The table now holds hardware and interconnect fixed and varies only
model and runtime, so rows are comparable. The Spark cluster moved to a separate
labeled block that says plainly its figure is inference from the interconnect.

**Also fixed:** the section heading asserted the conclusion ("two boxes, two very
different outcomes"), which is part of what let the mismatched row in.

**Caught by the reader, not by me.**

---

## 10. Overstated the Spark's CUDA advantage

**Claimed:** The Spark is the stack-parity option because it runs CUDA.

**More precisely:** it runs aarch64 CUDA on compute capability `sm_121`. NGC
containers work, many pip wheels do not, and you meet compute-capability-specific
bugs (such as the FP4-to-Marlin MoE fallback) before a large user population has
found them. True at the CUDA API level, misleading at the "will this repo just
run" level.

---

## 11. A framing error about model size

**Claimed, loosely:** the Spark handles larger models better than smaller ones.

**Actually three separate facts:** (a) on any machine, more active parameters
always means fewer tokens/sec, so larger is always slower in absolute terms;
(b) sparse beats dense on bandwidth-starved hardware, and large models today
happen to be sparse; (c) unified memory removes the offload cliff that kills
consumer cards past their VRAM limit, so the Spark's relative position improves
only because the competition disappears.

**Why it mattered:** the loose version invited a reasonable reader to conclude
something false about size.

---

## 12. Sales tax attributed to the wrong state

**Claimed:** ~11% California sales tax.

**Actual:** The rate was inferred from a timezone. Corrected to a
state-agnostic "~11% sales tax (a US West Coast metro rate)" for this export.

---

## The pattern

Four of these (1, 2, 3, 8) are the same error: treating a number with a clock on
it as a fact rather than an observation. Two (5, 6) are the same error in a
different costume: checking the canonical implementation, finding it absent, and
concluding the capability did not exist. One (7) is a model applied outside its
validated range. One (9) is a presentation failure that smuggled an assumption
in alongside measurements.

The conclusions in this repo will age. The habit of marking which numbers were
measured, which were derived, and which were assumed is what makes it possible
to tell what still holds.
