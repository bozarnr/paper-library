# AutoAlpha: an Efficient Hierarchical Evolutionary Algorithm for Mining Alpha Factors

## Source

- Zhang, Tianping; Li, Yuanqi; Jin, Yifei; Li, Jian (2020).
- arXiv: [2002.08245](https://arxiv.org/abs/2002.08245).
- Paper contribution: hierarchical evolutionary search, PCA-based quality
  diversity, warm start, replacement, and a ranking-based portfolio stage.

## Reproduction scope

The public reproduction scope is the research-system contract: a controlled
formula language, point-in-time evaluation, hierarchical candidate search, and
strict promotion gates. It is not a release of any employer code, private
market data, or original paper experiment artifact.

## Observable implementation evidence

The corresponding public lab implements an allow-listed expression evaluator,
historical-window operations, out-of-sample Rank IC, turnover, and explicit
transaction-cost accounting. See the companion repository's public code for a
dependency-light smoke implementation.

## Expected versus observed

The paper reports that its search procedure can discover useful formulaic
alphas under its experimental setup. In the recorded strict executable protocol
used for this replication line, search-generated candidates did not survive
frozen transfer and cost-aware promotion gates: the final candidate count was
zero. This supports an implementation claim about the pipeline, not a claim of
tradable alpha quality.

## Deviations and limits

- The original data, exact field definitions, and experimental environment are
  not assumed to be reproducible from the paper alone.
- The public record uses no private dataset or proprietary implementation.
- Historical close-to-close diagnostics are not treated as executable evidence.
- The completed price/amount/return formula space is closed to further tuning.

## Reproduction verdict

`implemented_not_deployable`: the core research mechanics and validation
discipline were reconstructed, but the strict promotion objective was rejected
under the recorded protocol. A new cycle requires an independent data segment,
a pre-registered mechanism, and a frozen fair baseline.
