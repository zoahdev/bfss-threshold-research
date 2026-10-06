#!/usr/bin/env python3
"""Exact scalar checks; not certification of analytical/domain arguments.
SPDX-License-Identifier: MIT
"""
from fractions import Fraction as F
import json
from pathlib import Path

h0, angular, hstar = F(49,4), F(18), F(121,4)
assert h0 + angular == hstar
assert (F(5,7) + F(2,7))/16 == F(1,16)
assert F(2,7)/16 == F(1,56)
assert F(1,2)*16*F(1,16)**2 == F(1,32)
assert F(1,2)*16*F(1,56)**2 == F(1,392)
assert 8*F(1,32) + 28*F(1,392) == F(9,28)
# Square of factor 2 sqrt(8) / sqrt(32) in the expectation estimate.
assert 4*8*F(1,32) == 1
# Reciprocal primitive rescaling when Q=sqrt(2)q: A=a/sqrt(2).
assert F(1,32)/2 == F(1,64)
assert F(9,28)/2 == F(9,56)
assert 4*16*F(1,64) == 1
beta=F(1,12)
width_checks=[]
for n1 in range(1,51):
    for n2 in range(1,51):
        ell2=F(1,n1)+F(1,n2)
        coeff=1/(4*beta**2*ell2)
        assert coeff >= angular
        width_checks.append(coeff)
assert min(width_checks)==angular
assert F((18-2)**2,4)==64 > hstar
margin_checks=[]
for c in [F(1), F(12), F(25), F(30), hstar-F(1,10**6)]:
    a=min(F(1,24),(hstar-c)/(4*(3*hstar+2)))
    lower=(1-3*a)*hstar-2*a
    assert lower > c and a<F(1,12)
    margin_checks.append({'c':str(c),'a':str(a),'paid_lower':str(lower),'margin':str(lower-c)})
for m in [F(0),F(4),F(5),F(8),F(9)-F(1,10**6)]:
    p=m/2+1
    assert p*p<hstar
assert (F(9)/2+1)**2 == hstar
out={
    'status':'passed',
    'primitive_fixed_generator_charge_sum_bound':'alpha^2 / 32',
    'fixed_rotation_generator_count':1,
    'charge_count':16,
    'primitive_all_36_generators_charge_sum_identity':'9 alpha^2 / 28',
    'charge_normalization':'{q_alpha,q_beta}=delta_alpha,beta h; sum||q g||^2=8h[g]',
    'baseline_rescaling':'Q=sqrt(2)q; A=a/sqrt(2); sum||Q g||^2=16h[g]',
    'rescaled_fixed_generator_charge_sum_bound':'alpha^2 / 64',
    'rescaled_all_36_generators_charge_sum_identity':'9 alpha^2 / 56',
    'nonsinglet_ball_constant':'1/4',
    'two_block_padded_width_max':'1/12',
    'partitions_checked':len(width_checks),
    'smallest_angular_payment':str(min(width_checks)),
    'radial_hardy_9d':str(h0),
    'singlet_slow_hardy':str(hstar),
    'center_hardy_18d':'64',
    'margin_checks':margin_checks,
    'moment_range':'0 <= m < 9',
    'endpoint_m9':'not established',
    'scope':'Exact scalar arithmetic only; not proof of BFSS local estimates, domains, symmetry, or gluing.'
}
Path(__file__).with_name('sharp_singlet_budget_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
