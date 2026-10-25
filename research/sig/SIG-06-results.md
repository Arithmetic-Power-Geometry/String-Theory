# SIG-06: Projected-norm enumeration novelty kill-test

**Decision: NO-GO for a speedup or novel mathematics claim from SIG-01–SIG-05.** Retain results and failed hypotheses. The published Narain paper is unchanged.

## Exact baseline

For G=[[a,d],[d,c]], x=m1+b*n2, y=m2-b*n1, W=n^T G n, the exact identity is

E = W + x*x/a + (a*y-d*x)^2/(a*(a*c-d*d)).

Enumerate n, discard when W>cutoff; enumerate m1, discard when W+x*x/a>cutoff; enumerate m2, evaluate the remaining nonnegative square and retain precisely when E<=cutoff. This is standard exact projected-norm lattice enumeration, not a new mathematical result.

## Test protocol and result

Local Python Fraction arithmetic, five b values (0,1/10,1/5,1/2,-1/5), cutoffs 1,2,3: 15 cases. Full 729-charge, SIG-05 max-of-two-Schur, and projected-norm methods produced **identical exact energy-spin Counters** in all 15 cases. G fixed at [[2,1/3],[1/3,3]]. The 729-charge box is the manuscript's analytically justified complete domain for its cutoff-3 rational witness; no general completeness claim is made for arbitrary G or cutoffs.

At b=1/5, cutoff=3: full enumeration 729 energy calls; SIG-05 27 full energy calls and 365 bound checks; projected-norm 39 full energy calls, 9 winding checks, 45 first-coordinate checks and 99 second-coordinate checks. All returned 39 low-energy states.

Median local timings, three batches of five runs: full 9.2682 ms, SIG-05 5.0363 ms, projected-norm 1.7969 ms. This is a preliminary machine-specific measurement, not a portable benchmark or complexity guarantee. The stronger standard baseline is approximately 2.8 times faster than SIG-05 in this test, despite making more full-energy calls.

## Research interpretation

Counting only full-energy evaluations was misleading. Standard search ordering avoids hundreds of bound checks. SIG-01–05 provide useful expository notation and correct finite optimizations, but no demonstrated new mathematics and no competitive algorithmic advantage against projected-norm enumeration.

## Next decision

Stop incremental bound-combination work. A SIG-07 project is justified only with a **different, nontrivial research question**, such as exact spin-resolved spectral separation thresholds or a theorem on minimal sufficient observations, subject to rigorous prior-art review. No SIG paper now.
