# E038 — P38 raw execution and integrity
Date: 2026-10-24
Command: python /mnt/data/p38/test_p38.py
Exit status: 0

## Raw stdout
```
P38 certified charge box: 729
P38 states per background through cutoff 3: 39
P38 witness energy: 3373/1325
P38 +B spin multiplicities: 2 0
P38 -B spin multiplicities: 0 2
P38 energy-only spectra equal below cutoff: YES
P38 exact full-energy isospectrality: analytic bijection
P38 no O(2,2;Z) duality: spin-spectrum invariant obstruction
P38 source SHA256: c262804643e8f418d96c44798316148d9548d966ab255564134c3cfbbd3d9af6
```

## Raw stderr
Empty (0 bytes).

## Source integrity
SHA256 of exact executed source: c262804643e8f418d96c44798316148d9548d966ab255564134c3cfbbd3d9af6
Git blob of exact executed source: d7664c509077fb5a8b7113b4c31f7f9034c04ec7

All 729 charge vectors in the certified complete box were checked for each background using exact Fraction arithmetic. Full-energy isospectrality and duality obstruction are analytic statements, not extrapolations from the finite test.
