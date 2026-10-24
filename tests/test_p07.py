from fractions import Fraction as F
from itertools import product

def energy(m,n): return sum(x*x+y*y for x,y in zip(m,n))
def pairing(m,n): return sum(x*y for x,y in zip(m,n))
def refined(charges):
    out={}
    for m,n in charges:
        key=(energy(m,n),pairing(m,n))
        out[key]=out.get(key,0)+1
    return out

A=[((1,1),(0,0))]
B=[((1,0),(1,0))]
assert [energy(*z) for z in A]==[energy(*z) for z in B]==[2]
assert refined(A)!=(refined(B))
count=0
K=((0,1),(-1,0)); BB=((F(0),F(1,2)),(-F(1,2),F(0)))
G=(F(2),F(3))
def en(m,n,b):
    v=[F(m[i])+sum(b[i][j]*n[j] for j in range(2)) for i in range(2)]
    return sum(v[i]*v[i]/G[i]+G[i]*n[i]*n[i] for i in range(2))
for v in product(range(-2,3),repeat=4):
    m,n=v[:2],v[2:]
    mp=tuple(m[i]-sum(K[i][j]*n[j] for j in range(2)) for i in range(2))
    bp=tuple(tuple(BB[i][j]+K[i][j] for j in range(2)) for i in range(2))
    assert pairing(m,n)==pairing(mp,n)
    assert en(m,n,BB)==en(mp,n,bp)
    count+=1
print('P07 exact checks passed:',count)
print('Unrefined singleton energy:',2,'refined A:',refined(A),'refined B:',refined(B))
