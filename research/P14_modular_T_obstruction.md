# P14 — Modular-T obstruction to continuous momentum-winding phase deformation
Date: 2026-10-24
Status: exact theorem for a formal theta-series deformation; NOT a breakthrough in string theory.

## Model
Fix R>0 and tau=tau1+i*tau2 with tau2>0. For real lambda set
Theta_(lambda,R)(tau)=sum_(m,n in Z) exp[-pi*tau2*(m^2/R^2+n^2*R^2)] * exp[2*pi*i*lambda*tau1*m*n].
The Gaussian series converges absolutely. This is a formal deformation of the compact-boson zero-mode theta factor, not a constructed unitary CFT.

## Theorem P14-T1
Theta_(lambda,R)(tau+1)=Theta_(lambda,R)(tau) for all tau in the upper half plane if and only if lambda is an integer.

Proof. If lambda is integral, exp(2*pi*i*lambda*m*n)=1 for all integer m,n. Conversely, evaluate at tau1=0. Let a_(m,n)>0 be the Gaussian weights. The undeformed sum is sum a_(m,n), while its T-transform is sum a_(m,n)*exp(2*pi*i*lambda*m*n). If the sums are equal, equality in the triangle inequality for an absolutely convergent series of strictly positive weights forces every phase to be 1 (the (0,0) term fixes common phase). Taking m=n=1 gives exp(2*pi*i*lambda)=1. Thus lambda is integral.

## Corollary P14-C1
No continuous interval of lambda around 1 consists entirely of modular-T-invariant theta functions of this form: any noninteger lambda violates T invariance.

## Interpretation
The conventional compact boson has the phase exp(2*pi*i*tau1*m*n) and the full partition function also includes |eta(tau)|^-2. Its modular T invariance is level matching. This theorem restates a known integrality obstruction for a specific proposed formal deformation. It does not show that APG itself is inconsistent, and integer lambda does not establish modular S invariance, positivity of operator products, or a valid CFT.

## Next P15
Investigate whether any APG exponent deformation can be realized as a modular-covariant deformation of the complete compact-boson theory, with consistent conformal weights and operator algebra. An infinitesimal formal deformation of the phase coefficient is obstructed, but changes of radius and other exactly marginal deformations remain allowed. Audit against known Narain moduli and modular bootstrap results.
