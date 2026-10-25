"""SIG-02 exact inversion-orbit comparison. Standard library only."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from statistics import median
from time import perf_counter

A,C,D,B=F(2),F(3),F(1,3),F(1,5)
Q=tuple(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))

def energy(v,b):
    m1,m2,n1,n2=map(F,v)
    x,y=m1+b*n2,m2-b*n1
    return (C*x*x-2*D*x*y+A*y*y)/(A*C-D*D)+A*n1*n1+2*D*n1*n2+C*n2*n2

def spin(v):
    return v[0]*v[2]+v[1]*v[3]

def enumerate_full(b,mode):
    out=Counter()
    for v in Q:
        e=energy(v,b)
        if e<=3:
            out[e if mode=="energy" else (e,spin(v))]+=1
    return out

def enumerate_orbits(b,mode):
    out=Counter()
    for v in Q:
        if v>tuple(-x for x in v):
            continue
        e=energy(v,b)
        if e<=3:
            out[e if mode=="energy" else (e,spin(v))]+=1 if v==(0,0,0,0) else 2
    return out

def run():
    assert len(Q)==729
    reps=[v for v in Q if v<=tuple(-x for x in v)]
    assert len(reps)==365
    for b in (B,-B):
        for mode in ("energy","spin"):
            original=enumerate_full(b,mode)
            reduced=enumerate_orbits(b,mode)
            assert original==reduced
            assert sum(original.values())==39
            timing={}
            for name,fn in (("full",enumerate_full),("orbit",enumerate_orbits)):
                trials=[]
                for _ in range(7):
                    start=perf_counter()
                    for _ in range(20):
                        fn(b,mode)
                    trials.append((perf_counter()-start)/20)
                timing[name]=median(trials)
            print("B=",b,"mode=",mode,"exact=PASS","full_ms=",round(timing["full"]*1000,3),"orbit_ms=",round(timing["orbit"]*1000,3),"speedup=",round(timing["full"]/timing["orbit"],3))
    print("PASS: 729 full candidates, 365 orbit representatives, 39 states per background")

if __name__=="__main__":
    run()
