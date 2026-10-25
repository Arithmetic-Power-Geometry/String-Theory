from fractions import Fraction as F
from itertools import product
A,C,D=F(2),F(3),F(1,3);det=A*C-D*D
T=(F(133,53),-F(6,53),F(18,53));lo,hi=F(1,10),F(2,5)
def pol(v,sg):
 m1,m2,n1,n2=map(F,v);x=sg*n2;y=-sg*n1
 return (A*n1*n1+2*D*n1*n2+C*n2*n2+(C*m1*m1-2*D*m1*m2+A*m2*m2)/det,(2*C*m1*x-2*D*(m1*y+m2*x)+2*A*m2*y)/det,(C*x*x-2*D*x*y+A*y*y)/det)
def f(p,t):return p[0]+p[1]*t+p[2]*t*t
for sg in (1,-1):
 gap=None;witness=0;where=[]
 for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
  if not (v[0]*v[2]+v[1]*v[3]):continue
  p=tuple(x-y for x,y in zip(pol(v,sg),T))
  if p==(0,0,0):witness+=1;continue
  candidates=[(f(p,lo),lo),(f(p,hi),hi)]
  if p[2]>0:
   x=-p[1]/(2*p[2])
   if lo<x<hi:candidates.append((f(p,x),x))
  vmin,tmin=min(candidates)
  if gap is None or vmin<gap:gap=vmin;where=[(v,tmin)]
  elif vmin==gap:where.append((v,tmin))
 assert gap==F(6,265) and witness==2
 print('PASS',sg,'gap',gap,'witness',witness,'minimizers',where)
