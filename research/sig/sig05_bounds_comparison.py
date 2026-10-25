"""SIG-05: exact comparison of elementary certified lower bounds."""
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
A,C,D=F(2),F(3),F(1,3)
Q=tuple(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
REPS=[v for v in Q if v<=tuple(-t for t in v)]
assert len(REPS)==365
def energy(v,b):
 m1,m2,n1,n2=map(F,v);x=m1+b*n2;y=m2-b*n1
 return (C*x*x-2*D*x*y+A*y*y)/(A*C-D*D)+A*n1*n1+2*D*n1*n2+C*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
def run(b,cut,method):
 out=Counter();evaluated=0;checks=0
 for v in REPS:
  m1,m2,n1,n2=v;x=F(m1)+b*n2;y=F(m2)-b*n1
  w=A*n1*n1+2*D*n1*n2+C*n2*n2
  if method!='full':
   checks+=1
   if method=='wind':lb=w
   elif method=='schur1':lb=w+x*x/A
   elif method=='schur2':lb=w+y*y/C
   elif method=='maxschur':lb=w+max(x*x/A,y*y/C)
   else:raise ValueError(method)
   if lb>cut:continue
  evaluated+=1;e=energy(v,b)
  if e<=cut:out[(e,spin(v))]+=1 if v==(0,0,0,0) else 2
 return out,evaluated,checks
def main():
 cases=[]
 for b in [F(0),F(1,10),F(1,5),F(1,2),-F(1,5)]:
  for cut in [F(1),F(2),F(3),F(4)]:
   baseline,_,_=run(b,cut,'full');methods={}
   for method in ['full','wind','schur1','schur2','maxschur']:
    out,k,checks=run(b,cut,method)
    assert out==baseline,(b,cut,method)
    methods[method]={'full_evaluations':k,'bound_checks':checks}
   cases.append({'b':str(b),'cutoff':str(cut),'states':sum(baseline.values()),'methods':methods})
 print(json.dumps({'cases':cases,'exact_equality':'PASS'},indent=2))
if __name__=='__main__':main()
