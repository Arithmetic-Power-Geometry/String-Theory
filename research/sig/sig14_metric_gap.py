"""SIG-14: independently executable exact interior-gap certificate."""
from fractions import Fraction as F
from itertools import product
A,C,D=F(2),F(3),F(1,3);DET=A*C-D*D
T=(F(133,53),-F(6,53),F(18,53))
L,R=F(1,10),F(2,5)
def poly(v,sg):
 m1,m2,n1,n2=map(F,v);p,q=sg*n2,-sg*n1
 return (A*n1*n1+2*D*n1*n2+C*n2*n2+(C*m1*m1-2*D*m1*m2+A*m2*m2)/DET,(2*C*m1*p-2*D*(m1*q+m2*p)+2*A*m2*q)/DET,(C*p*p-2*D*p*q+A*q*q)/DET)
def val(p,b):return p[0]+p[1]*b+p[2]*b*b
for sg in (1,-1):
 minimum=None;arg=None;witness=0;checked=0
 for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
  if v[0]*v[2]+v[1]*v[3]==0:continue
  checked+=1
  delta=tuple(x-y for x,y in zip(poly(v,sg),T))
  if delta==(0,0,0):witness+=1;continue
  vals=[(val(delta,L),L),(val(delta,R),R)]
  if delta[2]>0:
   vertex=-delta[1]/(2*delta[2])
   if L<vertex<R:vals.append((val(delta,vertex),vertex))
  z,x=min(vals)
  if minimum is None or z<minimum:minimum=z;arg=(v,x)
 assert checked==576 and witness==2 and minimum==F(6,265)
 print('PASS sign=',sg,'nonzero_spin=',checked,'witnesses=',witness,'minimum_gap=',minimum,'attained_at=',arg)
eps=F(1,10000)
assert 72*eps<F(6,265)
print('PASS metric_perturbation_entrywise_epsilon=',eps,'max_relative_gap_loss=',72*eps)
