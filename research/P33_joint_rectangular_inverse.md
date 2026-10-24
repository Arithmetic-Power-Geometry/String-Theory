# P33 — Joint unlabelled spectral recovery of two radii and B-field

Date: 2026-10-24.

## Theorem T1
For G=diag(a,c), 3/2<=a,c<=2, B=[[0,b],[-b,0]] with 0<=b<=1/2, the multiset of zero-mode energies E<=17/8, including multiplicities, uniquely determines the unordered pair {a,c} and b within this family.

## Proof
E=(m1+b n2)^2/a+(m2-b n1)^2/c+a n1^2+c n2^2. Every nonzero-winding state has E>=min(a,c)>=3/2, so all levels E<1 are pure momentum. Since 1/a and 1/c lie in [1/2,2/3], and any pure momentum with m1²+m2²>=2 has E>=1, the levels below 1 consist exactly of the two coordinate-momentum energies 1/a and 1/c, each with multiplicity two, or one level of multiplicity four if a=c. Hence the unlabelled spectrum determines {a,c}.

Given {a,c}, compute the full pure-momentum multiplicity P(E) from the known diagonal quadratic form and subtract it from the observed spectral multiplicity to obtain the nonzero-winding residual R(E). By P32's unit-winding argument, its first support is W=min(a,c)+b²/max(a,c). The upper bound W<=min(a,c)+1/(4max(a,c))<=2+1/8=17/8 ensures this onset is observed. Since b>=0, b=sqrt(max(a,c)*(W-min(a,c))). Thus the inverse is unique.

## Interpretation and limitations
This is an exact finite-window inverse theorem with unknown metric parameters in a compact rectangular family, modulo swapping axes. The family is not claimed to be a fundamental domain for the full O(2,2;Z) duality action. The theorem is about unlabelled zero-mode energies, not an assertion of direct experimental measurement. No global Narain inverse theorem or unprecedented string-physics discovery is claimed. The cutoff is sufficient; optimality is not established.

## Computational verification
tests/test_p33.py enumerates all charge vectors in [-4,4]^4. The box is complete for E<=17/8: winding components satisfy |n_i|<2, while |m_i| <= sqrt((17/8)*2)+(1/2)sqrt((17/8)/(3/2))<3, so [-4,4] safely covers all. Exact Fraction arithmetic; 36 reconstruction cases. SHA256 d50acf08027c560d57d43664a6c98d96473d451951c569071fb261c7a4958126.

## Related work
Henriksson, Kakkar, McPeak (2023), JHEP04(2023)011, DOI 10.1007/JHEP04(2023)011, already demonstrates that higher-genus data can separate some genus-one isospectral theories. Nilsson, Rowlett, Rydell (2023), DOI 10.1090/bull/1770, reviews flat-torus inverse spectral problems. P33's novelty against the full prior art remains to be assessed.
