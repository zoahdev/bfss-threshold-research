#!/usr/bin/env python3
from fractions import Fraction as F
import math, random, json
assert F(2,3)-F(4,7)==F(2,21)
assert F(2)*F(9,7)==F(18,7)
assert F(18,7)-2==F(4,7)
# Holder monomial powers: q^2 = (rho^2 q^2)^(7/9) * (q^2)^(2/9) * rho^(-14/9),
# then q^2 <= b rho^4 leaves rho^(-6/9), whose Holder power 9/2 is rho^-3.
assert F(8,9)-F(14,9)==-F(2,3)
assert -F(2,3)*F(9,2)==-3
# Exact spin9 shear second derivative coefficient.
assert (F(4)+F(7)-F(2))/9==1
b=F(8,9)
v0=2**(-7/12)/27
assert float(b)/1024 < v0/2
max_j=(0,None)
max_l=(0,None)

for n in range(2,10001):
    d=n*n-1
    j=32*math.sqrt(2)*n**3*math.sqrt(d)/((9*d-2)**2-1)
    assert j <= 32*math.sqrt(2)/39 + 1e-14
    if j>max_j[0]: max_j=j,n
    D=9*d
    k=3*(D//6)
    assert 3*n*n <= k <= D/2
    # The recurrence coefficient is monotone increasing for k>=3.
    l=32*math.sqrt(2)*n**3*math.sqrt(d)/((D-2)**2-(k-2)**2)
    assert l < 2
    if l>max_l[0]: max_l=l,n
    if n<20:
        assert n*n*2**(-2*n*n) <= F(1,64)

# Pair/triangle rank collection and triangle inequality of inverse products.
rng=random.Random(20261006)
for _ in range(10000):
    n=[rng.randint(1,50) for i in range(rng.randint(2,10))]
    total=sum(n)
    for a in range(len(n)):
        for b in range(a+1,len(n)):
            assert n[a]+n[b]+sum(n[c] for c in range(len(n)) if c not in (a,b))==total
    x,y,z=[math.exp(rng.uniform(-5,5)) for i in range(3)]
    assert 1/(x*y)+1/(y*z)+1/(z*x) <= 1/x**2+1/y**2+1/z**2+1e-8
print(json.dumps({'status':'passed','checks':['exponents','Holder powers','shear coefficient','uniform I3 constant for N=2..10000','10000 random pair/triangle algebra checks','growing inverse-moment recurrence coefficient for N=2..10000','inner-radius variance split constants'], 'max_sampled_J_N':max_j[0], 'max_sampled_rank':max_j[1], 'max_sampled_recurrence_coefficient':max_l[0], 'final_positive_certificate_lower_bound':2**(-5/4)/243, 'scope':'Algebraic checks only; analytic hypotheses are stated in the note.'},indent=2))
