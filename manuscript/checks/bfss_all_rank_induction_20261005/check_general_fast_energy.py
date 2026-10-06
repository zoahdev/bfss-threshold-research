"""Self-authored CPU regressions of the general frozen pair formulas.
Numerics corroborate, but are not the proof of the commutator-square bound.
"""
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).parent
rng=np.random.default_rng(51020261746)
# Real symmetric Spin(9), from left multiplication by imaginary octonions.
triples=[(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]
E=[]
for a in range(1,8):
    e=np.zeros((8,8));e[a,0]=1;e[0,a]=-1
    for u,v,w in triples:
        for x,y,z in ((u,v,w),(v,w,u),(w,u,v)):
            if a==x:e[z,y]=1;e[y,z]=-1
    E.append(e)
z=np.zeros((8,8));i8=np.eye(8)
gamma=[np.block([[z,e],[-e,z]]) for e in E]+[np.block([[z,i8],[i8,z]]),np.diag([1]*8+[-1]*8)]
assert max(np.linalg.norm(a@b+b@a-2*(i==j)*np.eye(16)) for i,a in enumerate(gamma) for j,b in enumerate(gamma))==0

def c(a,b):return a@b-b@a

def f2(A):return sum(np.linalg.norm(c(a,b))**2 for i,a in enumerate(A) for b in A[i+1:])

def family(A,B,r):
    n,m=A.shape[1],B.shape[1];d=n*m
    T=[np.kron(a,np.eye(m))-np.kron(np.eye(n),b.T) for a,b in zip(A,B)]
    Q=[t+(r if i==8 else 0)*np.eye(d) for i,t in enumerate(T)]
    H=sum(q@q for q in Q)
    C=[[c(a,b) for b in Q] for a in Q]
    K=np.block([[(H if i==j else np.zeros_like(H))-Q[i]@Q[j]+2*C[i][j] for j in range(8)] for i in range(8)])
    qi=np.linalg.inv(Q[8]);W=np.vstack(Q[:8])@qi;G=np.eye(8*d)+W@W.conj().T
    eg,ug=np.linalg.eigh(G);gh=(ug*np.sqrt(eg))@ug.conj().T
    BF=gh@K@gh
    D=sum(np.kron(g,q) for g,q in zip(gamma,Q));DH=np.kron(np.eye(16),H)
    S=sum(np.kron(gamma[i]@gamma[j],C[i][j]) for i in range(9) for j in range(i+1,9))
    ferm=.5*np.abs(np.linalg.eigvalsh(D)).sum();base=8*np.sqrt(np.linalg.eigvalsh(H)).sum()
    bos=np.sqrt(np.linalg.eigvalsh(BF)).sum();cc=f2(np.array(T));end=m*f2(A)+n*f2(B)
    e=bos-ferm
    stats={'n':n,'m':m,'r':r,'E':float(e),'F2':float(cc),'energy_ratio':float(abs(e)*r**3/cc) if cc>1e-25 else None,
           'bosonic_ratio':float(abs(bos-base)*r**3/cc) if cc>1e-25 else None,
           'fermionic_ratio':float(abs(ferm-base)*r**3/cc) if cc>1e-25 else None,
           'Kmin_scaled':float(np.linalg.eigvalsh(K).min()/r**2),'Dgap_scaled':float(np.abs(np.linalg.eigvalsh(D)).min()/r),
           'endpoint_weight_error':float(abs(cc-end)),
           'D_square_identity_error':float(np.linalg.norm(D@D-DH-S)),
           'S_Frobenius_identity_error':float(abs(np.linalg.norm(S)**2-16*cc))}
    return stats,(T,Q,H,C,K,G,BF,D)

def hermitian_tuple(n,radius,commuting=False):
    if n==1:return np.zeros((9,1,1),complex)
    if commuting:
        A=np.array([np.diag(rng.normal(size=n)) for _ in range(9)],complex)
    else:
        Z=rng.normal(size=(9,n,n))+1j*rng.normal(size=(9,n,n));A=(Z+Z.conj().transpose(0,2,1))/2
    A-=np.trace(A,axis1=1,axis2=2)[:,None,None]*np.eye(n)[None]/n
    A*=radius/np.linalg.norm(A)
    return A

def potential(X):return .5*f2(X)

out={'random':[],'commuting':[],'potential_regressions':[]}
for n,m in ((2,1),(3,1),(2,2),(3,2),(4,1)):
    for r in (.7,1.,2.3):
        A=hermitian_tuple(n,.004*r);B=hermitian_tuple(m,.004*r)
        st,data=family(A,B,r);out['random'].append(st)
        A0=hermitian_tuple(n,.004*r,True);B0=hermitian_tuple(m,.004*r,True)
        st0,data0=family(A0,B0,r);st0['commuting_GK_identity_error']=float(np.linalg.norm(data0[5]@data0[4]-np.kron(np.eye(8),data0[2])))
        out['commuting'].append(st0)
        # Direct full (n+m)-matrix potential quadratic coefficient. Centers are traceless.
        Z=(rng.normal(size=(8,n,m))+1j*rng.normal(size=(8,n,m)))*.1
        X=[];Y=[]
        for i in range(9):
            xi=np.zeros((n+m,n+m),complex);yi=np.zeros_like(xi)
            xi[:n,:n]=A[i]+(m*r/(n+m) if i==8 else 0)*np.eye(n)
            xi[n:,n:]=B[i]-(n*r/(n+m) if i==8 else 0)*np.eye(m)
            if i<8:yi[:n,n:]=Z[i];yi[n:,:n]=Z[i].conj().T
            X.append(xi);Y.append(yi)
        X=np.array(X);Y=np.array(Y)
        extracted=.5*(potential(X+Y)+potential(X-Y))-potential(X)-potential(Y)
        zz=Z.ravel();direct=np.vdot(zz,data[4]@zz).real
        out['potential_regressions'].append({'n':n,'m':m,'r':r,'direct':float(direct),'extracted':float(extracted),'absolute_error':float(abs(direct-extracted))})
# General real-trace word estimate: compare arbitrary order with canonical order.
wordmax=0.
for d in (2,3,5):
    X=hermitian_tuple(d,.02);kap=max(np.linalg.norm(x,2) for x in X);ff=f2(X)
    for q in range(2,11):
        inds=rng.integers(0,9,q)
        def traceword(ids):
            p=np.eye(d,dtype=complex)
            for idx in ids:p=p@X[idx]
            return np.trace(p).real
        err=abs(traceword(inds)-traceword(sorted(inds)))
        if q>=4:
            bound=q*(q-1)*(q-2)*(q-3)/8*kap**(q-4)*ff
            wordmax=max(wordmax,err/bound if bound else 0)
        else:assert err<1e-14
out['summary']={
    'cases':len(out['random']),
    'maximum_energy_ratio':max(x['energy_ratio'] for x in out['random']),
    'maximum_bosonic_ratio':max(x['bosonic_ratio'] for x in out['random']),
    'maximum_fermionic_ratio':max(x['fermionic_ratio'] for x in out['random']),
    'maximum_commuting_energy_abs':max(abs(x['E']) for x in out['commuting']),
    'maximum_commuting_GK_error':max(x['commuting_GK_identity_error'] for x in out['commuting']),
    'maximum_potential_quadratic_error':max(x['absolute_error'] for x in out['potential_regressions']),
    'maximum_endpoint_weight_error':max(x['endpoint_weight_error'] for x in out['random']),
    'maximum_D_square_error':max(x['D_square_identity_error'] for x in out['random']),
    'maximum_word_bound_ratio':wordmax,
}
(ROOT/'general_fast_energy_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out['summary'],indent=2))
