# P32 — Exact anisotropic rectangular Narain B-field spectral recovery

Date: 2026-10-24

## Setup
G=diag(a,c) with a,c>=1 and B=[[0,b],[-b,0]], b in [0,1/2]. The zero-mode energy of integer charge (m1,m2,n1,n2) is
E=(m1+b*n2)^2/a+(m2-b*n1)^2/c+a*n1^2+c*n2^2.

## T1 — Exact winding onset
The smallest energy among all n != 0 is W=min(a,c)+b^2/max(a,c).

Proof: For unit winding n=(+/-1,0), the nearest integer momenta give a+b^2/c; for n=(0,+/-1), they give c+b^2/a. Since ac>=1 and b^2<=1/4, the difference (c+b^2/a)-(a+b^2/c)=(c-a)(1-b^2/(ac)) has the sign of c-a. Thus the smaller unit-winding value is min(a,c)+b^2/max(a,c). All windings with n1^2+n2^2>=2 have energy at least 2 min(a,c). The unit-winding candidate is <=min(a,c)+1/(4 max(a,c)) <=(5/4)min(a,c)<2min(a,c). Hence higher winding cannot minimize.

## T2 — Recovery from the unlabelled spectrum
For known a,c, subtract the known pure-momentum multiplicity at each energy from the full unlabelled zero-mode multiplicity. This nonnegative residual counts n!=0 states and has first support at W. Since b>=0, the inverse is b=sqrt(max(a,c)*(W-min(a,c))). Thus the complete unlabelled zero-mode spectrum through the finite cutoff C*=min(a,c)+1/(4max(a,c)) identifies b within the restricted family.

## Scope and cautions
The theorem assumes a,c known and >=1 and a rectangular metric in a fixed family; it is not an inversion theorem on the full Narain duality quotient. Extracting the residual is a mathematical operation on an exact spectrum, not an assertion of direct charge measurement. Sharpness of C* as a minimax identification cutoff is NOT proved. Novelty against established Narain theta-function inverse problems is NOT proved. No physics breakthrough is claimed.

## Execution
Exact source: tests/test_p32.py; stdout and integrity: evidence/E032_execution.md. Executed SHA256 aa982fcf0626f8250b04fb775295fae89fd1991c8db27068bc50b864ad20ae63; Git blob a9ebdbcbe30f6677def177d46c2fb26489d8fc6d.

## Verified literature
Benjamin et al. (2021), JHEP 09 (2021) 174, DOI 10.1007/JHEP09(2021)174.
Henriksson, Kakkar and McPeak (2023), JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011.
