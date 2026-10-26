from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib,json
G=(F(2),F(1,3),F(3)); a,d,c=G; det=a*c-d*d
T=(F(133,53),F(-6,53),F(18,53))
def pol(v,sg):
 m1,m2,n1,n2=map(F,v);u=sg*n2;w=-sg*n1
 return (a*n1*n1+2*d*n1*n2+c*n2*n2+(c*m1*m1-2*d*m1*m2+a*m2*m2)/det,(2*c*m1*u-2*d*(m1*w+m2*u)+2*a*m2*w)/det,(c*u*u-2*d*u*w+a*w*w)/det)
def ev(p,x):return p[0]+p[1]*x+p[2]*x*x
def minimum(p,L,R):
 vals=[(ev(p,L),L),(ev(p,R),R)]
 if p[2]>0:
  x=-p[1]/(2*p[2])
  if L<x<R:vals.append((ev(p,x),x))
 return min(vals)
res={}; records=[]
for sg in (1,-1):
 counts=Counter(); exc=[];gap=None; minimizers=[]
 for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
  s=v[0]*v[2]+v[1]*v[3]
  if not s:continue
  delta=tuple(x-y for x,y in zip(pol(v,sg),T))
  mn,where=minimum(delta,F(0),F(1,2))
  assert mn>=0,(sg,v,delta)
  if delta==(0,0,0):typ='identical'
  elif ev(delta,F(0))==0:typ='zero'
  elif ev(delta,F(1,2))==0:typ='half'
  else:typ='strict';assert mn>0
  counts[typ]+=1
  if typ!='strict':exc.append((v,s,typ))
  if typ!='identical':
   g,x=minimum(delta,F(1,10),F(2,5))
   if gap is None or g<gap:gap=g;minimizers=[(v,x)]
   elif g==gap:minimizers.append((v,x))
  records.append([sg,list(v),s,[str(z) for z in delta],typ])
 assert counts==Counter({'strict':570,'zero':2,'half':2,'identical':2}),counts
 assert gap==F(6,265),gap
 res[str(sg)]={'counts':dict(counts),'exceptions':[(list(v),s,t) for v,s,t in exc],'gap':str(gap),'minimizers':[(list(v),str(x)) for v,x in minimizers]}
canonical=json.dumps(records,separators=(',',':'),sort_keys=True).encode()
res['sha256']=hashlib.sha256(canonical).hexdigest();res['record_count']=len(records)
open('certificate_results.json','w').write(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
