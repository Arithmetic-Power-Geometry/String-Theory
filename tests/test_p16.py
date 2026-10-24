from fractions import Fraction as F
radii=[F(1,5),F(1,3),F(1,2),F(2,3),F(1),F(3,2),F(2),F(3),F(5)]
for r in radii:
 u=r*r+1/(r*r)
 assert u>=2
 assert u==(1/r)**2+1/((1/r)**2)
 assert (r*r-1/(r*r))**2==u*u-4
 if r!=1:
  assert 4*(r*r-1/(r*r))**2==4*(u*u-4)
print('P16 exact quotient-coordinate checks:',len(radii))
