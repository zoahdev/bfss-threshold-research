#!/usr/bin/env python3
import numpy as np, itertools, json
from pathlib import Path
I=np.eye(2,dtype=np.int64); X=np.array([[0,1],[1,0]],dtype=np.int64); Z=np.diag([1,-1]); J=np.array([[0,1],[-1,0]],dtype=np.int64)
pauli=[I,X,Z,J]
strings=[x for x in itertools.product(range(4),repeat=4) if x.count(3)%2==0 and any(x)]
def anti(a,b): return sum(bool(x!=y and x and y) for x,y in zip(a,b))%2==1
# All Pauli strings with even J are real symmetric involutions.
def clique(cur,candidates):
 if len(cur)==9:return cur
 if len(cur)+len(candidates)<9:return None
 for t,a in enumerate(candidates):
  ans=clique(cur+[a],[b for b in candidates[t+1:] if anti(a,b)])
  if ans:return ans
 return None
chosen=clique([],strings)
def kron(s):
 v=np.array([[1]],dtype=np.int64)
 for c in s:v=np.kron(v,pauli[c])
 return v
G=[kron(s) for s in chosen]; eye=np.eye(16,dtype=np.int64)
for i in range(9):
 assert np.array_equal(G[i].T,G[i]);assert np.array_equal(G[i]@G[i],eye)
 for j in range(i):assert not np.any(G[i]@G[j]+G[j]@G[i])
E={k:[np.linalg.multi_dot([G[i] for i in c]) if k>2 else G[c[0]]@G[c[1]] for c in itertools.combinations(range(9),k)] for k in [2,3]}
checks={'gamma_pauli_strings':chosen,'clifford_relations':True}
for k,mats in E.items():
 arr=np.stack(mats)
 assert np.array_equal(np.einsum('iab,jab->ij',arr,arr),16*np.eye(len(mats),dtype=np.int64))
 assert np.array_equal(arr.transpose(0,2,1),-arr)
 bianchi=np.einsum('iab,icd->abcd',arr,arr)-np.einsum('iac,ibd->abcd',arr,arr)+np.einsum('iad,ibc->abcd',arr,arr)
 assert not np.any(bianchi),np.max(np.abs(bianchi))
 checks[f'gamma_{k}']={'dimension':len(mats),'norm_squared':16,'orthogonal':True,'fully_antisymmetric_four_spinor_tensor_vanishes':True}
# Diagonal h projection of sum_i h_i Gamma_i E Gamma_i.
h=np.arange(9,dtype=np.int64)-4
for k,mats in E.items():
 for inds,e in zip(itertools.combinations(range(9),k),mats):
  lhs=sum(h[i]*(G[i]@e@G[i]) for i in range(9))
  rhs=(-2 if k==2 else 2)*sum(h[i] for i in inds)*e
  assert np.array_equal(lhs,rhs)
checks['traceless_diagonal_h_fermion_projections']=True
from fractions import Fraction as F
# Exact Clifford bitmasks with {b_a,b_b}=delta_ab.
def cp(a,b):
 inv=sum((b & ((1<<i)-1)).bit_count() for i in range(16) if a>>i&1)
 return a^b,F((-1)**inv,2**((a&b).bit_count()))
for k,mats in E.items():
 total={}
 for e in mats:
  # K=(1/16)sum_ab E_ab b_a b_b, and F=-i K.
  terms={ (1<<a)|(1<<b):F(int(e[a,b]),8) for a in range(16) for b in range(a+1,16) if e[a,b]}
  for ma,ca in terms.items():
   for mb,cb in terms.items():
    mask,c=cp(ma,mb);total[mask]=total.get(mask,F(0))-ca*cb*c
 total={key:v for key,v in total.items() if v}
 assert total=={0:F(len(mats),32)},total
 checks[f'fermion_square_sum_{k}']=str(total[0])
# Isotropic h on the unit sphere in 44-dimensional traceless Sym(9).
# Gaussian h has covariance P_ij,kl=(delta_ik delta_jl+delta_il delta_jk)/2-delta_ij delta_kl/9.
# Divide its fourth moment by 44*46 for the unit-sphere fourth moment.
q6=np.diag([4]*3+[-2]*6)
T3=list(itertools.combinations(range(9),3))
K11=np.zeros((16,16),dtype=np.int64)
active=0
for inds,e in zip(T3,E[3]):
 r6=np.zeros((9,9),dtype=np.int64)
 if inds==(0,1,2):r6=q6.copy()
 elif inds[:2]==(0,1):r6[inds[2],2]=r6[2,inds[2]]=3
 elif inds[:2]==(0,2):r6[inds[2],1]=r6[1,inds[2]]=-3
 elif inds[:2]==(1,2):r6[inds[2],0]=r6[0,inds[2]]=3
 else:continue
 active+=1
 trace=int(np.sum(q6*r6))
 for m in range(9):
  for n in range(9):
   # Color A=B=0. All weights share denominator 648.
   P18=9*(int(m==n)+int(m==0 and n==0))-2*int(m==0 and n==0)
   weight=trace*P18+18*(q6[m,0]*r6[n,0]+q6[n,0]*r6[m,0])
   if weight:K11+=weight*(G[m]@e@G[n])
assert np.array_equal(K11,1728*E[3][T3.index((0,1,2))])
checks['polarization_average_interaction']={
 'configuration':'Z_1=T_1, Z_2=T_2, Z_3=T_3 in an embedded SU(2), other Z_i=0; Tr(T_a T_b)=delta_ab',
 'active_three_form_channels':active,
 'gaussian_K11_Gamma123_coefficient':str(F(1728,648)),
 'unit_polarization_K11_Gamma123_coefficient':str(F(1728,648*44*46)),
 'nonzero':True,
 'not_a_quantum_state':True}
checks['scope']={'actual_BFSS_ground_state_bound_proved':False,'polarization_interference_cancels_identically':False,'numerical_ground_state_experiment':False}
print(json.dumps(checks,indent=2))
Path(__file__).with_name('checks.json').write_text(json.dumps(checks,indent=2)+'\n')
