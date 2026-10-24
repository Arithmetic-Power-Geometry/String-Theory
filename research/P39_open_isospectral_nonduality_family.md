# P39 — Open family of energy-isospectral, T-duality-inequivalent Narain pairs

Date: 2026-10-24

## Theorem
Let G=[[a,d],[d,c]], B=[[0,b],[-b,0]] with rational or real parameters satisfying |a-2|, |c-3|, |d-1/3|, |b-1/5| <= 1/1000000. Then G is positive definite and the spin-refined Narain zero-mode spectrum is asymmetric under s->-s. In particular the two backgrounds (G,B) and (G,-B) have identical unlabelled total-energy spectra at all energies but are inequivalent under orientation-preserving O(2,2;Z) T-duality.

## Proof
For any G,B, the charge involution (m,n)->(-m,n) establishes complete energy isospectrality and flips s=m dot n. The P38 base point admits a witness charge (m1,m2,n1,n2)=(1,0,1,0) with s=1 and energy W=3373/1325, but no state of s=-1 at W. The nearest opposite-spin energy among all states E<=3 at the base point is 3313/1325, with gap 12/265.

To make the witness stable under perturbations, apply exact rational interval arithmetic to the explicit energy expression E=(c(m1+bn2)^2-2d(m1+bn2)(m2-bn1)+a(m2-bn1)^2)/(ac-d²)+a n1²+2d n1n2+c n2². On the stated parameter cube, Gershgorin bounds give lambda_min(G)>=1.65 and lambda_max(G)<=3.35, and |b|<=0.21. Thus any state E<=3 has ||n||²<2, hence n=0 or a coordinate unit vector, and |m_i|<=sqrt(3*3.35)+0.21<4. The finite charge box [-4,4]^2 x [-1,1]^2 is therefore complete for all states E<=3 at every point of the parameter cube.

The exact interval-arithmetic certificate in the locally executed tests/test_p39.py checks that the energy interval of the fixed +1-spin witness is disjoint from the energy interval of EVERY -1-spin charge in this complete box (68 opposite-spin charge vectors). The witness energy is <3 throughout the cube, so no omitted charge can match it. Consequently the spin-resolved spectra differ for all backgrounds in the cube. Because genuine O(2,2;Z) duality preserves both E and s, the B-reversed pair cannot be dual.

## Scientific limitations
This is an explicit certified open set, not a classification of all parity-asymmetric Narain backgrounds. The underlying parity-conjugation phenomenon is established in CFT and no previously unknown fundamental string-theory mechanism is claimed. Distinguish orientation-preserving T-duality from worldsheet parity. Novelty review remains pending.

## Execution
Local exact-arithmetic interval source SHA256: 6b677bf5c8167fe020df7231a2c1fcb4875abad6c39c351f2719c62b4ca98e44; Git blob of that executed local source: edf41ad7d615c90fcc9c0ad1aa4af04bb4ff26fa. See evidence/E039_execution.md for the execution record. The exact executed source is not yet archived in GitHub and must be uploaded byte-identically before an execution-provenance claim can be made.
