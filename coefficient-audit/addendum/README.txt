BFSS leading coefficient audit clarification
6 October 2026

Purpose
This is a ready-to-integrate clarification of the centered slow-Clifford
calculation and nonzero-A finite-sector transport in the 9-page leading
coefficient audit. It does not modify the canonical 116-page BFSS v2.1
manuscript, and does not certify the full BFSS or Hardy theorem.

Files
- slow_clifford_and_transport.tex: self-contained section body, requiring
  amsmath and amssymb; all labels use the auditadd: prefix
- addendum_standalone.tex: minimal wrapper for standalone compilation
- check_pair_clifford.py: new untraced coefficient regression
- check_pair_clifford.json and .log: output from the new regression
- check_centered_triangle.py: unchanged constructor dependency copied from
  the original audit; the new test imports its basis and GAM objects
- PROVENANCE.json: exact input hashes and scope

How to integrate
Insert the slow-Clifford subsection after the centered pair derivation,
and the transport subsection before the finite-sector resolvent argument.
Alternatively input the complete section as an addendum. Avoid duplicating
its source-scope claims in a way that suggests an independent certification
of Appendices A and B. Incorporate the exact computational exclusions below
into Section 7 and the audit README. Preserve the original audit as a prior
version and record the new source/test files in the revised checksum list.

Run the new check
    OPENBLAS_NUM_THREADS=1 python check_pair_clifford.py
Python with NumPy and SciPy is required because the original constructor
module imports SciPy. The new contraction itself uses NumPy only.

Exact computational scope
1. The original check_triangle_symbolic.py exactly simplifies rational
   identities between supplied scalar triangle formulas. It does not derive
   the complete reduced operator or prove that no term was omitted.
2. The original check_centered_triangle.py tests four centered singleton
   triangle geometries using deterministic floating-point Wick contractions.
   It supplies the singleton pair Born-Huang and mixed spin-Gauss terms as
   known constants. It does not retain a slow Clifford coefficient matrix.
3. The new check_pair_clifford.py constructs every slow quadratic coefficient
   of the centered Yukawa-source norm and mixed spin-Gauss square for pairs
   (1,1), (2,1), (2,2), (3,1), all at r=1. It compares the whole coefficient
   matrix with the predicted color Gram matrix and checks the antisymmetric
   part, before using CAR to report scalar values. It does not infer
   scalarity from a slow trace. The contraction logic is separate, but it
   reuses the original test's Spin(9) and color-basis constructors.
4. All floating tests are finite regression evidence. None of these scripts
   computes the nonzero-A multiplier, checks its spatial/internal derivatives,
   proves an arbitrary-block statement by computation, or verifies all-vector
   coercivity, unrestricted mixed-form estimates, localization, form domains,
   the global Hardy theorem, or constants uniform in N.

Analytic scope and conditions
The addendum proves its displayed pair slow-Clifford contractions for
arbitrary finite block sizes from the stated CAR/color conventions. Its
transport construction preserves actual oscillator sectors without choosing
internal eigenvectors, and proves the finite-sector resolvent bounds under
the exact positive kinetic/potential and gapped fermion-mass hypotheses of
Appendices A/B/D. The final coefficient estimate also uses the full W and
source inventories in the original audit; the addendum is not a new
independent derivation of all those inventories. No coefficient-level
counterexample was found in the adversarial review. The stronger global and
large-N claims remain unverified by this work.
