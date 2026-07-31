# Paper Alpha Replications

Evidence-first replications of quantitative-research papers. Every replication card separates the paper's claim, available implementation evidence, local observations, and unresolved deviations.

## Current record

| Paper | Status | Claim ceiling |
|---|---|---|
| [AutoAlpha (2020)](reproductions/autoalpha.md) | Method reconstruction complete; strict promotion record closed | `implemented`, not deployable |
| [DoubleEnsemble](reproductions/double-ensemble.md) | Quality-filtered model smoke comparison recorded | `implemented`, smoke only |
| [OpenFE](reproductions/openfe.md) | Controlled feature-combination search smoke recorded | `implemented`, smoke only |
| [SpatioTemporal Representation](reproductions/spatiotemporal-representation.md) | Event/entity context layer smoke recorded | `implemented`, context only |
| [FactorMAD](reproductions/factormad.md) | Multi-agent proposal/audit workflow smoke recorded | `implemented`, workflow only |

## Verification

```bash
python -m unittest discover -s tests -v
python scripts/verify_cards.py
```

The checks validate that each public card carries source, scope, deviation, and claim-boundary sections, and that each machine-readable paper card links to existing evidence. They do not validate trading performance.
The disclosure boundary is recorded in [DISCLOSURE.md](DISCLOSURE.md), and
`sample_data/evidence_matrix_sample.csv` is a synthetic schema fixture.

## Rules

- Do not upload employer code, private data, tokens, or non-public experiment logs.
- Do not report a replication as successful without a runnable command and an expected-versus-observed comparison.
- Record negative or partial results as first-class evidence.

## Repository layout

```text
reproductions/  human-readable replication cards
paper_cards/    machine-readable claim and evidence metadata
schemas/        lightweight schema contracts for paper cards
scripts/        static verification commands
tests/          regression tests for the evidence contract
```
