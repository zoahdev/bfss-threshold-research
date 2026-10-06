"""Exact integer regression for the rotation support estimate.
SPDX-License-Identifier: MIT
These finite Clifford checks corroborate the displayed analytic identities;
they do not prove closed-domain or localization statements.
"""
from pathlib import Path
from fractions import Fraction
import json
import numpy as np
# Real symmetric Spin(9) matrices from the octonion multiplication table.
# Kept local so this release has no dependency on an unbundled research script.
triples = [(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]
table = {}
for a,b,c in triples:
    for x,y,z in [(a,b,c),(b,c,a),(c,a,b)]:
        table[x,y] = (1,z)
        table[y,x] = (-1,z)
es = []
for a in range(1,8):
    M = np.zeros((8,8),dtype=np.int64)
    M[a,0] = 1
    M[0,a] = -1
    for b in range(1,8):
        if a != b:
            sign,c = table[a,b]
            M[c,b] = sign
    es.append(M)
I8 = np.eye(8,dtype=np.int64)
Z8 = np.zeros((8,8),dtype=np.int64)
gamma = np.asarray([np.block([[Z8,E],[-E,Z8]]) for E in es]
    + [np.block([[Z8,I8],[I8,Z8]]),np.block([[I8,Z8],[Z8,-I8]])],dtype=np.int64)
I = np.eye(16, dtype=np.int64)
zero = np.zeros((16, 16), dtype=np.int64)
for u in range(9):
    for v in range(9):
        assert np.array_equal(gamma[u] @ gamma[v] + gamma[v] @ gamma[u],
                              2 * int(u == v) * I)
# A[j,w]/112 is the coefficient matrix of x_w in a_{j,beta}.
stack_squares = [Fraction(0) for _ in range(9)]
for u in range(9):
    for v in range(u + 1, 9):
        gamma_uv = gamma[u] @ gamma[v]
        A = [5 * (int(w == u) * gamma[v] - int(w == v) * gamma[u])
             + 2 * gamma[w] @ gamma_uv for w in range(9)]
        for w in range(9):
            for t in range(9):
                scalar = int(np.sum(A[w] * gamma[t]))
                assert scalar == 112 * (int(w == u and t == v)
                                        - int(w == v and t == u))
                # Coefficient matrices of distinct x_w are Frobenius-orthogonal.
                gram = int(np.sum(A[w] * A[t]))
                expected = (16 * (49 if w in (u, v) else 4)) if w == t else 0
                assert gram == expected
            stack_squares[w] += Fraction(int(np.sum(A[w] * A[w])), 2 * 112**2)
        # Fermion bilinear in {Q,a} is precisely -i Theta gamma_uv Theta/4.
        assert np.array_equal(sum((gamma[w] @ A[w] for w in range(9)), zero.copy()),
                              28 * gamma_uv)
        # The interaction anticommutator vanishes by Clifford traces.
        for w in range(9):
            for s in range(9):
                for t in range(s + 1, 9):
                    assert int(np.trace(A[w].T @ gamma[s] @ gamma[t])) == 0
assert stack_squares == [Fraction(9, 28)] * 9
result = {
    'arithmetic': 'exact integer matrices and Fraction',
    'gamma_anticommutators': 81,
    'angular_generators_checked': 36,
    'orbital_coefficient': 'exact x_u p_v - x_v p_u',
    'spin_coefficient': 'exact -i Theta gamma_uv Theta / 4',
    'interaction_traces': 'all zero',
    'fixed_generator_charge_sum_identity': '(|x_u|^2+|x_v|^2)/32 + sum_other |x_w|^2/392',
    'fixed_generator_charge_sum_bound': 'alpha^2 / 32',
    'all_36_generators_charge_sum_identity': '9 alpha^2 / 28',
    'charge_normalization': '{q_alpha,q_beta}=delta_alpha,beta h; sum||q g||^2=8h[g]',
    'baseline_rescaling': 'Q=sqrt(2)q; A=a/sqrt(2); fixed bound alpha^2/64; all-generator sum 9alpha^2/56',
    'casimir_coercivity': '7 lambda / (72 R^2)',
    'nonsinglet_coercivity': '7 / (9 R^2)',
    'scope': 'finite Clifford algebra only; analytic proof and domains in manuscript Appendix K'
}
Path(__file__).with_name('angular_gate_clifford_checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
