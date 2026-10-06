"""Exact integer check of the two Spin(9) Bianchi projectors."""
import itertools
import numpy as np
# I, X, Z, J; J is real antisymmetric and J^2=-I.
p = [np.eye(2,dtype=int), np.array([[0,1],[1,0]]),
     np.array([[1,0],[0,-1]]), np.array([[0,1],[-1,0]])]
strings = [(0,0,0,1),(0,0,0,2),(0,0,3,3),(0,3,1,3),
           (1,3,2,3),(2,3,2,3),(3,0,2,3),(3,1,1,3),(3,2,1,3)]
gamma = []
for s in strings:
    g = np.ones((1,1),dtype=int)
    for k in s: g = np.kron(g,p[k])
    gamma.append(g)
assert all(np.array_equal(g,g.T) for g in gamma)
assert all(np.array_equal(gamma[i]@gamma[j]+gamma[j]@gamma[i],
                          2*(i==j)*np.eye(16,dtype=int))
           for i in range(9) for j in range(9))
for grade in (2,3):
    basis=[]
    for inds in itertools.combinations(range(9),grade):
        g=np.eye(16,dtype=int)
        for i in inds:g=g@gamma[i]
        basis.append(g)
    basis=np.array(basis)
    assert np.array_equal(np.einsum('xab,yab->xy',basis,basis),
                          16*np.eye(len(basis),dtype=int))
    t=np.einsum('xab,xcd->abcd',basis,basis)
    wedge=t-t.transpose(0,2,1,3)+t.transpose(0,2,3,1)
    assert not wedge.any()
    print(f'grade {grade}, dimension {len(basis)}: Frobenius and Bianchi verified exactly')
