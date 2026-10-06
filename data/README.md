# Input contract: institutional EDOM

Status: proposed canonical schema, pending inspection of the actual source and instrument. These names are internal fields, not claims about source headers. This directory contains no public institutional dataset.

## Unit of observation

The reported source consists of aggregated evaluation records associated with a lecturer and study program. A record is not an individual student response and must not be called a class without source documentation. The evaluation period and respondent counts are currently unverified or unavailable.

| Canonical field | Type | Rule |
|---|---|---|
| source_row_id | string | Stable reference to the snapshot and source row; retained privately. |
| lecturer_name | string | Preserve the source string privately; never publish it. |
| program | string | Preserve source labels and document normalization. |
| institutional_id | string or missing | Optional; preserve as text. Scientific notation or damaged values cannot verify identity. |
| entity_id | string | Assigned through documented identity reconciliation; mapping remains private. |
| P1 through P20 | numeric | All 20 items must parse as finite numbers and lie within the verified instrument range. |
| reported_total | numeric or missing | Optional diagnostic only; recompute the total from 20 valid items. |
| respondent_count | positive integer or missing | Optional; do not invent it or treat missing as zero. |
| evaluation_period | string or missing | Optional; never infer it from file dates or manuscript year. |

The expected 1–5 scale remains subject to instrument verification. Record delimiter, encoding, decimal convention, sheet, and header mapping before parsing. Do not silently coerce nonnumeric cells or guess a decimal convention.

## Identity and missingness

Inspect duplicate name–program pairs without automatically deleting them. Similar names do not establish a shared identity. If the roster is unavailable, name groups remain provisional and must not be presented as verified unique lecturers. Generic labels require an explicit exclusion rule.

Correct a damaged item only from an authoritative verified value with provenance. Otherwise document a whole-record complete-case exclusion scenario. Do not impute P4 from a damaged total, mean, or median. Keep valid low scores and use the same complete records for every dimension.

## Aggregation and dimensions

Without verified respondent counts, average complete program records with equal weights within each resolved entity. This is not a student-count-weighted mean. First aggregate P1–P20, then compute dimension means using the instrument mapping, provisionally Pedagogical P1–P6, Professional P7–P11, Personality P12–P16, and Social P17–P20.

## Private run artifacts

Keep the source manifest, header mapping, variable dictionary, identity reconciliation, exclusion and correction logs, cleaned records, and run outputs locally. A manifest records source hash/version, configuration, dependency versions, code commit, timestamp with timezone, stage counts, and output hashes. Private paths and identity-bearing logs must not appear in public artifacts.

Before analysis, reconcile input records against retained and excluded records; document overlapping exclusion reasons without double-counting. Report both record counts and entity counts and explain identity uncertainty.

## Source inspection update on 2026-10-06

The supplied LPM workbooks and question document have now been inspected read-only. Their item-table headers are `No.`, `Nama Dosen`, `Program Studi`, `Pertanyaan 1` through `Pertanyaan 20`, and `Rata-Rata`. Institutional ID is absent from these item tables, despite its presence in the earlier CSV; its origin remains to be traced. Each workbook contains several summary tables, including a second dimension table below the item table. Detect headers explicitly rather than reading all numbered rows as item records.

The question document supports the 6/5/5/4 competency grouping and lists categories 1–5. Its example frequency counts do not provide respondent counts for the full dataset. The source records remain aggregate item means. The invalid item in the earlier CSV has a verified source value; corrections must remain in a derivative with the original value and cell provenance recorded privately. Prior cohort selection and altered name strings still require reconciliation before freezing the data.
