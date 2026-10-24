# Independent critical peer review — 24 October 2026

**Manuscript:** Finite Spectral Reconstruction and Robust Non-Identifiability in Two-Dimensional Narain Compactifications  
**Inputs:** user-supplied 11-page manuscript PDF, LaTeX ZIP; private repository tests and evidence through P43.  
**Editorial estimate:** 82/100 (provisional, qualitative). **Recommendation: major revision before strong Q1 submission.** A journal's Q1 ranking and acceptance are not determined by this score.

## Verified strengths
- Clear separation between fixed charge-labelled energies, charge-blind energies, and joint energy-spin data.
- Five-probe algebraic inversion with fixed charge basis; bounded rectangular inverse.
- Independently checked exact rational witness: full 729-charge box; 39 states of energy ≤3 for each sign of b=1/5; at W=3373/1325, spin (+1,-1) multiplicities equal (2,0) for positive b and (0,2) for negative b.
- Independently reproduced rational interval separation for the four-parameter cube of radius 1/90: witness energy lies within approx [2.52344166,2.56830567] (<3), no opposite-spin charge interval in the complete box overlaps; minimum interval margin approx 0.00099316.
- The open-dense genericity and countable-exception scaling arguments have coherent proof mechanisms and logically careful quantifiers.
- Repository contains extensive tests/research and append-only evidence plus bibliographic verification records.

## Required revisions, prioritized
1. **Novelty gate (critical):** Standard B→−B parity and prior isospectral CFT examples are known. Explain theorem-by-theorem what is specifically new: precise inverse data regimes, bounded finite cutoffs, exact integer certificate, uniform four-parameter robustness, genericity, no universal spin-refined finite cutoff. Literature priority of these *specific* statements remains unverified; do not claim the first isospectral CFT.
2. **Theorem 7.1 proof (major clarification):** At E=L, saying four b=0 winding states are 'absent' for b=1/2 does not by itself prove unequal **total** multiplicity. Add proof that no b=1/2 nonzero-winding state reaches E=L: nᵀ(LI)n≥L and equality forces m+Bn=0, impossible for unit n at half-integral Bn. Pure momenta coincide. E.g., independently counted L=2 level multiplicities 8 versus 4.
3. **Theorem 7.2 scale argument (major clarity):** Explicitly define A_w and D_w from G0 and B; L⋅(E(v)−E(w))=A_w+L²D_w. Since every spin-−1 w differs at L=1, each polynomial is nonzero and has at most one positive-L root; the exceptional set is countable. State 'arbitrarily large L outside countable exceptions', not 'all sufficiently large L'.
4. **Proposition 6.1 certificate (major evidence):** Publish exact rational interval endpoints or a machine-readable per-charge certificate of all 68 opposite-spin comparisons, witness upper bound <3, code hashes, command and run logs. Independent interval reimplementation here supports claim; formal appendix still needed.
5. **Theorem 4.2 algorithm boundary (moderate):** At a=c, the two coordinate momenta have one distinct energy with multiplicity four. Theorem itself is not disproved; specify recovery from multiplicity rather than requiring two distinct subunit levels. Include explicit test at a=c=2 and b=1/2.
6. **Definition and physics scope (major):** 'Not O(2,2;Z)-dual' is not inequivalence after allowing worldsheet orientation reversal. Preserve careful parity caveat prominently. State only zero-mode exact data, no real detector/experiment claims.
7. **Five labelled probes (minor):** Define e1,e2,e4 explicitly as standard charges ordered (m1,m2,n1,n2). Clarify five suffices but minimality is unproved; recovered fixed basis representative is not a duality-invariant reconstruction.
8. **Theorem 4.1 proof (minor):** Supply concise check of nearest-integer momentum at b=1/2 and comparison with winding vectors of squared norm ≥2. No counterexample found.
9. **Figures and editing (minor):** Figure 2 y-axis should say 'nonzero-winding energy lower bound,' not generic 'zero-mode energy lower bound'. Ensure negative spin ticks are legible; audit Proposition/Theorem 5.1 reference, tables and all captions.
10. **Q1 ambition:** Strengthen contribution with effective bounds on compact reduced moduli or a quantitative stability theorem, not padded reference counts, decorative figures, or inflated breakthrough language. Include a clear theorem-oriented novelty comparison and limits.

## Assessment matrix
| Criterion | Score |
|---|---:|
| Research question | 92/100 |
| Proof credibility | 86/100 |
| Exact computation | 91/100 |
| Literature novelty (not fully verified) | 69/100 |
| Physical interpretation | 78/100 |
| Organization | 88/100 |
| Reproducibility | 82/100 |
| Anticipated Q1 referee reception | 70/100 |

**Verdict:** Promising theorem-driven inverse-spectral mathematics; **not yet 100/100 or ready for submission to a strong Q1 physics journal**. Keep the core claims, fix proof exposition and editorial issues, strengthen external literature positioning, archive a frozen reproducible release and independently verify bibliography entries. No unconditional novelty or acceptance guarantee.

## Independent checks and limits
Independent rational enumerations and interval checks were performed this review session, plus one exact L=2 multiplicity check; GitHub P39/P40/P43 research and scripts were inspected. **Not** all 43 research tasks or 40+ tests were re-executed; not all bibliography metadata or literature priority questions were independently verified. Repository source is private, so public peer access may require an archive/release with accessible code.
