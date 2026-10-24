# E021 — Exact P21 verification
Date: 2026-10-24
Executed command: python /mnt/data/p21/test_p21.py
Exit code: 0
stdout: P21 exact five-probe reconstruction cases: 72
stderr: empty (0 bytes)
SHA256 of exact executed Python source: 3f84a2781c26865398e9c923fe23a017d64ea3847a9f2c9c7f78b24874848b40
Inputs: a in {1,2,3/2}, c in {1,2}, d in {0,1/3,-1/2}, b in {-1,0,1/4,2/3}; all 72 positive-definite combinations. Uses fractions.Fraction throughout; tests exact recovery of G and b from five energies. Analytic theorem is independent of tests.
