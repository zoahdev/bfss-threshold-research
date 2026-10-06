#!/usr/bin/env python3
"""Self-authored finite-dimensional regression; not an analytic proof."""
import json
import numpy as np
from scipy.linalg import null_space
from pathlib import Path
rng=np.random.default_rng(621034)
d=9

def su(n):
    b=[]
    for a in range(n):
        for c in range(a+1,n):
            q=np.zeros((n,n),complex); q[a,c]=q[c,a]=1/np.sqrt(2); b.append(q)
            q=np.zeros((n,n),complex); q[a,c]=-1j/np.sqrt(2); q[c,a]=1j/np.sqrt(2); b.append(q)
    for k in range(1,n):
        q=np.zeros((n,n),complex); q[np.arange(k),np.arange(k)]=1/np.sqrt(k*(k+1)); q[k,k]=-k/np.sqrt(k*(k+1)); b.append(q)
    return b

def sample(ns,positions,scale=.008):
    N=sum(ns); k=len(ns); cuts=np.cumsum([0]+ns); pairs=[]
    cs=[]
    for w in null_space(np.sqrt(ns)[None,:]).T:
        q=np.zeros((N,N),complex)
        for a,n in enumerate(ns): q[cuts[a]:cuts[a+1],cuts[a]:cuts[a+1]]=np.eye(n)*w[a]/np.sqrt(n)
        cs.append(q)
    ins=[]; inblocks=[]
    for a,n in enumerate(ns):
        for q in su(n):
            t=np.zeros((N,N),complex); t[cuts[a]:cuts[a+1],cuts[a]:cuts[a+1]]=q; ins.append(t); inblocks.append(a)
    ms=[]
    for a in range(k):
        for b in range(a+1,k):
            for u in range(cuts[a],cuts[a+1]):
                for v in range(cuts[b],cuts[b+1]):
                    q=np.zeros((N,N),complex);q[u,v]=q[v,u]=1/np.sqrt(2);ms.append(q);pairs.append((a,b))
                    q=np.zeros((N,N),complex);q[u,v]=-1j/np.sqrt(2);q[v,u]=1j/np.sqrt(2);ms.append(q);pairs.append((a,b))
    gs=np.array(cs+ins+ms); ms=np.array(ms); D=N*N-1;m=len(ms); nc=len(cs);ni=len(ins)
    z=np.zeros((k,d));z[:,:len(positions[0])]=positions;z-=np.sum(np.array(ns)[:,None]*z,axis=0)/N
    rr=np.array([np.linalg.norm(z[a]-z[b]) for a,b in pairs]); rmin=min(rr)
    Z=np.zeros((d,N,N),complex)
    for a,n in enumerate(ns): Z[:,cuts[a]:cuts[a+1],cuts[a]:cuts[a+1]]=z[a,:,None,None]*np.eye(n)
    A=np.zeros_like(Z); alphas=[]
    for a,n in enumerate(ns):
        aa=np.zeros_like(Z)
        for g,block in zip(ins,inblocks):
            if block==a: aa+=rng.normal(size=d)[:,None,None]*g
        target=.003*min(np.linalg.norm(z[a]-z[b]) for b in range(k) if b!=a)
        norm=np.linalg.norm(aa)
        if norm: aa*=target/norm
        A+=aa;alphas.append(float(np.linalg.norm(aa)))
    Y=np.zeros_like(Z)
    for g,(a,b) in zip(ms,pairs):
        n=(z[a]-z[b])/np.linalg.norm(z[a]-z[b]); y=rng.normal(size=d);y-=n*np.dot(n,y);Y+=y[:,None,None]*g
    Y*=scale*rmin/np.linalg.norm(Y)
    def vec(X):return np.real(np.einsum('tij,dji->dt',gs,X)).ravel()
    def orbit(X):return np.stack([vec(1j*(g@X-X@g)) for g in ms],axis=1)
    BZ=orbit(Z); BA=orbit(A);BY=orbit(Y);O=BZ+BA+BY;E=BZ/rr[None,:]
    hcols=[]
    for typ,start in [(cs,0),(ins,nc)]:
        for a,g in enumerate(typ):
            for j in range(d):
                v=np.zeros((d,D));v[j,start+a]=1;hcols.append(v.ravel())
    for a,(pa,pb) in enumerate(pairs):
        n=(z[pa]-z[pb])/np.linalg.norm(z[pa]-z[pb])
        for t in null_space(n[None,:]).T:
            v=np.zeros((d,D));v[:,nc+ni+a]=t;hcols.append(v.ravel())
    H=np.stack(hcols,axis=1); h=H.shape[1];HC=H[:,:d*nc]
    OC=HC.T@O;OH=H.T@O;OV=E.T@O
    K=np.zeros((m,h));K[:,:d*nc]=OC.T/rr[:,None]
    K_direct=np.zeros_like(K)
    for a,g in enumerate(cs):
        for j in range(d):
            dz=np.zeros_like(Z);dz[j]=g;K_direct[:,a*d+j]=-orbit(dz).T@vec(Y)/rr
    g=np.eye(h)+K.T@K;W=np.eye(m)+K@K.T;M=OV-K@OH;F=E.T@(BZ+BA)
    S=H+E@K;Nmat=E-H@K.T
    T=np.block([[np.eye(h),OH],[K,OV]])
    amb=np.concatenate([S,O],axis=1)
    sg,ld=np.linalg.slogdet(T);sm,lm=np.linalg.slogdet(M)
    p=rng.normal(size=d*D)+1j*rng.normal(size=d*D)
    alpha=S.T@p;spin=O.T@p;pt=S@np.linalg.solve(g,alpha)
    beta=np.linalg.solve(M.T,spin-O.T@pt)
    reduced=np.vdot(alpha,np.linalg.solve(g,alpha)).real+np.vdot(beta,W@beta).real
    exact=np.vdot(p,p).real
    fp0=E.T@BY
    density_trace=np.trace(np.linalg.solve(F,fp0))
    normalized=M/rr[None,:]
    fp_bound=.006+2*scale+4*scale**2
    sym=np.max(np.abs(normalized-normalized.T))
    hess=-2*(BZ.T@O-OC.T@OC)
    # Numeric centered difference of Phi at stationary X along one gauge path.
    from scipy.linalg import expm
    xi=rng.normal(size=m)/rr;xi/=max(1,np.linalg.norm(xi))
    G=sum(v*t for v,t in zip(xi,ms));X=Z+A+Y
    def phi(t):
        U=expm(1j*t*G);Q=U@X@U.conj().T
        return sum(sum(np.trace(Q[j,cuts[a]:cuts[a+1],cuts[a]:cuts[a+1]]).real**2/ns[a] for j in range(d)) for a in range(k))
    # Avoid huge-centering cancellation by compare derivative of projected centers analytically.
    DX=1j*(G@X-X@G);D2X=1j*(G@DX-DX@G)
    hess_direct=2*np.linalg.norm(HC.T@vec(DX))**2+2*np.dot(vec(Z),vec(D2X))
    analytic=float(xi@hess@xi)
    # frozen pair adapted G is block diagonal, and no cross A metric occurs.
    rows_internal=slice(d*nc,d*(nc+ni))
    err_internal=np.linalg.norm(g[rows_internal,:]-np.eye(h)[rows_internal,:])
    res={
        'partition':ns,'separation_ratio':float(max(rr)/rmin),'max_internal_to_unrelated_rmin':float(max(alphas)/rmin),
        'ambient_orthogonal_frame_error':float(np.max(np.abs(np.concatenate([H,E],axis=1).T@np.concatenate([H,E],axis=1)-np.eye(d*D)))),
        'constraint_K_error':float(np.max(np.abs(K-K_direct))),
        'slice_tangent_constraint_error':float(np.max(np.abs(Nmat.T@S))),
        'internal_metric_error':float(err_internal),
        'fp_identity_error':float(np.max(np.abs(M-Nmat.T@O))),
        'jacobian_log_error':float(abs(ld-lm)),
        'kinetic_relative_error':float(abs(exact-reduced)/exact),
        'linear_density_trace':float(density_trace),
        'normalized_fp_symmetry_error':float(sym),
        'normalized_fp_deviation':float(np.linalg.norm(normalized-np.eye(m),2)),
        'claimed_fp_bound':float(fp_bound),
        'selector_hessian_relative_error':float(abs(analytic-hess_direct)/(1+abs(analytic))),
        'normal_determinant_positive':bool(sg*sm>0 and sm>0),
    }
    assert res['ambient_orthogonal_frame_error']<1e-10
    assert res['constraint_K_error']<1e-10
    assert res['slice_tangent_constraint_error']<1e-10
    assert res['internal_metric_error']<1e-10
    assert res['fp_identity_error']<1e-7
    assert res['jacobian_log_error']<1e-7
    assert res['kinetic_relative_error']<1e-9
    assert abs(density_trace)<1e-10
    assert sym<1e-10
    assert res['normalized_fp_deviation']<=fp_bound
    assert res['selector_hessian_relative_error']<1e-8
    return res

out=[]
for ns,pos in [([2,2],[[0,0],[1,1]]),([2,2,1],[[0,0],[1,0],[10,2]]),([3,1,1],[[100,17],[0,0],[1,0]]),([2,1,1],[[1000000,1000],[0,0],[1,0]]),([1,1,1,1],[[0,0],[1,0],[0,2],[7,9]])]:
    for scale in [.002,.009]:out.append(sample(ns,pos,scale))
result={'kind':'finite CPU regression, not a proof','samples':out,'max_kinetic_relative_error':max(x['kinetic_relative_error'] for x in out),'max_jacobian_log_error':max(x['jacobian_log_error'] for x in out)}
p=Path(__file__).with_name('multiblock_geometry_checks.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
