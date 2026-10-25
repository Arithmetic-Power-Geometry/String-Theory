# SIG-02 — Independent exact orbit-reduction benchmark

## Status
**GO for further investigation; NO-GO for claiming a new mathematical symmetry.**

The involution v -> -v preserves E_X(v) and s(v). It partitions the symmetric 729-charge candidate box into 364 two-element orbits and the zero singleton: 365 orbit representatives. Orbit weights retain exact spectral multiplicities. This applies to energy-only and energy-spin observations, not charge-labelled observations.

## Independently executed local test (25 October 2026)

Python 3 standard-library Fraction arithmetic; each mode and background compared complete Counters, not just totals. Both methods returned 39 states for each background. All four complete multiset comparisons passed.

| Background | Observation | Full median ms | Orbit median ms | Speedup |
|---|---|---:|---:|---:|
| +1/5 | Energy | 9.664 | 5.311 | 1.820x |
| +1/5 | Energy-spin | 10.446 | 5.577 | 1.873x |
| -1/5 | Energy | 9.306 | 4.995 | 1.863x |
| -1/5 | Energy-spin | 9.463 | 4.923 | 1.922x |

Method: seven timing batches, twenty executions per batch, median batch time divided by twenty. These are preliminary local wall-clock observations; environment, load, hardware and Python version were not captured, and cross-machine reproducibility is not established. Code: [sig02_orbit_benchmark.py](sig02_orbit_benchmark.py).

## Interpretation and limitations

Candidate evaluations decrease from 729 to 365 (49.93%). The local runtime improvement is real in this run but is **not** a proven asymptotic complexity improvement. Both methods still scan all 729 candidates to select canonical orbit representatives; arithmetic evaluations, not all loop iterations, are reduced. The symmetry is elementary and known. No novelty claim follows.

## Next gates

1. Independently run the committed script and capture environment/version metadata and machine-readable results.
2. Test a direct representative generator to avoid scanning duplicate charges, and benchmark against both baselines.
3. Preserve completeness and all spin multiplicities, including boundary cases.
4. Prior-art kill-test on theta series, lattice orbit reduction and inverse spectral threshold concepts.
5. Attempt a nontrivial new theorem only after those tests. Do not draft a new paper yet.
