#!/usr/bin/env python3
"""Finite algebra checks for the accompanying analytical note.
These checks do not establish BFSS existence or rank-uniform tail bounds.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import json
import random

checks = []
def passed(name):
    checks.append(name)
    print('PASS:', name)

# Exact coefficient in the isotropic mass expectation and singlet leakage.
c = F(1,2)*(F(1,9)*F(1,3)+F(1,36)*F(2,3))
assert c == F(1,36)
assert c/F(1,3) == F(1,12)
assert 2*c/F(1,3) == F(1,6)
passed('isotropic mass coefficient 1/36; singlet leakage 1/12; squared distance 1/6')

# Representation proof has three branches, with analytical minima.
assert min(F(2*a5+4,12) for a5 in range(1,20)) == F(1,2)
assert F(4,12) == F(1,3)
assert min(F(b,12) for b in range(1,20)) == F(1,12)
passed('lowest-weight lower bounds in the three unitary branches')

# Exhaust all discrete low-branch labels that can occur below singlet threshold.
# k=0 requires the base to be a singlet; even k is required by the SU(2) center.
# k=2 cannot have SU(4) center charge zero for either raising convention.
low_candidates = []
for a1,a2,a3 in product(range(4),repeat=3):
    b=a1+2*a2+3*a3
    if not (0 < b < 4):
        continue
    for k in range(9):
        if b+k >= 4 or k%2:
            continue
        low_candidates.append((a1,a2,a3,b,k))
        if k==0:
            assert (a1,a2,a3)!=(0,0,0)
        else:
            assert k==2 and b==1
            assert (b+k)%4 !=0 and (b-k)%4 !=0
passed('all potentially singlet descendants below m/3 excluded, including both SU(4) conventions')

# Normalization of the projected branch.
for i in range(10000):
    e=i/10000
    d2=2*(1-sqrt(1-e))
    assert d2 <=2*e+1e-14
    assert abs(d2-2*e/(1+sqrt(1-e)))<1e-13
passed('exact normalized projection distance and bound by twice leakage')

# Interpolation and rank exponents.
for k in (2,3):
    for p in (F(13,2),F(7),F(8),F(17,2),F(89,10)):
        if p<=2*k:
            continue
        alpha=2+4*p/(3*(p-2*k))
        assert (alpha-2)*(1-2*k/p)==F(4,3)
assert 2+4*F(9)/(3*(F(9)-6))==6
assert 2+4*F(9)/(3*(F(9)-4))==F(22,5)
assert F(2,3)-2 == -F(4,3)
assert 2-F(2,3) == F(4,3)
passed('weighted and unweighted mass exponents; incompatible certified mass windows')

# Weighted Holder on finite vectors, a consistency check of exponents.
rng=random.Random(20261006)
for k,p in ((2,7),(2,8),(3,7),(3,8)):
    for _ in range(200):
        radii=[10**rng.uniform(-2,2) for _ in range(20)]
        d=[rng.uniform(-1,1) for _ in radii]
        d0=sum(z*z for z in d)
        dp=sum(r**p*z*z for r,z in zip(radii,d))
        dk=sum(r**(2*k)*z*z for r,z in zip(radii,d))
        assert dk <= d0**(1-2*k/p)*dp**(2*k/p)*(1+1e-12)
passed('weighted Holder inequality with degree-four and degree-six squared observables')

# Exact abstract counterexample along m=j^-2.
example=[]
for j in (2,4,8,16,32,64):
    m=F(1,j*j)
    eigen=F(1,j*j)+m*m*j*j
    assert eigen == 2*m
    rayleigh=eigen*m
    assert rayleigh==2*m*m
    p2=1-m+m*j*j
    p6=1-m+m*j**6
    assert p2==2-m
    assert p6==1-m+m**(-2)
    endpoint_weight=m**3
    assert eigen*endpoint_weight==2*m**4
    assert 1-endpoint_weight+endpoint_weight*j**6==2-m**3
    assert endpoint_weight*j**6==1
    # Positive diagonal gap follows from (1/k - m*k)^2>=0.
    for k in range(1,4*j):
        assert F(1,k*k)+m*m*k*k-2*m == (F(1,k)-m*k)**2
    example.append({'j':j,'m':float(m),'Rayleigh':float(rayleigh),
                    'R2':float(p2),'R6':float(p6),'projection_norm_error':sqrt(float(m))})
passed('compact-regulator model has gap 2m and Rayleigh error 2m^2 but diverging sixth moment')

print('\nLOW-ENERGY LABEL CHECK:', low_candidates)
print('\nCOUNTEREXAMPLE:',json.dumps(example,indent=2))
print('\nALL',len(checks),'FINITE CHECKS PASSED')
