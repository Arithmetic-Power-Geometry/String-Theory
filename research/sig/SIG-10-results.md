# SIG-10: Spin-only exact certificate on the open interval (0, 1/2)

**Result:** Fix G=[[2,1/3],[1/3,3]] and B_±(b)=±[[0,b],[-b,0]]. For every real b satisfying 0<b<1/2, the first energy at which the joint energy-spin zero-mode spectra differ is

D_ES(b)=(133-6b+18b²)/53.

This extends SIG-09 (0,3/14]. The earlier 3/14 endpoint was **not** maximal.

## Proof

For any fixed b, worldsheet parity sends B to -B and flips spin, preserving energy. Thus the spin-zero spectral multiplicities match between B+ and B- at every energy. A first difference must involve nonzero spin.

The uniform completeness bound for energy <=3 is valid on 0<=b<=1/2: lambda_min(G)>5/3 and lambda_max(G)<10/3 imply |n|²<2 and |m+Bn|²<10. Therefore |n_i|<=1 and |m_i|<sqrt(10)+1/2<4. Every state below the proposed threshold (<3) is in the 729-charge box.

For each of the 576 charges in this box with nonzero spin, express E(v,b)-T(b) as a rational quadratic polynomial, with T=(133-6b+18b²)/53. For each sign, two charge polynomials are identically zero, carrying spin -1 for B+ and +1 for B-. All other 574 nonzero-spin charge polynomials are strictly positive for every 0<b<1/2. This is certified by exact endpoint values and any interior quadratic vertex; an exact positive interior value rules out an identically-zero polynomial or interior zero. Four of those 574 charges touch zero only at an endpoint.

Thus below T(b) there are no nonzero-spin states and parity forces equality. At T(b), there are two spin -1 states for B+ and two spin +1 states for B-, so the first difference is exactly T(b).

## Endpoints and limitations

At b=0, B+=B-, hence D_ES=infinity. At b=1/2, additional opposite-spin charges meet T, cancelling the spin imbalance at that energy. Exact finite enumeration through energy 3 at b=1/2 found no spin-resolved difference, but **no global all-energy equality or infinite threshold at b=1/2 is claimed**. The theorem is only on the open interval.

The exact script tests all 576 nonzero-spin charges per sign using Python Fraction arithmetic, including endpoint and vertex tests. Local independent execution: PASS.

## Novelty and publication gate

This is a more substantial continuum theorem for a fixed G and a one-dimensional B-family, but it remains a computer-assisted finite certificate based on elementary quadratic-form inequalities and parity. No broad novelty claim has passed prior-art review.

**Decision:** GO to SIG-11 for an independent implementation, investigate the b=1/2 endpoint and symmetry/duality explanation, and compare with established refined theta-series literature. No new SIG paper yet.
