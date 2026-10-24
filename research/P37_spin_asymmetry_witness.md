# P37 — Exact spin-asymmetry witness for a non-diagonal Narain background

## Certified result
For G=[[2,1/3],[1/3,3]] and B=[[0,1/5],[-1/5,0]], the joint zero-mode multiplicities at E=3373/1325 satisfy N(E,s=+1)=2 and N(E,s=-1)=0. The two +1 charges are (m1,m2,n1,n2)=(-1,0,-1,0) and (1,0,1,0).

## Complete exact certificate
Gershgorin gives lambda_min(G)>=5/3 and lambda_max(G)<=10/3. Any state of energy E<=3 obeys ||n||²<=3/(5/3)=9/5, so n=0 or a coordinate unit vector. Also ||m+Bn||²<=3*(10/3)=10 and ||Bn||<=1/5. Hence |m_i|<sqrt(10)+1/5<4. Every eligible integer charge therefore lies in [-4,4]^2 x [-1,1]^2. Exact rational exhaustive enumeration over this complete box yields 39 states with E<=3, and the first energy with unequal positive/negative spin multiplicities is 3373/1325. All claims are checkable by tests/test_p37.py.

## Interpretation
By P35, B->-B with momentum sign reversal sends N_(G,B)(E,s) to N_(G,B)(E,-s). Thus the two sign-related backgrounds have identical total-energy spectra but distinct spin-resolved zero-mode spectra for this fixed non-diagonal G. Consequently their spin-refined genus-one partition functions differ. This does NOT establish distinct full CFTs modulo O(2,2;Z), and a rigorous duality-orbit exclusion remains an explicit open gate.

## Novelty caution
Worldsheet parity, spin refinement and Narain theta functions are established subjects. This is a new-to-this-programme explicit exact witness, not a demonstrated previously unknown physical effect. Prior art must be checked before a novelty claim.

## Reproducibility
Executed source SHA256: 72d1b1375ecd69c784ef3760809831a268f0574d4df86ef9a06b6154a5f83c7c
Executed source Git blob: eb56081d375118862fe00796969686ae5647bce3
