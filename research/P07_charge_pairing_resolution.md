# P07 — Pairing-resolved APG observables: exact separation and novelty audit

Date: 2026-10-24. Status: exact finite charge-set theorem; no claim of new string physics.

For integer momentum m and winding n in Z^d, define J(m,n)=m dot n. With a positive torus metric G and antisymmetric B, use the P05 energy E=(m+Bn)^T G^-1(m+Bn)+n^T G n.

Define a finite refined polynomial T_S(x,y)=sum_(m,n in S) x^E(m,n) y^J(m,n) for integral energies, or the analogous Laplace series sum exp(-beta E) y^J for real energies. The unrefined energy polynomial is T_S(x,1).

THEOREM P07-T1 (finite charge-set separation). The unrefined energy polynomial does not determine the pairing-refined polynomial over arbitrary finite charge sets. Proof: at G=I and B=0 in d=2, take A={(m=(1,1),n=(0,0))}, B={(m=(1,0),n=(1,0))}. Each has E=2, hence T_A(x,1)=T_B(x,1)=x^2, but T_A(x,y)=x^2 and T_B(x,y)=x^2 y. This is a finite combinatorial fact, not a separation of full physical compactifications.

THEOREM P07-T2 (integral B-shift covariance). For any integral antisymmetric K, B'=B+K and m'=m-Kn, n'=n. Then E'=E and J'=J because n^T K n=0. The map is a bijection of integral charges, so energy-defined cutoffs and pairing-refined generating functions are invariant. Proof by substitution.

For the full O(d,d;Z) group, J is the standard invariant quadratic form (up to normalization) and the Narain construction already retains left/right lattice information. This refinement is NOT novel by itself; it is a known kind of Siegel-Narain theta information. A genuine new result requires a nontrivial theorem not reducible to existing theta-series identities.

Caveat: arbitrary finite subsets A and B need not be preserved by the full duality group. Do not infer physical distinguishability or string-theory contradiction.

Next target P08: seek a provably nonredundant observable for complete admissible compactifications, compare to full Siegel-Narain theta functions, modular covariance, and level-matching, and identify either a strict novelty theorem or a no-go certificate.
