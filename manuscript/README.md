# Finite rank BFSS exterior estimates and singlet decay

Version 2.1, 6 October 2026. Typesetting and exposition revision.
Public research archive as of 6 October 2026; not submitted or peer reviewed. The PDF is the preserved review draft.

## Results and proof status

The manuscript retains the baseline exterior estimate c < 49/4 for arbitrary physical vectors and adds the candidate estimate c < 121/4 for physical Spin(9) singlets. Hasler–Hoppe's existing invariance theorem then gives ordinary radial moments 0 <= m < 9 for every actual physical L2 zero mode of the compatible standard realization, provided the complete candidate analytical proof is correct.

All baseline local and global analytical dependencies remain substantive. Appendices A–J supply their candidate derivations; K–L detail the added rotation algebra and equivariant reference-domain construction. The argument retains full internal continua and assumes neither an internal spectral gap nor an internal ground-state projection. Its order is paid local ledger, zero extension, internal Haar averaging, then model-form estimates. The smaller retained coefficient 1-3a is used when extracting singlet coercivity.

This is a candidate mathematical proof, not an independent human review or a Lean/proof-assistant certificate. The packet does not establish zero-mode existence or uniqueness, the m=9 endpoint, full-Hamiltonian sharpness, c>49/4 for arbitrary nonsinglets, rank-uniform control, a large-N limit, zero-energy reduced-resolvent bounds, full soft theorems or scattering completeness. Polchinski's earlier L<9 Born–Oppenheimer expectation and the Sethi–Stern, Hasler–Hoppe and Agmon precedents are explicitly credited. No priority, affiliation or external endorsement is claimed.

## Revision and integrity

This v2.1 revision of 6 October 2026 corrects formula production and several explicitly logged exposition issues. See `CORRECTIONS_2026-10-06.txt`. It is a new review copy, not a replacement of the historical v2 file.

The historical 106-page PDF had SHA-256 `f3d49ba633799b8211a6b5d0ce5847f053ed5207979462157698f6b84196dcb6`. Historical recovery records are retained under `provenance/original_v2/`; those hashes describe the prior version. The current `SHA256SUMS` identifies this revised packet.

All eleven finite programs have been rerun. Their success is evidence only for their stated finite scope. Appendix D §§4.1–5 remains a priority for independent operator-level checking; no complete cancellation theorem is certified by the bundled symbolic tests.

## Contents

- `manuscript.pdf`: complete revised review document
- `manuscript.tex` and `appendices/`: full editable TeX sources
- `technical_notes/`: twelve readable mathematical notes
- `中文摘要.txt`: separate Chinese summary
- `CLAIMS_STATUS.json`: claims, dependencies and nonclaims
- `SOURCE_PROVENANCE.json`, `REVISION_STATUS.json`: revision identity and checks
- `FORMULA_TRANSCRIPTION.json`, `EDITORIAL_CORRECTIONS.json`: expression and correction records
- `transcription/original_notes/`: original plain-text notes for comparison
- `provenance/original_v2/`: historical recovery records
- `checks/`, `run_checks.py`, `results/`: eleven offline finite checks and fresh outputs
- `build_pdf.sh`: local XeLaTeX build with a fixed document timestamp
- `requirements-tested.txt`: tested Python dependencies
- `verify_manifest.py`, `SHA256SUMS`: byte-integrity verification
- `LICENSE-CODE.txt`, `LICENSE-DOCS.txt`: MIT code and CC BY 4.0 original documentation

No internal coordination transcript, private correspondence, raw recovery working file or downloaded third-party paper is included. Papers are cited and linked. The original source-level formulas in A–J are retained in the transcription record and original notes for coefficient-inventory review; the PDF uses typeset mathematics. Neither a moving projection nor a Schur minimizer is asserted to preserve the Hamiltonian operator domain D(H); the proofs use Q(H), the closed form domain.

## Reproduce

Before changing anything, verify the supplied bytes:

    python3 verify_manifest.py

Run the checks with Python 3, NumPy and SciPy:

    python3 run_checks.py

The programs need no network or files outside this packet. Floating-point outputs can vary with BLAS/LAPACK; run-time fields vary. A successful run certifies only each program's stated finite scope.

Build with XeLaTeX, the standard AMS/fontspec/fvextra/hyperref/needspace-related TeX Live packages, DejaVu fonts and Noto Serif CJK SC:

    bash build_pdf.sh

The builder downloads or installs nothing. It writes temporary files to `.build/` and the PDF to `manuscript.pdf`. Its fixed timestamp supports byte reproduction with the same toolchain; other TeX or font versions may change bytes. Rebuilding or rerunning can legitimately invalidate the supplied manifest, which identifies the frozen package.

Original code is MIT licensed and original documentation is CC BY 4.0. These licenses do not cover third-party references or dependencies. Substantial AI assistance is disclosed in the manuscript; no personal contribution beyond the stated existing authorship attribution is invented.

## Public release note

The 116-page PDF and its TeX mathematical content are preserved byte-for-byte from v2.1. Historical statements inside the preserved PDF and historical records describe their preparation date, not current GitHub availability. The later [leading-coefficient audit and clarification](../coefficient-audit/README_START_HERE.txt) are separate, conditional research notes. Their finite checks do not certify the global theorem. See the [repository status](../README.md), [AI disclosure](../AI_DISCLOSURE.md), and [publication changes](../PUBLICATION_CHANGES.md).
