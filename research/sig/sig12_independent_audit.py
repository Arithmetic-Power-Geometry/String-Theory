from fractions import Fraction as F
from itertools import product
from collections import Counter
A,C,D=F(2),F(3),F(1,3);DET=A*C-D*D
T=(F(133,53),-F(6,53),F(18,53))
def poly(v,s):
 m1,m2,n1,n2=map(F,v);p=s*n2;q=-s*n1
 w=A*n1*n1+2*D*n1*n2+C*n2*n2
 return (w+(C*m1*m1-2*D*m1*m2+A*m2*m2)/DET,(2*C*m1*p-2*D*(m1*q+m2*p)+2*A*m2*q)/DET,(C*p*p-2*D*p*q+A*q*q)/DET)
def val(p,x):return p[0]+p[1]*x+p[2]*x*x
for s in (1,-1):
 ident=Counter();extra=Counter();bad=[];total=0
 for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
  spin=v[0]*v[2]+v[1]*v[3]
  if not spin:continue
  total+=1;p=tuple(a-b for a,b in zip(poly(v,s),T))
  values=[val(p,F(0)),val(p,F(1,2))]
  if p[2]>0:
   x=-p[1]/(2*p[2])
   if 0<x<F(1,2):values.append(val(p,x))
  if min(values)<0:bad.append(v)
  if p==(0,0,0):ident[spin]+=1
  elif val(p,F(1,2))==0:extra[spin]+=1
 assert total==576 and not bad and ident==Counter({-s:2}) and extra==Counter({s:2})
 print('PASS sign',s,'nonzero',total,'identical',dict(ident),'additional endpoint',dict(extra),'violations',len(bad))
