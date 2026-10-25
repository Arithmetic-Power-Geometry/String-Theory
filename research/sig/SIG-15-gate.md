# SIG-15 — Independent verification and publication gate

## Independently reproduced

An independently implemented Python Fraction enumeration over the 729-charge completeness box confirms exactly two threshold witnesses per background sign and a minimum gap of 6/265 among all 574 other nonzero-spin charges on b in [1/10,2/5]. The minimizers occur at b=1/10. All comparisons use rational endpoint and quadratic-vertex evaluation. Local execution: PASS.

## Stability proof

For symmetric G with each entry within eps=1/10000 of G0=[[2,1/3],[1/3,3]], spectral norm ||G-G0|| <=2eps and lambda_min(G)>3/2. Thus ||G^-1-G0^-1|| <=4eps/5. For the relevant charge box, ||m+Bn||²<40, ||n||²<=2, and every energy shifts by at most 36eps. A competitor-to-witness energy gap shifts by at most 72eps=0.0072<6/265. The uniform charge-box completeness bound holds and the witness energy remains below 3. Hence the threshold witness remains first on this quantitative metric neighborhood. The exact polynomial T(b) is only for G0; for perturbed G the threshold is E_(G,B(+b))(-1,0,1,0).

## Prior-art kill-test

Verified literature examples:
1. 'Adding Flavor to the Narain Ensemble', JHEP 05 (2022) 090, https://cds.cern.ch/record/2753222/files/2102.12509.pdf. Standard Narain partition functions, conformal weights, moduli and dualities.
2. 'Spectral decomposition of the Narain partition function', JHEP 09 (2021) 174, https://inspirehep.net/files/8df4ba291ee56f17bd293b99f7b4d02d. Standard Narain partition-function spectral analysis.
3. SciPost Phys. 14, 019 (2023), https://scipost.org/SciPostPhys.14.2.019/pdf. Standard Siegel-Narain theta functions.

The foundational observables, spin refinement and integral B shifts are NOT new. This targeted search did not find the particular first-separation formula; that is not proof of priority.

## Decision

**GO for writing a carefully scoped research manuscript draft now; REVISE before submission.** Proposed focus: exact first spin-resolved distinguishing energy for a rational Narain two-torus family, its global periodic structure, and quantitative metric stability. Do not claim a new duality or new mathematical framework. Before submission, perform clean-environment script reruns, bibliography metadata checks, convention audit, and independent expert review. Preserve SIG-10's failed assertion and SIG-12 correction.
