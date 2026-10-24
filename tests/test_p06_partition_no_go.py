from fractions import Fraction as Q
from itertools import product

def z(energies, x, k=1):
    return sum((x ** (k*e) for e in energies), Q(0))

def defect(energies, x, q):
    weights=[x**e/z(energies,x) for e in energies]
    direct=1-sum((w**q for w in weights),Q(0))
    indirect=1-z(energies,x,q)/z(energies,x)**q
    assert direct==indirect
    return direct

n=0
for length in range(1,5):
    for energies in product(range(4),repeat=length):
        for x in [Q(1,2),Q(2,3),Q(3,4)]:
            for q in [2,3,4]:
                d=defect(energies,x,q)
                assert Q(0)<=d<=1-Q(1,length**(q-1))
                n+=1
print("P06 exact tests passed:",n)
