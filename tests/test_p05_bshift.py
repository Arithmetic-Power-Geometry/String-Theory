from fractions import Fraction as F
from itertools import product

def energy(G,B,m,n):
    v=[m[i]+sum(B[i][j]*n[j] for j in range(2)) for i in range(2)]
    a,b,c=G[0][0],G[0][1],G[1][1]
    det=a*c-b*b
    inv=[[c/det,-b/det],[-b/det,a/det]]
    return sum(v[i]*inv[i][j]*v[j] for i in range(2) for j in range(2))+sum(n[i]*G[i][j]*n[j] for i in range(2) for j in range(2))

G=[[F(2),F(0)],[F(0),F(3)]]
B=[[F(0),F(1,2)],[-F(1,2),F(0)]]
K=[[0,1],[-1,0]]
B2=[[B[i][j]+K[i][j] for j in range(2)] for i in range(2)]
count=0
for z in product(range(-2,3),repeat=4):
    m=z[:2]; n=z[2:]
    mp=[m[i]-sum(K[i][j]*n[j] for j in range(2)) for i in range(2)]
    assert energy(G,B,m,n)==energy(G,B2,mp,n)
    count+=1
print("exact B-shift charge-covariance tests passed:",count)
