from fractions import Fraction as F
from itertools import product
from collections import Counter

def E(v,L,b):
 m1,m2,n1,n2=v
 return ((F(m1)+b*n2)**2+(F(m2)-b*n1)**2)/L+L*(n1*n1+n2*n2)

def wind_spectrum(L,b,C):
 # C <= L+1/(4L) < 2L for L>=1: only unit winding can contribute
 out=Counter()
 for n1,n2 in ((1,0),(-1,0),(0,1),(0,-1)):
  for m1,m2 in product(range(-2,3),repeat=2):
   e=E((m1,m2,n1,n2),L,b)
   if e<=C:out[e]+=1
 return out

count=0
for L in (F(1),F(2),F(3),F(5)):
 for b in (F(0),F(1,10),F(1,4),F(1,3),F(1,2)):
  C=L+F(1,4)/L
  spectrum=wind_spectrum(L,b,C)
  onset=L+b*b/L
  assert min(spectrum)==onset
  assert spectrum[onset]>=4
  assert L*(onset-L)==b*b
  count+=1
print('P31 exact spectral-onset reconstructions:',count)
# All b in [0,1/2] are uniquely identified by their onset in this family.
for L in (F(1),F(2),F(5)):
 for b,c in product((F(0),F(1,10),F(1,4),F(1,3),F(1,2)),repeat=2):
  assert (L+b*b/L==L+c*c/L)==(b==c)
print('P31 pairwise spectral separation checks:',75)
