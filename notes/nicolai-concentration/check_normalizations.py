import sympy as s
u,t,N,w=s.symbols('u t N w', real=True)
A=s.Matrix([[0,1],[1,0]])/s.sqrt(2)
B=s.Matrix([[0,-s.I],[s.I,0]])/s.sqrt(2)
X,Y=(t+u)*A,(t-u)*B
C=X*Y-Y*X
V=s.simplify(-N*s.trace(C*C)/2)
Vm=s.simplify(N*w*w*s.trace(X*X+Y*Y)/2)
assert s.trace(A*A)==s.trace(B*B)==1
assert s.simplify(V-N*(t*t-u*u)**2)==0
assert s.simplify(s.diff(V,u,2).subs(u,0)+4*N*t*t)==0
assert s.simplify(s.diff(V+Vm,u,2).subs(u,0)/2-N*(w*w-2*t*t))==0
beta=s.symbols('beta', positive=True)
mid=s.sinh(w*beta/2)**2/(w*s.sinh(w*beta))
assert s.simplify((mid-s.tanh(w*beta/2)/(2*w)).rewrite(s.exp))==0
print('PASS: Pauli slice, mass curvature, Dirichlet massive midpoint covariance')
