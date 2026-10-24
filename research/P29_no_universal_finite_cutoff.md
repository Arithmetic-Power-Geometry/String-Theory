# P29 — No universal finite spectral cutoff on unrestricted two-torus Narain moduli
Date: 2026-10-24

## T1: Universal finite-window obstruction
For any finite C>0 choose L>C and G=L I_2, B_b=[[0,b],[-b,0]]. The zero-mode energy is E_b(m,n)=||m+B_b n||²/L+L||n||². For nonzero n, E_b>=L>C. Thus all energies <=C arise from n=0, where E_b(m,0)=||m||²/L is independent of b. Therefore the complete unlabelled energy multiset including multiplicities below C is independent of b. This is an exact statement for every real b, not a finite-sample inference.

## T2: Physically inequivalent witnesses
Choose integer L>C, b=0 versus b=1/2. At energy E=L, pure-momentum contributions are the same. For b=0, exactly four additional states with ||n||²=1 and m=0 have energy L. For b=1/2, all nonzero-winding states have E>L: if ||n||²>=2 then E>=2L; if ||n||²=1, Bn is half-integral and m+Bn !=0 for any integral m. Therefore multiplicity at E=L differs by four. Since T-duality preserves the full zero-mode spectrum, these backgrounds are not duality-equivalent.

## Consequence
There exists no background-independent finite cutoff that identifies every duality class from the unlabelled zero-mode spectrum over the unrestricted moduli space. This is a precise obstruction, not a proof that no finite cutoff exists on compact, bounded moduli subsets. Oscillator contributions in the same c=2 Narain CFT are universal; with a consistent normalization, the common low-energy zero-mode data also imply agreement of the corresponding sufficiently low conformal-dimension data. Full modular-invariant partition functions are not identical.

## Novelty and prior art
The proof uses standard winding-energy positivity and B-field dependence. Novelty against the broad literature on Narain moduli and inverse spectral theory is not established. It is a clean theorem and a decisive NO-GO for the programme's proposed unrestricted uniform-cutoff objective, not a fundamental physics breakthrough.

## Reproducibility
See tests/test_p29.py and evidence/E029_execution.md. Exact rational arithmetic. Executed SHA256 a238ccc4748804cd354e23338cceaf852e245ddf4a59cf7a8690517a72feb068. Executed Git blob d5e50c07ee7423dbccdcd8d7b7fcc799fd5a9041.
Next: prove effective thresholds on compact reduced moduli domains, or identify an intrinsic physical observable carrying nonstandard information. Do not repeat unbounded cutoff search.
