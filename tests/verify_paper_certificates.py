"""Exact rational checks for the two finite certificates in the paper.

Run from the repository root:
    python tests/verify_paper_certificates.py

Python standard library only. All numerical comparisons use Fraction.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product

A,C,D,B = F(2), F(3), F(1,3), F(1,5)
W, CUTOFF, RADIUS = F(3373,1325), F(3), F(1,90)
CHARGES = tuple(product(range(-4,5), range(-4,5), range(-1,2), range(-1,2)))

def spin(v):
    m1,m2,n1,n2=v
    return m1*n1+m2*n2

def energy(v,b=B):
    m1,m2,n1,n2=map(F,v)
    x,y=m1+b*n2,m2-b*n1
    return (C*x*x-2*D*x*y+A*y*y)/(A*C-D*D)+A*n1*n1+2*D*n1*n2+C*n2*n2

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[1],-x[0])
def mul(x,y):
    p=[u*v for u in x for v in y]
    return min(p),max(p)
def sq(x):
    return (F(0) if x[0]<=0<=x[1] else min(x[0]**2,x[1]**2),max(x[0]**2,x[1]**2))
def div(x,y):
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))
def interval_energy(v,r=RADIUS):
    m1,m2,n1,n2=map(F,v)
    a,c,d,b=((z-r,z+r) for z in (A,C,D,B))
    x=add((m1,m1),mul(b,(n2,n2)))
    y=add((m2,m2),neg(mul(b,(n1,n1))))
    determinant=add(mul(a,c),neg(sq(d)))
    numerator=add(add(mul(c,sq(x)),neg(mul((F(2),F(2)),mul(d,mul(x,y))))),mul(a,sq(y)))
    winding=add(add(mul(a,(n1*n1,n1*n1)),mul((2*n1*n2,2*n1*n2),d)),mul(c,(n2*n2,n2*n2)))
    return add(div(numerator,determinant),winding)

def verify():
    assert len(CHARGES)==729
    # Completeness for E<=3: Gershgorin bounds 5/3 <= eig(G) <= 10/3
    # imply |n|^2 <= 9/5 < 2 and |m_i| <= sqrt(10)+1/5 < 4.
    plus=Counter((energy(v,B),spin(v)) for v in CHARGES if energy(v,B)<=CUTOFF)
    minus=Counter((energy(v,-B),spin(v)) for v in CHARGES if energy(v,-B)<=CUTOFF)
    assert sum(plus.values())==sum(minus.values())==39
    assert (plus[(W,1)],plus[(W,-1)])==(2,0)
    assert (minus[(W,1)],minus[(W,-1)])==(0,2)
    assert all(energy(v,B)==energy((-v[0],-v[1],v[2],v[3]),-B) for v in CHARGES)
    assert all(plus[(e,s)]==minus[(e,-s)] for e,s in plus)
    opposite=[v for v in CHARGES if spin(v)==-1]
    assert len(opposite)==68
    wlo,whi=interval_energy((1,0,1,0))
    clearances=[]
    for v in opposite:
        lo,hi=interval_energy(v)
        assert hi<wlo or lo>whi,(v,lo,hi,wlo,whi)
        clearances.append(wlo-hi if hi<wlo else lo-whi)
    minimum=min(clearances)
    assert minimum==F(564868,568757475),minimum

    # Independently validate the published row table and summary, if present.
    import csv
    import hashlib
    import json
    from pathlib import Path
    base = Path(__file__).resolve().parent
    csv_path = base / "interval_certificate_68.csv"
    summary_path = base / "certificate_summary.json"
    with csv_path.open(newline="", encoding="utf-8") as fh:
        saved = list(csv.DictReader(fh))
    assert len(saved) == len(opposite) == 68
    indexed = {(int(r["m1"]), int(r["m2"]), int(r["n1"]), int(r["n2"])): r for r in saved}
    assert len(indexed) == 68
    for v in opposite:
        row = indexed[v]
        lo, hi = interval_energy(v)
        side = "below" if hi < wlo else "above"
        clearance = wlo - hi if side == "below" else lo - whi
        assert row["spin"] == "-1"
        assert row["energy_lower"] == str(lo)
        assert row["energy_upper"] == str(hi)
        assert row["side"] == side
        assert row["clearance"] == str(clearance)
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert hashlib.sha256(csv_path.read_bytes()).hexdigest() == summary["csv_sha256"]
    assert summary["candidate_charges"] == len(CHARGES)
    assert summary["states_plus"] == sum(plus.values())
    assert summary["states_minus"] == sum(minus.values())
    assert summary["opposite_spin_rows"] == len(saved)
    assert summary["minimum_interval_clearance"] == str(minimum)
    print("Published CSV, JSON and SHA-256 cross-check: PASS")
    print("729-charge complete enumeration: PASS")
    print("States E<=3 per background: 39 / 39")
    print("Spin multiplicities at 3373/1325: +B=(2,0), -B=(0,2)")
    print("68 opposite-spin interval checks: PASS")
    print("Parameter radius: 1/90")
    print("Minimum rational interval clearance:",minimum)
    print("ALL CERTIFICATES PASS")

if __name__=="__main__":
    verify()
