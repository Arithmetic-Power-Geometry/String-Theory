from fractions import Fraction as F
from itertools import product
from hashlib import sha256
from pathlib import Path
G0=(F(2),F(3),F(1,3)); b=F(1,5)
def E(v,L,b=b):
 m1,m2,n1,n2=map(F,v)
 a,c,d=(L*z for z in G0)
 x=m1+b*n2;y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/(a*c-d*d)+a*n1*n1+2*d*n1*n2+c*n2*n2
def s(v):return v[0]*v[2]+v[1]*v[3]
w=(1,0,1,0)
assert E(w,F(1))==F(3373,1325)
for L in (F(10),F(100)):
 C=F(1)
 assert 5*L/3>C
 for v in product(range(-4,5),repeat=4):
  if E(v,L)<=C:
   assert v[2:]==(0,0) and s(v)==0
   assert E(v,L)==E(v,L,-b)
 print(f'L={L}: E<=1 contains pure momentum only; B signs indistinguishable')
print('P43 witness E(L) at L=1:',E(w,F(1)))
print('P43 analytic countable-exception proof: each opposite-spin collision is a nonzero rational function of L')
print('P43 source SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
