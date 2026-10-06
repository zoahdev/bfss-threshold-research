#!/usr/bin/env python3
"""Exact rational checks of the assembled scalar budget, not the BFSS proof.

Only elementary constants/mass-metric identities are tested here. The analytic
source, domain, geometry, and form estimates remain mathematical dependencies.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

H0=F(49,4)

def partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for first in range(minimum,n+1):
            for tail in partitions(n-first,first):
                yield (first,)+tail

rows=[]
number=0
for n in range(2,21):
    worst=F(0)
    arg=None
    for pi in partitions(n):
        k=len(pi)
        if k<2:
            continue
        number+=1
        D=9*(k-1)
        hardy=F((D-2)**2,4)
        assert hardy>=H0
        nu=[F(1,a)+F(1,b) for a,b in combinations(pi,2)]
        K=sum((1/x for x in nu),F(0))/H0
        assert K<=F(n*k*(k-1),98) # each inverse nu <= N/4
        if K>worst:
            worst,arg=K,pi
        # Physical radius comparison used in the proof is r_ab² <= nu s².
        assert all(x<=2 for x in nu)
    rows.append({'N':n,'max_K':str(worst),'partition':arg})

budgets=[]
for c in (F(1,1000),F(1),F(9),F(10),H0-F(1,10),H0-F(1,10**6)):
    # Strictly below both bounds in Section 8.
    a=min(F(1,24),(H0-c)/(16*(H0+1)))
    coefficient=(1-2*a)*H0-2*a
    assert a<F(1,12)
    assert a<(H0-c)/(8*(H0+1))
    assert 1-3*a>0
    assert coefficient>c
    # Reserve cost is one quarter plus two eighths.
    reserve_remaining=1-F(1,4)-F(1,8)-F(1,8)
    assert reserve_remaining==F(1,2)
    for row in rows:
        K=F(row['max_K'])
        epsilon=a/(1+K)
        assert 1-epsilon>=1-a
        assert 1-epsilon-epsilon*K==1-a
    budgets.append({'c':str(c),'a':str(a),'retained_hardy':str(coefficient),
                    'strict_margin':str(coefficient-c)})

# Pair mass-coordinate identity: b=z_a-z_b and canonical xi=b/sqrt(nu).
# The coefficient of -Delta_b is nu, so Hardy is H0*nu/r_ab².
for na in range(1,21):
    for nb in range(1,21):
        nu=F(1,na)+F(1,nb)
        reduced_mass=F(na*nb,na+nb)
        assert reduced_mass*nu==1

# p=2 internal soft constant at exterior coefficient nine.
assert (F(9)-F(2)**2)/2==F(5,2)
# Ordinary m threshold: a_power=m/2+1 and a_power²<H0 iff m<5 (m>=0).
for m in (F(0),F(3),F(4),F(4999,1000),F(5),F(6)):
    assert ((m/2+1)**2<H0)==(m<5)

result={'status':'passed','scope':'Exact elementary budget and canonical mass identities only; not an analytic BFSS verification',
        'partition_types_checked':number,'rank_range':[2,20],
        'max_root_payment_by_rank':rows,'target_budgets':budgets,
        'soft_p':2,'soft_constant':'5/2','complementary_reserve_remaining':'1/2'}
path=Path(__file__).with_name('global_budget_checks.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'partition_types_checked':number,
                  'targets_checked':len(budgets),'output':str(path)}))
