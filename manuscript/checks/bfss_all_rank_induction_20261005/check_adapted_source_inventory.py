"""Finite regressions of the actual inverse-Gauss/density coefficient inventory.
Reuses the author's exact ambient coordinate constructor; the checks concern
Taylor coefficients, not full all-vector coercivity or a numerical theorem.
"""
from pathlib import Path
import json
import numpy as np
ROOT=Path(__file__).parent
src=(ROOT.parent/'bfss_multiblock_geometry_20261005/check_multiblock_geometry.py').read_text()
scope={'__file__':str(ROOT.parent/'bfss_multiblock_geometry_20261005/check_multiblock_geometry.py')}
exec(src.split('\nout=[]\n')[0].replace('    return res','    return locals()'),scope)
sample=scope['sample'];rng=np.random.default_rng(51020261841)
def sq(x):
    e,v=np.linalg.eigh(x);return (v*np.sqrt(e))@v.T
out=[]
for ns,pos in [([2,2],[[0,0],[1,1]]),([2,2,1],[[0,0],[1,0],[10,2]]),([3,1,1],[[100,17],[0,0],[1,0]]),([2,1,1],[[1000000,1000],[0,0],[1,0]])]:
    z=sample(ns,pos,scale=.009);H=z['H'];E=z['E'];F=z['F'];Kfull=z['K'];rr=z['rr'];BA=z['BA'];BY=z['BY'];nc=z['nc'];ni=z['ni'];d=9;h=z['h'];m=z['m']
    cs=slice(0,d*nc);ins=slice(d*nc,d*(nc+ni));fs=slice(d*(nc+ni),h)
    HF=H[:,fs];HI=H[:,ins];HC=H[:,cs]
    C=HF.T@BA;NY=HF.T@BY;IY=HI.T@BY;CY=HC.T@BY;L=E.T@BY;K=Kfull[:,cs];J2=K@CY;Fi=np.linalg.inv(F)
    pF=rng.normal(size=HF.shape[1])+1j*rng.normal(size=HF.shape[1]);pI=rng.normal(size=HI.shape[1])+1j*rng.normal(size=HI.shape[1]);pC=rng.normal(size=HC.shape[1])+1j*rng.normal(size=HC.shape[1]);spin=rng.normal(size=m)+1j*rng.normal(size=m)
    rhoI=rng.normal(size=len(pI));rhoC=rng.normal(size=len(pC));rhoF=rng.normal(size=len(pF))
    uI=pI+1j*rhoI;uC=pC+1j*rhoC
    D0=-Fi@C.T@pF
    D1=Fi@(spin-NY.T@pF)+Fi@L.T@Fi@C.T@pF
    D2=-Fi@(IY.T@uI+(CY.T+F@K)@uC+1j*C.T@rhoF)
    D2-=Fi@L.T@Fi@(spin-NY.T@pF)
    D2-=Fi@L.T@Fi@L.T@Fi@C.T@pF
    D2-=Fi@J2.T@Fi@C.T@pF
    D2-=.5*K@K.T@Fi@C.T@pF
    OH0=H.T@BA;OHY=H.T@BY
    phi2=-.5*np.trace(Fi@J2)-.25*np.trace(Fi@L@Fi@L)
    assert abs(np.trace(Fi@L))<1e-10
    rows=[]
    for eps in [.08,.04,.02,.01,.005]:
        M=F+eps*L-eps*eps*J2;We=np.eye(m)+eps*eps*K@K.T;ge=np.eye(h)+eps*eps*Kfull.T@Kfull
        pv=np.concatenate([eps*uC,eps*uI,pF+1j*eps*eps*rhoF])
        orbit=(OH0+eps*OHY).T+(F+eps*L).T@(eps*Kfull)
        exact=sq(We)@np.linalg.solve(M.T,eps*spin-orbit@np.linalg.solve(ge,pv))
        pred=D0+eps*D1+eps*eps*D2
        err=np.linalg.norm(exact-pred)
        logexact=.5*(np.linalg.slogdet(M)[1]-np.linalg.slogdet(F)[1]);logerr=abs(logexact-eps*eps*phi2)
        rows.append({'epsilon':eps,'D_remainder_norm':float(err),'D_remainder_over_epsilon3':float(err/eps**3),'log_density_remainder':float(logerr),'density_remainder_over_epsilon3':float(logerr/eps**3)})
    # The first three halvings should approach cubic remainder (floating logdet
    # cancellation can dominate the last density samples at the hierarchy).
    ratios=[rows[i]['D_remainder_norm']/rows[i+1]['D_remainder_norm'] for i in range(len(rows)-1)]
    assert min(ratios)>7.0 and max(ratios)<9.0
    out.append({'partition':ns,'gap_ratio':float(max(rr)/min(rr)),'D_halving_ratios':ratios,'samples':rows})
result={'scope':'Actual D0/D1/D2 and quadratic density Taylor coefficients from ambient matrices; not complementary coercivity.', 'cases':out}
(ROOT/'adapted_source_inventory_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
