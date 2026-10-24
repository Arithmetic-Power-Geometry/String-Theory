from fractions import Fraction as Q
from itertools import product
from collections import Counter
from hashlib import sha256
from pathlib import Path

A,C,D,B=Q(2),Q(3),Q(1,3),Q(1,5)
LIMIT=Q(3)
W=Q(3373,1325)

def energy(v,b):
    m1,m2,n1,n2=map(Q,v)
    det=A*C-D*D
    x=m1+b*n2
    y=m2-b*n1
    return (C*x*x-2*D*x*y+A*y*y)/det+A*n1*n1+2*D*n1*n2+C*n2*n2

def spin(v):
    return v[0]*v[2]+v[1]*v[3]

# Gershgorin: lambda_min(G)>=5/3, lambda_max(G)<=10/3.
# E<=3 => |n|^2<=9/5 <2; and |m|<=sqrt(10)+1/5<4.
# Hence the following 729 charge vectors include ALL states with E<=3.
charges=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
assert len(charges)==729
plus=Counter();minus=Counter();plus_witness=[];minus_witness=[]
for v in charges:
    for sign, counter, witnesses in ((1,plus,plus_witness),(-1,minus,minus_witness)):
        e=energy(v,sign*B)
        if e<=LIMIT:
            s=spin(v)
            counter[(e,s)]+=1
            if e==W and abs(s)==1:
                witnesses.append((v,s))
    m1,m2,n1,n2=v
    mirror=(-m1,-m2,n1,n2)
    assert energy(v,B)==energy(mirror,-B)
    assert spin(v)==-spin(mirror)
assert sum(plus.values())==sum(minus.values())==39
assert plus[(W,1)]==2 and plus[(W,-1)]==0
assert minus[(W,1)]==0 and minus[(W,-1)]==2
assert all(plus[(e,s)]==minus[(e,-s)] for e,s in plus)
assert Counter({e:sum(v for (z,s),v in plus.items() if z==e) for e,s in plus}) == Counter({e:sum(v for (z,s),v in minus.items() if z==e) for e,s in minus})
assert sorted(plus_witness)==[((-1,0,-1,0),1),((1,0,1,0),1)]
assert sorted(minus_witness)==[((-1,0,1,0),-1),((1,0,-1,0),-1)]
print('P38 certified charge box:',len(charges))
print('P38 states per background through cutoff 3:',sum(plus.values()))
print('P38 witness energy:',W)
print('P38 +B spin multiplicities:',plus[(W,1)],plus[(W,-1)])
print('P38 -B spin multiplicities:',minus[(W,1)],minus[(W,-1)])
print('P38 energy-only spectra equal below cutoff: YES')
print('P38 exact full-energy isospectrality: analytic bijection')
print('P38 no O(2,2;Z) duality: spin-spectrum invariant obstruction')
print('P38 source SHA256:',sha256(Path(__file__).read_bytes()).hexdigest())
