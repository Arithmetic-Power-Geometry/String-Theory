# SIG-07: Exact first spectral separation for the rational parity pair

**Status:** finite exact certificate PASS; mathematical novelty undetermined. Do not replace the original paper's valid witness without a manuscript-level review.

## Question
For the rational pair G=[[2,1/3],[1/3,3]], B=+/-[[0,1/5],[-1/5,0]], what is the **first** energy at which the joint energy-spin multiplicities differ?

## Result
The first difference is **3313/1325**, which is strictly below the manuscript's valid example at 3373/1325.

At E=3313/1325, the B+ spectrum has N(E,+1)=0 and N(E,-1)=2; the B- spectrum has N(E,+1)=2 and N(E,-1)=0. Every lower energy-spin multiplicity agrees.

## Certificate and proof scope
The independently executed Python Fraction program enumerates all 729 charges in [-4,4]^2 x [-1,1]^2 and retains all E<=3. The paper's analytic completeness argument establishes that this box includes every charge of energy <=3 for this fixed G and either B sign. The program finds 39 states per background, verifies equality of all lower spin-refined multiplicities, confirms the first mismatch, and verifies equality of unlabelled energy multiplicities throughout the window. Thus, conditional on the already-proved completeness bound, the first distinguishing energy is exact.

The full unlabelled energy spectra agree at all energies by the known parity correspondence; this is not a newly discovered symmetry. The spin-preserving duality qualifier remains essential.

## Novelty gate
This sharpens a concrete example, but does not by itself establish a novel mathematical framework. A genuinely new SIG theorem would need a general formula or rigorous bound for first separation across nontrivial background families, beyond standard theta-series comparisons. Check literature priority before any paper.

**Decision:** GO for independent validation and a general threshold theorem attempt; NO-GO for a SIG paper now.
