# P40 — Enlarged certified open family and novelty audit

Date: 2026-10-24

## T1: Enlarged exact open-family certificate
Fix G0=[[2,1/3],[1/3,3]] and b0=1/5. For all real parameters with max(|a-2|,|c-3|,|d-1/3|,|b-1/5|)<=1/90, the spin-resolved Narain spectrum is asymmetric. Consequently (G,B_b) and (G,B_-b) are energy-isospectral at all energies but inequivalent under the orientation-preserving O(2,2;Z) Narain duality group.

### Proof
Energy is E=(c(m1+b n2)^2-2d(m1+b n2)(m2-b n1)+a(m2-b n1)^2)/(ac-d²)+a n1²+2d n1n2+c n2²; spin is s=m dot n.

On the cube, a>=179/90, c<=271/90, |d|<=31/90, and |b|<=19/90. Gershgorin gives lambda_min(G)>=179/90-31/90=148/90>1.64, and lambda_max(G)<=271/90+31/90=302/90<3.36. Thus every state E<=3 has ||n||²<=3/(148/90)<2, so n=0 or a coordinate unit. Moreover ||m+Bn||²<=3*(302/90)<10.067, and ||Bn||<=19/90; hence |m_i|<sqrt(10.067)+19/90<4. Every state E<=3 lies in the finite charge box [-4,4]^2 x [-1,1]^2.

At the center, the witness v=(1,0,1,0) has spin +1 and energy W=3373/1325. The nearest opposite-spin energy is 3313/1325, a gap 12/265. For the full parameter cube, exact rational outward interval arithmetic bounds the witness energy and all 68 charge vectors with spin -1. The executed test checks that the witness interval is disjoint from every opposite-spin energy interval, and that its energy stays below 3. Therefore the witness remains unmatched in spin -1 for all real points in the cube. P38's exact spin-invariant obstruction rules out all O(2,2;Z) dualities between (G,B_b) and (G,B_-b), while (m,n)->(-m,n) gives all-energy isospectrality.

The cube has side 1/45 in each of four parameters and volume (1/45)^4=1/4100625 in these chosen coordinates. This coordinate volume is NOT a duality-invariant moduli-space measure.

## Comparison with prior work
| Research direction | Existing work | P40 contribution | Novelty assessment |
|---|---|---|---|
| Narain duality moduli and spin spectra | Afkhami-Jeddi et al. (2021); Benjamin et al. (2021) | A specific rigorously bounded inverse-spectral obstruction | Established foundation; specific certificate possibly new |
| Parity reversal and left/right exchange | Standard worldsheet parity in toroidal CFT | Explicit rational spin witness and certified open family | Mechanism not new |
| Isospectral CFTs distinguished at higher genus | Henriksson et al. (2023) | Different distinction: energy-only vs spin-resolved genus-one data | Not a priority claim over prior isospectral constructions |
| Narain ensembles and code constructions | Aharony et al. (2024) | No holographic or code-construction result | No novelty claimed |
| Exact robust parameter radius | P39 radius 1/1000000 | P40 radius 1/90 with outward rational intervals | Concrete quantitative improvement within this programme |

## Verdict
Mathematical GO: enlarged rigorously certified open set. Publication novelty: conditional and NOT established by this limited literature search. Radius 1/90 is sufficient, not optimal. No fundamental physics breakthrough claimed.

## Reproducibility
tests/test_p40.py is the byte-identical locally executed source; evidence/E040_execution.md contains raw stdout, stderr and hashes. tests/test_p39.py now closes the previous missing-source archive gate. Both Git blobs verified after GitHub upload.
