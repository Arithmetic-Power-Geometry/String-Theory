from itertools import product

def theta(S):
    d={}
    for x in S:d[x*x]=d.get(x*x,0)+1
    return d

def incidence(S):
    return sum(a+b==c for a,b,c in product(S,repeat=3))

A=(0,1,2)
B=(0,1,-2)
assert theta(A)==theta(B)=={0:1,1:1,4:1}
assert incidence(A)==6
assert incidence(B)==5
print("P08 exact finite incidence separation passed")
