"""SIG-08: exact rational polynomial interval certificate for first spin separation."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import json
A,C,D=F(2),F(3),F(1,3)
DET=A*C-D*D
LO,HI=F(19,100),F(21,100)
T=(F(133,53),-F(6,53),F(18,53))
Q=tuple(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
def polynomial(v,sgn):
 m1,m2,n1,n2=map(F,v)
 p,q=sgn*n2,-sgn*n1
 w=A*n1*n1+2*D*n1*n2+C*n2*n2
 return (w+(C*m1*m1-2*D*m1*m2+A*m2*m2)/DET,
         (2*C*m1*p-2*D*(m1*q+m2*p)+2*A*m2*q)/DET,
         (C*p*p-2*D*p*q+A*q*q)/DET)
def spin(v):return v[0]*v[2]+v[1]*v[3]
def exact_range(p):
 a,b,c=p
 values=[a+b*x+c*x*x for x in (LO,HI)]
 if c and LO<=-b/(2*c)<=HI:values.append(a-b*b/(4*c))
 return min(values),max(values)
def run():
 assert len(Q)==729
 assert T==polynomial((-1,0,1,0),1)
 assert T==polynomial((-1,0,-1,0),-1)
 results=[]
 for sgn in (1,-1):
  lower=defaultdict(lambda:defaultdict(int));equal=defaultdict(lambda:defaultdict(int));above=0
  for v in Q:
   p=polynomial(v,sgn);diff=tuple(x-y for x,y in zip(p,T))
   low,high=exact_range(diff)
   if high<0:lower[p][spin(v)]+=1
   elif low>0:above+=1
   elif low==high==0:equal[p][spin(v)]+=1
   else:raise AssertionError(('nonuniform ordering',sgn,v,str(low),str(high)))
  assert sum(sum(g.values()) for g in lower.values())==25
  assert sum(sum(g.values()) for g in equal.values())==2
  assert len(lower)==13
  assert all(set(group)=={0} for group in lower.values())
  assert set(equal)=={T}
  assert equal[T]==({-1:2} if sgn==1 else {1:2})
  assert above==702
  results.append({'sign':sgn,'strictly_lower_states':25,'strictly_lower_polynomial_groups':13,
                  'at_threshold':dict(equal[T]),'strictly_above_states':above})
 print(json.dumps({'status':'PASS','b_interval':[str(LO),str(HI)],
                   'first_threshold_coefficients':[str(z) for z in T],
                   'charge_box':len(Q),'results':results},indent=2))
if __name__=='__main__':run()
