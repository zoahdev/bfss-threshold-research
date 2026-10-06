"""Self-authored finite algebra regressions, not a proof of BFSS coercivity."""
import json, numpy as np
from pathlib import Path
rng=np.random.default_rng(20261005)
checks={}
# Exact pointwise completion, including unrestricted slow momenta.
errs=[]
for _ in range(20):
    A=.03*rng.normal(size=(5,7)); p=rng.normal(size=7)+1j*rng.normal(size=7)
    a=rng.normal(size=5)+1j*rng.normal(size=5)
    lhs=np.vdot(p,p).real+np.vdot(a+A@p,a+A@p).real
    rhs=np.linalg.norm(p+A.T@a)**2+np.linalg.norm(a)**2+np.linalg.norm(A@p)**2-np.linalg.norm(A.T@a)**2
    errs.append(abs(lhs-rhs)/max(1,lhs))
checks['slow_square_relative_error']=max(errs)
# Exact inverse expansion, moving the remainder onto the other side.
errs=[]
for _ in range(20):
    Z=.01*rng.normal(size=(8,8)); T=np.linalg.inv(np.eye(8)+Z)
    d=rng.normal(size=8)+1j*rng.normal(size=8); n=rng.normal(size=8)+1j*rng.normal(size=8)
    X=n-Z@d
    lhs=np.linalg.norm(T@(d+n))**2
    rhs=np.linalg.norm(d)**2+2*np.vdot(d,X).real-2*np.vdot(Z.T@d,T@X).real+np.linalg.norm(T@X)**2
    errs.append(abs(lhs-rhs)/max(1,lhs))
checks['inverse_remainder_relative_error']=max(errs)
# Finite Fock regression of exact Gaussian ground-state transform on a
# cubic triangle. The vector is supported below cutoff, so no truncation
# commutator meets the boundary.
m=6
an=np.diag(np.sqrt(np.arange(1,m)),1); eye=np.eye(m)
def local(mat,j):
    out=np.array([[1.]])
    for k in range(3): out=np.kron(out,mat if j==k else eye)
    return out
al=[local(an,j) for j in range(3)]
inds=[(i*m+j)*m+k for i in range(3) for j in range(3) for k in range(3)]
v=np.zeros(m**3,dtype=complex); v[inds]=rng.normal(size=len(inds))+1j*rng.normal(size=len(inds)); v/=np.linalg.norm(v)
errs=[]; weights=[]
for r in [(2.,3.,4.),(10.,1e3,1e3+5),(10.,1e6,1e6+5),(10.,1e9,1e9+5)]:
    y=[(al[j]+al[j].T)/np.sqrt(2*r[j]) for j in range(3)]
    p=[-1j*np.sqrt(r[j]/2)*(al[j]-al[j].T) for j in range(3)]
    ann=[np.sqrt(2*r[j])*al[j] for j in range(3)]
    for e,f,g in [(0,1,2),(1,0,2),(2,0,1)]:
        lhs=2*np.vdot(p[e]@v,y[f]@(p[g]@v)).real/r[e]
        grad=2*np.vdot(ann[e]@v,y[f]@(ann[g]@v)).real/r[e]
        drift=-2*r[g]*np.vdot(v,y[e]@(y[f]@(y[g]@v))).real
        errs.append(abs(lhs-grad-drift)/max(1,abs(lhs),abs(grad),abs(drift)))
        weights.append((min(r)*r[g]/(r[e]*r[f]),r[g]/(r[e]**2*r[f])/(r[e]**-2+r[f]**-2)))
checks['triangle_gaussian_transform_relative_error']=max(errs)
checks['triangle_weight_maxima']=[max(x[j] for x in weights) for j in range(2)]
# Negative control: a fixed loss of far boson kinetic on a far vacuum
# cannot be paid by an unrelated nearest-edge excitation gap.
checks['far_vacuum_negative_control']=[{'far_frequency':R,'short_excitation':20.,'fixed_fraction_loss':.01*R/2,'loss_over_short_gap':.01*R/40} for R in [1e3,1e6,1e9]]
checks['scope']='Algebra and oscillator-weight regression only; no numerical test replaces the coefficient, domain, or curvature proof.'
assert checks['slow_square_relative_error']<1e-12
assert checks['inverse_remainder_relative_error']<1e-12
assert checks['triangle_gaussian_transform_relative_error']<1e-11
assert checks['triangle_weight_maxima'][0]<=2+1e-12
assert checks['triangle_weight_maxima'][1]<=2+1e-12
out=Path(__file__).with_name('colored_reserve_checks.json'); out.write_text(json.dumps(checks,indent=2)+'\n')
print(out.read_text())
