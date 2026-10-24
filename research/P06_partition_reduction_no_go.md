# P06 — Exact partition-function reduction and novelty no-go
Date: 2026-10-24. Classification: proven mathematical identity and novelty filter, NOT a new string-theory theorem.

Let a finite energy-defined set S of N>=1 charge states have energies E_z>=0. For beta>0 set Z(beta)=sum_(z in S) exp(-beta E_z), p_z=exp(-beta E_z)/Z(beta). Let q>0 and define the APG-inspired power-sum defect D_(2q)=1-sum_z p_z^q.

**Theorem P06-T1 (partition reduction).** D_(2q)=1-Z(q beta)/Z(beta)^q, identically. Proof: substitute p_z and sum. Thus a power-sum APG deformation based only on Gibbs probabilities supplies no information beyond the partition function sampled at beta and q beta. In particular two backgrounds with identical energy theta series at all beta have identical D_(2q) for all beta,q. This is an exact no-go for using these scalar observables alone to distinguish isospectral backgrounds.

**Theorem P06-T2 (sharp finite-size range).** For q>1, 0<=D_(2q)<=1-N^(1-q). Equality on the right holds exactly for uniform probabilities (all selected energies equal), and equality on the left requires N=1 for finite beta and finite energies. Proof: Jensen gives sum p^q>=N^(1-q), while sum p^q<=sum p=1. For q<1 the inequalities reverse appropriately. The result is classical power-mean mathematics, not a novelty claim.

**Theorem P06-T3 (exact thermal sensitivity).** For q>0, d/d beta log[Z(q beta)/Z(beta)^q] = q[U(beta)-U(q beta)], where U(beta)=-d log Z(beta)/d beta. Since U'(beta)=-Var_beta(E)<=0, the derivative is nonnegative for q>1, nonpositive for 0<q<1, and zero for q=1. Therefore D_(2q) decreases as beta increases when q>1. This follows from standard Gibbs calculus.

**Implication.** The P05 escort-entropy proposal is not by itself a string-theory breakthrough. To obtain a new observable one must add independently justified charge-sector or interaction information not determined by the unrefined Narain theta series, and prove duality covariance and physical relevance. Such refinements may already be known in the literature and require an exhaustive novelty check.

Scope: finite energy-defined cutoffs; no claim that a finite cutoff partition function is a complete modular-invariant string partition function. References: existing bibliography plus the 2022 article 'Rényi Entropy and Free Energy' (Entropy 24, 706) cited in the verification record.
