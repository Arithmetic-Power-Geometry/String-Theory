from fractions import Fraction as F
from itertools import product
import hashlib

def E(v,g,b):
 a,c,d=g; det=a*c-d*d
 m1,m2,n1,n2=v
 x=F(m1)+b*n2; y=F(m2)-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2

def conjugate_b(v,g,b):
 a,c,d=g; det=a*c-d*d
 m1,m2,n1,n2=v
 u,vv=F(n2),F(-n1)
 q=(c*u*u-2*d*u*vv+a*vv*vv)/det
 if q==0:return None
 lin=2*(c*m1*u-d*(m1*vv+m2*u)+a*m2*vv)/det
 return -lin/q-b

probes=((1,0,0,0),(0,1,0,0),(1,1,0,0))
checks=0; distinct=0
for a,c,d,b in product((F(1),F(2),F(3,2)),(F(1),F(2)),(F(0),F(1,3),F(-1,2)),(F(-1),F(0),F(1,4),F(2,3))):
 if a*c<=d*d:continue
 g=(a,c,d)
 for v in ((1,0,0,1),(0,0,0,1),(1,1,1,1),(0,0,1,0),(1,-1,2,1)):
  other=conjugate_b(v,g,b)
  assert other is not None
  assert all(E(p,g,b)==E(p,g,other) for p in probes)
  assert E(v,g,b)==E(v,g,other)
  checks+=1
  if other!=b:distinct+=1
print('P22 exact four-probe ambiguity checks:',checks)
print('P22 distinct-background witnesses:',distinct)
assert distinct>0
