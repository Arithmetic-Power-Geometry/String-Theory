# Stage 2: independent theorem audit — 2026-10-26

Status: PARTIAL PASS; not submission-ready. This is append-only evidence, preserving SIG-10's failed endpoint assertion and SIG-12's correction.

## Independent exact audit
A second implementation using Python Fraction and direct adjugate-matrix expansion (not importing the prior polynomial checker) enumerated 1,152 nonzero-spin records in the 729-charge box. For each background sign: 570 strictly positive difference polynomials on [0,1/2], 2 identically zero witnesses, 2 zero-endpoint contacts, and 2 half-endpoint contacts. Every quadratic was minimized at rational endpoints and its rational vertex when applicable. The exact minimum non-witness gap on [1/10,2/5] is 6/265, attained at b=1/10. Independent result SHA256 over canonical result data: 27e7d556d86caf68b6f999650d3eb2e124c7756b07f826f25284632aeacde1a5. Script and JSON results are stored in the companion committed files.

## Fixed-family proof audit
* G0=[[2,1/3],[1/3,3]], G0 inverse=[[27,-3],[-3,18]]/53. For the +b witness m=(-1,0), n=(1,0), the energy is (27-6b+18b²)/53+2=(133-6b+18b²)/53, spin -1. For the -b witness m=(-1,0),n=(-1,0), energy is identical and spin +1.
* G0 eigenvalues lie in [5/3,10/3] by Gershgorin. Energy <=3 implies ||n||²<=9/5<2 and ||m+bJn||²<=10; for b in [0,1/2], |m_i|<=sqrt(10)+1/2<4. Therefore the 729-charge box covers every candidate below the threshold T(b)<3.
* The involution (m,n)->(m,-n) reverses spin and maps the +b energy to -b energy. Thus unlabelled energy and spin-zero multiplicities match. The finite certificate excludes all nonzero-spin charges below T and identifies the first opposite-spin witnesses.
* Integer B-shifts are charge relabellings: (m,n)->(m-kJn,n) maps E_(b+k) to E_b and preserves m.n since n.Jn=0. Integer and half-integer b are refined-spectrum equality points.
* For symmetric entrywise perturbations <=eps=1/10000, ||delta G||<=2eps, lambda_min(G)>3/2, lambda_max(G)<7/2 and ||G^-1-G0^-1||<=4eps/5. In the charge box, ||m+bJn||²<40 and ||n||²<=2, hence |delta E|<=36eps and relative witness gap changes <=72eps=0.0072<6/265. Perturbed completeness: E<=3 gives ||n||²<2 and ||m+bJn||²<21/2; |m_i|<sqrt(21/2)+2/5<4. The same finite box suffices on [1/10,2/5]. This is a sufficient, not optimal, radius.
* The leading zero-mode theta difference has coefficient -4i sin(2pi tau1) at energy T for the +b minus -b convention. At special tau1 this coefficient vanishes; a scalar leading-term claim must exclude those values. Do not infer full physical partition-function inequivalence.

## General theorem 1 — attainment (proved)
For positive definite quadratic forms Q1,Q2 on Z^d with any grading g:Z^d->S, each sublevel set {v:Qi(v)<=R} is finite by coercivity. The union of the two energy supports is locally finite. If graded multiplicities differ at any energy, the set of differing energies therefore has a least member. The first-separation infimum is attained. Elementary, not claimed novel.

## General theorem 2 — grading-preserving invariance (proved)
If f:Z^d->Z^d is a bijection satisfying Q2(f(v))=Q1(v) and g(f(v))=g(v), all refined counting functions coincide, hence D=+infinity. This follows by bijection of finite level sets. It is not a new string duality.

## General theorem 3 — conditional local witness chambers (proved)
Let Q_(sigma,x) be continuous positive-definite quadratic forms on a fixed lattice, uniformly coercive Q_(sigma,x)(v)>=c||v||² on a compact parameter neighborhood. Suppose finite witness sets W_sigma have a common continuous energy T(x) throughout that neighborhood; every other nonzero-grade charge has strictly greater energy at x0; witness refined counts differ at T throughout a neighborhood; and grade-zero multiplicities match for both systems at all energies throughout that neighborhood. Then D(x)=T(x) near x0. Proof: uniform coercivity confines all charges with energy <=sup T+1 to a fixed finite ball. Continuity preserves the finitely many strict competitor inequalities; the grade-zero matching excludes earlier differences, and witness imbalance establishes the difference at T. Essential persistent equalities and matching hypotheses must not be omitted. This conditional structural lemma is not a universal local stability theorem.

## General theorem 4 — theta-leading-term statement (proved with caveat)
For t>0, |z|=1, Theta_i(t,z)=sum_v exp(-t Qi(v)) z^g(v), where g is integer-valued. If first refined discrepancy D<infinity, then Theta_1-Theta_2=e^(-tD) P_D(z)+O_z(e^(-t(D+delta))) for some delta>0, where P_D(z)=sum_k (N1(D,k)-N2(D,k))z^k is a nonzero Laurent polynomial. Discreteness and exponential convergence justify the remainder. P_D(z) can vanish at specific z, so the leading scalar asymptotic requires P_D(z)!=0. A common oscillator factor does not prove full string-theory inequivalence.

## Rejected claims and failed hypotheses
* REJECTED: first-separation D is everywhere continuous. In this family D is finite in open chambers and +infinity at symmetry boundaries.
* REJECTED: a strict gap at one parameter suffices for local stability of D for arbitrary continuous pairs of quadratic forms. Previously matched lower-energy levels can split unless structural matching persists.
* NOT PROVED: universal threshold for arbitrary Narain metrics, new heterotic string models, new dualities, complete oscillator-dressed inequivalence, or novelty priority.
* PRESERVED FAILURE: SIG-10's incorrect count of four extra endpoint contacts; SIG-12 correctly found two.

## Outstanding checks
Independent external specialist review, prior-art verification, journal scope, final LaTeX integration and submission audit remain pending. No acceptance claim.
