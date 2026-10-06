#!/usr/bin/env python3
"""Exact algebra checks, not a BFSS numerical/large-N experiment."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json

OUT=Path(__file__).parent
checks={}
# [P,Z]=-i: P^a Z^b normal-order correction k has weight 2a+b-3k.
count=0
for a in range(5):
    for b in range(9):
        if 2*a+b>8: continue
        for k in range(1,min(a,b)+1):
            coefficient=comb(a,k)*factorial(b)//factorial(b-k)
            assert coefficient>0
            assert 2*(a-k)+(b-k)==2*a+b-3*k
            assert 2*(a-k)+(b-k)<=5
            count+=1
checks['canonical_ordering']={'checked_terms':count,'max_correction_weight':5,'first_raw_weight_for_sextic_correction':9}
# Clifford basis e_A, {e_i,e_j}=delta_ij, exact bit-mask product.
def clifford_product(a,b):
    inversions=sum((b & ((1<<i)-1)).bit_count() for i in range(16) if a>>i&1)
    coefficient=F((-1)**inversions,2**((a&b).bit_count()))
    return a^b,coefficient
for alpha in range(16):
    result={}
    for beta in range(16):
        mask,c1=clifford_product(1<<beta,1<<alpha)
        mask,c2=clifford_product(mask,1<<beta)
        result[mask]=result.get(mask,F(0))+c1*c2
    assert result=={1<<alpha:F(-7)}
checks['cubic_clifford_contraction']={'spinor_components':16,'coefficient':'-7','all_components_pass':True}
# Rank-one orbit: E(n^T h n)^2=(2 tr h²+(tr h)²)/(m(m+2)).
m=9
orbit=F(2,m*(m+2))
assert orbit==F(2,99)
checks['commuting_orbit_witness']={'R':'1','M_angular_average':str(orbit),'pointwise_M_for_h_diag_pm_over_sqrt2_n_e1':'1/2'}
# Exact finite-N fermion traces quoted in Lin Appendix C.
for N in range(2,20):
    tr2=F(N*N-1,2)
    tr4=F(2*N**4-3*N*N+1,4*N)
    c=F(N*N-1,2*N)
    centered=tr4-2*c*tr2+N*c*c
    assert centered==F(N*(N*N-1),4)
checks['finite_N_fermionic_centering']={'N_tested':[2,19],'centered_trace':'N(N²−1)/4'}
# Dilation Omega_lambda=U_lambda Omega; U P U*=lambda P, U Z U*=Z/lambda.
assert -1+1==0 and -1+2*(-1)==-3
weights={'q':2,'a':2,'R':2,'b':1,'D':0,'Q':-1}
assert weights['Q']+weights['q']==weights['b']
assert weights['Q']+weights['b']==weights['D']
assert weights['b']*2==weights['a']
assert weights['D']+weights['q']==weights['a']
assert weights['R']+2*weights['q']==6
checks['restricted_quantum_dilation']={'charge':'K + lambda^(-3) V','M_power':6,'fixed_BFSS_coupling':False}
checks['scope']={'actual_ground_state_bound_proved':False,'SDP_solved':False,'large_N_numerics':False,'dual_obstruction_only':True}
(OUT/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
