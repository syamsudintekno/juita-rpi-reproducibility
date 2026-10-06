# JUITA RPI Reproducibility

This repository supports the revision of “Restoring Distributional Properties of Ceiling-Compressed Student Evaluation of Teaching Data via Relative Performance Index”. Institutional EDOM remains the primary dataset. The separate ILAD application is outside this repository's scope.

## Current status

The repository now contains a source-based preprocessing and RPI pipeline, exact dependency pins, analysis/cohort configurations, eleven passing local synthetic tests, and a synthetic-only CI workflow. Original LPM workbooks and the question document were inspected read-only; source byte hashes and the first provisional empirical run are retained privately. Identity verification and the final cohort remain unresolved. Remote CI status has not yet been verified. Earlier chat counts and statistical outputs are archival, not acceptance targets.

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

The commands below run the implemented pipeline. CI uses synthetic inputs and requires no private EDOM access.

## Working formulation

For each dimension, use ascending midranks and `p = (r - 0.375) / (N + 0.25)`, then `z = Phi_inverse(p)`. The working composite is `C = sum(w_k * z_k)` with four weights of 0.25; `RPI = 50 + 10 * C`. Do not silently standardize C. The RPI standard deviation is not automatically 10. Verify primary references before making an attribution in the paper.

Compare RPI principally with the raw composite using the same dimension weights: `X = 20 * sum(0.25 * d_k)`. The sum of the 20 item means is an additional comparator with different effective dimension weights. Rankit preserves ties and cannot restore lost information or establish measurement validity.

See [AGENTS.md](AGENTS.md) for the complete methodological and editorial constraints and [the decision log](revision/decision_log.md) for project status.

## Environment and execution

The tested local interpreter is Python 3.12.14. Use Python 3.12 and install the exact runtime package versions from `requirements.lock` in a local virtual environment. In Windows PowerShell:

```powershell
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.lock
& .\.venv\Scripts\python.exe -m unittest discover -s tests -v
& .\.venv\Scripts\python.exe -m src.rpi_pipeline --source-manifest private/lpm_manifest.json --output private/runs/unique_run_name
```

Create the private source manifest from the reviewed original files as a JSON list of objects with `path` and lowercase `sha256` fields. It may contain additional private audit metadata. Every source must match its reviewed hash and contain exactly one item table with the verified headers. The reader stops at the next dimension header and does not count summary rows as item records. Duplicate name–program pairs require review rather than silent deduplication. Use a new output directory for every run.

The pipeline preserves original name strings as provisional grouping keys, excludes only documented collective/generic labels, excludes entire invalid records without imputation, and averages complete records equally within a name group. Source-corrected values are read directly from the authoritative workbook. The pipeline does not edit a CSV or workbook in place.

Outputs include retained records, per-record exclusion reasons, a PRIVATE identity mapping, item/dimension/rank/p/z/composite scores, two raw comparators, RPI, descriptive and tie statistics, aggregate-level alpha at two explicitly named levels, Pearson dimension correlations, ranking agreement, position shifts, percentile positions, quadrants, and Shapiro–Wilk diagnostics. A run manifest records input/config/code/output hashes, dependencies, commit, timestamp, and counts. All institutional outputs are restricted to `private/`; neither anonymous codes nor statistical aggregation automatically authorize public release.

Simulation and publication figures are not yet implemented. A statistical run on provisional name groups does not freeze lecturer identities, establish a ceiling mechanism, or demonstrate measurement validity.
