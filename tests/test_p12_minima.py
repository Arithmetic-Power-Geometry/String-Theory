from fractions import Fraction as F
from itertools import product

def levels(r,N=5):
    es=[F(m*m)/(r*r)+r*r*n*n for m,n in product(range(-N,N+1),repeat=2) if m or n]
    low=min(es)
    return low,es.count(low)

rs=[F(1,3),F(1,2),F(2,3),F(3,4),F(1),F(4,3),F(3,2),F(2),F(3)]
for r in rs:
    e,g=levels(r)
    assert e==min(r*r,1/(r*r))
    assert g==(4 if r==1 else 2)
    assert levels(r)==levels(1/r)
print('P12 exact minimum and degeneracy checks:',len(rs))
