from fractions import Fraction as F
from itertools import product
def energy(v,a,c,d,b):
 m1,m2,n1,n2=map(F,v); D=a*c-d*d
 x=m1+b*n2;y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/D+a*n1*n1+2*d*n1*n2+c*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
count=0
for a,c,d,b in ((F(2),F(3),F(1,3),F(1,5)),(F(3,2),F(7,4),F(-1,7),F(2,5)),(F(5,3),F(9,4),F(1,4),F(1,3))):
 for v in product(range(-2,3),repeat=4):
  m1,m2,n1,n2=v
  w=(-m1,m2,-n1,n2)
  assert energy(v,a,c,d,b)==energy(w,a,c,-d,-b)
  assert spin(v)==spin(w)
  count+=1
print('P36 exact geometric-reflection duality checks:',count)
