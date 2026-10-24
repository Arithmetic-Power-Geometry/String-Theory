from fractions import Fraction as Q
from itertools import product

def energy(g,b,m,n):
    # diagonal G, antisymmetric B_12=b
    v=(Q(m[0])+b*n[1],Q(m[1])-b*n[0])
    return v[0]*v[0]/g[0]+v[1]*v[1]/g[1]+g[0]*n[0]*n[0]+g[1]*n[1]*n[1]

def shift_test(g,b,k,N):
    # B'=B+K, m'=m-Kn; K_12=k
    for a,c,d,e in product(range(-N,N+1),repeat=4):
        m=(a,c);n=(d,e)
        mp=(a-k*e,c+k*d)
        assert energy(g,b,m,n)==energy(g,b+k,mp,n)
    return (2*N+1)**4

checks=0
for g in ((Q(1),Q(1)),(Q(2),Q(3)),(Q(1,2),Q(5,3))):
 for b in (Q(0),Q(1,3),Q(-2,5)):
  for k in (-2,-1,1,2):
   checks+=shift_test(g,b,k,2)
print('P17 exact charge-pair covariance cases:',checks)
