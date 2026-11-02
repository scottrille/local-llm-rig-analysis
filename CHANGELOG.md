# Changelog

Version history of the comparison page, from 28 August to 1 November 2026.

Prices were restated three times and several conclusions reversed. Where a
revision changed a verdict rather than just a number, that is called out.

---

## 1 Nov 2026: sortable cost table, plain wording, definitions

The three cost columns in "What memory actually costs" can be sorted. The first
click sorts from cheapest to most expensive, and a second click reverses it.

Replaced the benchmark jargon "depth" and "depth zero" in the context section
with "with an empty context" and "with 32K tokens of context". The methodology
doc defines "depth" for readers who meet it in benchmark results.

Added a "Terms used on this page" section at the end with 32 definitions,
grouped by topic, including batch size, quantization levels such as Q4 and Q8,
prefill, decode, KV cache and bin. The first uses of "batch size 1" and
"Q4-class quantization" link to their definitions. Added a 4-node change column
to the clustering table, and renamed the AMD section to "The AMD option,
compared to other discrete cards".

---

## 1 Nov 2026: general audience

Removed the Windows 11 + WSL2 framing that came from the original question, and
the Claude Code-specific content (the Anthropic-format endpoint row and
references to pointing Claude Code at a server). The page now answers the
general question of how to choose hardware for local inference.

Long-context costs are now described for chat, agents and document retrieval
in general, rather than for coding agents only. The Mac bin advice now says
that the faster bin's prefill gain matters for long prompts, which replaces a
claim that decode always dominates. Added a sentence to the opening on what
the page covers, and a short decision method at the top of the recommendations.

---

## 1 Nov 2026: cost per GB on the chart

Renamed "The trade space" to "Memory versus bandwidth". Bubble area on that
chart now shows delivered cost per gigabyte of usable memory, with a size key,
and each bubble is labeled with its $/GB. Labels were repositioned so that none
of them overlap a bubble, a line or another label.

---

## 1 Nov 2026: consistency and public-release pass

Rewrote the page so that it describes only the current state of the analysis.
Removed text that referred to earlier versions of the page ("better than this
page said", "a reversal", "now priced") and the per-row "since August" price
arrows and column. One paragraph in the footer now records how prices moved.

Fixed figures that contradicted the page's own inputs:

- RTX 5090 price change: +64% became about +13% (street floor) and +12%
  (delivered configuration). The page's own August street price was
  $4,288–$4,381 and the current floor is $4,921
- Two-Spark price change: +40% became +48%, matching the single Spark. The
  August comparison figures built on it ($50/GB, "$1,000 cheaper than the Mac")
  were $47/GB and about $1,600
- Dual RTX 3090 price change: +5% became +15%, consistent with the 23% rise in
  used 3090 prices
- gpt-oss-120b KV cache: 0.072 MB/token became 0.036 MB/token, because only
  half of its layers use full attention. At 32K the cache is ~1.2 GB, not
  ~2.4 GB, and that fits the measured 33% decode loss better
- Dense 70B decode at 32K: "barely notices" became "loses about a fifth"
- "Best model at ≥50 tok/s" for the M5 Ultra columns: 235B-class and 671B
  became gpt-oss-120b at Q8, since the page's own figures put the larger
  models at ~29 and ~31 tok/s
- M5 Ultra "concurrent serving" and "software stack" rows now reflect
  vllm-mlx, as the stack section already did
- Dual 3090 is "the only NVIDIA option under $5,000", not "the only option",
  since both R9700 configurations are cheaper. Removed a claim that the RTX
  5090 costs more than a 128 GB Spark ($6,000 versus $7,700)
- Memory bars for the RTX 3090 and RTX 5090 cards were scaled to an old
  maximum. They now match the 960 GB scale

Documented that GPU configurations include a host PC (about $500 to $1,500
before tax). Applied plain-language editing throughout.

---

## 1 Nov 2026: Radeon AI PRO R9700 added

Added single and dual R9700 configurations: 32 GB GDDR6 at 640 GB/s, ~$2,550
delivered for one. The cheapest 32 GB on the page, at 42% of an RTX 5090's cost
for the same capacity.

Given its own table comparing it with the other discrete cards rather than a
column in the main matrix, applying the apples-to-apples principle from the
clustering fix.

**Verdict change:** the earlier blanket dismissal of AMD was narrowed. It came
from Strix Halo (`gfx1151`); the discrete R9700 is `gfx1201` and ROCm 7.2 lists
it as officially supported. The prefill deficit (3.44x slower than a 5090 at 32K)
remains the reason not to buy it for agentic work.

Also corrected the sales-tax attribution from "California" to a state-agnostic
rate, since the original was inferred from a timezone.

---

## 28 Oct 2026: M5 Ultra 512GB real price

Apple published $22,299 for the 512 GB tier, about $24,750 delivered. The page
had estimated $16,000 by extrapolating Apple's own 96 to 256 GB rate linearly,
and was low by $6,300.

**Two verdicts reversed:**

- The 512 GB tier offers no better memory value than the 256 GB. Both are
  $52/GB, so it buys more memory in one box rather than cheaper memory. It lost
  the "best memory value" badge
- Two 256 GB machines (~$24,000) became $750 *cheaper* than one 512 GB machine,
  with 34% more throughput. The previous "hard to justify" verdict on the pair
  was an artifact of the estimate

---

## 19 Oct 2026: October repricing

NVIDIA raised the DGX Spark 128 GB from $4,699 to $6,950 (48%) and added a 64 GB
SKU at $4,999. The RTX 5090's new floor rose about 13% to $4,921, with used at
$5,880, above new. RTX 3090 used rose 23%. Apple changed nothing.

**Three verdicts reversed:**

- Apple went from losing on memory value to winning it. The Spark was $47/GB
  versus the Mac's $52 in August. It became $70 versus $52
- Two Sparks went from about $1,600 cheaper than a 256 GB M5 Ultra to $3,400 more
  expensive, for a quarter of the bandwidth. Moved from "hard to justify" to
  "avoid"
- The new 64 GB Spark was flagged as a trap for this use case: it costs more than
  the 128 GB did in August and ~55 GB usable will not hold gpt-oss-120b

---

## Late Aug / early Sep 2026: structural revisions

**Clustering table restructured.** A reader caught that it mixed three rows of
(model × runtime) with a fourth row for a different platform, a different model,
and an inferred number. Hardware and interconnect are now held fixed, and the
Spark cluster moved to a separate block labeled as inference.

**vllm-mlx correction.** The claim that Apple silicon has no continuous batching
or prefix caching was wrong. The community `vllm-mlx` project provides both plus
an Anthropic `/v1/messages` endpoint.

**Software stack section added.** Engine availability across four stacks,
capabilities that follow from the stack rather than the silicon, and model and
format availability. Established that all stacks expose an OpenAI-compatible HTTP
endpoint, so the client side is identical regardless of hardware.

**Roadmap section added.** AMD Gorgon Halo and Medusa Halo, NVIDIA's N1/N2 and
the absence of an announced Spark II, and Apple's revised M6/M7 plan, each tagged
with a confidence level.

**Mac configuration section added.** Both M5 Ultra GPU bins run at 1,200 GB/s, so
decode is identical and the $1,300 upgrade buys only ~25% prefill. The
configurator appears to pair 256 GB only with the 36/80 bin.

**Dual-Mac clusters added.** Measured EXO figures showed 34% gain on two nodes
with RDMA, and llama.cpp *losing* 16% on identical hardware. This also forced a
correction: the bandwidth model had overestimated very large MoE throughput, so
those figures moved to measurement-derived values.

**Context section added.** One vague row became three measured costs: KV cache
capacity, time to first token, and decode decay.

**Delivered-cost basis adopted.** Mac prices had been quoted pre-tax, while
the others included a build, and that skewed every comparison. Everything moved to
street price plus ~11% sales tax, applied uniformly.

**M5 Ultra added.** Announced 25 August, three days before the first version.
1.2 TB/s and 256 GB for about what two Sparks then cost, which inverted the
conclusion that the Spark was the capacity option.

---

## 28 Aug 2026: first version

Four configurations: dual RTX 3090, single RTX 5090, one DGX Spark, two DGX
Sparks. Built around the capacity-versus-bandwidth trade and the finding that
only the Spark could run gpt-oss-120b at interactive speed.

Prices in this version were launch-era MSRPs recalled rather than checked, and
were wrong by up to 90%. Corrected within hours of publication.
