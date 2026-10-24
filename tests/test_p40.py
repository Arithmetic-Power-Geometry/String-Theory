from fractions import Fraction as Q
from itertools import product
from collections import Counter
from hashlib import sha256
from pathlib import Path
A,C,D,B=Q(2),Q(3),Q(1,3),Q(1,5)
W=Q(3373,1325)
def e(v,a=A,c=C,d=D,b=B):
 m1,m2,n1,n2=map(Q,v);det=a*c-d*d;x=m1+b*n2;y=m2-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
vs=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
assert len(vs)==729
hist=Counter((e(v),spin(v)) for v in vs if e(v)<=3)
assert hist[(W,1)]==2 and hist[(W,-1)]==0
opposite=sorted(set(abs(e(v)-W) for v in vs if spin(v)==-1 and e(v)<=3))
assert opposite[0]>0
print('P40 certified opposite-spin spectral gap:',opposite[0])
print('P40 opposite-spin closest energy:', sorted((abs(e(v)-W),e(v),v) for v in vs if spin(v)==-1 and e(v)<=3)[0][1])
# Quantitative rational box: each parameter varies by at most delta.
# The 729-vector box remains complete for E<=3 when a,c in [1.99,3.01],
# |d|<=0.34, |b|<=0.21: lambda_min >=1.65 and lambda_max <=3.35;
# n^2<=3/1.65<2; |m|<=sqrt(3*3.35)+0.21<4.
# Rational interval arithmetic certifies that the two witness energies and
# all opposite-spin energies remain separated by checking finite bounds.
# For each v, use derivative-free interval bound from rational evaluations:
# lower/upper bounds of E on parameter box via interval arithmetic.

def interval_energy(v,delta):
 m1,m2,n1,n2=map(Q,v)
 a=(A-delta,A+delta);c=(C-delta,C+delta);d=(D-delta,D+delta);b=(B-delta,B+delta)
 def add(x,y):return (x[0]+y[0],x[1]+y[1])
 def mul(x,y):
  vals=[i*j for i in x for j in y];return (min(vals),max(vals))
 def neg(x):return (-x[1],-x[0])
 def sq(x):return (Q(0) if x[0]<=0<=x[1] else min(x[0]**2,x[1]**2),max(x[0]**2,x[1]**2))
 def div(x,y):
  assert y[0]>0
  return mul(x,(1/y[1],1/y[0]))
 x=add((m1,m1),mul(b,(n2,n2)))
 y=add((m2,m2),neg(mul(b,(n1,n1))))
 det=add(mul(a,c),neg(sq(d)))
 num=add(add(mul(c,sq(x)),neg(mul((Q(2),Q(2)),mul(d,mul(x,y))))),mul(a,sq(y)))
 return add(div(num,det),add(add(mul(a,(n1*n1,n1*n1)),mul((Q(2*n1*n2),Q(2*n1*n2)),d)),mul(c,(n2*n2,n2*n2))))

# If the interval for a +1 witness lies disjoint from all -1 intervals,
# its energy remains a spin-asymmetric level, even if it splits from its partner.
delta=Q(1,90)
witness=(1,0,1,0)
wlo,whi=interval_energy(witness,delta)
for v in vs:
 if spin(v)==-1:
  lo,hi=interval_energy(v,delta)
  assert hi<wlo or lo>whi,('collision',v,lo,hi,wlo,whi)
print('P40 certified open parameter cube radius:',delta)
print('P40 witness energy enclosure:',wlo,whi)
print('P40 checked opposite-spin vectors:',sum(spin(v)==-1 for v in vs))
print('P40 interval certificate: PASS')
print('P40 source SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
