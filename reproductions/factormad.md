# FactorMAD Replication Card

## Source

FactorMAD-style multi-agent factor discovery, audit, and repair. This card records the public evidence boundary for an agentic research workflow rather than exporting private prompts, data, or formulas.

## Reproduction scope

- Reconstructed the workflow as proposal, sandbox check, diagnostic audit, and promotion/rejection feedback.
- Emphasized falsifiable factor research: every proposed idea must pass static checks before it can be treated as evidence.
- Kept negative and partial results visible instead of presenting all generated ideas as discoveries.

## Expected versus observed

Expected behavior: an agent loop should increase research throughput only if it leaves behind auditable proposals, failure reasons, and claim ceilings.

Observed in the tracked product map: `diagnostic_feedback_agent_smoke_passed`. A small batch of `9` proposals was audited through the diagnostic workflow, with proposal-level review rather than blind promotion.

## Deviations and limits

- The public repository does not include private prompts, proprietary data, or non-public generated formulas.
- The smoke test does not prove that the agent discovers robust alpha.
- The strongest public claim is workflow reconstruction plus audit discipline.

## Reproduction verdict

`agent_workflow_smoke_only`: the multi-agent research pattern is represented, but no strict alpha-performance claim is made.
