# Decision log

## 2026-10-04 — Repository foundation

The institutional EDOM dataset remains the primary source. Original data and the submitted manuscript are read-only. ILAD remains a separate application and is outside this work's scope.

The public repository now has project instructions and conservative ignore rules. Institutional records and derivatives belong under ignored `data/` or `private/`; only reviewed authorized outputs belong in `public_results/`. Synthetic examples may be published when explicitly labeled and reviewed.

The working Rankit/RPI formulation and matched-weight comparator follow AGENTS.md. They are a protocol, not newly computed empirical results. The reported source counts, damaged P4, generic-label exclusions, and name groups remain provisional pending source inspection.

Documentation prepared: repository overview, proposed input contract, preprocessing protocol, and internal reviewer tracker. Reviewer responses remain pending. No cohort has been frozen, no dependency environment has been locked, and no statistical analysis has run in this checkout.

## Required inputs and unresolved decisions

- Authorized local source location, version, file format, header mapping, and decimal convention.
- Instrument confirming item scale and dimension mapping.
- Identity roster if available; evaluation period and respondent-count availability.
- Submitted manuscript, original reviewer comments, editor letter, journal template, and author guidelines.
- Whether the revision matrix counts toward the reported ten-page limit.
- Numerical tolerances, percentile definition, and exact quadrant axis/label convention before implementation.

Next: inspect supplied sources read-only, establish private provenance and reconciliation, then implement and verify a Python pipeline using synthetic inputs before an empirical run. Do not mark reviewer items complete until outputs and final manuscript locations exist.
