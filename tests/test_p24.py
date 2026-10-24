from fractions import Fraction as Q
from itertools import product

def E(v,g,b):
 a,c,d=g; det=a*c-d*d
 m1,m2,n1,n2=v
 x=Q(m1)+b*n2; y=Q(m2)-b*n1
 return (c*x*x-2*d*x*y+a*y*y)/det+a*n1*n1+2*d*n1*n2+c*n2*n2

def reconstruct(z):
 x,y,p,w,h=z
 u=(p-x-y)/2; delta=x*y-u*u
 if x<=0 or delta<=0:raise ValueError('invalid positive definite measurements')
 g=(y/delta,x/delta,-u/delta)
 b=(h-x-w)/(2*x)
 return g,b

P=((1,0,0,0),(0,1,0,0),(1,1,0,0),(0,0,0,1),(1,0,0,1))
cases=0
for a,c,d,b in product((Q(1),Q(2),Q(3,2)),(Q(1),Q(2)),(Q(0),Q(1,3),Q(-1,2)),(Q(-1),Q(0),Q(1,4),Q(2,3))):
 if a*c<=d*d:continue
 z=tuple(E(v,(a,c,d),b) for v in P)
 assert reconstruct(z)==((a,c,d),b)
 assert tuple(E(v,*reconstruct(z)) for v in P)==z
 cases+=1
print('exact five-probe reconstructions:',cases)
for k in (2,4,6):
 eps=Q(1,10**k)
 z=(Q(1),Q(1),Q(4)-2*eps,Q(1),Q(2))
 zp=(Q(1),Q(1),Q(4)-eps,Q(1),Q(2))
 g,b=reconstruct(z); gp,bp=reconstruct(zp)
 assert abs(zp[2]-z[2])==eps
 assert abs(gp[0]-g[0])>Q(1,5)/eps
 print('metric instability epsilon:',eps,'delta_G11:',abs(gp[0]-g[0]))
for k in (2,4,6):
 eps=Q(1,10**k)
 z=(eps,Q(1),eps+1,Q(1),eps+1)
 zp=(eps,Q(1),eps+1,Q(1),eps+1+eps)
 assert reconstruct(zp)[1]-reconstruct(z)[1]==Q(1,2)
 print('B instability witness epsilon:',eps,'delta_b:',Q(1,2))
