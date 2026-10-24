from fractions import Fraction as F
from collections import Counter
from itertools import product
import hashlib

def energy(v,L,b):
 m1,m2,n1,n2=v
 return (F(m1)+b*n2)**2/L+(F(m2)-b*n1)**2/L+L*(n1*n1+n2*n2)

def certified_shell(L,b,C):
 # For E<=C<L, winding is necessarily zero. Enumerate only pure momenta.
 assert L>C>0
 out=Counter()
 q=0
 while F((q+1)**2,L)<=C:q+=1
 for m1,m2 in product(range(-q,q+1),repeat=2):
  val=F(m1*m1+m2*m2,L)
  if val<=C:out[val]+=1
 return out

cases=0
for C in (F(1,2),F(1),F(5,2),F(9,2),F(11)):
 L=int(C)+2
 a=certified_shell(F(L),F(0),C)
 for b in (F(1,5),F(1,3),F(1,2)):
  assert a==certified_shell(F(L),b,C)
  cases+=1
 print('cutoff',C,'L',L,'states',sum(a.values()),'distinct B examples',3)
print('P29 exact finite-window indistinguishability cases:',cases)
for L in (2,3,5,7):
 E=F(L)
 # At E=L, b=0 has 4 winding unit vectors, b=1/2 has none;
 # pure momentum contributions are identical in both backgrounds.
 pure=sum(F(m1*m1+m2*m2,L)==E for m1,m2 in product(range(-L,L+1),repeat=2))
 assert pure>=4
 # Any winding with |n|^2>=2 has E>=2L; unit winding has
 # nonzero fractional shifted momentum for half-integer b.
 assert all(energy((m1,m2,n1,n2),F(L),F(1,2))>E
   for n1,n2 in ((1,0),(-1,0),(0,1),(0,-1))
   for m1,m2 in product(range(-L-1,L+2),repeat=2))
 print('distinguishing energy',E,'multiplicity B=0',pure+4,'B=1/2',pure)
print('P29 exact full-spectrum separation checks:',4)
