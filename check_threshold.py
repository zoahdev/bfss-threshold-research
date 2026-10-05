"""Self-authored diagnostic. This is NOT a BFSS Hamiltonian computation.
Verifies a free-channel nonuniformity example and resolvent/current identities.
Run: python check_threshold.py
"""
import json
import mpmath as mp
import sympy as sp
mp.mp.dps=60
E,z,a,b,c=sp.symbols('E z a b c', positive=True)
# Exact Taylor-remainder identity through degree three.
assert sp.simplify(1/(E+z)-sum((-z)**j/E**(j+1) for j in range(4))-z**4/(E**4*(E+z))) == 0
# Factorization for a source quadratic in energy and soft parameter.
u=E**2*a+z*E*b+z**2*c
v=E*a+z*(b-a)
w=c-b+a
assert sp.expand(u-(E+z)*v-z**2*w)==0
assert sp.simplify(u**2/(E+z) - ((E+z)*v**2+2*z**2*v*w+z**4*w**2/(E+z)))==0
# Exact low energy coefficients in the 9D free relative-channel example.
assert sp.simplify(sp.gamma(sp.Rational(7,2))*sp.gamma(sp.Rational(1,2))/sp.gamma(4)-5*sp.pi/16)==0
assert sp.simplify(sp.gamma(sp.Rational(9,2))*sp.gamma(sp.Rational(1,2))/sp.gamma(5)-35*sp.pi/128)==0

def fa(aa,zz):
    # E=t^2 makes the integral smooth on [0,1].
    return mp.quad(lambda t: 2*t**8/((t*t+aa)**4*(t*t+zz)), [0,mp.sqrt(aa),mp.sqrt(zz),1])
def finf(zz):
    return 2*mp.atan(1/mp.sqrt(zz))/mp.sqrt(zz)
def threshold_ratio(aa,zz):
    # (F_a - P_a)/(a^-4 z^(7/2)), evaluated without catastrophic subtraction.
    return 2*mp.quad(lambda t: 1/((1+t*t)*(1+zz*t*t/aa)**4), [0,1,mp.sqrt(aa/zz),1/mp.sqrt(zz)])
report={'identities':'passed', 'fixed_a_threshold_ratio_target':str(mp.pi),'fixed_a_threshold_ratios':[], 'large_parameter_convergence':[], 'diagonal_limit_target':str(35*mp.pi/128),'diagonal_limit':[]}
for power in [2,4,6,8]:
    zz=mp.mpf(10)**(-power)
    report['fixed_a_threshold_ratios'].append({'a':'0.3','z':str(zz),'ratio':str(threshold_ratio(mp.mpf('.3'),zz))})
for power in [2,4,6,8]:
    aa=mp.mpf(10)**(-power);zz=mp.mpf('.01')
    report['large_parameter_convergence'].append({'a':str(aa),'z':str(zz),'F_a':str(fa(aa,zz)),'F_infinity':str(finf(zz))})
    report['diagonal_limit'].append({'a=z':str(aa),'sqrt(z)*F_a':str(mp.sqrt(aa)*fa(aa,aa))})
print(json.dumps(report,indent=2))
