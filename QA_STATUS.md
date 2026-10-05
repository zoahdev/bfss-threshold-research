# Packaging verification

Executed 5 October 2026 in an isolated copy; Python 3.12, SymPy 1.14.0 and mpmath 1.3.0 where required. Original research sources were not overwritten.

- `check_quadrupole.py`: passed, exit 0
- `check_rank_normalization.py`: passed, exit 0
- `check_threshold.py`: passed, exit 0

- `check_descendant_cluster.py`: passed, exit 0; symbolic 3D-slice reflection check and exact 9D shell/scaling constants

These are reproducibility and implementation checks, not human peer review or a proof of unstated claims. Manuscript PDFs were checked for readable text and accidentally embedded local paths/contact data; this packaging pass did not retypeset or visually re-review the manuscripts.
