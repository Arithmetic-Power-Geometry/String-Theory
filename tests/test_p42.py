from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib
from pathlib import Path
A,C,D,B=F(2),F(3),F(1,3),F(1,5)
W=F(3373,1325)
def energy(v):
 m1,m2,n1,n2=map(F,v)
 x=m1+B*n2;y=m2-B*n1
 return (C*x*x-2*D*x*y+A*y*y)/(A*C-D*D)+A*n1*n1+2*D*n1*n2+C*n2*n2
def spin(v):return v[0]*v[2]+v[1]*v[3]
charges=list(product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)))
witness=(1,0,1,0)
assert energy(witness)==W and spin(witness)==1
opposite=[v for v in charges if spin(v)==-1]
assert len(opposite)==68
assert all(energy(v)!=W for v in opposite)
assert min(abs(energy(v)-W) for v in opposite)==F(12,265)
# Completeness: eigenvalue bounds 5/3 <= lambda(G) <= 10/3;
# E <= 3 => ||n||² <= 9/5 <2 and ||m||_infty < sqrt(10)+1/5 <4.
# For genericity, for each opposite-spin charge w, rational analytic
# f_w = E_witness - E_w is nonzero at the base point, hence nonzero
# analytic on the connected positive-definite parameter domain.
# Its zero set is closed nowhere dense and measure zero. Locally only
# finitely many w can collide with the witness because quadratic energies
# are uniformly coercive on compact parameter sets. Thus the union of
# collision sets is locally finite and CLOSED (not just F_sigma), and
# its complement is OPEN DENSE of full measure.
print('P42 base witness:', W)
print('P42 opposite-spin charges in certified cutoff:', len(opposite))
print('P42 nearest opposite-spin separation:', F(12,265))
print('P42 local finiteness argument: uniform positive-definite quadratic bound')
print('P42 strengthened theorem: OPEN DENSE and FULL MEASURE')
print('P42 source SHA256:',hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
