from fractions import Fraction as Q

def weights(radii, repaired=False):
    values = [(r*r + 1/(r*r)) if repaired else r*r for r in radii]
    total = sum(values)
    return tuple(x/total for x in values)

def defect4(weights):
    return 1 - sum(x*x for x in weights)

a = (Q(2), Q(3))
b = (Q(1, 2), Q(3))
assert weights(a) == (Q(4,13), Q(9,13))
assert weights(b) == (Q(1,37), Q(36,37))
assert defect4(weights(a)) == Q(72,169)
assert defect4(weights(b)) == Q(72,1369)
assert defect4(weights(a)) != defect4(weights(b))
assert weights(a, True) == weights(b, True) == (Q(153,481), Q(328,481))
assert defect4(weights(a, True)) == Q(100368,231361)
for x in (Q(1,3), Q(2), Q(3,2), Q(5)):
    for y in (Q(1,4), Q(3), Q(7,2)):
        r = (x,y)
        assert weights(r,True) == weights((1/x,y),True)
        assert weights(r,True) == weights((x,1/y),True)
        assert defect4(weights(r,True)) == defect4(weights((y,x),True))
print("P04 exact duality tests passed")
