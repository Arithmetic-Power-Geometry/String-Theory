# P38 — Full-energy isospectral but T-duality-inequivalent Narain backgrounds

Date: 2026-10-24

## Theorem (exact explicit counterexample)
Let G=[[2,1/3],[1/3,3]] and B_±=±[[0,1/5],[-1/5,0]]. The corresponding rank-two Narain backgrounds have identical unlabelled total zero-mode energy spectra at every energy, including multiplicities, but they are NOT equivalent under any O(2,2;Z) T-duality. Their spin-resolved zero-mode spectra differ at energy E=3373/1325.

## Proof, Part I — Isospectrality
For arbitrary positive G and antisymmetric B, E_(G,B)(m,n)=E_(G,-B)(-m,n), with the charge bijection (m,n)->(-m,n). Hence the entire unlabelled energy multisets coincide, not only the finite observed window.

## Proof, Part II — Exact complete spin witness
At W=3373/1325, the +B spectrum has N(W,+1)=2 and N(W,-1)=0, while the -B spectrum has N(W,+1)=0 and N(W,-1)=2. For +B the two +1 witnesses are (m1,m2,n1,n2)=(-1,0,-1,0) and (1,0,1,0).

Completeness of the finite witness enumeration: Gershgorin eigenvalue bounds for G are lambda_min>=5/3 and lambda_max<=10/3. If E<=3, then ||n||²<=9/5<2, so n is zero or a coordinate unit. Further ||m+Bn||²<=10 and ||Bn||<=1/5, hence |m_i|<=sqrt(10)+1/5<4. Enumerating the 729 charges in [-4,4]^2 x [-1,1]^2 includes all states of energy at most 3. Exact rational arithmetic finds 39 states per background below this cutoff, with the stated witness. This enumeration is independently reproducible in tests/test_p38.py.

## Proof, Part III — Duality obstruction
The O(2,2;Z) Narain T-duality group consists of integral automorphisms preserving the momentum-winding bilinear form. Such transformations preserve both the zero-mode energy (after transforming background) and s=m dot n, hence the complete joint multiplicity N(E,s). The unequal N(W,+1) multiplicities therefore rule out ANY O(2,2;Z) T-duality relating these two backgrounds. No bounded duality matrix search is needed.

## Corollary — Different oriented genus-one CFT partition functions
The left and right weights are determined by E and s. The oscillator sectors coincide for these two rank-two free-boson theories. Therefore the spin-resolved genus-one partition functions differ. Worldsheet parity exchanges left and right and can relate these theories as unoriented/parity-conjugate systems; that is not an orientation-preserving Narain T-duality.

## Scope and prior-art novelty
This is a concrete exact counterexample to injectivity of the total-energy spectrum on the orientation-preserving Narain T-duality quotient. The broader phenomenon of parity-conjugate spectra and left/right exchange is established in CFT literature; whether this explicit rational example or its formulation is publication-novel is NOT established. No new fundamental string dynamics or experimentally measured effect is claimed.

## References
Benjamin et al. (2021), Harmonic analysis of 2d CFT partition functions, JHEP09(2021)174, DOI 10.1007/JHEP09(2021)174, provides the Narain partition function and spin conventions. Afkhami-Jeddi et al. (2021), Free partition functions and an averaged holographic duality, JHEP01(2021)130, DOI 10.1007/JHEP01(2021)130, treats spinning spectra and the Narain moduli space. See reference/reference.bib and reference/P38_source_verification.md.

## Reproducibility
Exact executed source SHA256 c262804643e8f418d96c44798316148d9548d966ab255564134c3cfbbd3d9af6. Executed Git blob d7664c509077fb5a8b7113b4c31f7f9034c04ec7. Raw stdout/stderr and command: evidence/E038_execution.md.
