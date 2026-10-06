"""Independent exact-Wick finite tests of centered BFSS triangle cancellation.
No sampling of Gaussian states; floating matrix algebra, NOT an analytic proof.
"""
from pathlib import Path
import json, itertools
import numpy as np
from scipy.linalg import null_space

def gamma9():
    triples=[(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]
    es=[]
    for a in range(1,8):
        e=np.zeros((8,8));e[a,0]=1;e[0,a]=-1
        for u,v,w in triples:
            for x,y,z in ((u,v,w),(v,w,u),(w,u,v)):
                if a==x:e[z,y]=1;e[y,z]=-1
        es.append(e)
    z=np.zeros((8,8));i=np.eye(8)
    gs=np.array([np.block([[z,e],[-e,z]]) for e in es]+[np.block([[z,i],[i,z]]),np.diag([1]*8+[-1]*8)])
    assert max(np.max(np.abs(a@b+b@a-2*(j==k)*np.eye(16))) for j,a in enumerate(gs) for k,b in enumerate(gs))==0
    return gs
GAM=gamma9()

def basis(n):
    b=[];pairs=[]
    for a in range(n):
        for c in range(a+1,n):
            t=np.zeros((n,n),complex);t[a,c]=t[c,a]=1/np.sqrt(2);b.append(t);pairs.append((a,c))
            t=np.zeros((n,n),complex);t[a,c]=-1j/np.sqrt(2);t[c,a]=1j/np.sqrt(2);b.append(t);pairs.append((a,c))
    for k in range(1,n):
        t=np.zeros((n,n));t[np.arange(k),np.arange(k)]=1/np.sqrt(k*(k+1));t[k,k]=-k/np.sqrt(k*(k+1));b.append(t)
    return np.array(b),pairs

def eq2(A,cov):
    # Gaussian quadratic polynomial y^T A y second moment
    return np.einsum('...ii->...', A*cov[None,:])**2+2*np.einsum('...ij,...ji,i,j->...',A,A,cov,cov)

def ferm2(A,C):
    # A antisymmetric, q=theta^T A theta; Wick of ordered Majoranas
    mean=np.einsum('ab,ab->',A,C)
    return mean*mean-2*np.einsum('ab,cd,ac,bd->',A,A,C,C,optimize=True)

def run(positions):
    z=np.zeros((3,9));z[:,:len(positions[0])]=positions;z-=z.mean(axis=0)
    gs,pairs=basis(3);nc=8;nf=6
    f=np.empty((nc,nc,nc))
    for a,b in itertools.product(range(nc),repeat=2):
        f[a,b]=np.real(-1j*np.einsum('ij,cji->c',gs[a]@gs[b]-gs[b]@gs[a],gs))
    assert np.max(np.abs(f+f.swapaxes(0,1)))<1e-14
    rr=np.array([np.linalg.norm(z[a]-z[b]) for a,b in pairs]);bb=np.array([z[a]-z[b] for a,b in pairs])
    Z=np.einsum('ia,ac->ic',z.T,np.array([[g[a,a].real for g in gs] for a in range(3)]))
    # Y_i^A=H_iAm y_m, with exactly orthonormal root-transverse columns.
    hs=[];rcoord=[]
    for a,(u,v) in enumerate(pairs):
        for t in null_space((z[u]-z[v])[None,:]).T:
            h=np.zeros((9,nc));h[:,a]=t;hs.append(h);rcoord.append(rr[a])
    H=np.stack(hs,axis=-1);rcoord=np.array(rcoord);dim=len(rcoord);cov=1/(2*rcoord)
    # BY_ambient,gauge,m = i[gauge,Y_m] = -f(gauge,color,output)Y
    BY=-np.einsum('abC,ibm->iCam',f[:nf],H,optimize=True)
    BZ=-np.einsum('abC,ib->iCa',f[:nf],Z,optimize=True)
    E=BZ/rr[None,None,:]
    assert np.linalg.norm(np.einsum('iCa,iCb->ab',E,E)-np.eye(nf))<1e-12
    L=np.einsum('iCa,iCbm->abm',E,BY,optimize=True)
    CY=BY[:,nf:,:,:].reshape(18,nf,dim)
    NY=np.einsum('iCu,iCam->uam',H,BY,optimize=True)
    phi=-.5*np.einsum('sam,san,a->mn',CY,CY,rr**-2,optimize=True)-.25*np.einsum('abm,ban,a,b->mn',L,L,rr**-1,rr**-1,optimize=True)
    fastdensity=float(2*np.trace(phi))
    O=np.einsum('uam,a->aum',NY,rr**-1)
    opoly=np.einsum('aum,u->amu',O,rcoord)
    opoly=(opoly+opoly.swapaxes(1,2))/2
    orbital=float(eq2(opoly,cov).sum())
    # Complete quartic and cubic potential from structure constants.
    quartic=0.;cubic=np.zeros((dim,dim,dim))
    for i in range(9):
        for j in range(i+1,9):
            P=np.einsum('Abc,bm,cn->Amn',f,H[i],H[j],optimize=True)
            P=(P+P.swapaxes(1,2))/2
            quartic+=eq2(P,cov).sum()
            lin=np.einsum('Abc,b,cm->Am',f,Z[i],H[j],optimize=True)+np.einsum('Abc,bm,c->Am',f,H[i],Z[j],optimize=True)
            cubic+=2*np.einsum('Am,Anp->mnp',lin,P,optimize=True)
    cubic=sum(cubic.transpose(perm) for perm in itertools.permutations(range(3)))/6
    cubict=np.einsum('mnn,n->m',cubic,cov)
    cubicnorm=6*np.einsum('mnp,mnp,m,n,p->',cubic,cubic,cov,cov,cov)+9*np.dot(cubict*cov,cubict)
    # Fermion covariance for occupied negative energy states: (I+sign(Dad))/2.
    Dad=-1j*np.einsum('cab,ic->iab',f[:,:nf,:nf],Z,optimize=True)
    D=sum(np.kron(GAM[i],Dad[i]) for i in range(9))
    sign=D/np.tile(rr,16)[None,:]
    assert np.linalg.norm(sign@sign-np.eye(16*nf))<1e-10
    Cf=(np.eye(16*nf)+sign)/2
    assert np.linalg.norm(Cf+Cf.T-np.eye(16*nf))<1e-12
    spintri=0.
    for a in range(nf):
        A=-.5j*np.kron(np.eye(16),f[a,:nf,:nf])
        spintri+=ferm2(A,Cf).real/rr[a]**2
    yuknorm=0.
    for m in range(dim):
        A=-1j*sum(np.kron(GAM[i],np.einsum('Cab,C->ab',f[:,:nf,:nf],H[i,:,m])) for i in range(9))
        yuknorm+=cov[m]*ferm2(A,Cf).real
    # Full W for singleton triple. BH=36 per edge, slow density pair=16.
    pairweight=sum(1/rr[::2]**2)
    rho=np.zeros((3,9))
    for a,b in pairs[::2]:
        diff=z[a]-z[b];r=np.linalg.norm(diff);rho[a]+=diff/r**2;rho[b]-=diff/r**2
    rhocross=float(np.sum(rho*rho)-2*pairweight)
    BH=36*pairweight;slowdensity=16*pairweight+rhocross
    spinpair=16*pairweight
    W=BH+slowdensity+fastdensity+quartic+orbital+spinpair+spintri
    pairW=64*pairweight
    triangleW=W-pairW
    den=2*rr[::2].sum();schur=(cubicnorm+yuknorm)/den
    return dict(positions=positions,gaps=rr[::2].tolist(),rho_cross=rhocross,quartic=float(quartic),fast_density=fastdensity,orbital=orbital,spin_triangle=float(spintri),cubic_norm=float(cubicnorm),yukawa_triangle_norm=float(yuknorm),W_triangle=float(triangleW),Schur_triangle=float(schur),difference=float(triangleW-schur),relative_error=float((triangleW-schur)/max(abs(schur),1)),pair_W=float(pairW))

if __name__=='__main__':
    out=[]
    for pos in [[[0,0],[1,0],[2,0]],[[0,0],[1,0],[.2,1.3]],[[0,0],[1,0],[100,7]],[[0,0],[1,0],[10000,10]]]:
        x=run(pos)
        assert abs(x["difference"]) < 1e-10*(1+abs(x["Schur_triangle"]))
        out.append(x);print(json.dumps(x),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
