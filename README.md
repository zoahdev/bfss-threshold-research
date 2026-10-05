# BFSS threshold research: a work-in-progress snapshot

Snapshot date: 5 October 2026. This is an explicitly incomplete analytic investigation. It does not prove a BFSS soft-graviton theorem, rank-uniform nonperturbative spectral bound, generic scattering factorization, or eleven-dimensional Lorentz invariance.

## Latest descendant and cluster gate

`infrared_descendant_and_cluster_gate.md` gives an exact conditional reduction to a linear boson–fermion descendant, a sufficient positive Euclidean correlator bound at time scaling like N^(4/3), and the leading free two-cluster source coefficient. The required uniform correlator decay, distorted-wave matching, channel sum and nonzero-longitudinal source identification remain unproved. The favorable fixed-channel powers are not a full BFSS threshold law.

## Results recorded here

`quadrupole_rank_gate.md` states the physical normalization, a conditional lower-radius inequality, the distinction between the raw tensor and traceless spin-2 source, and the exact additional double-trace or low-energy spectral bounds that a proof would need. Its energy-form refinement removes a full fourth-moment requirement but leaves an unproved physical rank-uniform low-energy estimate.

- `check_threshold.py`: algebraic resolvent identities and numerical diagnostics for a nine-dimensional free-channel countermodel. This is explicitly not a BFSS Hamiltonian calculation or a BFSS counterexample
- `check_quadrupole.py`: exact SO(9) angular constants, tail power counting and free-channel double-Laplacian algebra
- `check_rank_normalization.py`: conditional finite-N Schur-minimum algebra and exact rank/physical-energy scale conversion

Recorded JSON outputs preserve earlier calculations. The current rank-normalization script also prints energy-form checks following its JSON block, so its complete stdout is not one JSON document.

## Reproduce

Python 3.11+, SymPy 1.14.0 and mpmath 1.3.0:

```sh
python check_threshold.py
python check_quadrupole.py
python check_rank_normalization.py
python check_descendant_cluster.py
```

Run normal Python, not `python -O`, because the checks use assertions. The scripts only check the documented algebra and diagnostic integrals. They do not establish domain hypotheses, construct scattering states, or control the matrix-rank limit.

## Principal limitations

The established current identity concerns the zero longitudinal Fourier mode. Its extension to a rank-changing or nonzero-longitudinal soft source remains missing. Ground-state/Ward and form-domain hypotheses must be justified. Neither scalar radius lower bounds nor assumed planar factorization supply the required connected spin-2 or low-energy spectral upper estimate. Fixed-rank decay does not justify an exchange of soft and decompactification limits.

## Sources

The note provides section-specific references. Main sources include [Soft Theorems in Matrix Theory](https://arxiv.org/abs/2312.15111), [matrix-current relations](https://arxiv.org/abs/hep-th/9803003), [fermionic completion](https://arxiv.org/abs/hep-th/9812239), [Lin–Yin asymptotic ground states](https://arxiv.org/abs/1402.0055), [Lin's bootstrap](https://arxiv.org/abs/2302.04416), and [Lin–Zheng's BFSS bootstrap](https://arxiv.org/abs/2410.14647). The current identities and general spectral tools are prior work, not discoveries claimed here.

See `AI_DISCLOSURE.md` and `LICENSE_STATUS.md`. This folder is a frozen checkpoint of ongoing research and should retain that status in any public repository description.
