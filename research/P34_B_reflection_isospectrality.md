# P34 — B-field reflection isospectrality of Narain total energies

## Theorem
For any positive definite symmetric 2x2 G and antisymmetric B, define E_(G,B)(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n on Z^2 x Z^2. Then E_(G,-B)(-m,n)=E_(G,B)(m,n). Consequently the full unlabelled total-energy multiset, with all multiplicities, is identical at B and -B, at every energy.

## Proof
The shifted momentum transforms as -m-Bn=-(m+Bn), and a quadratic form is even. The winding term is unchanged. The mapping (m,n)->(-m,n) is a lattice bijection.

## Spin distinction and physical limitation
The standard integral momentum-winding pairing m dot n changes sign under this relabelling. Therefore this particular bijection does not preserve the Narain bilinear form and is not itself an O(2,2;Z) T-duality. This observation does not prove that B and -B are never related by some *other* duality; for special backgrounds they may be. It also does not prove the full spin-resolved CFT partition functions coincide. The result concerns total zero-mode energy alone.

## Consequence
Any inversion procedure using only the unlabelled total-energy spectrum cannot determine the sign of B on an unrestricted parameter domain. This is an exact information obstruction that remains even at infinite spectral cutoff. Restricting b>=0 in P31–P33 was therefore essential to those inversions. No novelty claim is made without a rigorous comparison to prior art.

## Evidence
tests/test_p34.py and evidence/E034_execution.md. Three exact non-diagonal rational metrics, 625 charges each, total 1875 checks; analytic proof covers all admissible backgrounds.
