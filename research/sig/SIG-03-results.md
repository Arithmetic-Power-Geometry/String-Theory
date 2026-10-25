# SIG-03: Direct inversion-orbit generation

Status: exact finite test PASS; computational optimization validated locally; mathematical novelty NOT established.

## Construction and proof
In the symmetric charge box [-4,4]^2 x [-1,1]^2, each nonzero orbit under v -> -v has exactly two members. Select the member whose first nonzero coordinate is negative. The zero vector is the unique singleton. A direct generator partitions representatives by the position of their first nonzero coordinate, assigns that coordinate a negative value, sets all preceding coordinates to zero, and allows every later coordinate its full permitted range. These cases are mutually exclusive and exhaustive, so each nonzero inversion orbit has exactly one representative. Assign weight two to each nonzero representative and weight one to zero.

Since E_X(-v)=E_X(v) and s(-v)=s(v), the weighted multiset of energy-only or energy-spin observations equals the full multiset exactly. Charge-labelled observations do not satisfy this invariance. The algorithm visits 365 representatives instead of scanning 729 candidates.

## Executed benchmark
Python 3.13.5, Linux x86_64, exact Fraction arithmetic. Seven batches of 20 repetitions; median per-execution wall-clock time, milliseconds. Local measurements, not portable speed guarantees.

| B | Observation | Full | Filter scan | Direct | Direct/full speedup |
|---|---|---:|---:|---:|---:|
| +1/5 | energy | 10.0681 | 5.6536 | 4.9298 | 2.042x |
| +1/5 | energy-spin | 9.5223 | 5.2091 | 5.0121 | 1.900x |
| -1/5 | energy | 9.7731 | 5.5723 | 5.1825 | 1.886x |
| -1/5 | energy-spin | 10.6059 | 5.4130 | 5.3616 | 1.978x |

All four exact Counter comparisons passed; each background has 39 states at E<=3. The partition covers all 729 charges with 365 weighted representatives.

## Scope and next gate
The result is a correct implementation of standard inversion symmetry, not a new mathematical symmetry or a novel complexity class. For a family of symmetric charge boxes of size N, both full and direct enumeration are O(N) in the number of candidates, although direct generation reduces constant factors.

Next: benchmark stronger established baselines; investigate more substantial algebraic pruning, including certified energy lower bounds; test at multiple cutoffs and backgrounds; review prior art. No SIG paper should be drafted yet.
