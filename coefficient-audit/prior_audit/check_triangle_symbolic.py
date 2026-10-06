"""Exact rational verification of the displayed analytical triangle identities.
SymPy verifies the final finite coefficient identity, not operator domains.
"""
import sympy as s
from pathlib import Path
import json
a,b,c=s.symbols('a b c',positive=True)
r=[a,b,c]
G=s.Matrix([[a*a,(c*c-a*a-b*b)/2,(b*b-c*c-a*a)/2],[(c*c-a*a-b*b)/2,b*b,(a*a-b*b-c*c)/2],[(b*b-c*c-a*a)/2,(a*a-b*b-c*c)/2,c*c]])
basis=[s.eye(3)[:,i] for i in range(3)]
def dot(x,y):return (x.T*G*y)[0]
x=basis[1]-G[0,1]/a**2*basis[0]
y=basis[2]-G[1,2]/b**2*basis[1]
z=basis[0]-G[2,0]/c**2*basis[2]
cos=lambda i,j:G[i,j]/(r[i]*r[j])
T2=dot(x,x)*(7+cos(1,2)**2)+dot(y,y)*(7+cos(0,2)**2)+dot(z,z)*(7+cos(0,1)**2)
T2+=2*(dot(x,y)-dot(x,basis[2])*dot(y,basis[2])/c**2+dot(x,z)-dot(x,basis[1])*dot(z,basis[1])/b**2+dot(y,z)-dot(y,basis[0])*dot(z,basis[0])/a**2)
T2=s.factor(T2)
area16=2*(a*a*b*b+b*b*c*c+c*c*a*a)-(a**4+b**4+c**4)
R=area16/(a*a*b*b*c*c)
quartic=s.Rational(1,2)*sum((57-cos(i,j)**2)/(r[i]*r[j]) for i in range(3) for j in range(i+1,3))
orbital=0;spin=0;yuk=0
for i in range(3):
 j=(i+1)%3;k=(i+2)%3
 orbital+=(r[j]-r[k])**2*(7+cos(j,k)**2)/(2*r[i]**2*r[j]*r[k])
 spin+=8*(1+cos(j,k))/r[i]**2
 yuk+=32*(4-3*cos(j,k)-cos(i,j)*cos(i,k))/r[i]
W=s.factor(-R/2+quartic+orbital+spin)
cubic=4*T2/(a*b*c)
res=s.factor(2*(a+b+c)*W-yuk-cubic)
print('T norm squared =',T2)
print('W triangle =',W)
print('Yukawa norm squared =',s.factor(yuk))
print('Cubic norm squared =',s.factor(cubic))
print('Residual =',res)
assert res==0
K2=area16/4
p=a*b*c
perimeter=a+b+c
inv2=a**-2+b**-2+c**-2
assert s.factor(W-(32*perimeter/p-2*K2**2/(perimeter*p**3)))==0
assert s.factor(yuk-32/p*(2*perimeter**2-K2*inv2))==0
assert s.factor(cubic-4*K2/p*(8*inv2-K2/p**2))==0
d,M=s.symbols('d M')
assert s.expand(18*d*M+8*M+14*d*M+8*d*M-16*M-8*(d-1)*M-32*d*M)==0
out={'scope':'Exact rational symbolic reduction of displayed triangle contractions','T_norm_squared':str(T2),'W_triangle':str(W),'Yukawa_norm_squared':str(s.factor(yuk)),'Cubic_norm_squared':str(s.factor(cubic)),'residual':str(res)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
