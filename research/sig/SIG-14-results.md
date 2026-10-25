# SIG-14 — Quantitative metric robustness and paper readiness

## New result

Fix G0=[[2,1/3],[1/3,3]]. For any real b in [1/10,2/5], and any symmetric real 2x2 metric G with max entrywise difference |G-G0| <= 1/10000, the first joint energy-spin separation of (G,B(+b)) and (G,B(-b)) occurs at the energy of charge (-1,0,1,0) in the positive-B background, with two spin -1 witnesses; the negative-B counterpart has two spin +1 witnesses. Its energy is now T_G(b)=E_(G,B(+b))(-1,0,1,0), generally **not** the fixed-G polynomial T(b).

## Exact certificate

The independent SIG-14 script compares all 576 nonzero-spin charges per B sign in the uniform 729-charge box to T_G0(b). On the entire closed b interval [1/10,2/5], precisely two charges per sign are identically at threshold; the minimum of the other 574 quadratic energy gaps, including endpoint and vertex checks, is exactly 6/265.

For the metric perturbation H=G-G0 with |H_ij|<=eps=1/10000, the spectral norm ||H||_2<=2eps. Since lambda_min(G0)>=5/3, lambda_min(G)>=5/3-2eps>3/2. The inverse perturbation bound is ||G^-1-G0^-1||_2 <= (2eps)/((5/3)(3/2)) = 4eps/5. In the 729 box and b<=2/5, ||m+Bn||^2 <40 and ||n||²<=2, so each energy changes by at most (4/5)*40eps+2eps*2=36eps. The difference between any candidate energy and the witness threshold changes by at most 72eps=9/1250 <6/265. Therefore the 574 strict gaps remain positive for all permitted metrics. The two witness charge polynomials remain exactly equal because of inversion symmetry, and the opposite B sign maps witness charges by n->-n.

Uniform completeness remains valid: if E<=3, then ||n||²<=3/(5/3-2eps)<2, so n_i in {-1,0,1}; also ||m+Bn||²<=3*(10/3+2eps), hence |m_i|<=sqrt(10+6eps)+(2/5)*sqrt(2)<4. The proposed witness energy is <3 throughout the parameter rectangle. Thus no excluded integer charge can beat the witness. Spin-zero counts match by parity, proving the claim.

## Improvements and limits

This is a rigorous quantitative local stability result for a **three-dimensional parameter family** (three independent G entries) times the one-dimensional b interval, not a universal Narain theorem. The robustness margin is conservative; no maximality claim. The integer B-shift periodic extension applies to any fixed G but the precise threshold formula changes with G.

Novelty is unresolved: B-shifts, parity, spectral theta functions, perturbation estimates and lattice bounds are established. The candidate contribution is the explicit first-separation formula plus an independently checkable quantitative stability theorem.

## Manuscript gate

**REVISE.** Start an outline and a theorem/proof dossier now; write a full journal manuscript only after an independent reproduction of SIG-14, reference verification, and a strong novelty kill-test on existing spin-refined theta-series and Narain partition-function literature. Avoid claiming a new mathematics or a new duality. Preserve SIG-10's incorrect endpoint assertion and SIG-12 correction append-only.
