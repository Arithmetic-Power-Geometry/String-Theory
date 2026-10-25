# SIG-13: Independent audit and novelty kill-test

Independent Python Fraction execution: PASS. For each B sign, all 576 nonzero-spin charges in the 729-charge complete low-energy box were checked against T(b)=(133-6b+18b²)/53 on [0,1/2]. Exact endpoint and quadratic vertex checks find: 570 strictly above throughout the closed interval, 2 meeting only at b=0, 2 meeting only at b=1/2, 2 identically at threshold. Zero violations. The script prints all exceptional charge vectors and spins.

The original SIG-10 script incorrectly asserted four additional endpoint charges and would fail. SIG-12 corrected this to two; SIG-13 independently confirms that correction. Retain failed files.

The resulting fixed-G open-interval threshold formula remains supported, conditional on the uniform analytic charge-box completeness bound from SIG-10. The global periodic extension relies on the algebraic integral B-shift bijection from SIG-11. This does not prove any general result for varying G.

Prior art: Narain partition functions and parity-invariant symmetrization are already treated in arXiv:hep-th/0211230 (https://archive.ymsc.tsinghua.edu.cn/pacm_download/58/489-017-0211230.pdf). Spin-sensitive Narain partition functions are standard (https://open.bu.edu/bitstreams/0636b7de-38aa-41e7-ae68-2979ed85fd54/download). Siegel–Narain theta functions and duality are established (https://www.osti.gov/pages/servlets/purl/2576103). Standard lattice enumeration is established. No novelty claim for the observables, parity, B-shifts or pruning survives.

Publication gate: REVISE. The exact threshold polynomial might be a specific new result, but a limited literature search cannot establish priority. Next investigate a structural proof and variation of G; obtain independent execution of the exact committed code.
