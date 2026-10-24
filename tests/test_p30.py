from fractions import Fraction as Q
from itertools import product
from collections import Counter

def energy(v,L,b):
    m1,m2,n1,n2=v
    return ((Q(m1)+b*n2)**2+(Q(m2)-b*n1)**2)/L+L*(n1*n1+n2*n2)

def exact_shell(L,b,C):
    # Any state of energy <= C obeys L||n||^2<=C and
    # ||m+B n||^2 <= L*C; hence |m_i| <= sqrt(LC)+|b|sqrt(C/L).
    N=0
    while L*(N+1)**2<=C: N+=1
    M=0
    bound=(L*C)**Q(1,2) if False else None
    # Rational upper bound: |m_i| <= LC+1+|b|(C/L+1), valid for C>=0.
    M=int(L*C+1+abs(b)*(C/L+1))+2
    return Counter(energy(v,L,b) for v in product(range(-M,M+1),repeat=2) for n1,n2 in product(range(-N,N+1),repeat=2) for v in [(v[0],v[1],n1,n2)] if energy(v,L,b)<=C)

checks=0
for L in (Q(2),Q(3),Q(4)):
    for b in (Q(1,5),Q(1,3),Q(1,2)):
        # All energies strictly below L are pure momentum; exact spectra agree.
        C=L-Q(1,10)
        assert exact_shell(L,Q(0),C)==exact_shell(L,b,C)
        # At energy L, b=0 has 4 more states than any nonintegral b in (0,1).
        s0=exact_shell(L,Q(0),L)
        sb=exact_shell(L,b,L)
        assert s0[L]-sb[L]==4
        checks+=1
print('P30 sharp visibility checks:',checks)
# Explicit first winding threshold at b in [0,1/2] for unit winding:
for L in (Q(2),Q(3),Q(4)):
    for b in (Q(0),Q(1,5),Q(1,3),Q(1,2)):
        minE=min(energy((m1,m2,n1,n2),L,b) for m1,m2 in product(range(-2,3),repeat=2) for n1,n2 in ((1,0),(-1,0),(0,1),(0,-1)))
        assert minE==L+b*b/L
print('P30 unit-winding onset checks:',12)
