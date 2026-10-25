# SIG-11 — Exact B-shift symmetry and global periodic threshold formula

**Status:** Algebraic theorem plus finite exact tests. This strengthens SIG-10 and resolves the b=1/2 endpoint globally, not only at a cutoff.

## Definitions

Fix G=[[2,1/3],[1/3,3]], B(b)=[[0,b],[-b,0]], integer charge v=(m1,m2,n1,n2), energy E_b(v)=(m+B(b)n)^T G^{-1}(m+B(b)n)+n^TGn, and spin s(v)=m^Tn. Let X_+(b)=(G,B(b)), X_-(b)=(G,-B(b)). Define D_ES(b) as the infimum energy cutoff at which their complete joint (energy,spin) multisets differ, infinity if they never differ.

## Lemma: integral B-shift preserves energy and spin

For every integer k, define S_k(m1,m2,n1,n2)=(m1+k*n2,m2-k*n1,n1,n2). Then

E_b(v)=E_(b-k)(S_k(v)), s(v)=s(S_k(v)),

because B(b-k)n=B(b)n-k*(n2,-n1) and (k*n2,-k*n1) dot n=0. S_k is an integer lattice bijection with inverse S_-k. Hence the **complete** joint energy-spin spectra are invariant under b->b-k, with no cutoff restriction.

## Theorem: periodic extension of SIG-10

Let t=dist(b,Z) in [0,1/2]. For every real b with 0<t<1/2,

D_ES(b)=(133-6*t+18*t^2)/53.

For t=0 or t=1/2, D_ES(b)=infinity.

**Proof:** By integer shifts, the complete spin-refined spectrum at b is that at its fractional part r in [0,1). If r in (0,1/2), SIG-10 applies to the pair B(r), B(-r). If r in (1/2,1), integer shifts map B(r) to B(r-1)=B(-(1-r)), swapping the two signs; first separation is unchanged by exchanging the pair. Thus the threshold is T(min(r,1-r)). At r=0 the backgrounds coincide. At r=1/2, B(+1/2) and B(-1/2) differ by the integral antisymmetric matrix [[0,1],[-1,0]], so S_1 gives an exact energy-and-spin-preserving bijection of **all** integer charges, proving equality of the complete spectra and infinite distinguishability threshold. QED.

The theorem inherits SIG-10's computer-assisted finite certificate for 0<t<1/2; the periodic extension and endpoint equivalence are purely algebraic.

## Independent local check

Python standard-library Fraction script checks 2500 exact charge identities across four rational b values, verifies the half-integer bijection, and checks sample periodic threshold values. All PASS. Finite tests supplement, not replace, the all-charge algebraic proof.

## Important scope / novelty

- The integer B-shift is a **standard Narain O(2,2;Z) duality**, not a newly discovered symmetry.
- The periodic first-separation formula for this fixed metric G is a sharper consequence of SIG-10. Its originality relative to known spin-refined theta functions has **not** been established.
- No implication is made that every pair of geometries with matching unlabelled spectra is non-dual. The b=1/2 endpoint is in fact spin-preserving dual.

## Research decision

**GO for independent proof audit; REVISE for publication.** Next SIG-12 should independently reproduce the SIG-10 interval certificate, explicitly test the claimed 576-charge count and endpoint degeneracies, and conduct a targeted scholarly prior-art review. Keep all earlier experiments and failures append-only. Do not draft a SIG paper yet.
