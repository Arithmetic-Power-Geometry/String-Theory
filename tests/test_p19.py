from fractions import Fraction as F
from itertools import product

def energy(v,g,b):
 m1,m2,n1,n2=v
 a=F(m1)+b*n2; c=F(m2)-b*n1
 return a*a/g[0]+c*c/g[1]+g[0]*n1*n1+g[1]*n2*n2

def chiral(v,g,b,sign):
 m1,m2,n1,n2=v
 a=F(m1)+b*n2; c=F(m2)-b*n1
 return (a+sign*g[0]*n1,c+sign*g[1]*n2)

def bilinear(v,w,g,b,sign):
 a=chiral(v,g,b,sign); c=chiral(w,g,b,sign)
 return (a[0]*c[0]/g[0]+a[1]*c[1]/g[1])/2

def L(v,w):return v[0]*w[2]+v[1]*w[3]+v[2]*w[0]+v[3]*w[1]

states=list(product(range(-1,2),repeat=4))
checks=0
for g in ((F(1),F(1)),(F(2),F(3)),(F(1,2),F(5,3))):
 for b in (F(0),F(1,3),F(-2,5)):
  for v in states:
   assert bilinear(v,v,g,b,1)+bilinear(v,v,g,b,-1)==energy(v,g,b)
   for w in states:
    assert bilinear(v,w,g,b,1)-bilinear(v,w,g,b,-1)==L(v,w)
    checks+=1
print('P19 exact genus-two slice identities:',checks)
