"""SIG-09: independent exact rational interval audit of SIG-08."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
A,C,D=F(2),F(3),F(1,3);DET=A*C-D*D
T=(F(133,53),-F(6,53),F(18,53));END=F(3,14)
def polynomial(v,sg):
 m1,m2,n1,n2=map(F,v);p,q=sg*n2,-sg*n1
 w=A*n1*n1+2*D*n1*n2+C*n2*n2
 return (w+(C*m1*m1-2*D*m1*m2+A*m2*m2)/DET,
 (2*C*m1*p-2*D*(m1*q+m2*p)+2*A*m2*q)/DET,
 (C*p*p-2*D*p*q+A*q*q)/DET)
def val(p,b):return p[0]+p[1]*b+p[2]*b*b
def audit():
 results=[]
 for sg in (1,-1):
  low=Counter();equal=Counter();high=0;endpoint=Counter()
  for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
   p=polynomial(v,sg);diff=tuple(p[i]-T[i] for i in range(3))
   spin=v[0]*v[2]+v[1]*v[3]
   at0=val(diff,F(0));atend=val(diff,END);mid=val(diff,F(1,5))
   if mid<0:
    assert at0<=0 and atend<=0
    if diff[2]>0:assert val(diff,max(F(0),min(END,-diff[1]/(2*diff[2]))))<=0
    low[spin]+=1
   elif mid>0:
    assert at0>=0 and atend>=0
    if diff[2]>0:
     vertex=max(F(0),min(END,-diff[1]/(2*diff[2])))
     assert val(diff,vertex)>0 or vertex in (0,END)
    high+=1
   else:
    assert diff==(0,0,0)
    equal[spin]+=1
   if atend==0:endpoint[spin]+=1
  assert low==Counter({0:25}) and high==702
  assert equal==Counter({-sg:2})
  assert endpoint==Counter({-sg:2,0:2})
  results.append({'B_sign':sg,'strictly_lower_spin_counts':dict(low),
   'threshold_spin_counts':dict(equal),'strictly_above':high,
   'endpoint_threshold_spin_counts':dict(endpoint)})
 print(json.dumps({'status':'PASS','interval':'0 < b <= 3/14',
  'threshold_polynomial':[str(x) for x in T],'results':results},indent=2))
if __name__=='__main__':audit()
