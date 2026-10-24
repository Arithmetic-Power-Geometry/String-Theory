from fractions import Fraction as F
from itertools import product

def calc(es,x,q):
    z=sum((x**e for e in es),F(0))
    zq=sum((x**(q*e) for e in es),F(0))
    p=[x**e/z for e in es]
    return 1-sum((a**q for a in p),F(0)),1-zq/z**q

n=0
for length in range(1,5):
    for es in product(range(4),repeat=length):
        for x in (F(1,2),F(2,3),F(3,4)):
            for q in (2,3,4):
                a,b=calc(es,x,q)
                assert a==b
                assert 0<=a<=1-F(1,length**(q-1))
                n+=1
print('P09 exact finite cutoff tests:',n)
