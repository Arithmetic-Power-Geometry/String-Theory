# P36 — Coordinate-reflection duality and correction to B-sign interpretations

## Theorem
For any G positive definite, antisymmetric B, and R in GL(2,Z), the backgrounds (G,B) and (R^T G R,R^T B R) are equivalent under the integer charge transformation (m,n)->(R^T m,R^(-1)n), with a suitable convention for the metric coordinate transformation. More explicitly, for the involutive orthogonal reflection R=diag(-1,1), the charge map (m,n)->(Rm,Rn) preserves both energy and spin, while (a,c,d,b)->(a,c,-d,-b) in G=[[a,d],[d,c]], B=[[0,b],[-b,0]].

Proof for the reflection: R^T=R=R^-1, and B'=RBR, G'=RGR. Thus m'+B'n'=R(m+Bn), G'^-1=RG^-1R, and n'^T G'n'=n^T G n. Also m' dot n'=m dot n. The transformation is integral and preserves the Narain momentum-winding bilinear form, so is an allowed lattice-coordinate duality.

## Corollary
When d=0, G'=G and b'=-b. Thus the two sign-related diagonal-metric backgrounds are physically duality-equivalent, not examples of inequivalent CFTs with the same spectrum.

## Research implication
P34 and P35's algebraic identities remain correct but should not be interpreted as a physical nonuniqueness theorem on the Narain duality quotient. For d != 0 the reflection also changes d; the question whether (G,b) and (G,-b) are otherwise equivalent remains open here. No breakthrough or general inequivalence theorem is asserted.

## Verification
tests/test_p36.py checks 1875 charge identities on three exact rational non-diagonal backgrounds. Executed stdout/stderr and source integrity should be checked in evidence/E036_execution.md.
