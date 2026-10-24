from fractions import Fraction as F
from itertools import product

def energy(v,g,b):
 m1,m2,n1,n2=v
 x=F(m1)+b*n2; y=F(m2)-b*n1
 return x*x/g[0]+y*y/g[1]+g[0]*n1*n1+g[1]*n2*n2

def pair(v,w):
 return v[0]*w[2]+v[1]*w[3]+v[2]*w[0]+v[3]*w[1]

def shift(v,k):
 m1,m2,n1,n2=v
 return (m1-k*n2,m2+k*n1,n1,n2)

def oracle(g,b,C):
 # Since E >= g_i*n_i^2, bound winding coordinates first.
 N=[int((float(C/g[i]))**.5)+1 for i in (0,1)]
 hits=set()
 for n1 in range(-N[0],N[0]+1):
  for n2 in range(-N[1],N[1]+1):
   # Since E >= (m_i+(Bn)_i)^2/g_i, bound each shifted momentum.
   A=[int((float(C*g[i]))**.5)+1 for i in (0,1)]
   center=(-b*n2,b*n1)
   for m1 in range(int(center[0])-A[0]-1,int(center[0])+A[0]+2):
    for m2 in range(int(center[1])-A[1]-1,int(center[1])+A[1]+2):
     v=(m1,m2,n1,n2)
     if energy(v,g,b)<=C:hits.add(v)
 return hits

cases=0
for g in ((F(1),F(1)),(F(2),F(3)),(F(1),F(2))):
 for b in (F(0),F(1,4)):
  for k in (-1,1):
   C=F(1)
   a=oracle(g,b,C); aa=oracle(g,b+k,C)
   assert {shift(v,k) for v in a}==aa
   assert sorted(energy(v,g,b) for v in a)==sorted(energy(v,g,b+k) for v in aa)
   for v in a:
    for w in a:
     assert pair(v,w)==pair(shift(v,k),shift(w,k))
   cases+=1
print('P20 certified energy-ball duality cases:',cases)
