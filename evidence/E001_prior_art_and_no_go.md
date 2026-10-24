# E001 — First research iteration (2026-10-24)

Status: foundational source review; **NO-GO for claims of a string-theory disproof**.

## Inputs inspected
User-provided APG V, VI, VIII, X; Cospectral Boolean Sensitivity Graphs; Physical Distinction Theory. Full PDFs were available in the conversation; this repository records their titles and conceptual relevance, not redistributed copyrighted PDFs. Bibliographic metadata for self-authored manuscripts requires separate version verification before BibTeX insertion.

## Verified prior-art findings
1. Rabadán and Shiu (2003) investigated isospectral compactification manifolds; equal Kaluza–Klein masses do not uniquely specify compactification geometry. Thus the generic nonuniqueness thesis is **not novel**.
2. Nilsson–Rowlett–Rydell (2023) survey isospectral nonisometric flat tori and explicit constructions. Thus flat-torus isospectrality alone is **not novel**.
3. Schaefer (2024) identifies eigenfunction triple products as geometric reconstruction data. Thus saying ‘add all triple products to recover geometry’ is **not novel**.
4. Schaefer (2026) extends triple-product reconstruction to certain differential operators. Thus generic extensions to weighted/Schrödinger operators face direct prior art.

## Mathematically controlled baseline — energy bound
For compact connected smooth Riemannian X, positive Laplacian Δ, mean-zero F and u solving Δu=F, E(F)=<F,Δ⁻¹F>=Σ_{j≥1}|<F,φ_j>|²/λ_j ≤ ||F||²/λ₁. This follows termwise from λ_j≥λ₁; equality holds when F is entirely supported in the first positive eigenspace. This is standard spectral theory, **not a new theorem or evidence against string theory**.

## Falsification conditions
A candidate fails if (a) it merely reproduces a classical spectral inequality, (b) it swaps graph adjacency for a manifold Laplacian without a justified map, (c) proposed physics depends on non-invariant eigenvector coordinates, (d) it ignores possible dualities, (e) the compactification violates physical consistency, or (f) the proposed observable is already covered by earlier reconstruction work.

## Open work
Build explicit isospectral geometries; choose fully specified operator, eigenbasis gauge, normalized coupling tensor, and observer limitations; seek an exact **finite robust distinguishing certificate** with a proof not supplied by these references. Until then, novelty and physical significance remain unconfirmed.

## Provenance
Sources and verification register: reference/ . Baseline independent calculation: tests/test_spectral_energy.py . Exact numerical test output must be recorded separately from analytic identity; no test execution is claimed merely by committing a script.
