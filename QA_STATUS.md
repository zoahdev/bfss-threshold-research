# Public archive validation

Validation date: 6 October 2026. Full machine-readable scope and script hashes: [PUBLICATION_VALIDATION.json](PUBLICATION_VALIDATION.json).

- 29 scientific check programs completed successfully: 4 earlier repository checks, 11 manuscript regressions, 3 coefficient-audit/clarification checks, and 11 programs across 9 subsequent branches
- The actual-Hamiltonian and shear-Ward branches supplied no standalone scripts; no computation is claimed for those branches
- 3 notation-parser unit tests passed
- The v2.1 manuscript rebuilt from the included mathematical TeX sources to the exact original 116-page PDF SHA-256
- The 9-page audit and 4-page clarification PDFs match their original supplied bytes; all three PDFs were inspected for text, metadata and accidentally embedded private data
- Source, result and documentation files were screened for private paths, credentials, personal contact data and conversation identifiers; raw internal review reports were replaced with public scientific findings
- Current manifests check file identity only

## Interpretation limits

The scripts test finite algebra, constants, selected numerical cases and explicitly restricted countermodels. Some tests take analytical formulas or source inventory as inputs. They do not reconstruct every operator term, certify inventory completeness, verify all nonzero-internal jets, justify infinite-dimensional domain steps, or prove the global exterior theorem.

The main PDF had prior typesetting/render checks recorded under `manuscript/results/`; this publication pass preserved its bytes and rebuilt it rather than performing a new human page-by-page review. “Reviewed” in inherited production/audit records denotes AI-assisted checking, not independent human specialist review.

All branches retain their conditional hypotheses. No BFSS rank-uniform upper estimate, large-N limit, full soft/scattering theorem, human peer review or formal proof certification is claimed. There is no configured GitHub Actions workflow in this archive; local successful runs should not be described as a GitHub CI pass.
