import sympy as S
r=S.symbols('r', positive=True)
psi_tail=r**-9*S.log(r)
V_tail=S.simplify(S.diff(psi_tail,r,2)/psi_tail+8/r*S.diff(psi_tail,r)/psi_tail-18/r**2)
assert S.simplify(V_tail+11/(r*r*S.log(r)))==0
assert 2*(2+7)==18
assert S.Rational(7,72)*18==S.Rational(7,4)
assert S.Rational(49,4)+18==S.Rational(121,4)
a=S.symbols('a')
phi=r**2*(1+a*r**2)
V_origin=S.limit((S.diff(phi,r,2)+8/r*S.diff(phi,r)-18/r**2*phi)/phi,r,0)
assert V_origin==26*a
print({'tail_potential':str(V_tail),'casimir_44':18,'support_coefficient':'7/4','singlet_hardy':'121/4','origin_potential_coefficient':str(V_origin)})
