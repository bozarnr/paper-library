# Paper Alpha Replications

Replication notes for quant papers, written with a claim ceiling attached. A paper can be interesting, code can run, and the result can still be unusable as an alpha. This repo keeps those states separate.

这里记录论文、实现证据、本地观察和偏差。目标不是把论文包装成策略，而是留下以后能继续查、继续复现、继续反驳的记录。

## Showcase

- [Replication Index](reproductions/index.md): current paper list, status meanings, and claim ceilings.

## Related repos

- [AI-Alpha-Research-Lab](https://github.com/bozarnr/AI-Alpha-Research-Lab): formula search, evaluation, and rejection gates.
- [Paper-Alpha-Replications](https://github.com/bozarnr/Paper-Alpha-Replications): replication notes with claim ceilings.
- [Quant-Research-Toolkit](https://github.com/bozarnr/Quant-Research-Toolkit): reusable checks for factor panels and diagnostics.
- [Strategy-Game-Agents](https://github.com/bozarnr/Strategy-Game-Agents): repeated-choice experiments and baseline agents.

## Current record

| Paper | Status | Claim ceiling |
|---|---|---|
| [AutoAlpha (2020)](reproductions/autoalpha.md) | Method reconstruction complete; strict promotion record closed | `implemented`, not deployable |

## Run checks

```bash
python -m unittest discover -s tests -v
```

The tests check that each card has source, scope, deviation, and claim-boundary sections. They do not validate trading performance.

## Rules

- Do not upload employer code, private data, tokens, or non-public experiment logs.
- Do not call a replication successful without a runnable command and expected-versus-observed comparison.
- Treat negative and partial results as useful evidence, not as cleanup items.
