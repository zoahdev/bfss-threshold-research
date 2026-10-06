BFSS leading coefficient cancellation audit
6 October 2026

Read BFSS_Leading_Coefficient_Audit_2026-10-06.pdf first.

The audit reconstructs the complete W(A) Gaussian/Fock contraction inventory,
proves the centered pair and triangle cancellation, and gives the root-local
analytic perturbation and finite-sector resolvent argument for Appendix D
(4.2), (5.1), and (5.2) of the supplied BFSS v2.1 manuscript.

This is a leading-coefficient result at fixed finite N. It does not certify
the all-vector complementary reserve, all higher-order mixed estimates,
localization, form domains, or the global exterior Hardy theorem. It is
AI-assisted mathematical checking, not independent human peer review or a
proof-assistant certificate. The canonical manuscript was not changed.

Reproduce finite checks:
    python run_checks.py

check_triangle_symbolic.py verifies an exact rational identity with SymPy.
check_centered_triangle.py reconstructs the ambient SU(3) matrices and uses
explicit Gaussian and Majorana Wick contractions with floating arithmetic.
Its four test geometries include noncollinear and highly unequal-gap cases.
The JSON outputs record the actual coefficients and residuals. The script
contains explicit assertions and fails if a cancellation test exceeds its
stated tolerance. Finite tests are not substitutes for the analytic proof.

Rebuild the PDF, with XeLaTeX, DejaVu fonts and standard AMS packages:
    bash build_pdf.sh

requirements-tested.txt records the Python dependency versions used.
SHA256SUMS records all deliverable files except the checksum file itself.
