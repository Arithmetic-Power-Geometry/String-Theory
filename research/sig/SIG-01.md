# SIG-01: Spectral information and exact reduction

Status: exploratory. No new-mathematics or performance novelty claim.

Let X=(G,B), v=(m,n) in Z^4, E_X(v)=(m+Bn)^T G^(-1)(m+Bn)+n^T G n, and s(v)=m^T n. At cutoff C, define O(phi,C,X) as the multiset of phi(v,E_X(v),s(v)) over all charges with E_X(v)<=C. Choices phi=(v,E), E, and (E,s) recover labelled, unlabelled, and spin-refined observations. All multisets retain multiplicity.

Define X ~_(phi,C) Y when their observations agree. If phi1=f(phi2), equality under phi2 implies equality under phi1: apply f to equal multisets. This is standard information forgetting, not novel.

Define D_phi(X,Y) as the infimum of cutoffs where the observations differ, infinity if never. Positive-definite quadratic energies give locally finite charge spectra, so every finite D_phi is attained at a spectral energy. Finer observations can only lower this threshold.

For the manuscript's parity pair, D_energy=infinity and D_energy-spin <=3373/1325. Equality for the latter is not established by the witness alone. Inequivalence is relative to spin-preserving T-duality, not parity.

## First exact computation reduction

Charge inversion v -> -v preserves energy and s. Thus energy-only and energy-spin enumeration may evaluate one representative per inversion orbit, weighting each nonzero orbit by two. The manuscript's inversion-invariant box has 729 charges: 364 nonzero pairs and one origin = 365 representatives. Reduction in candidate evaluations: 364/729 = 49.93%. This does NOT establish a corresponding runtime speedup. It does not apply to charge-labelled spectra. Inversion pairing is standard, not a novel mathematical symmetry.

## Next validation gates

1. Independently compare exact full and orbit-weighted multisets at cutoff 3, including all multiplicities and 39 states per background.
2. Measure repeated runtime and memory; retain full 729-charge certificate as baseline.
3. Investigate stronger, valid symmetry groups and compare against existing lattice and theta-series reductions.
4. Review prior art before claiming a novel operator, threshold, theorem or algorithm.
5. Publish no SIG paper until a genuinely nontrivial result passes these gates.

Decision: GO for an independent method experiment; NO-GO for novelty claims now.
