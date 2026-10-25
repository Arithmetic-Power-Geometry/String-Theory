"""SIG-03: exact direct inversion-orbit generator and benchmark (Python stdlib)."""
from fractions import Fraction as F
from collections import Counter
from itertools import product
from time import perf_counter
from statistics import median
import platform, sys, json
A,C,D,B=F(2),F(3),F(1,3),F(1,5)
Q=tuple(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))

def energy(v,b):
    m1,m2,n1,n2=map(F,v)
    x,y=m1+b*n2,m2-b*n1
    return (C*x*x-2*D*x*y+A*y*y)/(A*C-D*D)+A*n1*n1+2*D*n1*n2+C*n2*n2

def spin(v):
    return v[0]*v[2]+v[1]*v[3]

def representatives():
    yield (0,0,0,0),1
    bounds=(range(-4,5),range(-4,5),range(-1,2),range(-1,2))
    for i,rg in enumerate(bounds):
        for negative in (x for x in rg if x<0):
            for tail in product(*bounds[i+1:]):
                yield (0,)*i+(negative,)+tail,2

def full(b,mode):
    out=Counter()
    for v in Q:
        e=energy(v,b)
        if e<=3:out[e if mode=="energy" else (e,spin(v))]+=1
    return out

def scan(b,mode):
    out=Counter()
    for v in Q:
        if v>tuple(-x for x in v):continue
        e=energy(v,b)
        if e<=3:out[e if mode=="energy" else (e,spin(v))]+=1 if v==(0,0,0,0) else 2
    return out

def direct(b,mode):
    out=Counter()
    for v,weight in representatives():
        e=energy(v,b)
        if e<=3:out[e if mode=="energy" else (e,spin(v))]+=weight
    return out

def run():
    reps=list(representatives())
    assert len(reps)==365 and sum(w for v,w in reps)==729
    assert len({v for v,w in reps})==365
    assert {v for v,w in reps}|{tuple(-x for x in v) for v,w in reps}==set(Q)
    results=[]
    for b in (B,-B):
        for mode in ("energy","spin"):
            baseline=full(b,mode)
            assert baseline==scan(b,mode)==direct(b,mode)
            assert sum(baseline.values())==39
            timing={}
            for name,fn in (("full",full),("scan",scan),("direct",direct)):
                trials=[]
                for _ in range(7):
                    start=perf_counter()
                    for _ in range(20):fn(b,mode)
                    trials.append((perf_counter()-start)/20)
                timing[name]=round(median(trials)*1000,4)
            results.append({"b":str(b),"mode":mode,"states":39,"times_ms":timing,
                            "direct_speedup":round(timing["full"]/timing["direct"],3)})
    print(json.dumps({"python":sys.version.split()[0],"platform":platform.platform(),
          "charge_box":729,"direct_representatives":365,
          "partition_check":"PASS","exact_multisets":"PASS","results":results},indent=2))

if __name__=="__main__":
    run()
