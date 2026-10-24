# P17 — Certified Gaussian theta tails for two-dimensional Narain charge lattices
Date: 2026-10-24

## Exact theorem P17-T1
Let H be any real symmetric positive-definite 4x4 matrix, lambda=lambda_min(H)>0, t>0. Put Z_H(t)=sum_{v in Z^4} exp(-t v^T H v) and Z_(H,N)(t)=sum_{||v||_infty<=N} exp(-t v^T H v). Then
0 <= Z_H(t)-Z_(H,N)(t) <= exp[-t*lambda*(N+1)^2/2] * (1+sqrt(2*pi/(t*lambda)))^4.

Proof. For each omitted v, ||v||² >= (N+1)² and v^T H v >= lambda ||v||². Split exp(-t lambda ||v||²) into equal halves, bound one by exp[-t lambda (N+1)²/2] and sum the other over all Z^4. The one-dimensional Gaussian theta bound sum_{k in Z} exp(-a k²) <= 1+sqrt(pi/a) follows by monotone-integral comparison; use a=t lambda/2. Multiply four factors.

## Narain model and exact B-shift covariance P17-T2
For diagonal G=diag(g1,g2)>0, B=[[0,b],[-b,0]], and integer m,n in Z², E_(G,B)(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n. Under integer antisymmetric K=[[0,k],[-k,0]], the transformation B'=B+K, m'=m-Kn preserves E termwise. The bijection of Z^4 preserves the complete theta sum, but does NOT generally preserve a fixed coordinate-box truncation. Certified tails address the latter issue; use energy cutoffs for manifest covariance.

## Scientific status
Gaussian-tail certification and integral B-shift duality are established techniques, not a string-theory breakthrough. This is a proof-grade numerical foundation for investigating duality-invariant APG quantities. Do not confuse the positive real Gaussian zero-mode sum with a complete modular-invariant torus CFT partition function.

## Next step P18
Build certified energy-cutoff enumeration with rigorous finite-search completeness and full O(2,2;Z) generator tests; search for genuinely new bounds on physically motivated observables. Compare against known Narain theta and inverse spectral literature.
