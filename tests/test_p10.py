from fractions import Fraction as F
from itertools import product

def defect(r,q):
    a,b=r*r,1/(r*r)
    x,y=a/(a+b),b/(a+b)
    return 1-x**q-y**q

n=0
for r in [F(1,5),F(1,3),F(1,2),F(2,3),F(1),F(3,2),F(2),F(3),F(5)]:
    for q in (2,3,4,5):
        v=defect(r,q)
        assert v==defect(1/r,q)
        assert v<=1-F(1,2**(q-1))
        assert (v==1-F(1,2**(q-1)))==(r==1)
        n+=1
print('P10 exact two-sector tests passed:',n)
