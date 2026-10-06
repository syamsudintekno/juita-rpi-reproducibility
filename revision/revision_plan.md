# Revision plan grounded in the original reviews

Status as of 2026-10-06: original Reviewer A PDF and Reviewer B comments are available. The supplied local manuscript is a revision baseline candidate; its exact relationship to the submitted version remains to be verified. Original sources remain unchanged. This is a planning document, not a completed author response.

## Editorial requirements

The author supplied the decision email dated 2026-10-03: RESUBMIT FOR REVIEW, with 30 days for revision. The nominal date obtained by adding 30 calendar days is 2026-11-02; verify the actual OJS deadline and counting convention before relying on it.

Follow the official template and IMRaD, use English throughout, use numbered IEEE citations without narrative author-name citations, highlight changes consistently, and append the completed revision matrix. Preserve verified author order and identity. Translate Indonesian research text into English with the original Indonesian in italics where required. Cite JUITA articles only when substantively relevant.

The decision email specifies a ten-page maximum. The public author guidelines checked on 2026-10-06 describe A4, one column, Times New Roman 11, single spacing, 8–10 pages after layout, or up to 12 DOCX pages only if specified. Apply the decision's ten-page maximum; whether the matrix is included remains unresolved. The guidelines also require native editable Word equations, a 10–15-word title, a 100–200-word abstract, and 3–5 keywords. Reconcile the manuscript with the actual linked template before layout.

Official guidelines: https://jurnalnasional.ump.ac.id/index.php/JUITA/about/submissions

## Reviewer A work packages

| Original item | Required revision | Completion evidence |
|---|---|---|
| 1a–b | Correct full journal names and reference titles/style | Bibliography verified against original publications and IEEE formatting |
| 2a | Add 3–5 references for EACH of ceiling effect and distribution transformation | Relevant primary-source literature and updated research-position table |
| 2b | Identify the specific transformation in comparator studies | Method-specific comparison with the proposed framework |
| 3a | Correct the research-flow order | Preprocessing → aggregation → dimensions → Rankit → composite → RPI |
| 3b | Label Q1–Q4 areas in Figure 5 | Figure and descriptive median-based definitions agree |
| 4a | Explain the origin of 0.375 and 0.25 | Verified primary source and complete plotting-position formula |
| 4b | Explain 50 and 10 | Location/scale explanation and actual composite SD; no automatic SD=10 claim |
| 5a–e | Show raw input, Rankit, and RPI together for several examples | Input aggregate scores, record counts, dimensions, ranks, p, z, C, RPI and positions, using synthetic or explicitly authorized anonymous examples |
| 6 | Examine ranking agreement at moderate dimension correlations and compare literature | Matched-weight comparator, achieved correlations, repetition summaries, and position shifts |
| 7 | Demonstrate visualization, percentile analysis, and longitudinal monitoring concretely | Actual visualization/percentile outputs; longitudinal illustration clearly synthetic unless repeated observations and defensible calibration exist |

## Reviewer B work packages

B1–B7 below remain internal categories; the original Reviewer B comment is a narrative.

- B1: Operationalize ceiling behavior using observed maxima, ties and distribution patterns; do not treat Shapiro–Wilk or threshold 85 as proof.
- B2: Identify the aggregation level and missingness policy for alpha; do not claim student-response reliability from program-level aggregate records.
- B3: Provide a complete reproducible RPI formula, weighting, tie conventions, and preprocessing provenance.
- B4: Distinguish expected marginal normalization from measurement validity, information recovery, or fairness.
- B5: Moderate halo-effect interpretation of aggregate dimension correlations.
- B6: Explain cohort relativity and the need for reference calibration/equating for longitudinal and cross-institutional comparisons.
- B7: Simplify the flow diagram and substantially edit English.

## Baseline issues that require resolution

The supplied local manuscript states 2024–2025, whereas the previously inspected Drive version 3 states 2025–2026. The CSV header has no evaluation-period field. Neither date is accepted as verified evidence. Both versions use N=370; source inspection found 370 name strings, not 370 verified individual lecturers. Neither cohort nor old W/p values is frozen for the revision.

The prior notebook imputes invalid cells with median values, aggregates source totals, and exports names. Its non-individual regex and coverage require repair. Recompute totals, define whole-record exclusion scenarios, keep identity reconciliation private, and compare corrected outputs against archival results. Do not run the legacy notebook as if it implements the new protocol.

## Execution order

1. Preserve source hashes and original reviewer text privately; establish which manuscript was submitted.
2. Obtain instrument, period evidence, identity roster if available, and any authoritative correction of the invalid item. Continue synthetic implementation independently.
3. Implement and test preprocessing, item aggregation, matched-weight scoring, ties, and covariance-dependent composite scaling.
4. Recompute the empirical analysis with a documented provisional identity scenario; freeze only after unresolved facts are addressed.
5. Generate authorized worked examples, diagnostics, sensitivity results, and simple journal figures.
6. Edit a separate manuscript revision and populate author responses with completed evidence. Do not insert invented results or final page numbers.
7. Verify final layout, highlights, citations, author details, and the ten-page constraint before resubmission. Submission itself requires an explicit author instruction.

## Linked template and matrix checked on 2026-10-06

The linked JUITA formatting DOCX was read through the Drive connector. It specifies A4, one column, margins 19 mm top, 43 mm bottom, and 14.3 mm left/right; title 24 pt, authors 12 pt, affiliations italic 11 pt, and email Courier 10 pt. Main text uses Times New Roman 11 pt, with justified indented paragraphs. Figures have captions below; tables have titles above and are limited to one page. Equations must be native Word equations, numbered and with defined variables. The template does not require author-supplied page numbers, headers, or footers. Final page locations must still be verified for the matrix.

The linked Matrix of Revision Note has Paper ID, Title, Authors, and three columns: No., Reviewer's & Editor's Comments, and Revision. Its Revision column must include revised sections, corrections, and page numbers. Preserve this native structure in the final submission; the repository's expanded tracker is an internal planning tool. Paper ID is not yet available.

No manuscript layout or equation rendering has been verified in this audit. Text extraction is insufficient for that verification.
