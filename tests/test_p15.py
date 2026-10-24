import math
from fractions import Fraction
from itertools import product

def obstruction_lower(R,t,lam):
    a=math.exp(-math.pi*t*(R*R+1/(R*R)))
    return 4*a*(1-math.cos(2*math.pi*lam))

def real_gap(R,t,lam,N=9):
    return sum(math.exp(-math.pi*t*(m*m/(R*R)+n*n*R*R))*(1-math.cos(2*math.pi*lam*m*n)) for m,n in product(range(-N,N+1),repeat=2))

count=0
for R in (0.75,1.0,1.5):
 for t in (0.6,1.0,2.0):
  for lam in (0.0,0.25,0.5,1.0,1.25):
   gap=real_gap(R,t,lam)
   bound=obstruction_lower(R,t,lam)
   assert gap+1e-12>=bound,(R,t,lam,gap,bound)
   if lam in (0.0,1.0): assert abs(gap)<1e-12
   if lam in (0.25,0.5,1.25): assert gap>0
   count+=1
print('P15 quantitative modular-T lower-bound tests passed:',count)
