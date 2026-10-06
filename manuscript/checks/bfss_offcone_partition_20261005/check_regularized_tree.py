import itertools,json
from pathlib import Path
import numpy as np
rng=np.random.default_rng(5102026)
kappa=.05; L=3.; delta=kappa*np.exp(-L)
def angle(X,B):
 n=len(X);ids=np.array(sorted(B));outs=np.array([j for j in range(n) if j not in B]);c=X[ids].mean(0);dev=X[ids]-c;a=np.linalg.norm(dev)
 if a==0:return 0.,np.zeros_like(X)
 out=X[outs]-c;q=np.sum(out*out,axis=1)+a*a;F=np.sum(1/q);d=F**-.5;t=np.log(a/(delta*d))/L
 if t<=0:return 0.,np.zeros_like(X)
 if t>=1:return np.pi/2,np.zeros_like(X)
 # C2 rather than C-infinity profile is sufficient for this finite regression.
 th=np.pi/2*(6*t**5-15*t**4+10*t**3);dth=np.pi/2*30*t*t*(t-1)**2
 ga=np.zeros_like(X);ga[ids]=dev/a
 gd=d**3*a*np.sum(q**-2)*ga
 gd[outs]+=d**3*out/q[:,None]**2;gd[ids]-=np.sum(d**3*out/q[:,None]**2,axis=0)/len(ids)
 return th,dth/L*(ga/a-gd/d)
def partitions(n):
 def rec(i,bs):
  if i==n:
   if len(bs)>=2:yield tuple(frozenset(b) for b in bs)
   return
  for j in range(len(bs)):
   bs[j].append(i);yield from rec(i+1,bs);bs[j].pop()
  bs.append([i]);yield from rec(i+1,bs);bs.pop()
 yield from rec(0,[])
def symmetric(X,bs,ang):
 factors=[];E=0.
 keys=[(B,True) for B in bs if len(B)>=2]
 for k in range(2,len(bs)):
  for S in itertools.combinations(bs,k):keys.append((frozenset().union(*S),False))
 w=1.;dw=np.zeros_like(X)
 for B,select in keys:
  th,g=ang[B];E+=np.sum(g*g)
  if select:f=0. if th>=np.pi/2 else np.cos(th);df=-np.sin(th)*g
  else:f=0. if th<=0 else np.sin(th);df=np.cos(th)*g
  dw=dw*f+w*df;w*=f
 return w,dw,E

def check(X):
 X=X-X.mean(0);n=len(X);subs=[frozenset(B) for m in range(n-1,1,-1) for B in itertools.combinations(range(n),m)];ang={B:angle(X,B) for B in subs};tree={}
 def recurse(i,sel,w,dw,E):
  if w==0. and not np.any(dw):return
  if i==len(subs):
   bs=sel+[frozenset([j]) for j in range(n) if not any(j in B for B in sel)];key=tuple(sorted(tuple(sorted(B)) for B in bs));tree[key]=(w,dw,E);return
  B=subs[i]
  if any(B&C for C in sel):return recurse(i+1,sel,w,dw,E)
  th,g=ang[B];c=0. if th>=np.pi/2 else np.cos(th);s=0. if th<=0 else np.sin(th);e=np.sum(g*g)
  recurse(i+1,sel+[B],w*c,dw*c-w*s*g,E+e);recurse(i+1,sel,w*s,dw*s+w*c*g,E+e)
 recurse(0,[],1.,np.zeros_like(X),0.)
 ws=[];direct=payable=0.;wdiff=gdiff=0.
 for bs in partitions(n):
  w,g,e=symmetric(X,bs,ang);ws.append(w);direct+=np.sum(g*g);payable+=w*w*e
  key=tuple(sorted(tuple(sorted(B)) for B in bs));tw,tg,te=tree.get(key,(0.,np.zeros_like(X),0.));wdiff=max(wdiff,abs(w-tw));gdiff=max(gdiff,np.linalg.norm(g-tg))
 return {'N':n,'nonzero_leaves':int(sum(w!=0 for w in ws)),'partition_error':abs(np.dot(ws,ws)-1),'IMS_error':abs(direct-payable),'IMS_relative_error':abs(direct-payable)/max(1,direct,payable),'tree_weight_error':wdiff,'tree_gradient_error':gdiff}
cases=[]
# Two simultaneous pairs, then nested pair-in-triple, then a repeated eigenvalue.
for coordinates in [ [[-10,-.1],[-10,.1],[10,-.1],[10,.1]], [[-10,0],[-10,.001],[-9.9,0],[10,0]], [[-10,0],[-10,0],[10,-.1],[10,.1]], [[-10,-.1],[-10,.1],[10,-.1],[10,.1],[0,15]] ]:
 X=np.zeros((len(coordinates),9));X[:,:2]=coordinates;cases.append(check(X))
for n in range(2,9):
 for j in range(8):
  X=rng.normal(size=(n,9))
  if n>=3:X[:2]=X[0]+rng.normal(size=(2,9))*10**rng.uniform(-5,-.8)
  if n>=4 and j%2==0:X[2:4]=X[2]+rng.normal(size=(2,9))*10**rng.uniform(-5,-.8)
  cases.append(check(X))
out={'cases':len(cases),'parameters':{'kappa':kappa,'L':L},'max_partition_error':max(c['partition_error'] for c in cases),'max_relative_IMS_error':max(c['IMS_relative_error'] for c in cases),'max_tree_weight_error':max(c['tree_weight_error'] for c in cases),'max_tree_gradient_error':max(c['tree_gradient_error'] for c in cases),'structured_cases':cases[:4]}
assert out['max_partition_error']<1e-12
assert out['max_relative_IMS_error']<1e-10
assert out['max_tree_gradient_error']<1e-8
print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
