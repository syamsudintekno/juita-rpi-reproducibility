# Preprocessing and analysis protocol

Status: planned, not executed. The institutional source and instrument have not been inspected in this checkout.

## Source and cohort

Read a source snapshot without writing to the original. Record its SHA-256, format, sheet, encoding, and verified header mapping privately. Validate numeric parsing, missing cells, item bounds, reported totals, and duplicate name–program pairs. Reconcile identities with an authoritative roster when available; damaged identifiers are not reliable keys.

Record generic labels and invalid cells before deciding exclusions. Recover values only from a verified authoritative source. If recovery is impossible, report whole-record complete-case exclusion as a documented scenario. Retain valid low values. Record counts at each stage, with separate record and entity counts, and compare plausible preprocessing scenarios. Freeze the final cohort only after reconciliation. The earlier 1,105/1,101 record counts and 370/369 name groups are unverified conversation findings, not acceptance targets.

## Scoring

Aggregate each item across retained records within an entity using equal record weights unless a justified alternative has been verified. Compute dimensions after item aggregation. Verify P1–P6, P7–P11, P12–P16, and P17–P20 against the instrument.

Use ascending midranks for each dimension. With N equal to the actual analysis cohort, compute `p = (r - 0.375)/(N + 0.25)`, `z = Phi_inverse(p)`, `C = sum(w_k*z_k)`, and `RPI = 50 + 10*C`. Require finite, nonnegative weights summing to one. Working weights are 0.25 each. Validate p strictly inside (0,1). Keep full precision; choose and document numerical tolerances before implementation. Do not silently standardize C.

Use three comparators: the sum of 20 item means, raw `X = 20*sum(0.25*d_k)`, and equal-dimension-weight RPI. Compare X with RPI to isolate the transformation under matched weights. For verified 1–5 items, both raw scores have a theoretical range of 20–100.

## Diagnostics and interpretation

Report descriptive statistics, skewness, excess kurtosis, IQR, theoretical and observed maxima, and ties at item, dimension, and composite levels. State calculation conventions. Report aggregate-level alpha with its analysis level, N, items, and missingness policy, and Pearson dimension correlations. Neither establishes individual-response reliability or a student-level halo effect.

Use Spearman midranks and Kendall tau-b. Use descending minimum ranks for position changes. Define quadrants by medians, assigning equality to the high group; freeze axis and Q1–Q4 labels before publication. Define percentile conventions explicitly before coding. If Shapiro–Wilk is retained, recompute it on the final cohort; old W/p values cannot be reused.

Upper-range concentration, observed ceiling behavior, and latent information loss require separate interpretation. A threshold of 85 or nonnormality alone does not establish a ceiling effect. RPI is cohort-relative. Transformation does not restore information, distinguish tied inputs, or demonstrate validity, fairness, or longitudinal comparability.

## Simulation and verification

After cohort freeze, implement Gaussian-copula sensitivity scenarios with empirical dimension marginals, latent correlations 0.30, 0.50, 0.70, and 0.98, initially 200 repetitions and seed 20261004. Document the generator and sampling method, report achieved Pearson correlations, and compare matched-weight ranking agreement and position changes. New row combinations are synthetic, but empirical-marginal simulation outputs still require institutional disclosure review. Between-repetition intervals are not population confidence intervals.

Test invalid parsing, whole-record exclusions, aggregation, dimension mapping, weights, ties, rank direction, p bounds, and the dependence of RPI standard deviation on covariance. Record and explain differences from the conversation audit without forcing numerical agreement. No test or empirical result is claimed by this protocol.
