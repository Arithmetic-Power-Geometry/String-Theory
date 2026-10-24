# P04 — Duality-compatible Arithmetic Power Geometry on rectangular tori
Date: 2026-10-24
Status: exact mathematical construction, restricted toy model; no string-theory breakthrough claim.

## Motivation and source mapping
APG I and Shannon–Rényi Control motivate the power-sum closure defect 1-sum_i w_i^(p/2) at the Euclidean baseline p=2. APG II develops information-geometric weights; APG V insists on respecting arithmetic and geometric domains. The APG IX–XIII spectral route does not establish physical T-duality invariance. Here we impose the basic radius-inversion symmetry required by factorized toroidal T-duality, rather than identifying APG exponent variation with string worldsheet dynamics.

## Definition
Work in string units alpha'=1 on a diagonal rectangular d-torus with radii R_i>0 and vanishing B field. Consider only factorized radius inversions R_i -> 1/R_i and coordinate permutations. The full O(d,d;Z) duality group is NOT treated; other background fields, dilaton transformations, moduli and string interactions are NOT modeled.

Define ordinary squared-radius weights w_i=R_i^2/(sum_j R_j^2). Define modified q_i=R_i^2+R_i^(-2), v_i=q_i/(sum_j q_j). For real p>0 set D_p(v)=1-sum_i v_i^(p/2), and H(v)=-sum_i v_i log(v_i).

## Proposition P04-T1 (exact restricted invariance)
For every d>=1, positive radius vector and p>0, D_p(v) and H(v) are invariant under each R_i -> 1/R_i and under permutations. Proof: q_i is unchanged by inversion; permutations permute the q_i; sums of symmetric functions of normalized q_i are unchanged. In particular D_2=0. This is elementary symmetry and not a claim of a novel general invariant.

## Proposition P04-T2 (raw APG weights fail duality invariance)
For d=2, R=(2,3) gives w=(4/13,9/13), D_4(w)=72/169. Inverting the first radius gives R'=(1/2,3), w'=(1/37,36/37), D_4(w')=72/1369. Therefore naive radius-squared APG defect does not descend to the restricted duality quotient.

## Proposition P04-T3 (exact repaired witness)
For both R and R', q=(17/4,82/9), v=(153/481,328/481) and D_4(v)=100368/231361. This is verified by exact rational arithmetic.

## Interpretation
T1 is a mathematically correct quotient construction. It is NOT evidence that APG modifies string theory, since duality-invariant functions of radii are abundant and the full O(d,d;Z) action on the generalized metric is not addressed. Physical quantities require mass spectra, dilaton and B-field consistency and an actual worldsheet or effective-action derivation.

## Falsification and next step
P05: construct a full O(d,d;Z)-invariant quantity from the Narain momentum-winding lattice and ask whether an APG power-sum deformation supplies a nontrivial, convergent and independently meaningful invariant beyond theta series and partition functions. Compare to established Narain lattice and automorphic literature. Any expression merely derived from the known partition function is not a breakthrough.
