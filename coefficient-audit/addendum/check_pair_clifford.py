"""Untraced slow-Clifford coefficient regression for centered block pairs.

Separate coefficient contraction logic; reuses gamma9/basis constructors from
check_centered_triangle.py. No slow Fock representation or slow trace is used
to establish scalarity: all slow quadratic coefficients are compared first.
Floating-point finite tests, not an arbitrary-rank/nonzero-A proof.
"""
from pathlib import Path
import itertools
import json
import numpy as np
from check_centered_triangle import basis, GAM


def run(n, m):
    N = n + m
    generators, _ = basis(N)
    nc = N*N-1
    fast = [i for i,g in enumerate(generators) if np.linalg.norm(g[:n,n:])>0]
    slow = [i for i in range(nc) if i not in fast]
    nf, ns = len(fast), len(slow)
    generators = generators[fast+slow]
    assert np.max(np.abs(np.einsum('aij,bji->ab',generators,generators)-np.eye(nc))) < 1e-12
    f = np.empty((nc,nc,nc))
    for a,b in itertools.product(range(nc),repeat=2):
        f[a,b] = np.real(-1j*np.einsum('ij,cji->c',
            generators[a]@generators[b]-generators[b]@generators[a], generators))
    z = np.diag([m/N]*n+[-n/N]*m)
    zcolor = np.einsum('ij,cji->c',z,generators).real
    Dad = -1j*np.einsum('cab,c->ab',f[:,:nf,:nf],zcolor)
    mass = np.kron(GAM[8],Dad)
    assert np.linalg.norm(mass@mass-np.eye(16*nf)) < 1e-10
    covariance = (np.eye(16*nf)+mass)/2
    assert np.linalg.norm(covariance+covariance.T-np.eye(16*nf)) < 1e-12

    # Complex endpoint action; its Gram matrix is independent of vec convention.
    actions = np.stack([np.kron(g[:n,:n],np.eye(m))-
                        np.kron(np.eye(n),g[n:,n:].T) for g in generators[nf:]])
    gram = np.einsum('cij,dji->cd',actions,actions)
    assert np.max(np.abs(gram.imag)) < 1e-12
    gram = gram.real
    assert abs(np.trace(gram)-n*m*(n+m)) < 1e-11

    # Source coefficient K_(ia),(alpha h),(beta c), before fast expectation.
    yukawa = np.stack([-2j*np.einsum('xy,abc->axbyc',GAM[i],f[:nf,:nf,nf:])
        .reshape(nf,16*nf,16*ns) for i in range(8)])
    yukawa = yukawa.reshape(8*nf,16*nf,16*ns)
    # Minus: move the first slow generator past the second fast generator.
    # The 1/2 is the r=1 Gaussian variance.
    Qy = -.5*np.einsum('mbc,mde,bd->ce',yukawa,yukawa,covariance,optimize=True)
    gauss = -1j*np.einsum('xy,abc->axbyc',np.eye(16),f[:nf,:nf,nf:])
    gauss = gauss.reshape(nf,16*nf,16*ns)
    Qg = -np.einsum('mbc,mde,bd->ce',gauss,gauss,covariance,optimize=True)
    expected_g = np.kron(np.eye(16),gram)
    expected_y = 16*expected_g
    out = {
        'block_sizes':[n,m], 'gap':1.0,
        'slow_majoranas':16*ns,
        'source_coefficient_max_error':float(np.max(np.abs(Qy-expected_y))),
        'gauss_coefficient_max_error':float(np.max(np.abs(Qg-expected_g))),
        'source_antisymmetric_max':float(np.max(np.abs(Qy-Qy.T))),
        'gauss_antisymmetric_max':float(np.max(np.abs(Qg-Qg.T))),
        'source_scalar':float((.5*np.trace(Qy)).real),
        'source_scalar_expected':128*n*m*(n+m),
        'gauss_scalar':float((.5*np.trace(Qg)).real),
        'gauss_scalar_expected':8*n*m*(n+m),
    }
    for key in ('source_coefficient_max_error','gauss_coefficient_max_error',
                'source_antisymmetric_max','gauss_antisymmetric_max'):
        assert out[key] < 1e-10, (key,out)
    assert abs(out['source_scalar']-out['source_scalar_expected']) < 1e-9
    assert abs(out['gauss_scalar']-out['gauss_scalar_expected']) < 1e-9
    return out


if __name__=='__main__':
    results = [run(n,m) for n,m in [(1,1),(2,1),(2,2),(3,1)]]
    result = {
        'scope':'Centered r=1 untraced slow quadratic Clifford coefficients; finite floating tests',
        'excluded':['nonzero internal coordinates','slow derivatives','full W reconstruction',
                    'arbitrary block proof by computation','all-vector/global Hardy theorem'],
        'results':results,
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
