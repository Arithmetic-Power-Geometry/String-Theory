# P35 — Spin-reflected Narain spectra and left/right exchange

Date: 2026-10-24

## Exact theorem
Let G be any positive definite real symmetric 2-by-2 matrix, and B an antisymmetric matrix. For integer m,n define E_(G,B)(m,n)=(m+Bn)^T G^(-1)(m+Bn)+n^T G n and s(m,n)=m dot n. The map (m,n)->(-m,n) is a bijection of the charge lattice satisfying E_(G,-B)(-m,n)=E_(G,B)(m,n) and s(-m,n)=-s(m,n). Therefore the joint unlabelled multiplicity function obeys N_(G,-B)(E,s)=N_(G,B)(E,-s) at every energy and spin.

## Partition function consequence
With the standard left and right zero-mode weights h0=(E+2s)/4, hbar0=(E-2s)/4 (subject to the normalization convention for E), the spin-reflection bijection exchanges h0 and hbar0. Hence the full toroidal partition functions with identical oscillator sectors satisfy the formal identity Z_(G,-B)(q,qbar)=Z_(G,B)(qbar,q). This does not mean the two partition functions are always different; a parity-symmetric spectrum can make them equal.

## Decision criterion
The joint (E,s) spectrum distinguishes B from -B exactly if there is some (E,s) with N_(G,B)(E,s) != N_(G,B)(E,-s). This is a necessary-and-sufficient criterion for distinguishing the two spectra, not a proof that such a witness always exists. The charge bijection is not an O(2,2;Z) isometry because it reverses the integral momentum-winding pairing. Another unrelated T-duality might exist at special backgrounds. No general inequivalence assertion is made.

## Scientific status
This is an exact algebraic consequence of worldsheet orientation reversal. Its originality is not established and it must not be called a new fundamental string-theory effect. Further work should search for a certified spin-asymmetric witness, audit parity/duality equivalences, and compare with existing Narain CFT literature.

## Evidence and bibliography
Exact regression: tests/test_p35.py; raw stdout/stderr and hashes: evidence/E035_execution.md. 1875 exact charge-level checks on three non-diagonal rational metrics.
Relevant publisher-verified prior art: Ando, Kawabata and Nishioka (2026), DOI 10.1007/JHEP02(2026)058; Furuta (2022), DOI 10.1007/JHEP09(2022)146. The bibliography is maintained in reference/reference.bib.
