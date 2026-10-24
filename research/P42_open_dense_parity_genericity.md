# P42 — Open-dense full-measure parity asymmetry, with priority correction

## Theorem
Let D={(a,c,d,b) in R^4: a>0, ac>d^2}. For a fixed integer charge v=(1,0,1,0) with spin +1, let U consist of backgrounds where no spin -1 charge w has E(w)=E(v). Then U is OPEN, DENSE, and of full four-dimensional Lebesgue measure in D. For every background in U, its B-sign-reversed partner has identical unlabelled energy spectrum at all energies but cannot be related by O(2,2;Z) T-duality.

## Proof
E_x(w) is a positive-definite quadratic form on R^4 in the integer charge vector w, depending continuously (indeed analytically) on x=(a,c,d,b). For any compact K subset D, uniform coercivity supplies a constant alpha_K>0 such that E_x(w)>=alpha_K ||w||² for all x in K and all integer w. The fixed witness energy E_x(v) is bounded above by M_K on K. Hence any charge w satisfying E_x(w)=E_x(v) for some x in K must satisfy ||w||²<=M_K/alpha_K. Only finitely many integer w meet this condition. Thus the collision loci Z_w={x:E_x(w)=E_x(v)} indexed by spin(w)=-1 form a LOCALLY FINITE family of closed sets, so their union Z is closed in D.

For each w, E_x(v)-E_x(w) is real analytic on the connected open D. It is not identically zero: at the rational base point x0=(2,3,1/3,1/5), E(v)=3373/1325, while the exact complete P38 certificate proves no spin -1 charge has this energy. The finite certificate is independently checked by tests/test_p42.py: every state with energy <=3 lies in [-4,4]^2 x [-1,1]^2, and 68 opposite-spin charges in that box have minimum absolute separation 12/265 from the witness. For charges outside the box, E>3>E(v). Therefore each Z_w is closed, nowhere dense and measure zero.

A locally finite union of nowhere dense closed sets is nowhere dense, and the countable union is null. Hence U=D\Z is open, dense and full measure. For x in U, the spin +1 witness has no opposite-spin counterpart. The charge map (m,n)->(-m,n) proves full-energy isospectrality for B and -B but flips spin; O(2,2;Z) preserves spin and therefore cannot relate them. QED.

## Limits
U is a sufficient subset of spin-asymmetric backgrounds, not a complete classification of all such backgrounds. Open/dense/full-measure refers to parameter domain D before duality quotient; coordinate Lebesgue measure is not claimed to be a canonical normalized Narain measure. Worldsheet parity is distinct from orientation-preserving O(2,2;Z). No physical discovery or absolute novelty claim is made.

## Prior art and priority correction
Hosono, Lian, Oguiso, Yau (2003), *c=2 Rational Toroidal Conformal Field Theories via the Gauss Product*, Communications in Mathematical Physics 241, 245–286, DOI 10.1007/s00220-003-0927-0, explicitly define parity-invariant partition functions and discuss worldsheet parity (tau,rho)->(tau,-conjugate(rho)). This directly precedes the parity aspect of P34–P42. Dulat and Wendland (2000), *Crystallographic Orbifolds: Towards a Classification of Unitary Conformal Field Theories with Central Charge c=2*, JHEP 06 (2000) 012, DOI 10.1088/1126-6708/2000/06/012, classify c=2 orbifold families. These works must be cited and compared before publication.

## Reproducibility
Exact executed test SHA256 41b408ea50c17eec6832f02acfdb79a9609a3bfee7290ce551bc1a5b21f7c04f; Git blob 2f6269d3bb6b99bfed65f25fe039c9024f0eb42a. The Python test verifies the finite witness; the local finiteness and genericity conclusions are mathematical deductions, not computer-verified exhaustive claims.
