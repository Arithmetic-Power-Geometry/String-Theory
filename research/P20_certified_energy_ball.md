# P20 — Certified energy-ball enumeration and B-shift covariance
Date: 2026-10-24

## Exact theorem
For diagonal G=diag(g1,g2)>0 and B12=b=-B21, E(m,n)=(m+Bn)^T G^-1(m+Bn)+n^T G n. For energy threshold C>=0, all vectors satisfying E<=C obey |n_i|<=sqrt(C/g_i), |m1+b*n2|<=sqrt(C*g1), |m2-b*n1|<=sqrt(C*g2). Therefore a finite enumeration over these bounds finds all and only charge vectors in the energy ball S_C. Proof: every summand of E is nonnegative, so each is <=C.

Under integral antisymmetric K, B'=B+K and m'=m-Kn, E_(G,B')(m',n)=E_(G,B)(m,n) exactly. Thus the induced map S_C(G,B)->S_C(G,B') is bijective. It preserves L(v,w)=m·n'+m'·n because K is antisymmetric. Unlike coordinate boxes, energy balls are preserved by the B-shift.

## Evidence
Local command: python /mnt/data/p20/test_p20.py
stdout: P20 certified energy-ball duality cases: 12
stderr: empty
exit code: 0
SHA256: dc55dd48da59c90c1dbd57ab470200323804f13c206c078043581106863119eb
Test domain: 3 positive rational diagonal metrics, 2 rational B backgrounds, shifts k=-1,+1, threshold C=1; exact Fraction energies and pairing comparisons. Completeness follows from analytic inequalities; the Python implementation uses conservative floating-point derived bounds with padding and is not itself a formal machine-checked certificate for arbitrary rational inputs.

## Novelty gate
The finite energy-ball enumeration is standard geometry-of-numbers methodology. Do not claim a string-theory breakthrough. Higher-genus Narain theta functions already encode pairings; see Henriksson, Kakkar, McPeak, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011.

## P21 decision
Build a proof-carrying exact rational energy-ball enumerator with integer-square-root bounds (no floats), compare independent enumerators, and search for a concrete inequivalent-isospectral pair. If no new invariant or separating theorem arises, stop this direction rather than repeat APG reparametrizations.
