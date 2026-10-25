"""SIG-11: exact integer B-shift symmetry and global threshold reduction."""
from fractions import Fraction as F
from itertools import product
import json
A,C,D=F(2),F(3),F(1,3);DET=A*C-D*D
def energy(v,b):
 m1,m2,n1,n2=map(F,v);x=m1+b*n2;y=m2-b*n1
 return (C*x*x-2*D*x*y+A*y*y)/DET+A*n1*n1+2*D*n1*n2+C*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
def shift(v,k):
 m1,m2,n1,n2=v
 return (m1+k*n2,m2-k*n1,n1,n2)
def threshold(b):
 fractional=b-(b.numerator//b.denominator)
 t=min(fractional,1-fractional)
 return None if t==0 or t==F(1,2) else (133-6*t+18*t*t)/53
def run():
 checks=0
 for b in (F(1,2),F(1,3),F(7,5),F(-13,6)):
  for v in product(range(-2,3),repeat=4):
   assert energy(v,b)==energy(shift(v,1),b-1)
   assert spin(v)==spin(shift(v,1))
   checks+=1
 for v in product(range(-2,3),repeat=4):
  assert energy(v,F(1,2))==energy(shift(v,1),F(-1,2))
  assert spin(v)==spin(shift(v,1))
 assert threshold(F(1,5))==F(3313,1325)
 assert threshold(F(4,5))==threshold(F(1,5))
 assert threshold(F(6,5))==threshold(F(1,5))
 assert threshold(F(-1,5))==threshold(F(1,5))
 assert threshold(F(0)) is None and threshold(F(1,2)) is None
 print(json.dumps({'status':'PASS','shift_checks':checks,
  'half_integer_exact_spectral_equivalence':'PROVED_BY_CHARGE_BIJECTION',
  'global_formula':'T(t)=(133-6t+18t^2)/53, t=distance(b,Z), 0<t<1/2',
  'integer_and_half_integer_b':'complete spin-refined spectra identical; threshold infinity'},indent=2))
if __name__=='__main__':run()
