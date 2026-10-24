# P25 — Charge scaling and certified error attenuation
Date: 2026-10-24

Let E(v) be the quadratic Narain energy and let P21 use five charge probes v1,...,v5. For every integer k>=1, E(kv)=k^2 E(v). Hence dividing five scaled charge measurements by k^2 recovers the original five exact measurements, and P21 reconstructs (G,B).

THEOREM P25-T1: If each raw scaled-charge energy observation differs from its true value by at most epsilon in absolute value, its normalized value differs from E(v) by at most eta=epsilon/k^2. The P24 sufficient positive-definiteness certificate therefore applies with eta=epsilon/k^2. In particular, for x=E(e1)>0, if only the fifth raw measurement has additive error delta, the reconstructed b error is exactly delta/(2*k^2*x). This is a deterministic, absolute-noise result, not a statistical noise model.

THEOREM P25-T2: With x,y,p,w,h the true unscaled measurements, u=(p-x-y)/2 and Delta=xy-u^2, define eta=epsilon/k^2 and D=(|x|+|y|+3|u|)*eta+(13/4)*eta^2. If x>eta and Delta>D, every five-component error vector bounded by eta produces a positive-definite reconstructed inverse metric. Furthermore |bhat-b|<=((3/2)+|b|)*eta/(x-eta). Proof: expand the determinant and use |u'-u|<=3eta/2; use quotient perturbation for b=(h-x-w)/(2x).

LIMITATION: k-scaled states can have energy growing as k^2, so this does not prove practical improvement when noise, preparation cost, or accessible energies scale with charge. Scaling and perturbation theory are standard mathematics. No new physical prediction or established breakthrough.

EXACT EXECUTION: python /mnt/data/p25/test_p25.py exited 0. 288 scaled reconstructions and 512 bounded-noise corners passed. The exact executed source SHA256 is fe722ba14baed133bb8af6d47f7c2329379c79b7ceb5e720123972ad04b0c23e. See E025 evidence. 
NEXT: establish an explicit cost/error model and optimize charge magnitude subject to physical constraints; seek a genuinely nontrivial optimal-design theorem rather than claiming quadratic scaling is novel.