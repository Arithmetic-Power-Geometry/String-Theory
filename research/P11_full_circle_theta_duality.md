# P11 — Complete circle momentum-winding lattice and APG power-sum covariance
Date: 2026-10-24. Status: exact full-lattice theorem; classical T-duality, NOT a string-theory breakthrough.

Define E_R(m,n)=m²/R²+n²R² for R>0 and integer m,n. Let Theta_R(t)=sum_(m,n in Z²) exp(-t E_R(m,n)) for t>0. This converges absolutely as a product of two one-dimensional Gaussian theta series.

THEOREM P11-T1: Theta_R(t)=Theta_(1/R)(t) for all R,t>0. Proof: E_(1/R)(n,m)=E_R(m,n); (m,n)->(n,m) bijects Z².

THEOREM P11-T2: Define p_(m,n)=exp(-tE_R(m,n))/Theta_R(t). For q>1, D_(2q)=1-sum p_(m,n)^q=1-Theta_R(qt)/Theta_R(t)^q. Then D_(2q)(R,t)=D_(2q)(1/R,t). Proof: absolutely convergent sums, substitution, and T1.

THEOREM P11-T3: For every finite symmetric square cutoff |m|,|n|<=N, the multisets of energies at R and 1/R coincide. This follows from the same bijection, which preserves the square. The exact-rational test covers 28 radius/cutoff pairs.

LIMITATIONS: This is a charge-lattice theta factor, not a proof of modular invariance of a full string partition function. Theta covariance and Renyi/Gibbs reduction are established. The self-dual point R=1 is fixed by inversion, but T1-T2 alone do NOT prove global extremality of D_(2q) there. No novel physical prediction or breakthrough claimed.

NEXT: derive a new sharp, nonredundant full-lattice inequality, including physically justified operator/interaction information, and check against established lattice theta minimization and CFT results.
