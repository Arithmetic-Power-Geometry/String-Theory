import math
from fractions import Fraction as F

def sector(x,q):
 a=math.exp(-x)
 return 1-(1+a**q)/(2**(q-1)*(1+a)**q)

def full(r,t,q,N=12):
 energies=[m*m/(r*r)+n*n*r*r for m in range(-N,N+1) for n in range(-N,N+1) if m or n]
 z=sum(math.exp(-t*e) for e in energies)
 zq=sum(math.exp(-q*t*e) for e in energies)
 return 1-zq/z**q

for x in (0.0,0.3,1.0,2.0,4.0):
 for t in (30.,60.,120.):
  # solve t*(r^2-r^-2)=x, positive r
  y=(x/t+math.sqrt((x/t)**2+4))/2
  r=math.sqrt(y)
  assert abs(full(r,t,2)-sector(x,2))<2e-8
  assert abs(full(1/r,t,2)-full(r,t,2))<2e-12
print('P13 asymptotic crossover checks passed: 15')
