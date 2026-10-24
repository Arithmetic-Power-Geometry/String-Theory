# E005 — Exact arithmetic test of a Narain B-field shift

Date: 2026-10-24.
G=diag(2,3), B=[[0,1/2],[-1/2,0]], K=[[0,1],[-1,0]].
For every charge tuple (m1,m2,n1,n2) in {-2,-1,0,1,2}^4, independently calculate E_(G,B)(m,n) and E_(G,B+K)(m-Kn,n) using exact rational arithmetic.

Command: python3 tests/test_p05_bshift.py
Observed stdout: exact B-shift charge-covariance tests passed: 625
Observed stderr: empty.
Observed exit status: 0.
This checks 625 cases. The accompanying algebraic proof applies to all integer charges. It does not prove a novel string-theory result.
