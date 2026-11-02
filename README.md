# Local LLM Inference Hardware: Bandwidth or Usable Memory

A comparison of eleven hardware configurations for running large language models
locally, built between August and November 2026 during a severe DRAM and NAND
shortage that repriced the entire category mid-analysis.

**[View the page](https://scottrille.github.io/local-llm-rig-analysis/)**, or
open `index.html` in any browser. It is a single self-contained file, with no
build step and no dependencies beyond three Google Fonts families.

## The thesis

Token generation is memory-bandwidth-bound. Every token requires reading the
active model weights out of memory once, so:

```
tokens/sec ≈ (bandwidth × efficiency) / bytes read per token
```

Model size sets the floor on how much memory you need. Those two numbers,
usable memory and bandwidth, determine almost everything else, and nothing on
the market offers plenty of both at a reasonable price. Every configuration here is short
of one or the other.

## Headline findings

**Mixture-of-experts changes which number matters.** A 117B-parameter MoE like
gpt-oss-120b activates about 5.1B parameters per token, so it needs memory for
all of them but bandwidth for only a slice. That is why a DGX Spark runs a 120B
MoE at 60 tok/s and a 32B dense model at 8 tok/s. See `docs/methodology.md`.

**The cheapest memory on the page is Apple's.** All four M5 Ultra
configurations cost about $52 per gigabyte of usable memory. The DGX Spark was
$47/GB in August and is $70/GB after NVIDIA's October price increase.

**Prefill matters more than decode for agentic work.** An agent loop re-sends its
whole context every turn, so the time to the first token is most of the wait
that you notice. This is where the low-bandwidth machines and the AMD card are
weakest, and it does not show up in the tokens/sec figures that people usually
quote.

**The software decides whether a second box adds speed.** Two Macs over
Thunderbolt 5 with RDMA and EXO gain about 34% throughput, and two DGX Sparks
running vLLM with tensor parallelism gain about a third. The same Macs running
llama.cpp *lose* 16%, because it splits the model by layers and the machines take
turns.

**Prices moved more than the analysis did.** Between August and October NVIDIA
raised the DGX Spark 128GB list price 48%, used RTX 3090s rose 23%, the lowest
new RTX 5090 price rose about 13%, and Apple changed nothing. Several
conclusions reversed without any hardware changing. `docs/corrections.md` tracks
every reversal.

## Contents

| Path | What it is |
|---|---|
| `index.html` | The comparison page, self-contained |
| `CHANGELOG.md` | Version history of the page, with what changed and why |
| `docs/methodology.md` | How every number was derived; the bandwidth model and its limits |
| `docs/corrections.md` | Every claim that turned out wrong, and the fix |
| `docs/conversation-log.md` | The question-by-question thread this came from |
| `docs/sources.md` | All cited sources, grouped by topic |
| `data/configurations.csv` | The configuration matrix as machine-readable data |
| `scripts/validate_html.py` | Structure and table-consistency checker for the page |
| `scripts/wrap_document.py` | Wraps an HTML fragment as a complete document |
| `LICENSE` | The CC BY 4.0 license |

## Confidence

Treat every performance figure as accurate to roughly ±20%. Sources differ in
quantization, inference engine, and context length, and some figures are derived
from the bandwidth model rather than measured. `docs/methodology.md` marks which
is which, and `docs/corrections.md` is the honest record of where the derivations
failed.

Prices are street rates checked between 19 October and 1 November 2026. They are
delivered cost: street price plus about 11% sales tax on every configuration,
plus a host PC for the GPU builds (about $500 before tax for one card, $600 for
two, $1,500 for the RTX PRO 6000 workstation). They were wrong twice during this
analysis and will be wrong again. Check them again before you buy anything.

## License

Copyright 2026 Scott Cottrille. Everything in this repo is licensed under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)
(CC BY 4.0), and the full text is in `LICENSE`. You can copy, adapt and use any
of it for any purpose, including commercially. In return, you must credit the
author, link to the license, and say whether you changed anything.

The benchmark figures on the page come from the sources credited in
`docs/sources.md`. If you reuse a figure, credit its original source too.
