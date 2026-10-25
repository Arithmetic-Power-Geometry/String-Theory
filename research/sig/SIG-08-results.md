# SIG-08 — Exact first-separation formula on a continuum of backgrounds

**Status:** GO for mathematical development; no independent novelty claim or new paper yet.

## Theorem (certified family-level threshold)

Fix G = [[2,1/3],[1/3,3]]. Let B_+(b)=[[0,b],[-b,0]] and B_-(b)=-B_+(b). For every real b in [19/100,21/100], the **first energy at which the joint (energy, spin) zero-mode multiplicities of the two backgrounds differ** is

D_ES(b) = (133 - 6b + 18b^2)/53.

At that energy, the B_+ multiplicities are N(E,+1)=0 and N(E,-1)=2; the B_- multiplicities are N(E,+1)=2 and N(E,-1)=0. All lower spin-resolved spectral multiplicities agree. The complete unlabelled energy spectra agree for all b by the known parity correspondence. Duality statements concern spin-preserving O(2,2;Z), not parity.

## Proof and exact certificate

For v=(m1,m2,n1,n2), write x=m1+b*n2, y=m2-b*n1, det(G)=53/9, and

E(v,b)=(3*x*x-(2/3)*x*y+2*y*y)/(53/9)+2*n1*n1+(2/3)*n1*n2+3*n2*n2.

The charge v=(-1,0,1,0) for B_+ (and v=(-1,0,-1,0) for B_-) gives the displayed polynomial and spin -1 (respectively +1). Its inversion partner gives multiplicity two.

The target energy is <3 throughout the stated b interval. The analytic completeness argument is uniform: G has eigenvalues between 5/3 and 10/3, so E<=3 implies |n|^2<=9/5<2; thus n1,n2 are in [-1,1]. Moreover |m+Bn|^2<=10, so each |m_i|<=sqrt(10)+21/100<4. Thus every charge with energy <=3 lies in [-4,4]^2 x [-1,1]^2 (729 candidates).

Each charge energy is a rational quadratic polynomial in b. Subtract the target polynomial and calculate its exact minimum and maximum on [19/100,21/100], evaluating both endpoints and its vertex if inside the interval. For each sign of B, the exact calculation finds:
- 25 charges strictly below the target, in 13 polynomial-energy groups, **all with spin zero**;
- exactly two charges at the target, with spin -1 for B_+ and +1 for B_-;
- 702 charges strictly above the target;
- no charge whose relative ordering changes inside the interval.

Because all lower states have spin zero, and parity identifies their energy multiplicities, the spin-resolved spectra agree strictly below the target. At the target they differ as stated. Hence the displayed formula is the exact first spin-refined separation threshold for the entire interval.

The executable certificate is [sig08_symbolic_family.py](sig08_symbolic_family.py), which uses Python standard-library Fraction arithmetic, checks all 729 candidate polynomials for both signs, and asserts the above counts. Locally executed: PASS.

## Scope and novelty limits

This is a stronger continuum-level mathematical statement than SIG-07's fixed rational point. It is a certified theorem for a **fixed metric G and one-dimensional B-parameter interval**, not a theorem on all four-dimensional Narain backgrounds. The certificate is a finite exhaustive proof plus uniform analytic charge bound. No claim is made that the idea of a first spectral difference or its computation is new in the literature.

## Next step / publication gate

SIG-09: independent implementation and exact reproduction of the interval certificate; strongest prior-art check for parameter-dependent first differences of spin-refined theta spectra; attempt a non-enumerative structural proof or a larger interval with exact endpoint characterization. Preserve failures and sources. No SIG manuscript yet.
