# SIG-04: Exact lower-bound pruning

**Decision:** GO for algorithm research, NO-GO for claiming a new mathematical theory or paper.

## Mathematical certificate

Let G=[[a,d],[d,c]] be positive definite, B=[[0,b],[-b,0]], x=m1+b*n2, y=m2-b*n1. By completing the square,

(x,y)^T G^(-1)(x,y) = x^2/a + (a*y-d*x)^2/(a*(a*c-d*d)).

Therefore E >= n^T G n + x^2/a. The difference is an exact nonnegative rational square. A charge can be discarded when this lower bound exceeds the cutoff. Equality and boundary cases are retained.

This is the standard Schur-complement/completing-the-square bound, not a newly invented inequality.

## Exact executed local test

At cutoff 3, for both b=+1/5 and b=-1/5, and both energy-only and energy-spin observations:
- Direct inversion representatives: 365.
- Certified exclusions from the lower bound: 315.
- Full energy evaluations remaining: 50.
- Lower-bound checks: 365.
- Complete exact Counter equality with SIG-03: PASS.
- Total states with energy <=3: 39 per background.
- Reduction in full energy evaluations: 315/365 = 86.30%.

## Local timing (milliseconds per run)

Seven batches, 20 runs per batch; median per-run time; Python 3.13.5, Linux x86_64. Timings are environment-specific.

| b | Observation | SIG-03 ms | SIG-04 ms | Ratio |
|---|---|---:|---:|---:|
| +1/5 | energy | 4.3615 | 3.8859 | 1.122x |
| +1/5 | energy-spin | 4.9924 | 4.4915 | 1.112x |
| -1/5 | energy | 4.8400 | 4.4916 | 1.078x |
| -1/5 | energy-spin | 4.5625 | 4.1072 | 1.111x |

The improvement in expensive full evaluations is **not** an 86% runtime improvement. Cheap bound checks still cost time. The 729-charge analytic completeness bound is inherited from the original paper, not re-proved here.

## Next gate

SIG-05 should compare the standard Schur-complement bound against coordinate-free eigenvalue bounds, two-coordinate pruning, and direct bounded-lattice enumeration over multiple backgrounds/cutoffs. Record exact arithmetic operation counts and end-to-end runtime. Search prior art before novelty claims. Keep the published manuscript unchanged.
