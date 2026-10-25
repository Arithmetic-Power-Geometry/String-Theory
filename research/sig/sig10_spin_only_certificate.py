"""SIG-10: exact spin-only polynomial certificate for 0 < b < 1/2."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
A,C,D=F(2),F(3),F(1,3);DET=A*C-D*D
HI=F(1,2);T=(F(133,53),-F(6,53),F(18,53))
def poly(v,sg):
 m1,m2,n1,n2=map(F,v);p,q=sg*n2,-sg*n1
 w=A*n1*n1+2*D*n1*n2+C*n2*n2
 return (w+(C*m1*m1-2*D*m1*m2+A*m2*m2)/DET,
         (2*C*m1*p-2*D*(m1*q+m2*p)+2*A*m2*q)/DET,
         (C*p*p-2*D*p*q+A*q*q)/DET)
def value(p,b):return p[0]+p[1]*b+p[2]*b*b
def audit():
 results=[]
 for sg in (1,-1):
  total=0;ident=Counter();boundary=Counter();other=0
  for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
   spin=v[0]*v[2]+v[1]*v[3]
   if spin==0:continue
   total+=1
   delta=tuple(x-y for x,y in zip(poly(v,sg),T))
   if delta==(0,0,0):
    ident[spin]+=1;continue
   checks=[value(delta,F(0)),value(delta,HI)]
   if delta[2]>0:
    vertex=-delta[1]/(2*delta[2])
    if F(0)<vertex<HI:checks.append(value(delta,vertex))
   assert min(checks)>=0,(sg,v,delta)
   assert value(delta,F(1,4))>0,(sg,v,delta)
   if min(checks)==0:boundary[spin]+=1
   other+=1
  assert total==576 and other==574
  assert ident==Counter({-sg:2})
  assert boundary==Counter({sg:4})
  results.append({'sign':sg,'nonzero_spin_charges':total,'identical_threshold_charges':dict(ident),
    'strictly_above_threshold_in_open_interval':other,'endpoint_touching_charges':dict(boundary)})
 print(json.dumps({'status':'PASS','parameter_interval':'0 < b < 1/2',
  'threshold_coefficients':[str(z) for z in T],'results':results},indent=2))
if __name__=='__main__':audit()
