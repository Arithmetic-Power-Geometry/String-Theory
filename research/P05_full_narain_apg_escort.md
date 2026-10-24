# P05 — Narain-lattice APG escort functionals and exact duality covariance

Date: 2026-10-24. Status: proved restricted mathematical statements; not established as novel physics.

For a positive-definite d by d matrix G and antisymmetric B, define E_(G,B)(m,n)=(m+Bn)^T G^(-1)(m+Bn)+n^T G n on integer charge pairs (m,n). For t>0 and cutoff L>=0 let S_L be all nonzero charge pairs with E<=L. Set Z_L(t)=sum_(S_L) exp(-t E) and normalized escort weights p_z=exp(-t E_z)/Z_L(t), when S_L nonempty. Define APG power-sum defect D_s=1-sum_z p_z^(s/2) for s>0, and Shannon H=-sum_z p_z log p_z.

THEOREM P05-T1. If an integral charge bijection U preserves the energy under a background transformation (G,B)->(G',B'), then S_L and S'_L correspond bijectively and D_s, H and Z_L are identical. Proof: the bijection preserves the energy cutoff, individual Boltzmann weights and normalization. This is a standard consequence of lattice covariance, not an independently novel T-duality theorem.

THEOREM P05-T2. For an integral antisymmetric K, B'=B+K and m'=m-Kn, n'=n give E_(G,B')(m',n')=E_(G,B)(m,n) exactly. Hence all P05-T1 observables are invariant under integral B shifts. Proof: m'+B'n'=m+Bn.

The construction uses an energy-defined cutoff, not a fixed coordinate box; coordinate-box truncation generally breaks invariance under arbitrary integral charge transformations.

APG link: APG I and the Shannon-Renyi manuscript define power-sum deformations of normalized positive weights. P05 instantiates this familiar construction on physical momentum-winding energy weights. It does not change the string partition function or establish a new observable: Z_L and escort power sums are functions of a known energy spectrum.

Novelty gate: identify a nontrivial invariant or inequality not reducible to standard Narain theta-series / Renyi entropy identities; independently prove it and test against published prior art. Full O(d,d;Z) invariance follows if the standard Narain charge/background covariance is applied; this note explicitly proves only the integral B-shift generator and the abstract covariance lemma. No physical prediction is claimed.
