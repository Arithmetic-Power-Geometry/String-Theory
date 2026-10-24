# P13 — Full-lattice self-dual crossover theorem
Date: 2026-10-24. Status: mathematically proved scaling limit; novelty in string theory unestablished.

Let E_R(m,n)=m²/R²+n²R² on Z² minus (0,0). Define Z*(R,t)=sum_nonzero exp(-t E_R), p=exp(-t E_R)/Z*, D*_(2q)=1-sum p^q, q>1.

THEOREM P13-T1. Along any sequence t->infinity and R->1 with t*abs(R²-R^-2)->x in [0,infinity), D*_(2q) converges to
F_q(x)=1-(1+exp(-q*x))/(2^(q-1)*(1+exp(-x))^q).

PROOF. Write a=min(R²,R^-2), b=max(R²,R^-2), delta=b-a. The four unit charges have energies a (multiplicity 2) and b (multiplicity 2). The remainder Z_tail=sum over all other nonzero charges exp(-tE). In a fixed neighborhood of R=1, all other charges have E>=2a, whereas the leading states have E=a. For any t>=t0>0, factor exp(-ta) and bound the tail using a convergent Gaussian majorant and dominated convergence; Z_tail/exp(-ta)->0 uniformly as R->1 and t->infinity. Thus exp(ta)Z* = 2(1+exp(-t delta))+o(1). Similarly exp(qta)Z*(R,qt)=2(1+exp(-qt delta))+o(1). Their ratio yields F_q(x). The theorem is invariant under R->1/R.

ENDPOINTS. F_q(0)=1-4^(1-q); lim_(x->infinity)F_q(x)=1-2^(1-q). At finite t, D* is continuous in R. These statements explain the noncommuting limits in P12.

LIMITATIONS. This is a low-temperature conditioned nonvacuum charge ensemble, not a complete modular-invariant string partition function or a physical phase transition. The crossover is a standard two-doublet Gibbs scaling structure. No breakthrough or prior-art novelty is asserted.

NEXT SCIENTIFIC GATE. Replace the conditioned ensemble with a physical modular-covariant observable, prove a genuinely new sharp estimate with error terms and independently compare to established compact-boson and Narain literature.
