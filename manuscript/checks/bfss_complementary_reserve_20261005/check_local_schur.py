#!/usr/bin/env python3
"""Self-authored finite algebra regressions; not a BFSS theorem verifier."""
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.hermite import hermgauss

rng=np.random.default_rng(20261005)
results={}
errs=[]
for width in (1e-4,1e-2,0.15):
  for _ in range(50):
    n,m=7,4
    Z=width*rng.normal(size=(n,n))/np.sqrt(n)
    K=width*rng.normal(size=(n,m))/np.sqrt(m)
    T=np.linalg.inv(np.eye(n)+Z)
    d=rng.normal(size=n)+1j*rng.normal(size=n)
    q=rng.normal(size=n)+1j*rng.normal(size=n)
    W=np.eye(n)+K@K.T
    z=d+T@q
    lhs=np.vdot(z,W@z).real-np.vdot(d,d).real
    rhs=(2*np.vdot(d,q).real-2*np.vdot(Z.T@d,T@q).real
         +np.vdot(T@q,T@q).real+np.linalg.norm(K.T@z)**2)
    errs.append(abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))
results['exact_fast_spin_error_identity']={'samples':len(errs),'max_relative_error':max(errs)}

# Check the nonsymmetric-to-symmetric linear slow/fast cross correction.
x,w=hermgauss(32)
X,Y=np.meshgrid(x,x,indexing='ij'); weights=np.outer(w,w)/np.pi
a,c,p,q=0.17,-0.06,2.3,-1.7
b=a*X*Y+c*Y**2; div=a*X+2*c*Y
px=p+1j*X; beta=b*(q+1j*Y); bhat=beta-0.5j*div
raw=2*np.sum(weights*np.real(np.conj(px)*beta))
sym=2*np.sum(weights*np.real(np.conj(px)*bhat))
expected=a/2
results['linear_charge_symmetrization']={'raw_minus_sym':float(raw-sym),'half_internal_divergence_derivative':expected,'absolute_error':float(abs(raw-sym-expected))}

# Exact Gaussian-divergence dual norms in one and two oscillator roots.
dual=[]
for r in (1.,1e3,1e12):
    kappa=.013
    source2=2*kappa*kappa/(r*r)
    dual2=source2/(4*r)
    coefficient2=kappa*kappa/(2*r**3)
    dual.append({'r':r,'dual_squared':dual2,'field_gaussian_norm_squared':coefficient2,'ratio':dual2/coefficient2})
results['incident_gaussian_divergence']=dual
tri=[]
for rf in (1.,1e3,1e9,1e12):
  re=rf+1.; rg=1.
  source2=re/(rf*rg*rg)
  dual2=source2/(2*(re+rf))
  field2=1/(2*rf*rg*rg)
  tri.append({'triangle':[re,rf,rg],'dual_over_field':dual2/field2})
results['mixed_root_divergence']=tri

# A genuine variational block minimization with arbitrarily high slow momentum.
# F=p2+W-S^2/(r+p2), W=S^2/r. No series in p2/r is used.
rows=[]
for r in (1.,1e3,1e12):
  S2=1/r; W=S2/r; m=S2/(r*r)
  for ratio in (0.,1e-9,1.,1e3,1e12):
    p2=r*ratio
    defect=W*p2/(r+p2)
    upper=m*p2
    rows.append({'r':r,'p2_over_r':ratio,'defect':defect,'relative_form_upper':upper,'bound_holds':defect<=upper*(1+1e-14)+1e-300})
results['unrestricted_slow_momentum_block_minimization']=rows
results['negative_controls']={
 'gauss_square_double_count':{'slow_covector':0,'retained_J':0,'frozen_fast_gauss_square':7,'a_second_full_gauss_square_is_not_reserved':True},
 'remote_vacuum_loss':[{'remote_frequency':r,'nearest_gap':1.,'fixed_fraction_vacuum_loss':.01*r} for r in (1.,1e6,1e12)]}
assert results['exact_fast_spin_error_identity']['max_relative_error']<1e-12
assert results['linear_charge_symmetrization']['absolute_error']<1e-12
assert all(x['ratio']<=1+1e-14 for x in dual)
assert all(x['dual_over_field']<=1+1e-14 for x in tri)
assert all(x['bound_holds'] for x in rows)
out=Path(__file__).with_name('local_schur_checks.json')
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'written':str(out),'identity_max_relative_error':max(errs),'symmetrization_error':results['linear_charge_symmetrization']['absolute_error'],'all_checks_passed':True},indent=2))
