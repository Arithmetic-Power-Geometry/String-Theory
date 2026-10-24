# P19 — Exact embedding of P18 pair interaction geometry in Siegel–Narain genus-two theta
Date: 2026-10-24
VERDICT: NO-GO for novelty of P18 as a distinct string-theory invariant.

Let G be positive definite and B antisymmetric in d=2. Define p_L/R(v)=G^(-1/2)(m+Bn +/- Gn)/sqrt(2). The sum p_L(v)^2+p_R(v)^2 equals E(v)=(m+Bn)^T G^-1(m+Bn)+n^T G n. The difference of mixed inner products p_L(v)·p_L(w)-p_R(v)·p_R(w)=m·n'+m'·n=L(v,w); antisymmetric B cancels.

Define the conventional lattice genus-two theta with period matrix Omega (symmetric with Im Omega positive definite) by
Theta^(2)(Omega)=sum_(v,w in Z^4) exp[i*pi*(Omega11*p_L(v)^2+2 Omega12*p_L(v)·p_L(w)+Omega22*p_L(w)^2) - i*pi*(conj(Omega11)*p_R(v)^2+2 conj(Omega12)*p_R(v)·p_R(w)+conj(Omega22)*p_R(w)^2)].
For Omega=[[i*t/pi,z/(2*pi)],[z/(2*pi),i*s/pi]], t,s>0, z real, this is exactly P18's P(t,s,z)=sum_(v,w) exp[-t E(v)-s E(w)+i*z*L(v,w)].
Proof: diagonal terms give -t E(v)-s E(w); real offdiagonal term gives i*z*(p_L(v)·p_L(w)-p_R(v)·p_R(w))=i*z L(v,w). The upper half-space condition holds since Im Omega=diag(t/pi,s/pi)>0.

Thus the pair structure is a special slice of an established genus-two theta function, not an independent new invariant. It is not automatically the full genus-two CFT partition function: oscillator/determinant factors and geometric conventions also matter. The exact arithmetic verification checks the chiral identities independently.

Prior art: Henriksson, Kakkar, McPeak, Narain CFTs and quantum codes at higher genus, JHEP 04 (2023) 011, DOI 10.1007/JHEP04(2023)011, https://doi.org/10.1007/JHEP04(2023)011.

Next research gate: pursue a concrete conjecture not expressible as a standard higher-genus theta specialization; prove a sharp bound or classification theorem for physical modular-covariant quantities, with literature novelty review before naming a breakthrough.
