from fractions import Fraction as F
from itertools import product
from collections import Counter

def e(v,a,c,d,b):
 m1,m2,n1,n2=map(F,v); D=a*c-d*d
 x=m1+b*n2; y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/D+a*n1*n1+2*d*n1*n2+c*n2*n2

def s(v):return v[0]*v[2]+v[1]*v[3]

backgrounds=[(F(2),F(3),F(1,3),F(1,5)),(F(3,2),F(7,4),F(-1,7),F(2,5)),(F(5,3),F(9,4),F(1,4),F(1,3))]
N=2
count=0
for a,c,d,b in backgrounds:
 assert a*c>d*d
 plus=Counter(); minus=Counter()
 for v in product(range(-N,N+1),repeat=4):
  m1,m2,n1,n2=v; mirror=(-m1,-m2,n1,n2)
  assert e(v,a,c,d,b)==e(mirror,a,c,d,-b)
  assert s(v)==-s(mirror)
  plus[(e(v,a,c,d,b),s(v))]+=1
  minus[(e(v,a,c,d,-b),s(v))]+=1
  count+=1
 assert all(plus[(E,k)]==minus[(E,-k)] for E,k in plus)
 print('background spin-reflection multiset certified on symmetric charge box',a,c,d,b)
print('P35 charge-wise exact checks:',count)
