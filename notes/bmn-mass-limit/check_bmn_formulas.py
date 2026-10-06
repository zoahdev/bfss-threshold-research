"""Exact algebra checks for the BMN research note. Requires SymPy.

These checks do not solve the interacting BMN/BFSS wavefunctions.
"""
import itertools
import sympy as s

N, m, K, n = s.symbols('N m K n', positive=True)

# Gradient identities in a representative raw-coordinate model with two colors.
# Their dimension-independent proof is in the note.
z = s.symbols('z0:6', real=True)
lam = [1 / s.sqrt(2), -1 / s.sqrt(2), 0]
rho2 = sum(x*x for x in z) / N
q = sum(lam[i] * z[2*i+a]**2 for i in range(3) for a in range(2)) / N
a = sum(lam[i]**2 * z[2*i+j]**2 for i in range(3) for j in range(2)) / N
rho = s.sqrt(rho2)
gq = [s.diff(q, x) for x in z]
gr = [s.diff(rho, x) for x in z]
assert s.simplify(sum(t*t for t in gq) - 4*a/N) == 0
assert s.simplify(sum(t*t for t in gr) - 1/N) == 0
assert s.simplify(sum(u*v for u,v in zip(gq, gr)) - 2*q/(N*rho)) == 0
gf = [s.diff(rho*q, x) for x in z]
assert s.simplify(sum(t*t for t in gf) - (4*rho2*a+5*q*q)/N) == 0
print('PASS: raw-color gradients, including weighted coefficient 5')

# Independent Gaussian monomial evaluation, not a Monte Carlo estimate.
def moment(exponents, variances):
    ans = s.Integer(1)
    for p, v in zip(exponents, variances):
        if p % 2:
            return s.Integer(0)
        if p:
            ans *= s.factorial2(p-1) * v**(p//2)
    return ans

for k in [1, 2, 3, 5]:
    d = 9*k
    variances = [s.Rational(3,2)/m]*3 + [s.Integer(3)/m]*6
    variances *= k
    q2 = 0
    rq2 = 0
    for u, v in itertools.product(range(k), repeat=2):
        exp = [0]*d
        for j in [9*u+3, 9*u+4, 9*v+3, 9*v+4]:
            exp[j] += 1
        q2 += 2*moment(exp, variances)
        for j in range(d):
            exp2 = exp.copy()
            exp2[j] += 2
            rq2 += 2*moment(exp2, variances)
    assert s.simplify(q2 - 18*k/m**2) == 0
    assert s.simplify(rq2 - (405*k*k+216*k)/m**3) == 0
print('PASS: exact Wick enumeration K=1,2,3,5; coefficients 18,405,216,621')

# General-K cumulant trace formula for the same SO(6) polarization.
D = s.diag(*([s.Rational(3,2)/m]*3 + [s.Integer(3)/m]*6))
h = s.zeros(9)
h[3,4] = h[4,3] = 1/s.sqrt(2)
assert s.trace(h*h) == 1 and s.trace(h) == 0
assert s.trace(h*D) == 0
var = 2*K*s.trace(h*D*h*D)/N**4
mixed = (2*K*K*s.trace(D)*s.trace(h*D*h*D)
         + 8*K*s.trace(D*h*D*h*D))/N**6
assert s.simplify(var-18*K/(N**4*m*m)) == 0
assert s.simplify(mixed-(405*K*K+216*K)/(N**6*m**3)) == 0
assert s.simplify(var-(18*K/(N*N*m))/(N*N*m)) == 0
print('PASS: general-K cumulants and saturation of finite-mass quadrupole bound')

# Two-block mass normalization.
trzz = (n*((N-n)/N)**2 + (N-n)*(n/N)**2)/N
assert s.simplify(trzz - n*(N-n)/N**2) == 0
assert s.simplify(N*N*trzz-n*(N-n)) == 0
print('PASS: two-block reduced mass and normalized trace')

# Physical BMN mass and coupling conversion.
R, ell, mu, c = s.symbols('R ell mu c', positive=True)
E = R*N**s.Rational(1,3)/ell**2
mass = mu/E
assert s.simplify(1/(N*mass**3)-R**3/(mu**3*ell**6)) == 0
mN = c*N**s.Rational(-2,3)
assert s.simplify(1/(N*mN**3)-N/c**3) == 0
assert s.simplify(1/(N*N*mN)-N**s.Rational(-4,3)/c) == 0
print('PASS: physical rescaling and N^(-4/3) mass scale')

# SO(9)-invariant tensor contractions: holomorphic square vs positive norm.
u = s.Matrix([1,s.I]+[0]*7)
uc = s.conjugate(u)
assert (u.T*u)[0] == 0 and (uc.T*u)[0] == 2
A, B = s.symbols('A B', real=True)
T = lambda i,j,k,l: A*s.KroneckerDelta(i,j)*s.KroneckerDelta(k,l) + B*(
    s.KroneckerDelta(i,k)*s.KroneckerDelta(j,l)+s.KroneckerDelta(i,l)*s.KroneckerDelta(j,k))
hol = sum(u[i]*u[j]*u[k]*u[l]*T(i,j,k,l)
          for i,j,k,l in itertools.product(range(2), repeat=4))
pos = sum(uc[i]*uc[j]*u[k]*u[l]*T(i,j,k,l)
          for i,j,k,l in itertools.product(range(2), repeat=4))
assert s.simplify(hol) == 0 and s.simplify(pos-8*B) == 0
assert s.simplify(sum(h[i,j]*h[k,l]*T(i,j,k,l)
    for i,j,k,l in itertools.product(range(9), repeat=4))-2*B) == 0
print('PASS: SO(9) positive-norm factor 1/4 and vanishing holomorphic square')
print('ALL EXACT CHECKS PASSED')
