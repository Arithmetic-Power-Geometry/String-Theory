# SIG-05 — Exact complementary Schur bounds and novelty gate

Status: **20/20 exact multiset comparison cases PASS** in local independent Python Fraction execution. This is a finite computational experiment, not a claim of new mathematical theory.

For G=[[a,d],[d,c]], x=m1+b*n2, y=m2-b*n1, and W=n^T G n, completing the square in either coordinate gives E >= W+x^2/a and E >= W+y^2/c. Thus E >= W+max(x^2/a,y^2/c). Prune only when the lower bound is strictly greater than cutoff; exact boundary cases are retained.

All results used the original symmetric box of 729 charges, reduced to 365 inversion representatives. Five b values (0,1/10,1/5,1/2,-1/5) and four cutoffs (1,2,3,4) were tested. The complete exact (energy,spin) Counter was equal for full, winding-only, first Schur, second Schur and maximum-Schur pruning in **all 20 cases**. These are five parameter values of b with G fixed, not 20 independently sampled geometries.

## Exact number of full energy evaluations

Columns: b, cutoff, states, no bound, winding, Schur1, Schur2, max-Schur.

| b | cutoff | states | full | winding | Schur1 | Schur2 | max |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 9 | 365 | 41 | 14 | 14 | 5 |
| 0 | 2 | 15 | 365 | 122 | 32 | 32 | 14 |
| 0 | 3 | 43 | 365 | 203 | 59 | 68 | 28 |
| 0 | 4 | 75 | 365 | 203 | 95 | 104 | 52 |
| 1/10 | 1 | 9 | 365 | 41 | 14 | 14 | 5 |
| 1/10 | 2 | 13 | 365 | 122 | 32 | 23 | 13 |
| 1/10 | 3 | 39 | 365 | 203 | 50 | 68 | 27 |
| 1/10 | 4 | 75 | 365 | 203 | 95 | 104 | 52 |
| 1/5 | 1 | 9 | 365 | 41 | 14 | 14 | 5 |
| 1/5 | 2 | 13 | 365 | 122 | 32 | 23 | 13 |
| 1/5 | 3 | 39 | 365 | 203 | 50 | 68 | 27 |
| 1/5 | 4 | 75 | 365 | 203 | 95 | 104 | 52 |
| 1/2 | 1 | 9 | 365 | 41 | 14 | 14 | 5 |
| 1/2 | 2 | 13 | 365 | 122 | 32 | 23 | 13 |
| 1/2 | 3 | 39 | 365 | 203 | 50 | 77 | 30 |
| 1/2 | 4 | 67 | 365 | 203 | 86 | 95 | 44 |
| -1/5 | 1 | 9 | 365 | 41 | 14 | 14 | 5 |
| -1/5 | 2 | 13 | 365 | 122 | 32 | 23 | 13 |
| -1/5 | 3 | 39 | 365 | 203 | 50 | 68 | 27 |
| -1/5 | 4 | 75 | 365 | 203 | 95 | 104 | 52 |

The combined bound needs 27 full evaluations at b=1/5 and cutoff 3, versus 50 with Schur1, a 46% reduction in full evaluations. It still computes 365 lower bounds, and **no SIG-05 wall-clock improvement has been measured**.

## Strongest prior-art challenges

- Classical lattice enumeration already uses exact projected-norm bounds and branch-and-bound (Fincke-Pohst and Schnorr-Euchner): https://cseweb.ucsd.edu/~daniele/Lattice/Enum.html
- Modern lattice enumeration pruning: https://www.mdpi.com/2227-7390/11/3/766
- Narain CFT partition functions already encode lattice theta series and refined spectral data: https://inspirehep.net/files/a4114600f231e0b863f9b88bc7333031
- Spin selection in Narain CFTs is an active established topic: https://doi.org/10.1007/JHEP02(2026)058

These sources provide relevant baseline context, not an exhaustive novelty determination. The max-of-two-bound approach is elementary and cannot be presented as a new mathematics invention.

## Research decision

**REVISE / CONTINUE** as an exact algorithmic investigation. **NO-GO** on a SIG novelty or publication claim from SIG-05 alone. SIG-06 must compare a complete exact projected-norm (sphere-decoding) enumeration baseline, measure runtime and arithmetic work, and seek a nontrivial theorem beyond standard lattice enumeration. Preserve the existing string-theory manuscript unchanged.
