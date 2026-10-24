# P26 — Optimal charge scale under charge-dependent measurement error

Date: 2026-10-24. Scope: mathematical inverse-design model for labelled Narain energy measurements, **not** a claim that the noise model is physically realized.

## T1: Exact optimal scaling
For a charge-homogeneous energy E(kv)=k²E(v), assume an absolute error bound epsilon(k)=a+c k^p with a,c>0 and p>0. Normalized measurement error is eta(k)=a/k²+c k^(p-2).

If 0<p<=2, eta is strictly decreasing on k>0 (for p=2 it tends to c). If p>2, eta decreases up to k*=(2a/((p-2)c))^(1/p) and increases afterwards. This is the unique continuous global minimizer, proved by differentiating eta and observing the sign of (p-2)c k^p-2a.

For integer k in {1,...,K}, the exact optimum occurs at the admissible floor or ceiling of k* after clipping to [1,K] (or at K if p<=2). This is a two-candidate certificate for p>2. The script tests exact integer optima by independent exhaustive comparison.

## T2: Energy-budget bound
Let M=max_i E(v_i)>0 for the five unscaled labelled probes. If the accessible charge-energy budget is E(kv_i)<=C for all probes, then k<=floor(sqrt(C/M)). If C<M no scaled scheme with integer k>=1 is feasible. Combine with T1 to get an energy-constrained exact optimum. The bound is a mathematical resource constraint, not an experimental implementation.

## T3: No improvement under purely relative error
If epsilon(k)=r k², then normalized uncertainty is identically r. Thus quadratic charge scaling provides **no** improvement under constant relative uncertainty. This disproves any unconditional physical advantage from P25.

## Independent exact checks
225 integer optima independently compared against all allowed integers; 18 monotonic model parameter combinations; one quartic-noise example and a 99-scale relative-noise counterexample. Executed source and raw stdout/stderr in tests/test_p26.py and evidence/E026_execution.md. No novelty or physics breakthrough claimed: optimal design under power-law noise follows classical calculus. Next gate: verify whether charge-resolved energy observations and error/cost scaling have an operational physical interpretation, or stop this programme.
