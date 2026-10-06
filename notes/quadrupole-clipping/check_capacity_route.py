"""Algebra checks for the BFSS scalar-primitive capacity route.

These checks verify finite algebra, not the BFSS domain assumptions,
ground-state existence, or a rank-uniform estimate.
"""
from pathlib import Path
import json
import sympy as sp
import numpy as np

r, c, f, fp, s, n = sp.symbols('r c f fp s n', positive=True, real=True)
j = r**2*(1-f)**2/18+c*(-(1-f)*fp/(2*r)+fp**2/8+s*n**2*f**2/4)
completed = c*(fp-2*(1-f)/r)**2/8+(r**2/18-c/(2*r**2))*(1-f)**2+s*n**2*c*f**2/4
assert sp.simplify(j-completed) == 0
assert sp.simplify(r**2/18-(2*r**4/sp.Integer(99))/(2*r**2)-r**2/22) == 0
A, B = r**2/22, s*n**2*c/4
fstar = sp.simplify(A/(A+B))
harmonic = sp.simplify((A*(1-f)**2+B*f**2).subs(f,fstar))
assert sp.simplify(harmonic-s*n**2*r**2*c/(4*r**2+22*s*n**2*c)) == 0

# Every real symmetric traceless 9 by 9 matrix has 44 polarizations.
basis = []
for i in range(9):
    for k in range(i+1,9):
        H = np.zeros((9,9)); H[i,k]=H[k,i]=1/np.sqrt(2)
        basis.append(H)
for k in range(1,9):
    H = np.zeros((9,9)); H[np.arange(k),np.arange(k)]=1
    H[k,k]=-k; H /= np.sqrt(k*(k+1))
    basis.append(H)
basis=np.asarray(basis)
assert len(basis)==44
assert np.allclose(np.einsum('aij,bij->ab',basis,basis),np.eye(44))

rng=np.random.default_rng(20261006)
max_projection_error=0.
max_residual_error=0.
for N in [2,3,4,8,16]:
    for _ in range(100):
        Z=rng.normal(size=(9,N*N-1))
        M=Z@Z.T/N
        rho2=np.trace(M)
        projected=np.einsum('aij,ji->a',basis,M)
        D=np.trace(M@M)-rho2**2/9
        max_projection_error=max(max_projection_error,abs(projected@projected-D))
        assert np.isclose(projected@projected,D)
        assert -1e-10 <= D <= 8*rho2**2/9+1e-10
        H=basis[rng.integers(44)]
        q=np.trace(H@M); ah=np.trace(H@H@M)
        ff,ffp=rng.normal(size=2)
        residual=(1-ff)*H@Z-q*ffp/(2*np.sqrt(rho2))*Z
        direct=np.sum(residual**2)/(2*N)
        formula=(1-ff)**2*ah/2-(1-ff)*ffp*q*q/(2*np.sqrt(rho2))+ffp**2*q*q/8
        max_residual_error=max(max_residual_error,abs(direct-formula))
        assert np.isclose(direct,formula)

# Pointwise comparison used to identify the necessary anisotropy profile.
u=np.logspace(-14,14,1000)
assert np.all(u/(4+22*u) >= np.minimum(1,u)/26*(1-1e-13))

# Finite dimensional self-adjoint Q check: exact variational formula,
# including a zero mode. This is the abstract identity, not BFSS data.
Q=np.diag([-4.,-1.,0.,0.1,2.])
w=rng.normal(size=5)
ss=.03
v=np.linalg.solve(Q@Q+ss*np.eye(5),Q@w)
jj=np.linalg.norm(w-Q@v)**2+ss*np.linalg.norm(v)**2
kk=ss*w@np.linalg.solve(Q@Q+ss*np.eye(5),w)
assert np.isclose(jj,kk)

result={
    'symbolic_square_completion': True,
    'symbolic_radial_coefficient': '1/22',
    'symbolic_harmonic_mean': str(harmonic),
    'profile_comparison_constant': '1/26',
    'spin2_polarizations': len(basis),
    'random_configurations': 500,
    'max_projection_absolute_error': max_projection_error,
    'max_residual_absolute_error': max_residual_error,
    'finite_matrix_variational_identity_error': abs(jj-kk),
    'scope': 'Algebra only; no BFSS ground-state or uniform-in-rank bound claimed.'
}
Path(__file__).with_name('capacity_route_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
