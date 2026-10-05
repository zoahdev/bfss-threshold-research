"""Exact tests of SO(9) tail power counting and free-channel current algebra.
These checks do not establish existence/uniformity of BFSS bound-state estimates.
"""
import json
import sympy as s
x=s.symbols('x0:9',real=True)
r2=sum(t*t for t in x)
psi=x[0]*x[1]*r2**(-s.Rational(11,2))
g=(x[0]**2-x[1]**2)/s.sqrt(2)
def lap(f):
    return s.factor(sum(s.diff(f,t,2) for t in x))
assert lap(psi)==0
lhs=lap(lap(g*psi))
rhs=8*(s.diff(psi,x[0],2)-s.diff(psi,x[1],2))/s.sqrt(2)
assert s.simplify(lhs-rhs)==0
# h=diag(1,-1,0,...)/sqrt(2), trace h^2=1.
# <n_i^4>=3/[d(d+2)], <n_i^2 n_j^2>=1/[d(d+2)] (i!=j).
d=s.Integer(9)
angular=(2*s.Rational(3,d*(d+2))-2*s.Rational(1,d*(d+2)))/2
assert angular==s.Rational(2,99)
L=s.symbols('L',positive=True)
r=s.symbols('r',positive=True)
assert s.integrate(r**(-6),(r,L,s.oo))*angular==s.Rational(2,495)/L**5
assert s.integrate(r**(-10),(r,L,s.oo))==1/(9*L**9)
print(json.dumps({'harmonic_9d_tail':'passed','double_laplacian_identity':'passed','unit_polarization_angular_average':'2/99','quadrupole_tail_coefficient':'2/(495 L^5), times mu^2 |C|^2','probability_tail_coefficient':'1/(9 L^9), times |C|^2'},indent=2))
