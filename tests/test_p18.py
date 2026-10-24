from fractions import Fraction as F
from itertools import product

def E(v,g,b):
 m1,m2,n1,n2=v
 x=F(m1)+b*n2; y=F(m2)-b*n1
 return x*x/g[0]+y*y/g[1]+g[0]*n1*n1+g[1]*n2*n2

def pairing(v,w):
 return v[0]*w[2]+v[1]*w[3]+v[2]*w[0]+v[3]*w[1]

def transform(v,k):
 m1,m2,n1,n2=v
 return (m1-k*n2,m2+k*n1,n1,n2)

states=list(product(range(-1,2),repeat=4))
checks=0
for g in ((F(1),F(1)),(F(2),F(3))):
 for b in (F(0),F(1,3)):
  for k in (-2,-1,1,2):
   for v in states:
    assert E(v,g,b)==E(transform(v,k),g,b+k)
    checks+=1
   for v in states:
    for w in states:
     assert pairing(v,w)==pairing(transform(v,k),transform(w,k))
     checks+=1
print('P18 exact covariance checks:',checks)
a=((1,0,0,0),(0,0,1,0))
c=((1,0,0,0),(0,1,0,0))
assert tuple(E(v,(F(1),F(1)),F(0)) for v in a)==tuple(E(v,(F(1),F(1)),F(0)) for v in c)
assert pairing(*a)==1 and pairing(*c)==0
print('P18 energy-only pair-statistic counterexample: passed')
