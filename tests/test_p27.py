from fractions import Fraction as F
from itertools import product
import hashlib

def energy(v,b):
    m1,m2,n1,n2=v
    x=F(m1)+b*n2
    y=F(m2)-b*n1
    return x*x+y*y+n1*n1+n2*n2

def shift(v,k):
    m1,m2,n1,n2=v
    return (m1-k*n2,m2+k*n1,n1,n2)

def pairing(v,w):
    return v[0]*w[2]+v[1]*w[3]+v[2]*w[0]+v[3]*w[1]

states=list(product(range(-2,3),repeat=4))
checks=0
for k in (-3,-2,-1,1,2,3):
    for v in states:
        assert energy(v,F(0))==energy(shift(v,k),F(k))
        checks+=1
assert energy((0,0,0,1),F(0))==1
assert energy((0,0,0,1),F(1))==2
assert energy((1,0,0,1),F(0))==2
assert energy((1,0,0,1),F(1))==5
assert energy(shift((0,0,0,1),1),F(1))==1
assert energy(shift((1,0,0,1),1),F(1))==2
print('P27 exact duality-covariant charge checks:',checks)
print('P27 fixed-label e4 energies:',energy((0,0,0,1),F(0)),energy((0,0,0,1),F(1)))
print('P27 fixed-label e1+e4 energies:',energy((1,0,0,1),F(0)),energy((1,0,0,1),F(1)))
print('P27 transformed-label e4 energy:',energy(shift((0,0,0,1),1),F(1)))
print('P27 transformed-label e1+e4 energy:',energy(shift((1,0,0,1),1),F(1)))
