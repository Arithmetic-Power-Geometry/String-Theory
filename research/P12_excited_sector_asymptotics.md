# P12 — Exact low-temperature APG excitation entropy and self-dual degeneracy
Date: 2026-10-24. Scope: full circle charge lattice, excluding the vacuum, in alpha'=1 units. Novelty: NOT ESTABLISHED.

Let E_R(m,n)=m²/R²+n²R². On S=Z²\{(0,0)}, define Z*_R(t)=sum_S exp(-tE_R) and p*_(m,n)=exp(-tE_R)/Z*_R(t). Define the APG escort defect D*_(2q)=1-sum_S (p*)^q, q>1.

THEOREM P12-T1. Let g(R) be the multiplicity of the lowest positive energy. Then lim_(t->infinity) D*_(2q)(R,t)=1-g(R)^(1-q). For R !=1, g(R)=2; for R=1, g(1)=4. Therefore the limit equals 1-2^(1-q) off the self-dual point and 1-4^(1-q) at it. Proof: the positive-definite quadratic form has a discrete spectrum and a strictly positive gap to the next distinct energy. Factor exp(-t E_min) out of Z* and its q-temperature counterpart. Dominated convergence for any fixed t0>0 shows Z*_R(t) exp(t E_min)->g(R). Substitute D*=1-Z*(qt)/Z*(t)^q. The minimal nonzero charges are (+/-1,0) or (0,+/-1), with both families tied exactly at R=1.

THEOREM P12-T2. D*_(2q)(R,t)=D*_(2q)(1/R,t) for all R,t>0 and q>1. Proof: exchange momentum and winding integer charges.

NONCOMMUTING LIMITS. At R=1, lim_(t->infinity)D*=1-4^(1-q). But lim_(R->1)lim_(t->infinity)D*=1-2^(1-q). Thus the low-temperature and self-dual-radius limits do not commute. At any finite t>0 the function of R is continuous.

PHYSICAL LIMITATION. This is a conditioned distribution on excited lattice charges, not the thermal state of the full compact boson CFT. Excluding the vacuum is a mathematical conditioning, not a claim of a new physical order parameter. The degeneracy enhancement at self-dual radius is familiar from compact-boson theory; the power-sum limit is standard Gibbs asymptotics. This is a sharp theorem and useful APG research diagnostic, not an established string-theory breakthrough.

NEXT. Derive uniform crossover bounds as R->1, t->infinity with t*(R²-R^-2) fixed, then check whether the scaling function is already standard two-level statistical mechanics.
