import sympy as s
from itertools import combinations
A,C,D,B=s.symbols('a c d b',real=True)
M=s.Matrix([[A,D],[D,C]]); J=s.Matrix([[0,1],[-1,0]])
def en(v):
 m=s.Matrix(v[:2]);n=s.Matrix(v[2:]);x=m+B*J*n
 return (x.T*M.inv()*x+n.T*M*n)[0]
vec=[(1,0,0,0),(0,1,0,0),(1,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,0,1),(0,1,1,0),(1,0,1,0),(0,1,0,1),(1,1,1,1)]
pt={A:s.Rational(2),C:s.Rational(3),D:s.Rational(1,3),B:s.Rational(1,4)}
for comb in combinations(vec,4):
 jac=s.Matrix([en(v) for v in comb]).jacobian([A,C,D,B]);det=s.factor(jac.det())
 if det!=0 and det.subs(pt)!=0:
  print('FOUR_PROBES',comb)
  print('JACOBIAN_DET',det)
  print('AT_POINT',det.subs(pt));break
else:raise RuntimeError('no witness')
