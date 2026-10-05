"""Bounded symbolic verification of algebra in quadrupole_rank_gate.md.
This does not verify BFSS ground-state existence, domains, or large-N estimates.
"""
import json
import sympy as s
N,g2,D,k,R,ell,p=s.symbols('N g2 D k R ell p', positive=True)
a=k*k/(1296*N**3)+9*g2*D*D/(8*k)
kstar=9*g2**s.Rational(1,3)*N*D**s.Rational(2,3)
assert s.simplify(s.diff(a,k).subs(k,kstar))==0
amin=s.Rational(3,16)*g2**s.Rational(2,3)*D**s.Rational(4,3)/N
assert s.simplify(a.subs(k,kstar)-amin)==0
# SO(d) covariance <Mij Mkl>=a0 deltaij deltakl + b0(deltaik delt ajl + deltail deltajk)
d,a0,b0=s.symbols('d a0 b0', positive=True)
trM2=d*a0+(d*d+d)*b0
trM_sq=d*d*a0+2*d*b0
spin2=s.factor(trM2-trM_sq/d)
dim=(d-1)*(d+2)/2
assert s.simplify(spin2/dim-2*b0)==0
assert s.simplify(((1-1/d)/dim).subs(d,9)-s.Rational(2,99))==0
# Physical quadrupole squared prefactor, with q=Tr(hZZ)/N.
pref=ell**4*N**s.Rational(10,3)/R**2
assert s.simplify(pref.subs(R,N/p)-ell**4*p*p*N**s.Rational(4,3))==0
# Dimensionless first moment from physical first moment / (quadrupole scale)^2 / energy unit.
qscale=ell**2*N**s.Rational(5,3)/R
Escale=R*N**s.Rational(1,3)/ell**2
x2=s.symbols('x2',positive=True) # <tr Z_1^2>
physical_first=2*ell**2*N**s.Rational(5,3)*x2/R
assert s.simplify(physical_first/qscale**2/Escale-2*x2/N**2)==0
print(json.dumps({'finite_N_Schur_minimum':'passed','spin2_covariance_dimension':'44','SO9_radial_upper_constant':'2/99','physical_decompactification_prefactor':'ell^4 (p+)^2 N^(4/3)','dimensionless_first_moment':'2 <tr Z_1^2>/N^2','scope':'algebra only, not a BFSS bound-state or uniformity proof'},indent=2))
# Follow-up: physical inverse-energy source weight from the energy-form norm.
a,delta,eps=s.symbols('a delta eps',positive=True)
c=ell**2*N**s.Rational(5,3)/R
Lambda=R*N**s.Rational(1,3)/ell**2
m1hat=2*a/N**2
assert s.simplify(c*c*Lambda*m1hat-2*ell**2*N**s.Rational(5,3)*a/R)==0
assert s.simplify(c*c*Lambda**3-R*N**s.Rational(13,3)/ell**2)==0
ward_bound=(delta**2/4)*c*c*Lambda*m1hat
assert s.simplify(ward_bound.subs(R,N/p)-delta**2*ell**2*p*N**s.Rational(2,3)*a/2)==0
assert s.simplify((delta/Lambda).subs(R,N/p)-delta*ell**2*p*N**s.Rational(-4,3))==0
assert s.simplify((c*c*Lambda).subs(R,N/p)-ell**2*p*N**s.Rational(8,3))==0
assert s.simplify(ward_bound.subs(R,N/p).subs(delta,eps*N**s.Rational(-1,3))-eps**2*ell**2*p*a/2)==0
print('Energy-form follow-up: all six physical/dimensionless scaling checks passed')
