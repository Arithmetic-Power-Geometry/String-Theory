# P31 — Finite-window B-field recovery in a bounded Narain subfamily

Date: 2026-10-24.

## Theorem P31-T1
Fix G=L I_2 with L>=1 and B_b=[[0,b],[-b,0]] with b in [0,1/2]. Let the unlabelled zero-mode energy spectrum include multiplicities. Define the known pure-momentum spectral multiplicity P_L(E) from n=0, and the residual R_b(E)=multiplicity(E)-P_L(E). Then R_b(E) is a nonnegative integer and its smallest supported energy is W_b=L+b^2/L.

Proof: The energy is ||m+B_b n||^2/L+L||n||^2. For unit winding, the minimum over integer m is L+b^2/L because the nearest integer to b in [0,1/2] is zero (ties at 1/2). For ||n||^2>=2, energy >=2L; since L>=1 and b<=1/2, L+b^2/L<=L+1/(4L)<2L. Thus the minimum winding energy is W_b. The full spectral multiplicity is the sum of the pure-momentum and nonzero-winding counts, so subtracting the known pure-momentum multiplicities recovers the winding residual without individually labelling observed states.

## Corollary P31-C1 — Explicit inverse and uniform finite cutoff
The parameter b is uniquely determined on [0,1/2] by b=sqrt(L*(W_b-L)). Every W_b is <= C*=L+1/(4L). Therefore the full unlabelled spectrum through C* identifies b for known L in this restricted family. The claim is NOT an unrestricted Narain moduli reconstruction theorem. Distinct b values in this interval yield different complete zero-mode spectra and therefore cannot be T-dual.

## Sharpness of uniform cutoff
For b=1/2 the first winding state has energy exactly C*. Every cutoff C<C* misses that state's onset. However, whether a smaller cutoff could already distinguish b=1/2 from *all* other b is a separate question; do not infer a universal minimax optimality claim from the onset alone.

## Caveats
The result relies on prior knowledge of L and a restricted gauge interval for b. The restriction is an assumed family, not a claimed complete O(2,2;Z) fundamental domain. The zero-mode spectrum is a component of the CFT data; the theorem does not assert experimentally accessible measurements or originality relative to theta-series inverse problems. This is a clean positive theorem complementing P29's unrestricted NO-GO.

## Evidence
tests/test_p31.py, evidence/E031_execution.md. Exact arithmetic, 20 onset checks and 75 pairwise separation checks. SHA256 1c333b834b023363657c341c0d4deaea6ee3d85be79b8e3b750754da23e2b667.
