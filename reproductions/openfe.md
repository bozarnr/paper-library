# OpenFE Replication Card

## Source

OpenFE-style automated feature engineering for tabular prediction. This card keeps only the public, clean-room claim boundary and excludes private datasets, internal prompts, and non-public logs.

## Reproduction scope

- Implemented a controlled feature-combination search pattern with explicit candidate accounting.
- Focused on leakage-safe feature generation, candidate tracking, and observed-versus-expected comparison.
- Used the result to document research process discipline rather than to advertise a tradable strategy.

## Expected versus observed

Expected behavior: a constrained feature grammar should generate auditable candidates and allow weak families to be rejected or promoted based on diagnostics.

Observed in the tracked product map: `combination_search_smoke_passed`, with `37` generated candidates. The strongest smoke family was illiquidity-like, with Rank IC in the approximate `0.06` to `0.07` band.

## Deviations and limits

- Candidate names and formulas are not exported from private work.
- The public record does not prove robustness across universes, dates, costs, or implementation choices.
- The observed IC band is a smoke observation, not a production claim.

## Reproduction verdict

`implemented_smoke_only`: useful feature-search machinery was reconstructed, but the claim ceiling is an auditable implementation smoke test.
