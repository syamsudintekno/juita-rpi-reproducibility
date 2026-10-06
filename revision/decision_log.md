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

## 2026-10-04 — Read-only review of previous work

The author supplied the earlier Drive workspace. A source CSV, prior notebook, manuscript candidate, template, and multiple output generations were located. A private source inventory and audit were recorded under ignored `private/`; no original source was modified or added to Git.

Connector text was inspected with JavaScript, not the new Python pipeline. It supports the earlier concern about an invalid item and generic records, but identity reconciliation, raw-byte provenance, and the final cohort remain unresolved. The prior notebook uses median imputation and source totals; these must be replaced or explicitly reconciled against the revision protocol. Its composite scaling, aggregate reliability interpretation, ceiling/halo claims, and quadrant labels also need correction. Existing statistics are archival, not newly validated results.

The candidate manuscript has not yet been confirmed as the submitted version. The instrument, identity roster, editor letter, and original reviewer comments remain outstanding. Next: establish a verified source snapshot, then implement preprocessing and scoring with synthetic tests before recomputing empirical results.

## 2026-10-06 — LPM source workbooks and instrument inspected

The author supplied five original LPM workbooks and the question document. Read-only inspection and private SHA-256 manifests now exist. The instrument supports the four dimension groups in the protocol. The workbooks contain aggregate lecturer–program item means; individual student responses and record-level respondent counts have not been found. The source filenames identify the odd semester of academic year 2024–2025, unlike the later draft's period claim. The units comprise four faculties and a postgraduate unit.

The invalid item in the earlier CSV has a numeric authoritative counterpart in a uniquely matched LPM source row. A provenance-backed correction in a derivative can replace the earlier provisional exclusion scenario; originals remain unchanged. Source and prior CSV coverage differ, and some lecturer-name strings differ despite matching program and item vectors. Those lineage candidates require review and do not verify identity. The exclusion history and final cohort remain unresolved. Detailed counts, source paths, identities, source hashes, and correction evidence are kept in ignored private audit files.

Next: reconcile prior cohort selection and naming changes, document the verified correction, then implement the pipeline and substantive synthetic tests. Do not force the provisional cohort size or reuse archival statistical results.

## 2026-10-06 — Retrospective exclusion context and explicit cohort rules

The author recalls removing collective lecturer and generic supervisor records manually; no historical script/log is available. Inspection of the omitted labels supports a source-based exclusion scenario using an anchored team-label rule and explicit generic-role labels. The provisional rules are stored in configs/cohort.toml, with no hardcoded target N. The private run reconciles retained and excluded records and retains the authoritative valid item counterpart.

Only generic roles are excluded; named individual supervisors remain eligible. Original source name strings are preserved, with normalization used only to classify labels. The old CSV's naming alterations are not silently copied into the source-based scenario. Counts and identity-bearing logs remain private, and the final cohort has not been frozen. This independently documented scenario must not be described as an exact reconstruction of undocumented historical deletions.
