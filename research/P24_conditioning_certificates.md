# P24 — Conditioning and certified perturbation bounds for five-probe Narain reconstruction

Date: 2026-10-24. This result concerns **stability**, not a new fundamental string-theory prediction.

With x=E(e1), y=E(e2), p=E(e1+e2), w=E(e4), h=E(e1+e4), let u=(p-x-y)/2 and delta=xy-u^2>0. P21 reconstructs G=delta^-1 [[y,-u],[-u,x]], b=(h-x-w)/(2x).

THEOREM T1 (nonuniform instability). The reconstruction map is not globally Lipschitz on the admissible measurement domain. Choose x=y=1, u=1-epsilon, and perturb only p by epsilon (so u becomes 1-epsilon/2). Both datasets have positive delta, the input difference is epsilon, and G11 changes on the order of 1/epsilon. Thus the output/input ratio diverges as epsilon->0. Independently choose x=epsilon, y=1, u=0, w=1, h=epsilon+1 and perturb h by epsilon. Then b changes by 1/2 for input change epsilon, so the ratio is 1/(2epsilon). Both are exact rational families.

THEOREM T2 (conditional certificate). Suppose all five measured energies are perturbed in absolute value by at most eta. Then |u'-u|<=3eta/2 and
|delta'-delta| <= (|x|+|y|+3|u|)eta+(13/4)eta^2.
If x>eta and delta> (|x|+|y|+3|u|)eta+(13/4)eta^2, the perturbed inverse-metric matrix A' is positive definite, so the reconstruction remains valid. For the B-field,
|b'-b| <= (3eta/2+|b|eta)/(x-eta).
Proof: expand x'y'-u'^2 and apply triangle inequalities; write b'=N'/(2x'), b=N/(2x) with |N'-N|<=3eta and |x'-x|<=eta. The bound is exact for any real measurements satisfying the stated inequalities. Metric entrywise bounds follow from |1/delta'-1/delta|=|delta'-delta|/(delta*delta') and the adjugate entries.

IMPORTANT: This is classical inverse-problem conditioning analysis applied to the specific P21 formula. No originality claim against the literature and no string-theory breakthrough.

NEXT: P25 should determine if alternative charge-probe designs improve worst-case stability on a precisely bounded moduli domain, with independently verified optimization certificates.
