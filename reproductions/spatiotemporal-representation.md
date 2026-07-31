# SpatioTemporal Representation Replication Card

## Source

Spatio-temporal representation learning ideas for financial panels, event streams, and entity context. This public card records the reconstruction boundary without exposing non-public source material or data.

## Reproduction scope

- Built a graph-context smoke layer that links event records, entities, and static context.
- Evaluated the feasibility of moving beyond flat tabular factors toward event-aware representation learning.
- Preserved point-in-time caution as a first-class artifact.

## Expected versus observed

Expected behavior: event and entity context should be represented in a way that can later be tested against strict point-in-time labels.

Observed in the tracked product map: `finbee_graph_context_smoke_passed`, with `582` event records and `1609` static context edges. The useful finding was not a tradable signal; it was the discovery that many events lacked `report_date`, so the current layer is context-only rather than a valid point-in-time signal.

## Deviations and limits

- Missing or weak timestamp provenance prevents a strict predictive claim.
- The public artifact does not include raw event data or private graph exports.
- The current work should not be described as a successful alpha replication.

## Reproduction verdict

`context_layer_smoke_only`: the graph/context layer works as infrastructure, but the current claim ceiling stops before point-in-time alpha evidence.
