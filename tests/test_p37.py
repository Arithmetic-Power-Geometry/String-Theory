from fractions import Fraction as F
from itertools import product
from collections import Counter
from hashlib import sha256

a,c,d,b=F(2),F(3),F(1,3),F(1,5)
C=F(3)

def energy(v, b=b):
 m1,m2,n1,n2=map(F,v);D=a*c-d*d;x=m1+b*n2;y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/D+a*n1*n1+2*d*n1*n2+c*n2*n2

def spin(v):return v[0]*v[2]+v[1]*v[3]

# Gershgorin eigenvalue bounds: 5/3 <= eigenvalues(G) <= 10/3.
# E<=3 implies ||n||² <= 9/5 <2; hence n=0 or unit winding.
# ||m+Bn|| <= sqrt(3*10/3)=sqrt(10); ||Bn||<=1/5,
# so |m_i| <4. Thus [-4,4]^2 x [-1,1]^2 contains all states.
hist=Counter(); vectors={}
for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
 z=energy(v)
 if z<=C:
  key=(z,spin(v));hist[key]+=1;vectors.setdefault(key,[]).append(v)
W=F(3373,1325)
assert hist[(W,1)]==2 and hist[(W,-1)]==0
asym=sorted((z,k,hist[z,k],hist[z,-k]) for z,k in hist if k>0 and hist[z,k]!=hist[z,-k])
assert asym[0]==(W,1,2,0)
print('P37 certified cutoff:',C)
print('P37 first spin-asymmetry:',asym[0])
print('P37 positive-spin witness charges:',vectors[(W,1)])
print('P37 complete states under cutoff:',sum(hist.values()))
print('P37 source SHA256:',sha256(open(__file__,'rb').read()).hexdigest())
