from fractions import Fraction as Q
from itertools import product

def energy(v,G,b):
    a,c,d = G
    det=a*c-d*d
    A11,A12,A22=c/det,-d/det,a/det
    m1,m2,n1,n2=v
    x=Q(m1)+b*n2
    y=Q(m2)-b*n1
    return A11*x*x+2*A12*x*y+A22*y*y+a*n1*n1+2*d*n1*n2+c*n2*n2

def recover(values):
    x,y,z,w,h=values
    A11=x; A22=y; A12=(z-x-y)/2
    det=A11*A22-A12*A12
    assert det>0
    G=(A22/det,A11/det,-A12/det)
    b=(h-x-w)/(2*x)
    assert energy((0,0,0,1),G,b)==w
    return G,b

e1=(1,0,0,0);e2=(0,1,0,0);e4=(0,0,0,1)
probes=(e1,e2,(1,1,0,0),e4,(1,0,0,1))
cases=0
for a,c,d,b in product((Q(1),Q(2),Q(3,2)),(Q(1),Q(2)),(Q(0),Q(1,3),Q(-1,2)),(Q(-1),Q(0),Q(1,4),Q(2,3))):
    if a*c<=d*d: continue
    G=(a,c,d)
    vals=tuple(energy(v,G,b) for v in probes)
    assert recover(vals)==(G,b)
    cases+=1
print('P21 exact five-probe reconstruction cases:',cases)
