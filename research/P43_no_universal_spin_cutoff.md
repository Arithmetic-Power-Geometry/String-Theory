# P43 — No universal finite spin-refined spectral cutoff on unrestricted Narain moduli

## Theorem
For every real C>0, there exist rank-two Narain backgrounds (G,B) and (G,-B) that have the same complete unlabelled energy spectrum, have identical joint energy-and-spin multiplicities at every E<=C, but are inequivalent under O(2,2;Z). Their complete joint energy-spin spectra differ.

## Proof
Take G_L=L G0 with G0=[[2,1/3],[1/3,3]], B=([[0,1/5],[-1/5,0]]) and L>0. Gershgorin gives lambda_min(G_L)>=5L/3. For any nonzero winding n, E(m,n)>=n^T G_L n>=5L/3. Choose L>3C/5. Thus all states with E<=C have n=0 and s=m dot n=0; their energy is m^T G_L^-1 m, independent of B. Therefore the spin-refined finite-cutoff spectra agree.

For every spin -1 integer charge w, define f_w(L)=E_(G_L,B)(v)-E_(G_L,B)(w) with fixed v=(1,0,1,0), spin +1. Since G_L=L G0, E(m,n)=L n^T G0 n + L^-1 (m+Bn)^T G0^-1 (m+Bn). Thus L f_w(L) is a polynomial in L² of degree at most one. At L=1, P38's complete exact certificate proves f_w(1)!=0 for every spin -1 charge w. Hence each f_w is a nonzero rational function with finitely many positive zeros. The union of exceptional scales over countably many w is countable. In particular arbitrarily large L avoid all collisions, and at those L the energy E(v) occurs at spin +1 but never at spin -1.

For any such L, the exact involution (m,n)->(-m,n) identifies the complete energy spectra of B and -B and reverses spin. Hence their joint energy-spin spectra differ, which obstructs every O(2,2;Z) duality, as that group preserves spin. Combining with the cutoff argument proves the theorem.

## Interpretation and limits
The quantifiers are: for EVERY fixed finite C, there EXISTS a sufficiently large L outside a countable exceptional set. This is not a claim that EVERY large L yields a nondual pair, nor that finite data are useless on compact moduli subsets. The result concerns orientation-preserving Narain duality, not worldsheet parity. The analytic step uses the P38 complete witness certificate at L=1, not finite numeric extrapolation.

## Novelty and publication status
P29 already proved no universal finite cutoff for unrefined energy data. P43 extends this to finite spin-refined data while insisting on genuine O(2,2;Z) inequivalence, rather than just differing B labels. It is a new theorem within the programme; global literature novelty is unverified. Published code-CFT isospectral examples and parity literature prevent claiming first discovery of isospectral CFTs.

## Evidence
Exact Python tests at L=10 and L=100 with cutoff 1, plus analytic proof for arbitrary C. Source SHA256 640c9d7149551c485828b1938b12d58889a7dd6701a3a0e6a7913b1636a2a538; Git blob 1c0d1684b5bc38801210eb54368c1925e5120e15.
