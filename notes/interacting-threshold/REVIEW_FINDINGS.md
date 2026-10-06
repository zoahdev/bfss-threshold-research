# Review findings: interacting threshold reduction

Author: Yicheng Pan. Research checkpoint: 6 October 2026.

**Conditional/provisional. No independent human expert review has been supplied.** These findings summarize the existing analytical material and finite checks; they are not a new mathematical certification. The large-rank BFSS upper bound remains open.

## Conditional content

The note derives weighted full-sector consequences from the candidate all-vector exterior Hardy input of the [corrected manuscript](../../manuscript/manuscript.pdf). It retains the complete physical Spin(9) 44 sector, including transverse excitations and coupled internal continua. It does not replace that sector with a free-channel approximation.

Under the stated exterior, self-adjointness, zero-mode and domain hypotheses, the argument gives fixed-rank quadrupole susceptibility and inverse spectral moments strictly below order 5/2, including a fixed-rank small-positive-regulator statement. These consequences do not certify the exterior hypothesis itself and do not imply rank-uniform constants.

## Finite checks

- The 44 Casimir is 18, the support coefficient is 7/4, and the singlet Hardy coefficient is 121/4
- `check_ims.py` constructs exact rational positive Bernstein coefficients for the two displayed IMS polynomials
- `check_source.py` checks the comparison tail r^(−9)log r, its potential −11/(r² log r), and the origin coefficient 26a

The logarithmic comparison example limits what follows from the specified Hardy information; it is not an actual BFSS zero-mode counterexample. The endpoint E^(5/2) source statement, a positive-energy limiting absorption principle, BFSS existence/uniqueness and the requested large-rank estimate are not established.

The source package records a separate AI-assisted mathematical check, not human peer review. The finite scripts do not check every functional-analytic step or the complete infinite-dimensional exterior proof. All primary references and qualifications remain in the scientific note.
