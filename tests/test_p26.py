from fractions import Fraction as F
from itertools import product
from math import isqrt

def eta(k,a,c,p):
    return a/F(k*k)+c*F(k)**(p-2)

def integer_optimum(a,c,p,kmax):
    if kmax<1 or a<=0 or c<=0 or p<1: raise ValueError('invalid inputs')
    return min(range(1,kmax+1),key=lambda k:(eta(k,a,c,p),k))

def independently_verified_optimum(a,c,p,kmax,k):
    assert 1<=k<=kmax
    return all(eta(k,a,c,p)<=eta(j,a,c,p) for j in range(1,kmax+1))

cases=0
for a,c,p,kmax in product((F(1,10),F(1),F(7)),(F(1,20),F(1),F(3)),(1,2,3,4,5),(1,2,3,8,16)):
    k=integer_optimum(a,c,p,kmax)
    assert independently_verified_optimum(a,c,p,kmax,k)
    cases+=1
print('P26 independently checked integer optima:',cases)
for p in (1,2):
    for a,c in product((F(1,10),F(1),F(7)),(F(1,20),F(1),F(3))):
        assert all(eta(k+1,a,c,p)<eta(k,a,c,p) for k in range(1,32))
print('P26 monotone subquadratic and quadratic noise models: 18')
a,c,p=F(8),F(1),4
assert eta(2,a,c,p)==F(6)
assert integer_optimum(a,c,p,12)==2
print('P26 quartic-noise optimum: k=2; eta=6')
# Adversarial model: multiplicative measurement error scales as k^2, so normalization cannot reduce it.
assert all(F(1,100)*k*k/F(k*k)==F(1,100) for k in range(1,100))
print('P26 relative-noise floor: exact')
