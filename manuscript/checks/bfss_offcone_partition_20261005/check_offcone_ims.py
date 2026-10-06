"""Finite branch regression; finite differences validate, rather than prove, IMS transport."""
import json,itertools
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.optimize import root
rng=np.random.default_rng(1051026)
N=4; spatial=3;kappa=.05;L=3.;delta=kappa*np.exp(-L)
parts=[((0,1),(2,3)),((0,1),(2,),(3,)),((0,),(1,),(2,3)),((0,),(1,),(2,),(3,))]
# Orthogonal trace-free ambient Hermitian coordinates.
basis=[]
for p in range(N):
 for q in range(p+1,N):
  H=np.zeros((N,N),complex);H[p,q]=H[q,p]=1/np.sqrt(2);basis.append(H)
  H=np.zeros((N,N),complex);H[p,q]=1j/np.sqrt(2);H[q,p]=-1j/np.sqrt(2);basis.append(H)
for q in range(1,N):
 H=np.diag([1.]*q+[-q]+[0.]*(N-q-1))/np.sqrt(q*(q+1));basis.append(H.astype(complex))
basis=np.array(basis)

def theta(a,d):
 if a==0:return 0.
 z=np.log(a/(delta*d))/L
 if z<=0:return 0.
 if z>=1:return np.pi/2
 return np.pi/2*(6*z**5-15*z**4+10*z**3)

def branch_setup(bs):
 group={p:a for a,B in enumerate(bs) for p in B};pairs=[(p,q) for p in range(N) for q in range(p+1,N) if group[p]!=group[q]];Hs=[]
 for p,q in pairs:
  H=np.zeros((N,N),complex);H[p,q]=H[q,p]=1/np.sqrt(2);Hs.append(H)
  H=np.zeros((N,N),complex);H[p,q]=1j/np.sqrt(2);H[q,p]=-1j/np.sqrt(2);Hs.append(H)
 return pairs,np.array(Hs)
setups=[branch_setup(bs) for bs in parts]
def branch(X,j,start=None):
 bs=parts[j];pairs,Hs=setups[j];k=len(bs)
 def convert(v):
  U=expm(1j*np.einsum('a,aij->ij',v,Hs));T=np.einsum('ab,ibc,cd->iad',U.conj().T,X,U);z=np.array([[np.trace(Ti[np.ix_(B,B)]).real/len(B) for Ti in T] for B in bs]);return T,z
 def residual(v):
  T,z=convert(v);out=[]
  g={p:a for a,B in enumerate(bs) for p in B}
  for p,q in pairs:
   a=g[p];b=g[q];c=np.dot(z[a]-z[b],T[:,p,q]);out.extend([c.real,c.imag])
  return np.array(out)
 v0=np.zeros(len(Hs)) if start is None else start
 sol=root(residual,v0,tol=1e-10)
 err=np.linalg.norm(residual(sol.x))
 if err>1e-8:raise RuntimeError((j,sol.message,err))
 T,z=convert(sol.x);A=[T[:,B,:][:,:,B]-z[a,:,None,None]*np.eye(len(B))[None] for a,B in enumerate(bs)];alpha=np.array([np.vdot(aa,aa).real for aa in A]);ns=np.array([len(B) for B in bs]);angles=[];select=[]
 nodes=[(tuple([a]),True) for a,B in enumerate(bs) if len(B)>=2]
 nodes +=[(I,False) for m in range(2,k) for I in itertools.combinations(range(k),m)]
 for I,sel in nodes:
  I=list(I);center=np.sum(ns[I,None]*z[I],axis=0)/sum(ns[I]);a2=sum(alpha[I])+np.sum(ns[I]*np.sum((z[I]-center)**2,axis=1));a=np.sqrt(max(0,a2));F=0.
  for b in range(k):
   if b in I:continue
   Q=A[b]+(z[b]-center)[:,None,None]*np.eye(ns[b])[None];H=np.einsum('iab,ibc->ac',Q,Q)+a2*np.eye(ns[b]);F+=np.trace(np.linalg.inv(H)).real
  angles.append(theta(a,F**-.5));select.append(sel)
 vals=[(0. if a>=np.pi/2 else np.cos(a)) if s else (0. if a<=0 else np.sin(a)) for a,s in zip(angles,select)]
 return float(np.prod(vals)),np.array(angles),sol.x,err

def check(X,step=2e-7):
 base=[branch(X,j) for j in range(4)];q=np.array([b[0] for b in base]);dq=[];dangles=[[] for j in range(4)];maxroot=max(b[3] for b in base)
 for i in range(spatial):
  for H in basis:
   D=np.zeros_like(X);D[i]=step*H;column=[]
   for j in range(4):
    p=branch(X+D,j,base[j][2]);m=branch(X-D,j,base[j][2]);column.append((p[0]-m[0])/(2*step));dangles[j].append((p[1]-m[1])/(2*step));maxroot=max(maxroot,p[3],m[3])
   dq.append(column)
 dq=np.array(dq).T;Q=np.dot(q,q);dQ=2*q@dq;E=np.sum(dq*dq)/Q-np.dot(dQ,dQ)/(4*Q*Q);Ej=np.array([np.sum(np.array(da)**2) for da in dangles]);R=np.dot(q*q,Ej)/Q
 B=sum(np.linalg.norm(X[i]@X[j]-X[j]@X[i])**2 for i in range(spatial) for j in range(i+1,spatial));rho=np.linalg.norm(X)
 return {'Q':float(Q),'E':float(E),'R':float(R),'scaled_defect':float((E-R)*rho*rho),'t':float(B/rho**4),'max_stationarity_residual':float(maxroot),'weights':list(q/np.sqrt(Q))}
X0=np.zeros((spatial,N,N),complex);X0[0]=np.diag([-1,-1,1,1]);X0[1]=np.diag([-.006,.006,-.006,.006]);pert=np.einsum('ia,ajk->ijk',rng.normal(size=(spatial,len(basis))),basis);pert/=np.linalg.norm(pert)
out=[]
for tau in [0.,2e-5,1e-5,5e-6]:
 result=check(X0+tau*pert);result['perturbation_norm']=tau;out.append(result);print(json.dumps(result),flush=True)
report={'scope':'Four active unordered branches near a simultaneous 2+2 commuting transition; omitted partitions have constant zero weights locally. Finite difference and root errors prevent interpreting tiny defects as exact.','parameters':{'N':N,'spatial_dimensions':spatial,'kappa':kappa,'L':L,'finite_difference_step':2e-7},'cases':out}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
