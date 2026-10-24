# P28 — Exact low-energy isospectral windows and a duality-invariant separation

Date: 2026-10-24.

## Theorem T1
For rectangular two-torus Narain zero modes with B=0 and G=diag(a,c), the unlabelled zero-mode energies are E=m1²/a+m2²/c+a n1²+c n2². Consider A: (a,c)=(1/4,1), B: (a,c)=(1/4,2). For any cutoff 1/4<=C<1/2, the complete multiset of energies <=C is identical for A and B: the vacuum at E=0 with multiplicity 1, and E=1/4 with multiplicity 2. At E=1/2, B has multiplicity 2 and A has multiplicity 0. Hence the complete zero-mode spectra differ; in particular, the backgrounds are not related by any exact Narain T-duality preserving zero-mode energies.

Proof: All energy summands are nonnegative. In A, the coefficients are (4,1,1/4,1), so below 1/2 only n1=0,+1,-1 contribute. In B the coefficients are (4,1/2,1/4,2), so the same statement holds below 1/2. At E=1/2, B additionally has m2=+1,-1, whereas A has no vector of that energy. Exact counts follow.

## Theorem T2 — Continuous indistinguishable family
Fix a=1/4 and let c range continuously in [1,2]. For C=3/8, the full unlabelled zero-mode spectrum <=C is constant: {(0,1),(1/4,2)}. Indeed, c>=1, 1/c>=1/2, and 1/a=4. The next possible contributions beyond n1=+/-1 have energy >=1/2. This family exhibits failure of finite-window identifiability even with perfect degeneracy data. No claim is made that all c values are pairwise inequivalent under the full duality group; the endpoint pair is inequivalent because their complete spectra differ.

## Rigorous completeness certificate
For positive diagonal coefficients q=(1/a,1/c,a,c), let lambda=min(q)>0. Every charge v with E(v)<=C satisfies ||v||_2²<=C/lambda, hence ||v||_infty<=sqrt(C/lambda). The test enumerates a certified sufficient box and filters using exact fractions.

## Limitations and novelty
This is an elementary explicit inverse-spectral counterexample, not evidence of a fundamental new string-theory mechanism. It refutes universal identification from this specified finite low-energy window; it does not rule out a larger finite threshold on a compact moduli domain or identification from the entire CFT spectrum. The zero-mode energy spectrum is not the full CFT spectrum, but an exact duality preserves it. Do not assert a physics breakthrough.

## Next research gate
P29: derive a sharp cutoff-identifiability threshold on a bounded rectangular-moduli domain, and distinguish full zero-mode spectral data from physical modular-invariant CFT observables. Require prior-art novelty audit.
