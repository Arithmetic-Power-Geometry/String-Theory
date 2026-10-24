from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib

def energy(m1,m2,n1,n2,a,c,b):
    return (F(m1)+b*n2)**2/a+(F(m2)-b*n1)**2/c+a*n1*n1+c*n2*n2

def winding_min(a,c,b):
    # Certified enumeration: the witness <= 5/4 min(a,c) < 2 min(a,c),
    # so any minimizer has unit winding, and nearest momentum is in [-1,1]^2.
    candidates=[]
    for n1,n2 in ((1,0),(-1,0),(0,1),(0,-1)):
        for m1,m2 in product(range(-1,2),repeat=2):
            candidates.append(energy(m1,m2,n1,n2,a,c,b))
    return min(candidates)

cases=0
for a,c in product((F(1),F(5,4),F(2),F(3)),repeat=2):
    for b in (F(0),F(1,10),F(1,4),F(1,3),F(1,2)):
        observed=winding_min(a,c,b)
        predicted=min(a,c)+b*b/max(a,c)
        assert observed==predicted,(a,c,b,observed,predicted)
        assert max(a,c)*(observed-min(a,c))==b*b
        cases+=1
print('P32 exact rectangular onset and inverse checks:',cases)

pairs=0
for a,c in product((F(1),F(2),F(3)),repeat=2):
    for b,d in product((F(0),F(1,10),F(1,4),F(1,3),F(1,2)),repeat=2):
        assert (winding_min(a,c,b)==winding_min(a,c,d))==(b==d)
        pairs+=1
print('P32 pairwise identifiability checks:',pairs)
print('P32 test source SHA256:',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
