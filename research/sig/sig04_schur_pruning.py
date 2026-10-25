"""SIG-04: exact Schur-complement pruning, standard library only."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from statistics import median
from time import perf_counter
import json,sys,platform
A,C,D,B=F(2),F(3),F(1,3),F(1,5)
DET=A*C-D*D
def energy(v,b):
 m1,m2,n1,n2=map(F,v);x,y=m1+b*n2,m2-b*n1
 return (C*x*x-2*D*x*y+A*y*y)/DET+A*n1*n1+2*D*n1*n2+C*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
def reps():
 yield (0,0,0,0),1
 bounds=(range(-4,5),range(-4,5),range(-1,2),range(-1,2))
 for i,rg in enumerate(bounds):
  for negative in (x for x in rg if x<0):
   for tail in product(*bounds[i+1:]):yield (0,)*i+(negative,)+tail,2
def direct(b,mode):
 out=Counter();evaluated=0
 for v,w in reps():
  e=energy(v,b);evaluated+=1
  if e<=3:out[e if mode=='energy' else (e,spin(v))]+=w
 return out,evaluated
def pruned(b,mode):
 out=Counter();evaluated=0;excluded=0;checks=0
 for v,w in reps():
  m1,m2,n1,n2=v
  wind=A*n1*n1+2*D*n1*n2+C*n2*n2
  x=F(m1)+b*n2
  lower=wind+x*x/A
  checks+=1
  if lower>3:
   excluded+=1
   continue
  e=energy(v,b);evaluated+=1
  if e<=3:out[e if mode=='energy' else (e,spin(v))]+=w
 return out,evaluated,excluded,checks
def run():
 rows=[]
 for b in (B,-B):
  for mode in ('energy','spin'):
   original,n=direct(b,mode)
   new,k,excluded,checks=pruned(b,mode)
   assert original==new and sum(new.values())==39
   times={}
   for name,fn in (('direct',direct),('pruned',pruned)):
    samples=[]
    for _ in range(7):
     start=perf_counter()
     for __ in range(20):fn(b,mode)
     samples.append((perf_counter()-start)/20)
    times[name]=round(median(samples)*1000,4)
   rows.append(dict(b=str(b),mode=mode,exact='PASS',states=39,baseline_evaluations=n,pruned_evaluations=k,excluded=excluded,bound_checks=checks,times_ms=times,speedup=round(times['direct']/times['pruned'],3)))
 print(json.dumps(dict(python=sys.version.split()[0],platform=platform.platform(),results=rows),indent=2))
if __name__=='__main__':run()
