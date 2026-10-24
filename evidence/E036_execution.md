# E036 — P36 exact arithmetic verification

Date: 2026-10-24
Environment: Python 3, fractions.Fraction, itertools.product.

An independent inline Python verification was executed in the working container using the same energy identity and three parameter tuples as tests/test_p36.py, over all 625 charge vectors in [-2,2]^4 per background. Exit code 0.

Raw stdout:
```
P36 exact checks passed: 1875
```

Stderr: empty.

The independent inline test is not byte-identical to tests/test_p36.py; no executed-source SHA256 identity is claimed. The committed regression file contains the corresponding exact-arithmetic test. The mathematical theorem is analytic.
