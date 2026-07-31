# Paper Alpha Replications

Evidence-first replications of quantitative-research papers. Every replication
card separates the paper's claim, the available implementation evidence, local
observations, and unresolved deviations.

中文简介：这是量化论文复现证据库。每个条目都明确区分论文原主张、可运行
实现、实际观察到的结果与未解决偏差，避免把“读过论文”或“代码能运行”写成
策略有效。

## Public Research Stack

This repository is one part of a public AI-quant portfolio:

- [AI Alpha Research Lab](https://github.com/bozarnr/eee): formula-alpha research with strict promotion gates.
- [Paper Alpha Replications](https://github.com/bozarnr/paper-library): evidence-first paper replication ledger.
- [Quant Research Toolkit](https://github.com/bozarnr/experiment): reusable time-safe factor diagnostics.
- [Strategy Game Agents](https://github.com/bozarnr/behavioral-finance-experiment): behavioral experiment tooling plus strategy-agent simulation.

## Current record

| Paper | Status | Claim ceiling |
|---|---|---|
| [AutoAlpha (2020)](reproductions/autoalpha.md) | Method reconstruction complete; strict promotion record closed | `implemented`, not deployable |

## Verification

```bash
python -m unittest discover -s tests -v
```

The check validates that each public card carries source, scope, deviation, and
claim-boundary sections. It does not validate trading performance.

## Rules

- Do not upload employer code, private data, tokens, or non-public experiment logs.
- Do not report a replication as successful without a runnable command and an
  expected-versus-observed comparison.
- Record negative or partial results as first-class evidence.
