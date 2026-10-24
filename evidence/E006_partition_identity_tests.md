# E006 — Exact finite partition reduction audit
Date: 2026-10-24
Source: tests/test_p06_partition_no_go.py
Method: rational Boltzmann fugacity x in {1/2,2/3,3/4}; finite integer energies 0..3, sequence lengths 1..4; q in {2,3,4}. Compute direct APG power sums and independent partition-ratio form using Python Fraction; test sharp Jensen bounds.

Expected 3*(4+16+64+256)*3=3060 cases. No Monte Carlo; exhaustive finite parameter grid. A result here establishes elementary exact algebra, not a new string-theory theorem. Primary novelty decision: NO-GO for unrefined escort-power-sum functional.
