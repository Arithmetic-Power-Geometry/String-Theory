# First spin-resolved spectral discrepancy in a Narain two-torus family

Exact computational certificate supporting the first energy–spin discrepancy theorem for the rational metric
`G₀ = [[2, 1/3], [1/3, 3]]` and opposite antisymmetric fields `B(b) = ±b[[0,1],[-1,0]]`.

For `0 < b < 1/2`, the first differing zero-mode energy is

`D_ES(G₀,b) = (133 - 6b + 18b²)/53`.

Integral antisymmetric shifts extend this formula to all real `b`, with equal refined spectra at integer and half-integer parameters. On `1/10 ≤ b ≤ 2/5`, the exact minimum gap to any other nonzero-spin charge is `6/265`.

## Exact certificate

The low-energy completeness argument restricts charges to `[-4,4]² × [-1,1]²` (729 vectors). For each field sign there are 576 nonzero-spin charges. The exact polynomial classification is:

| Classification | Each sign |
|---|---:|
| Identically at the threshold | 2 |
| Touching only at b = 0 | 2 |
| Touching only at b = 1/2 | 2 |
| Strictly above throughout [0, 1/2] | 570 |

`verify_certificate.py` checks the full interval for all 1,152 nonzero-spin polynomial records using exact rational endpoint and vertex tests, checks the uniform competing-charge gap, and writes `certificate_results.json`.

Run from this directory:

```bash
python3 verify_certificate.py
```

**Canonical polynomial-record SHA-256:** `3ab2a33813961595c77b2e9a6e8823eceee58560f72cd4cc69ae12432354f435`

The canonical digest covers the sorted-key, compact JSON serialization of the complete polynomial records constructed by the script. The computational certificate supports the finite-charge step; analytic completeness, symmetry, theta-sum and metric-perturbation arguments are provided by the research article.

## Citation

Akhtar, M. A. K. (2026). *The First Spin-Resolved Spectral Discrepancy in a Narain Two-Torus Family: Exact Thresholds, Symmetry Boundaries, and Stability* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23666390

## Scope

These are zero-mode energy–spin calculations in the stated normalization; they do not assert an inequivalence of complete oscillator-dressed string theories. The repository root separately documents the earlier inverse-spectral investigation.

## Copyright and license

Copyright © 2026 Mohammad Amir Khusru Akhtar.

The original verification code and computational materials in this directory are licensed under the **Apache License, Version 2.0 (Apache-2.0)**. See the repository-root [LICENSE](../../LICENSE) and [NOTICE](../../NOTICE). The research article and third-party works retain their respective copyright and publication terms.
