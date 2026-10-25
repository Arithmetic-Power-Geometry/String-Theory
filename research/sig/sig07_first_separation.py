"""SIG-07: exact first spin-refined distinguishing energy for the rational pair."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
A,C,D,B=F(2),F(3),F(1,3),F(1,5)
def energy(v,b):
    m1,m2,n1,n2=map(F,v)
    x,y=m1+b*n2,m2-b*n1
    return (C*x*x-2*D*x*y+A*y*y)/(A*C-D*D)+A*n1*n1+2*D*n1*n2+C*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
def run():
    q=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
    plus=Counter((energy(v,B),spin(v)) for v in q if energy(v,B)<=3)
    minus=Counter((energy(v,-B),spin(v)) for v in q if energy(v,-B)<=3)
    assert sum(plus.values())==sum(minus.values())==39
    diff=sorted(k for k in plus.keys()|minus.keys() if plus[k]!=minus[k])
    first=F(3313,1325)
    assert diff and diff[0][0]==first
    assert all(plus[k]==minus[k] for k in plus.keys()|minus.keys() if k[0]<first)
    assert (plus[(first,1)],plus[(first,-1)])==(0,2)
    assert (minus[(first,1)],minus[(first,-1)])==(2,0)
    energies={k[0] for k in plus}|{k[0] for k in minus}
    assert all(sum(n for (e,s),n in plus.items() if e==t)==sum(n for (e,s),n in minus.items() if e==t) for t in energies)
    print("PASS: first energy-spin difference =",first)
    print("At threshold: B+ (+1,-1)=(0,2); B- (+1,-1)=(2,0)")
    print("All lower energies agree with multiplicity; 39 states each through cutoff 3")
if __name__=="__main__":run()
