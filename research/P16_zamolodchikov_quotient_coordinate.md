# P16 — APG duality coordinates and the Zamolodchikov quotient metric
Date: 2026-10-24. Status: exact geometry theorem, classical coordinate geometry; no novel physics claimed.

Use alpha'=1 and the established compact-boson Zamolodchikov line element ds²=4(dR/R)², R>0. The duality R~1/R identifies x=log R with -x. APG's P04 inversion-invariant quantity in one radius is u=R²+R^-2=2 cosh(2x), u>=2.

THEOREM P16-T1: For R!=1, ds²=du²/(u²-4). Proof: du/dx=2(R²-R^-2), so (du/dx)²=4(u²-4); substitute into ds²=4 dx².

THEOREM P16-T2: The coefficient 1/(u²-4) diverges as u->2+, but this is only a coordinate singularity. On the quotient half-line define ell=arcosh(u/2)=2|log R|>=0. Then ds²=dell². The fixed point R=1 is ell=0, the boundary of the quotient half-line. The map R->u has vanishing derivative at R=1 and is not a local smooth coordinate on the covering manifold there.

COROLLARY P16-C1: Any smooth inversion-invariant scalar f(R) on the covering line has derivative df/dx=0 at x=0, because f(x)=f(-x). Thus no single smooth duality-invariant scalar can be a local coordinate with nonzero derivative at the fixed point on the covering space. Proof: differentiate f(x)=f(-x) at zero.

Interpretation: P04's q_i=R_i²+R_i^-2 is a legitimate invariant, but its use as a smooth coordinate at the self-dual point requires quotient geometry. This is a standard reflection-quotient phenomenon, not a new physical singularity or string-theory breakthrough.

Tool-selection verdict: physically justified metric first, then APG coordinate transformation; do not infer new geometry from coordinate divergences.

Sources verified: JHEP10(2020)187, https://inspirehep.net/files/8c850caa4858c00767eac0802768c56a (section 2.1 gives ds²=4dR²/R²); https://cds.cern.ch/record/2813483/files/2206.11287.pdf (metric proportional to dR²/R²); https://onlinelibrary.wiley.com/doi/10.1002/prop.70098 (2026 prior art on Narain Zamolodchikov geometry).
