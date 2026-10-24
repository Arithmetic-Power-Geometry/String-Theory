from fractions import Fraction as F
from itertools import product

def phase_classes(lam,N):
    return {lam*m*n for m,n in product(range(-N,N+1),repeat=2)}

count=0
for den in range(1,9):
 for num in range(-12,13):
  lam=F(num,den)
  phases=phase_classes(lam,3)
  all_integral=all(x.denominator==1 for x in phases)
  assert all_integral==(lam.denominator==1)
  count+=1
print('P14 exact modular-T obstruction tests:',count)
