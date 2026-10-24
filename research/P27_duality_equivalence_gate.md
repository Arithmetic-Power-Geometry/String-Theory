# P27 — Operational equivalence gate for labelled Narain reconstruction

Date: 2026-10-24.

## Theorem
For two-torus backgrounds, the energy E_(G,B)(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n. If K is integral antisymmetric, then E_(G,B+K)(m-Kn,n)=E_(G,B)(m,n). Thus charge-resolved energies are **equivariant** under the duality action, not invariant at fixed coordinate labels.

## Counterexample
For G=I, B=0 and B'=J=[[0,1],[-1,0]], the charge e4=(0,0,0,1) has energy 1 at B=0 and energy 2 at B'=J if the numerical label is held fixed. The charge e1+e4 has energies 2 and 5. Under the correct relabelling, e4 maps to (-1,0,0,1), energy 1 at B'=J, and e1+e4 maps to (0,0,0,1), energy 2 at B'=J.

Therefore the P21 five-probe reconstruction yields a coordinate-dependent representative of the background; without a physical prescription for identifying and transporting charge labels, it is not a duality-invariant observable of the CFT. This is a conceptual obstruction to treating P21–P26 as a new physical reconstruction breakthrough. It does not imply that charge-resolved data are meaningless: once a basis is chosen, reconstruction is exact.

## Research decision
No new string-theory breakthrough is established. Further probe optimization without resolving observability, duality quotient, and prior-art novelty should stop. A defensible next project would define a duality-invariant inverse problem from intrinsic CFT observables, compare existing Narain spectral rigidity/ispectrality literature, and seek a genuinely new separation theorem.

## Reproducibility
See tests/test_p27.py and evidence/E027_execution.md. The exact source is committed verbatim from the locally executed file; compare SHA256 after checkout.
