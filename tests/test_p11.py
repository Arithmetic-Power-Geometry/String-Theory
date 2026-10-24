from fractions import Fraction as F
from itertools import product

def E(r,m,n):return F(m*m)/(r*r)+r*r*n*n

def spectrum(r,N):return sorted(E(r,m,n) for m,n in product(range(-N,N+1),repeat=2))

count=0
for r in (F(1,3),F(1,2),F(2,3),F(1),F(3,2),F(2),F(3)):
 for N in range(1,5):
  assert spectrum(r,N)==spectrum(1/r,N)
  count+=1
print('P11 exact full-square cutoff duality tests:',count)
