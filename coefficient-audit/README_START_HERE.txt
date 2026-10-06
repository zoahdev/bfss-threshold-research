BFSS leading coefficient audit with clarification addendum
6 October 2026

This is a new preservation archive. The original audit is retained unchanged
under prior_audit/. The complete clarification and new coefficient regression
are under addendum/. The canonical 116-page BFSS v2.1 manuscript is not changed.

Read both PDFs together. The addendum expands the untraced slow-Clifford
calculation and finite-sector transport. This archive does not provide a newly
merged PDF; it preserves the reviewed 9-page audit and 4-page addendum, together
with their source and reproduction files.

Computational coverage must be read narrowly:
- The original symbolic test simplifies supplied scalar formulas; it does not
  reconstruct every operator term or prove inventory completeness.
- The original direct Wick test covers four centered singleton triangles. Its
  pair Born-Huang and mixed spin-Gauss terms are supplied constants; it does
  not retain the untraced slow Clifford coefficient matrix.
- The added test constructs the full slow quadratic coefficient matrices for
  centered pairs (1,1), (2,1), (2,2), (3,1), at r=1. It reuses the prior color
  and Spin(9) constructors but has separate contraction logic.
- No script computes the nonzero-A multiplier or its spatial/internal jets,
  or verifies arbitrary-rank claims, all-vector coercivity, global localization,
  form domains, the global Hardy theorem, or constants uniform in N.

The analytic claims remain conditional on the exact reduced kinetic and frozen
pair definitions in canonical Appendices A/B/D. The addendum also relies on the
full W and source inventories in the original audit. This is AI-assisted
mathematical checking, not independent human peer review or formal verification.
See addendum/README.txt and PROVENANCE.json for the detailed scope.

Publicly archived on GitHub on 6 October 2026. No journal submission or external expert certification is claimed. Historical provenance fields record the state at preparation time.
