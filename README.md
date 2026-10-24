# Finite Spectral Reconstruction and Robust Non-Identifiability in Two-Dimensional Narain Compactifications

**Mohammad Amir Khusru Akhtar**  
Usha Martin University, Ranchi, Jharkhand, India

Copyright © 2026 Mohammad Amir Khusru Akhtar

**Publication:** Akhtar, M. A. K. (2026). *Finite Spectral Reconstruction and Robust Non-Identifiability in Two-Dimensional Narain Compactifications* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23621602

## Overview

This repository provides exact-arithmetic computations and supporting certificates for the zero-mode inverse spectral problems studied in the accompanying paper. For a two-dimensional Narain background with positive-definite metric `G`, antisymmetric field `B`, and integer momentum and winding charges `m,n`, the energy and spin are

```text
E(m,n) = (m + Bn)^T G^(-1) (m + Bn) + n^T G n
s(m,n) = m^T n
```

The analysis distinguishes charge-labelled energy evaluations, unlabelled energy multiplicities, and joint energy–spin multiplicities. It establishes exact reconstruction in specified families and non-identifiability results on unrestricted parameter domains.

## Mathematical results and verification

- **Five labelled evaluations:** An explicit algebraic inverse reconstructs the metric and antisymmetric field in a fixed integral charge basis.
- **Rectangular backgrounds:** For `3/2 <= a,c <= 2` and `0 <= b <= 1/2`, unlabelled energies through `17/8` determine the unordered pair of diagonal metric entries and `b`.
- **Exact spin-asymmetry witness:** The rational backgrounds `G = [[2,1/3],[1/3,3]]` and `B = ±[[0,1/5],[-1/5,0]]` have identical complete unlabelled energies but different joint energy–spin multiplicities. At `E = 3373/1325`, the `B+` background has multiplicities `N(E,+1)=2` and `N(E,-1)=0`; these are reversed for `B-`.
- **Complete charge search:** The analytic bounds reduce all states of energy at most `3` to `[-4,4]^2 × [-1,1]^2`, comprising `729` candidate charges; `39` states per background satisfy the cutoff.
- **Perturbation certificate:** Outward rational interval bounds certify spin separation throughout a four-parameter cube of radius `1/90`. The certificate covers `68` opposite-spin charge vectors with minimum interval clearance `564868/568757475`.
- **Finite-window limitations:** The paper proves that no background-independent finite energy cutoff, even with spin-resolved multiplicities, distinguishes every duality class on unrestricted Narain moduli space.

## Reproducibility resources

- [Verification scripts](tests/)
- [Standalone paper-certificate verification](tests/verify_paper_certificates.py)
- [Additional verification scripts](tests/)

Run the two principal finite certificates from the repository root:

```bash
python tests/verify_paper_certificates.py
```

The script asserts the complete 729-charge enumeration, the 39 low-energy states in each background, the witness spin multiplicities, all 68 opposite-spin interval comparisons, and the exact minimum clearance. The analytic completeness and global non-identifiability arguments are given in the paper.

The computations use exact rational arithmetic and integer charge enumeration. The finite certificates support the stated rational examples and parameter bounds; the continuum and genericity results also require the analytical arguments in the paper. The inequivalence claims concern spin-preserving `O(2,2;Z)` T-duality, not equivalence after worldsheet parity.

## Citation

Akhtar, M. A. K. (2026). *Finite Spectral Reconstruction and Robust Non-Identifiability in Two-Dimensional Narain Compactifications* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23621602

Citation metadata is also provided in [CITATION.cff](CITATION.cff).

## License

Original verification code and computational materials: Apache License, Version 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). The published manuscript and cited third-party works retain their own terms.
