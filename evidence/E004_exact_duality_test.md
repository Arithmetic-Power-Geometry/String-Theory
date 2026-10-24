# E004 — Exact duality witness
Date: 2026-10-24
Status: proved by rational arithmetic and independently recomputable.

Input radii: (2,3) and (1/2,3). Squared-radius weights: (4/13,9/13) and (1/37,36/37). For D4=1-sum(w_i^2), values are 72/169 and 72/1369, different.

Repaired weights use q_i=R_i^2+R_i^-2, giving q=(17/4,82/9) and normalized weights (153/481,328/481) in both backgrounds. The repaired D4 is 100368/231361 in both.

Exact commands: python3 tests/test_p04_duality.py
Expected stdout: P04 exact duality tests passed

Limitations: elementary two-radius example; only factorized T-duality for a diagonal torus with B=0 and alpha'=1. Does not establish O(d,d;Z) invariance, physical equivalence of full backgrounds without dilaton adjustment, novelty or a new string-theory theorem.
