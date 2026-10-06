"""Self-authored finite regressions for the scoped multiblock source lemma.
The sparse Fock model checks the oscillator homological identity and graph
energy bookkeeping, not the full BFSS coefficient inventory.
"""
from pathlib import Path
import json, math
import numpy as np

ROOT=Path(__file__).parent
rng=np.random.default_rng(51020261815)
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

def herm(n):
    x=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));x=(x+x.conj().T)/2
    x-=np.trace(x)*np.eye(n)/n
    return x/max(np.linalg.norm(x),1.)

def sqrtm(x):
    e,v=np.linalg.eigh(x);return (v*np.sqrt(e))@v.conj().T

def family(T,t,r):
    d=T[0].shape[0];Q=[t*a+(r if i==8 else 0)*np.eye(d) for i,a in enumerate(T)]
    H=sum(a@a for a in Q);C=lambda i,j:Q[i]@Q[j]-Q[j]@Q[i]
    K=np.block([[(H if i==j else np.zeros_like(H))-Q[i]@Q[j]+2*C(i,j) for j in range(8)] for i in range(8)])
    F=Q[8];Fi=np.linalg.inv(F);w=np.vstack(Q[:8])@Fi;G=np.eye(8*d)+w@w.conj().T
    Gh=sqrtm(G);Gih=np.linalg.inv(Gh);Omega=Gih@sqrtm(Gh@K@Gh)@Gih
    D=sum(np.kron(g,q) for g,q in zip(gamma,Q));ev,v=np.linalg.eigh(D);S=(v*np.sign(ev))@v.conj().T
    P=(np.eye(16*d)-S)/2
    return Omega,P,S,Fi

jets=[]
for n,m in [(2,1),(2,2),(3,1),(3,2)]:
    T=[np.kron(herm(n),np.eye(m))-np.kron(np.eye(n),herm(m).T) for _ in range(9)]
    d=n*m;r=1.7;Tc=herm(d);step=2e-5
    Om, Pm, Sm, Fm=family(T,-step,r);Op,Pp,Sp,Fp=family(T,step,r)
    dOm=(Op-Om)/(2*step);dP=(Pp-Pm)/(2*step)
    expectedOmega=np.kron(np.eye(8),T[8])
    expectedP=-sum(np.kron(gamma[i],T[i]) for i in range(8))/(2*r)
    # Real Gaussian metric is 1/8 Tr_real[(Omega^-1 dOmega)^2].
    bos=2*np.trace(dOm@dOm).real/(8*r*r)
    ferm=np.trace(dP@dP).real/2
    expected=2*sum(np.trace(t@t).real for t in T)/(r*r)
    def spinpartial(S,Fi):
        ss=S.reshape(16,d,16,d)
        return np.einsum('ab,ibja->ij',Tc@Fi,ss).imag
    dspin=(spinpartial(Sp,Fp)-spinpartial(Sm,Fm))/(2*step)
    jets.append({'n':n,'m':m,'bosonic_first_jet_error':float(np.linalg.norm(dOm-expectedOmega)),
                 'fermionic_projector_first_jet_error':float(np.linalg.norm(dP-expectedP)),
                 'vacuum_metric_relative_error':float(abs(bos+ferm-expected)/max(expected,1)),
                 'spin_compression_first_jet_norm':float(np.linalg.norm(dspin))})

# Exact sparse supersymmetric oscillator algebra, two modes per root edge.
M=6
vac=(tuple([0]*M),tuple([0]*M))
def state(bo=(),fe=()):
    b=[0]*M;f=[0]*M
    for j in bo:b[j]+=1
    for j in fe:f[j]=1
    return tuple(b),tuple(f)
def add(out,s,c):out[s]=out.get(s,0)+c

def q_apply(v,r):
    out={}
    for (b,f),c in v.items():
        for j in range(M):
            pre=(-1)**sum(f[:j]);scale=math.sqrt(2*r[j//2])
            if f[j]:
                bb=list(b);ff=list(f);bb[j]+=1;ff[j]=0
                add(out,(tuple(bb),tuple(ff)),c*pre*scale*math.sqrt(b[j]+1))
            elif b[j]:
                bb=list(b);ff=list(f);bb[j]-=1;ff[j]=1
                add(out,(tuple(bb),tuple(ff)),c*pre*scale*math.sqrt(b[j]))
    return {s:c for s,c in out.items() if abs(c)>1e-20}
def energy(s,r):
    b,f=s;return 2*sum(r[j//2]*(b[j]+f[j]) for j in range(M))
def h_inv(v,r):
    assert vac not in v
    return {s:c/energy(s,r) for s,c in v.items()}
def inner(v,w):return sum(np.conj(c)*w.get(s,0) for s,c in v.items())
def diffnorm(v,w):return math.sqrt(sum(abs(v.get(s,0)-w.get(s,0))**2 for s in v.keys()|w.keys()))

focks=[]
for r in [(1.,1.3,1.7),(1.,1e3,1e3+.2),(1.,1e9,1e9+.2)]:
    graphs=[]
    for e in range(3):
        graphs.append({state((2*e,2*e)):1+.2j,state((),(2*e,2*e+1)):.3-.4j})
    graphs.append({state((0,2),(4,)):.7-.2j,state((),(0,2,4)):.5+.1j,state((0,4),(2,)):-.4+.3j})
    ee=[4*x for x in r]+[2*sum(r)]
    err_e=max(abs(energy(s,r)-ee[g])/max(ee[g],1) for g,v in enumerate(graphs) for s in v)
    source={}
    for v in graphs:
        for s,c in v.items():add(source,s,c)
    qb=q_apply(source,r);back=q_apply(h_inv(qb,r),r)
    z={s:-c for s,c in h_inv(qb,r).items()}
    predicted=sum(inner(v,v).real/e for v,e in zip(graphs,ee))
    focks.append({'r':r,'graph_energy_error':float(err_e),
        'homological_inverse_error':float(diffnorm(source,back)/math.sqrt(inner(source,source).real)),
        'dressing_norm_identity_error':float(abs(inner(z,z).real-predicted)/max(predicted,1)),
        'gram_cancellation_error':float(abs(inner(qb,h_inv(qb,r))-inner(source,source))/max(inner(source,source).real,1))})

weights=[]
for ratio in [1,3,1e3,1e6,1e9,1e12]:
    points=np.array([[0.,0.],[1.,0.],[ratio,.7]])
    rr=np.array([np.linalg.norm(points[0]-points[1]),np.linalg.norm(points[1]-points[2]),np.linalg.norm(points[2]-points[0])])
    s=rr.sum();w=(rr**-2).sum()
    maxorb=0.
    for e in range(3):
        for f in range(3):
            if e==f:continue
            g=3-e-f
            lhs=math.sqrt(rr[f]/rr[e])/rr[g]
            rhs=1.5/rr[g]+.5/rr[e]
            maxorb=max(maxorb,lhs/rhs)
    # Allowed alpha at the far vertex touches edges 1 and 2 only.
    kappa=.002;alpha=kappa*min(rr[1:]);m=w/s
    active=(rr**-1).sum()**2*w/s
    weights.append({'ratio':ratio,'r':rr.tolist(),'orbital_weight_ratio':maxorb,
       'far_vertex_yukawa_ratio':alpha*m/(kappa*w),
       'active_derivative_to_W5_ratio':active/(rr**-5).sum(),
       'coarse_wrong_far_alpha_rmin_minus3':float(alpha/min(rr)**3)})
# Explicit spectator correction: active scale M, unrelated spectator scale 1.
spectator={'active_r':1e6,'spectator_r':1.,'m_g':1e-18,'active_d_g':1e-30,
           'spectator_derivative_weight':1e-18,'omitted_term_to_active_derivative':1e12}

out={'vacuum_jets':jets,'sparse_fock_checks':focks,'hierarchical_weights':weights,'spectator_negative_control':spectator,
     'scope':'Finite regressions of vacuum jets, oscillator denominators and graph weights; not the missing full BFSS nonzero-internal H1/H2 inventory.'}
assert max(x['vacuum_metric_relative_error'] for x in jets)<1e-7
assert max(x['spin_compression_first_jet_norm'] for x in jets)<1e-6
assert max(x['homological_inverse_error'] for x in focks)<1e-12
assert max(x['orbital_weight_ratio'] for x in weights)<=1+1e-12
assert max(x['far_vertex_yukawa_ratio'] for x in weights)<=1+1e-12
(ROOT/'multiblock_root_source_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
