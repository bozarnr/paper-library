# DoubleEnsemble Replication Card

## Source

DoubleEnsemble-style denoising and ensemble training for financial prediction. This public card records a clean-room reconstruction boundary rather than republishing source paper text, private notebooks, or proprietary data.

## Reproduction scope

- Reconstructed the workflow as a quality-filtered model comparison: baseline predictor, sample/feature quality controls, and an ensemble-style candidate path.
- Kept the public artifact at the evidence-contract level: what was implemented, what was observed, and what cannot be claimed.
- Treated the result as a research-system smoke test, not as a deployable alpha.

## Expected versus observed

Expected behavior: a denoising/quality-filtering layer should be measurable against a simple baseline without leaking labels or future data.

Observed in the tracked internal product map: `quality_filtered_model_smoke_passed`. A smoke comparison recorded test Rank IC `0.035440` versus baseline `0.022629`.

## Deviations and limits

- The public repository does not include employer data, raw experiment logs, or paper-exact datasets.
- The smoke result is not a full replication under the paper's original market, universe, and training protocol.
- No live-trading, production, or deployable-performance claim is made.

## Reproduction verdict

`implemented_smoke_only`: the engineering reconstruction is present and bounded, but the strict replication ceiling remains below paper-level reproduction.
