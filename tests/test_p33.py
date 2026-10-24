from fractions import Fraction as F
from itertools import product
from collections import Counter
from hashlib import sha256

A=[F(3,2),F(7,4),F(2)]
B=[F(0),F(1,5),F(1,3),F(1,2)]

def energy(v,a,c,b):
 m1,m2,n1,n2=v
 return (F(m1)+b*n2)**2/a+(F(m2)-b*n1)**2/c+a*n1*n1+c*n2*n2

def spectrum(a,c,b,C):
 # E<=C implies |n_i|<=sqrt(C/min(a,c)) <=2;
 # |m_i| <= sqrt(C*max(a,c))+|b|*sqrt(C/min(a,c)) <4 for C<=17/8.
 return Counter(energy(v,a,c,b) for v in product(range(-4,5),repeat=4) if energy(v,a,c,b)<=C)

def recover(a,c,b):
 C=F(17,8)
 s=spectrum(a,c,b,C)
 positive=sorted(e for e in s if 0<e<1)
 if a==c:
  assert s[positive[0]]==4
  aa=cc=1/positive[0]
 else:
  assert s[positive[0]]==s[positive[1]]==2
  aa,cc=sorted((1/positive[0],1/positive[1]))
 p=Counter()
 for m1,m2 in product(range(-4,5),repeat=2):
  e=F(m1*m1)/aa+F(m2*m2)/cc
  if e<=C:p[e]+=1
 residual=s-p
 assert all(v>0 for v in residual.values())
 onset=min(residual)
 bb2=max(aa,cc)*(onset-min(aa,cc))
 assert bb2==b*b
 return aa,cc,bb2

cases=0
for a,c,b in product(A,A,B):
 assert recover(a,c,b)==(min(a,c),max(a,c),b*b)
 cases+=1
print('P33 joint inverse cases:',cases)
print('P33 uniform cutoff:',F(17,8))
print('P33 exact source SHA256:',sha256(open(__file__,'rb').read()).hexdigest())
