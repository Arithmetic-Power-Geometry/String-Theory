from fractions import Fraction as F
from itertools import product
from collections import Counter
from hashlib import sha256

C=F(3,8)

def energy(v,a,c):
    m1,m2,n1,n2=v
    return F(m1*m1)/a+F(m2*m2)/c+a*n1*n1+c*n2*n2

def shell(a,c,cutoff):
    # Conservative integer search, independently justified by E >= min(a,1/a,c,1/c)*||v||^2
    lam=min(a,1/a,c,1/c)
    n=0
    while lam*(n+1)**2<=cutoff:n+=1
    return Counter(energy(v,a,c) for v in product(range(-n,n+1),repeat=4) if energy(v,a,c)<=cutoff)

A=(F(1,4),F(1)); B=(F(1,4),F(2))
assert shell(*A,C)==shell(*B,C)==Counter({F(0):1,F(1,4):2})
assert shell(*A,F(1,2))==Counter({F(0):1,F(1,4):2})
assert shell(*B,F(1,2))==Counter({F(0):1,F(1,4):2,F(1,2):2})
print('P28 identical spectra up to C=3/8:', sorted(shell(*A,C).items()))
print('P28 first distinguishing level E=1/2: A multiplicity',shell(*A,F(1,2))[F(1,2)],'B multiplicity',shell(*B,F(1,2))[F(1,2)])
# Continuous isospectral low-energy family: c in [1,2], C<1/2.
for c in (F(1),F(9,8),F(5,4),F(3,2),F(7,4),F(2)):
    assert shell(F(1,4),c,C)==Counter({F(0):1,F(1,4):2})
print('P28 exact low-window family checks:',6)
# Independent coefficient-wise lower-bound certificate for the enumeration.
for a,c in (A,B):
    lam=min(a,1/a,c,1/c)
    assert lam==F(1,4)
    for v in product(range(-3,4),repeat=4):
        assert energy(v,a,c)>=lam*sum(z*z for z in v)
print('P28 lower-bound exact checks:',2*7**4)
