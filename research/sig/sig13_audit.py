from fractions import Fraction as F
from itertools import product
from collections import Counter
import json
A,C,D=F(2),F(3),F(1,3);DET=A*C-D*D
T=(F(133,53),-F(6,53),F(18,53))
def polynomial(v,sgn):
 m1,m2,n1,n2=map(F,v);p,q=sgn*n2,-sgn*n1
 w=A*n1*n1+2*D*n1*n2+C*n2*n2
 return (w+(C*m1*m1-2*D*m1*m2+A*m2*m2)/DET,
 (2*C*m1*p-2*D*(m1*q+m2*p)+2*A*m2*q)/DET,
 (C*p*p-2*D*p*q+A*q*q)/DET)
def val(p,b):return p[0]+p[1]*b+p[2]*b*b
def main():
 results=[]
 for sign in (1,-1):
  counts=Counter();exceptions={'identical':[],'zero':[],'half':[]}
  for v in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
   s=v[0]*v[2]+v[1]*v[3]
   if s==0:continue
   delta=tuple(a-b for a,b in zip(polynomial(v,sign),T))
   values=[val(delta,F(0)),val(delta,F(1,2))]
   if delta[2]>0:
    vertex=-delta[1]/(2*delta[2])
    if 0<vertex<F(1,2):values.append(val(delta,vertex))
   assert min(values)>=0,(sign,v,delta)
   if delta==(0,0,0):kind='identical'
   elif val(delta,F(0))==0:kind='zero'
   elif val(delta,F(1,2))==0:kind='half'
   else:kind='strict'
   if kind=='strict':assert min(values)>0
   counts[kind]+=1
   if kind!='strict':exceptions[kind].append({'charge':v,'spin':s})
  assert counts==Counter({'strict':570,'identical':2,'zero':2,'half':2}),counts
  results.append({'B_sign':sign,'counts':dict(counts),'exceptions':exceptions})
 print(json.dumps({'status':'PASS','test':'exact polynomial endpoint and vertex certificate','results':results},indent=2))
if __name__=='__main__':main()
