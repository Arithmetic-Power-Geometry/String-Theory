from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib,json

def poly(z,sgn):
 a,c,u,v=z
 x=(F(a),F(sgn*v));y=(F(c),F(-sgn*u))
 def mult(p,q,k):
  return sum((p[i]*q[k-i] for i in range(2) if 0<=k-i<2),F(0))
 p=[(27*mult(x,x,k)-6*mult(x,y,k)+18*mult(y,y,k))/53 for k in range(3)]
 p[0]+=2*u*u+F(2,3)*u*v+3*v*v
 return tuple(p)
def at(q,b):return q[0]+q[1]*b+q[2]*b*b
def low(q,L,R):
 xs=[L,R]
 if q[2]>0:
  x=-q[1]/(2*q[2])
  if L<x<R:xs.append(x)
 return min((at(q,x),x) for x in xs)
def main():
 T=(F(133,53),F(-6,53),F(18,53));result={}
 for sign in (-1,1):
  cnt=Counter();w=[];zero=[];half=[];gap=None;gaparg=None
  for z in product(range(-4,5),range(-4,5),range(-1,2),range(-1,2)):
   if z[0]*z[2]+z[1]*z[3]==0:continue
   p=poly(z,sign);q=tuple(p[i]-T[i] for i in range(3))
   assert low(q,F(0),F(1,2))[0]>=0,(sign,z,q)
   if q==(0,0,0):cnt['identical']+=1;w.append(z)
   elif at(q,F(0))==0:cnt['zero']+=1;zero.append(z)
   elif at(q,F(1,2))==0:cnt['half']+=1;half.append(z)
   else:cnt['strict']+=1
   if q!=(0,0,0):
    g,x=low(q,F(1,10),F(2,5))
    if gap is None or g<gap:gap=g;gaparg=(z,str(x))
  assert cnt==Counter({'identical':2,'zero':2,'half':2,'strict':570}),cnt
  assert gap==F(6,265)
  result[str(sign)]={'classes':dict(cnt),'witnesses':w,'zero_endpoint':zero,'half_endpoint':half,'interior_gap':str(gap),'gap_arg':gaparg}
 blob=json.dumps(result,sort_keys=True,separators=(',',':'))
 print(json.dumps({'status':'PASS','records':1152,'results':result,'sha256':hashlib.sha256(blob.encode()).hexdigest()},indent=2))
if __name__=='__main__':main()
