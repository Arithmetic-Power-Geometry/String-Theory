"""SIG-06: independent exact projected-norm baseline versus SIG max-bound."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from statistics import median
from time import perf_counter
import json,platform,sys
a,c,d=F(2),F(3),F(1,3)
det=a*c-d*d
M=range(-4,5);N=range(-1,2)
def energy(v,b):
 m1,m2,n1,n2=map(F,v);x=m1+b*n2;y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
def full(b,cut):
 out=Counter();calls=0
 for v in product(M,M,N,N):
  e=energy(v,b);calls+=1
  if e<=cut:out[(e,spin(v))]+=1
 return out,{'full_energy':calls}
def maxschur(b,cut):
 out=Counter();calls=0;checks=0
 for v in product(M,M,N,N):
  if v>tuple(-z for z in v):continue
  m1,m2,n1,n2=v;x=F(m1)+b*n2;y=F(m2)-b*n1
  w=a*n1*n1+2*d*n1*n2+c*n2*n2
  checks+=1
  if w+max(x*x/a,y*y/c)>cut:continue
  e=energy(v,b);calls+=1
  if e<=cut:out[(e,spin(v))]+=1 if v==(0,0,0,0) else 2
 return out,{'full_energy':calls,'bound_checks':checks}
def projected(b,cut):
 out=Counter();calls=0;first=0;second=0;wind=0
 for n1,n2 in product(N,N):
  w=a*n1*n1+2*d*n1*n2+c*n2*n2;wind+=1
  if w>cut:continue
  for m1 in M:
   x=F(m1)+b*n2;lower=w+x*x/a;first+=1
   if lower>cut:continue
   for m2 in M:
    y=F(m2)-b*n1
    exact=lower+(a*y-d*x)**2/(a*det);second+=1
    if exact>cut:continue
    v=(m1,m2,n1,n2);e=energy(v,b);calls+=1
    assert e==exact
    out[(e,spin(v))]+=1
 return out,{'full_energy':calls,'winding_checks':wind,'first_checks':first,'second_checks':second}
def timing(fn,b,cut):
 trials=[]
 for _ in range(3):
  t=perf_counter()
  for _ in range(5):fn(b,cut)
  trials.append((perf_counter()-t)/5)
 return round(median(trials)*1000,4)
def main():
 rows=[]
 for b in (F(0),F(1,10),F(1,5),F(1,2),-F(1,5)):
  for cut in (F(1),F(2),F(3)):
   base,bc=full(b,cut);mx,mc=maxschur(b,cut);pr,pc=projected(b,cut)
   assert base==mx==pr,(b,cut)
   rows.append({'b':str(b),'cutoff':str(cut),'states':sum(base.values()),'full':bc,'maxschur':mc,'projected':pc,'time_ms':{name:timing(fn,b,cut) for name,fn in (('full',full),('maxschur',maxschur),('projected',projected))}})
 print(json.dumps({'python':sys.version.split()[0],'platform':platform.platform(),'exact_multisets':'PASS','results':rows},indent=2))
if __name__=='__main__':main()
