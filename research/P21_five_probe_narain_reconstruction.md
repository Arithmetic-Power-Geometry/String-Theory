# P21 — Five labelled probes reconstruct a two-dimensional Narain background

Date: 2026-10-24. Result: exact global constructive reconstruction for a fixed charge basis. Novelty against inverse Narain literature is NOT established.

Let G=[[a,d],[d,c]] positive definite, B=[[0,b],[-b,0]], and E(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n. Write charge vectors in order (m1,m2,n1,n2), with standard basis e1,e2,e3,e4.

THEOREM P21-T1: The five labelled energies x=E(e1), y=E(e2), z=E(e1+e2), w=E(e4), h=E(e1+e4) uniquely determine (G,B). Specifically, A=G^-1 has A11=x, A22=y, A12=(z-x-y)/2. Set G=A^-1 and b=(h-x-w)/(2x). Since G is positive definite, x>0 and A is invertible.

Proof: The first three energy measurements are pure-momentum evaluations of the quadratic form G^-1. Their polarization gives A. For n=e4, Bn=(b,0). Therefore E(e1+e4)-E(e1)-E(e4)=2 b A11. Solve for b. Every step is reversible, proving uniqueness.

COROLLARY P21-C1: These labelled measurements determine the entire infinite-lattice energy function E and therefore its zero-mode theta function. They do NOT reconstruct a background from five unlabelled energy levels or from a partition function without charge labels.

LIMITATIONS: The five-probe count is a sufficiency bound, not proved minimal. Physical availability of charge-resolved measurements is not established. The reconstruction is coordinate-dependent and must be interpreted modulo O(2,2;Z) duality for physical equivalence. This is elementary quadratic-form polarization applied to Narain backgrounds; do not claim a breakthrough without a novelty audit.

NEXT GATE P22: prove minimality or find a smaller universal labelled-probe family, analyze robustness to errors, and determine whether a charge-blind modular-invariant observable admits a comparable finite certificate. Audit against existing inverse spectral and Narain reconstruction results.
