# P41 — Generic spin asymmetry and full-measure energy-isospectral nondual pairs

## Theorem
Let D={(a,c,d,b) in R^4 : a>0, ac>d²}, G=[[a,d],[d,c]], B=[[0,b],[-b,0]]. Outside a measure-zero, meagre subset of D, the Narain spin-resolved zero-mode spectrum is asymmetric under spin reversal. For every such parameter, (G,B) and (G,-B) are identical in the entire unlabelled total-energy spectrum but are not related by any orientation-preserving O(2,2;Z) T-duality.

## Proof
Fix v=(m1,m2,n1,n2)=(1,0,1,0), with spin +1. For each integer w with m_w dot n_w=-1, define f_w(a,c,d,b)=E(v)-E(w). This is real-analytic on connected D (indeed rational with nonvanishing determinant ac-d²). At the exact rational base point (2,3,1/3,1/5), E(v)=3373/1325 and NO spin -1 charge has that energy. Completeness is certified as follows: Gershgorin eigenvalues of G are bounded below by 5/3 and above by 10/3. Any state of energy E<=3 has ||n||²<=9/5<2, and |m_i|<=sqrt(10)+1/5<4. Hence all possible opposite-spin charges at E(v)<3 lie in [-4,4]^2 x [-1,1]^2. Exact Fraction enumeration verifies no collision (68 opposite-spin charges in the box), with minimum absolute energy gap 12/265. For charges outside the box, E(w)>3>E(v). Therefore f_w is not identically zero on D for every spin -1 charge w.

The zero set of a nonzero real-analytic function on a connected open domain has Lebesgue measure zero and empty interior. The countable union Z=union_{w:spin(w)=-1} {f_w=0} is null and meagre. For each parameter outside Z, the energy E(v) is attained at spin +1 but not spin -1, so the spin spectrum is asymmetric. By the universal charge bijection (m,n)->(-m,n), total-energy spectra of (G,B) and (G,-B) coincide at every energy, while the joint spin multiplicities reflect s->-s. Since O(2,2;Z) preserves the spin pairing, the spin-asymmetric pair cannot be related by such a T-duality. QED.

## Meaning
This strengthens P39/P40 from a particular nonempty open cube to a full-Lebesgue-measure, comeagre set of backgrounds. It does not say the complement is empty, nor does it imply physical inequivalence when worldsheet parity is admitted as an equivalence. The measure is ordinary coordinate Lebesgue measure on D, not a normalized invariant measure on moduli space.

## Novelty limitations
The parity mechanism, Narain theta functions and spin-resolved partition functions are established. The countable analytic-zero-set argument and concrete certified rational base witness may be a useful explicit inverse-spectral theorem, but literature priority is unestablished. No claim of discovering new fundamental string dynamics.

## Test provenance
tests/test_p41.py was executed locally with exact rational arithmetic, exit 0. Source SHA256 e182deab2071875fb15854479abe00eb13c73717fc1a417fea63f5370bb8df73; Git blob 965bf6a0b18c15e88f880d2d37f5b159c4426d62. Evidence/E041_execution.md contains stdout and stderr.
