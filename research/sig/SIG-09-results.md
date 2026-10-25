# SIG-09: Expanded exact first-separation interval and independent audit

**Result:** For G=[[2,1/3],[1/3,3]] and B_±(b)=±[[0,b],[-b,0]], the exact first joint energy-spin spectral difference is

D_ES(b) = (133-6b+18b²)/53 for every 0<b<=3/14.

This extends the SIG-08 certified interval [19/100,21/100]. **Do not claim 3/14 is a maximal interval.**

## Proof

1. For every charge v in [-4,4]^2 x [-1,1]^2, its energy E_±(v,b) is an exact rational quadratic polynomial in b.
2. Compare each of the 729 polynomials with T(b)=(133-6b+18b²)/53. At b=1/5, 25 charge states are below T, two equal T and 702 above T for each sign.
3. Independently audit signs of all polynomial differences on [0,3/14] using exact endpoint and vertex evaluations. The 25 strictly lower charges have spin zero; the two identically equal polynomials carry spin -1 for B+ and +1 for B-. No charge changes the relevant strict classification in the open interval. At b=3/14, two extra spin-zero charges meet the threshold for each background, without cancelling the spin difference.
4. The complete unlabelled energy spectra agree by parity, so the spin-zero states strictly below T match; no lower spin-refined difference occurs. At T the spin counts differ.
5. Uniform completeness for E<=3: eigenvalues of G lie in [5/3,10/3]; hence |n|²<=9/5<2 and |m+Bn|²<=10. For 0<=b<=3/14, |m_i|<=sqrt(10)+3/14<4. Thus the 729-charge box contains all E<=3 states, and T(b)<3 throughout the interval.
6. At b=0 the backgrounds coincide; D_ES(0)=infinity. Exclude b=0.

The independent exact Fraction audit prints PASS and checks all 729 charge-polynomial comparisons per sign, including endpoint degeneracy. This is a computer-assisted finite certificate with an analytic uniform charge bound.

## Failure and novelty register

- Hypothesis that 3/14 is the maximal validity endpoint: **NOT ESTABLISHED**. Some energy-polynomial orderings change at 3/14, but the earliest spin-refined spectral difference can remain at T(b) beyond that point.
- Claim of a new branch of mathematics: **NOT ESTABLISHED**. Spectral theta-series comparisons and parameter-dependent quadratic forms have substantial prior art.
- A competitive speedup over standard lattice enumeration: **REJECTED in SIG-06**.
- Novelty of the continuum first-separation formula: **UNRESOLVED**, requires targeted literature verification and stronger structural analysis.

**Decision:** REVISE / CONTINUE SIG-10 with a genuinely independent algorithm and determine actual endpoint(s) of validity, rather than treating the first polynomial crossing as a spectral threshold transition. Do not draft a new paper yet.
