from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib

def energy(v,a,c,d,b):
 m1,m2,n1,n2=map(F,v)
 det=a*c-d*d
 x=m1+b*n2; y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2

def spin(v):
 m1,m2,n1,n2=v
 return m1*n1+m2*n2

params=[(F(2),F(3),F(1,3),F(1,5)),(F(3,2),F(7,4),F(1,7),F(2,5)),(F(5,3),F(9,4),F(-1,4),F(1,3))]
N=2
count=0
for a,c,d,b in params:
 assert a*c>d*d
 for v in product(range(-N,N+1),repeat=4):
  m1,m2,n1,n2=v
  mirror=(-m1,-m2,n1,n2)
  assert energy(v,a,c,d,b)==energy(mirror,a,c,d,-b)
  assert spin(mirror)==-spin(v)
  count+=1
print('P34 exact B-reflection energy and spin checks:',count)
# This parity involution is not a charge-lattice isometry of the Narain spin pairing:
assert spin((1,0,1,0))==1 and spin((-1,0,1,0))==-1
print('P34 non-duality of the specific relabelling: spin pairing reversed')
print('P34 SHA256:',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
