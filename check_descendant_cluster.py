"""Symbolic checks only; no BFSS numerical state or spectral assumption."""
import json
import sympy as s
x,y,z=s.symbols('x y z',real=True)
a,b,d,e,f=s.symbols('a b d e f',real=True)
k=s.Matrix([x,y,z]); r2=(k.T*k)[0]
h=s.Matrix([[a,d,e],[d,b,f],[e,f,-a-b]])
R=s.eye(3)-2*k*k.T/r2
T=s.zeros(3)
for i in range(3):
    for j in range(3):
        T[i,j]=sum(h[p,q]*s.diff(k[i]*k[j]/r2,k[p],k[q]) for p in range(3) for q in range(3))
reflection=all(s.simplify((r2*T-2*R*h*R)[i,j])==0 for i in range(3) for j in range(3))
orthogonal=s.simplify(R*R)==s.eye(3)
E,D,mu,K=s.symbols('E D mu K',positive=True)
A2=s.symbols('abs_A_squared',positive=True)
rho=K*mu**s.Rational(9,2)*A2*E**s.Rational(3,2)
F=s.integrate(E*rho,(E,0,D)); W=s.integrate(E**3*rho/4,(E,0,D))
S8=2*s.pi**s.Rational(9,2)/s.gamma(s.Rational(9,2))
Kvalue=s.simplify(2**s.Rational(3,2)*4*S8/(2*s.pi)**9)
N,delta,ell,p,C=s.symbols('N delta ell p C',positive=True)
epsilon=delta*ell**2*p*N**(-s.Rational(4,3))
Fphysical=s.simplify(ell**2*p*N**s.Rational(8,3)*4*s.E/N**2*C*s.sqrt(epsilon))
res={
  'reflection_hessian_identity_symbolic_3d_slice':reflection,
  'reflection_orthogonal':orthogonal,
  'S8':str(s.simplify(S8)),
  'K_9d_shell':str(Kvalue),
  'Fv_leading':str(F.subs(K,Kvalue)),
  'W_leading':str(W.subs(K,Kvalue)),
  'W_over_Fv_leading':str(s.simplify(W/F)),
  'physical_bound_if_G_le_C_t_minus_half':str(Fphysical),
  'physical_W_bound_if_G_le_C_t_minus_half':str(s.simplify(delta**2*Fphysical/4)),
  'status':'Conditional identities and free leading channel only; no exact BFSS rank-uniform spectral estimate proved.'
}
assert reflection and orthogonal
assert s.simplify(W/F-7*D**2/44)==0
assert s.simplify(Fphysical-4*s.E*C*(ell**2*p)**s.Rational(3,2)*s.sqrt(delta))==0
print(json.dumps(res,indent=2))
