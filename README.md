# JUITA RPI Reproducibility

This repository supports the revision of “Restoring Distributional Properties of Ceiling-Compressed Student Evaluation of Teaching Data via Relative Performance Index”. Institutional EDOM remains the primary dataset. The separate ILAD application is outside this repository's scope.

## Current status

The repository contains project instructions, a privacy policy enforced through `.gitignore`, a proposed input contract, a preprocessing protocol, and an internal revision tracker. An earlier Drive CSV, notebook, and manuscript candidate have been inspected read-only through connector text; a private audit is retained locally. Raw-byte provenance and the final cohort remain unverified. No empirical analysis, Python pipeline, dependency lock, or CI run is available yet. Counts from the earlier conversation are provisional and must be recomputed.

## Data and publication boundaries

Read original sources without modifying them. Keep institutional data and derivatives under `data/` or `private/`; these locations are ignored except for `data/README.md`. The `results/` and `notebooks/` directories are also ignored. Store only reviewed and authorized publication outputs in `public_results/`. Public examples must be explicitly synthetic and stored in `examples/synthetic/`. Anonymization alone does not authorize publication.

Never commit names, institutional identifiers, identity mappings, private download links, credentials, or record-level institutional exports. Review notebook outputs, image metadata, logs, and staged diffs. `.gitignore` does not remove files already tracked by Git.

## Starting a reproducible run

1. Obtain authorized local access to the source, instrument, identity roster if available, submitted manuscript, and original reviewer comments.
2. Record a source checksum and version in a private manifest. Verify the header mapping and item scale against [the input contract](data/README.md).
3. Follow [the preprocessing protocol](revision/preprocessing_protocol.md), documenting corrections, exclusions, and unresolved identities.
4. Freeze the cohort and configuration before generating final results. Do not assume the earlier cohort size is correct.
5. Implement the main pipeline in Python with a locked environment and substantive tests. Record input hashes, configuration, dependency versions, commit, timestamp, reconciliation counts, and output checksums for every run.
6. Review the resulting evidence before updating the manuscript and [revision tracker](revision/reviewer_matrix.md).

Execution commands will be added when an implemented and tested pipeline exists. CI must use synthetic inputs and require no private EDOM access.

## Working formulation

For each dimension, use ascending midranks and `p = (r - 0.375) / (N + 0.25)`, then `z = Phi_inverse(p)`. The working composite is `C = sum(w_k * z_k)` with four weights of 0.25; `RPI = 50 + 10 * C`. Do not silently standardize C. The RPI standard deviation is not automatically 10. Verify primary references before making an attribution in the paper.

Compare RPI principally with the raw composite using the same dimension weights: `X = 20 * sum(0.25 * d_k)`. The sum of the 20 item means is an additional comparator with different effective dimension weights. Rankit preserves ties and cannot restore lost information or establish measurement validity.

See [AGENTS.md](AGENTS.md) for the complete methodological and editorial constraints and [the decision log](revision/decision_log.md) for project status.
