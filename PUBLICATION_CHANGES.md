# Public archive preparation, 6 October 2026

This release extends the existing public checkpoint. The earlier scientific notes, programs, result files and license texts are retained. Root navigation, disclosure, validation and integrity records are updated for the expanded archive.

## Preserved material

- The canonical v2.1 manuscript PDF is unchanged: 116 pages, SHA-256 `daef0d76c50de0a1366c58edcac0eb86e10f628ef3122827b581cf25b007bb8c`
- The manuscript's mathematical TeX and appendix content are unchanged
- The separate 9-page coefficient audit and 4-page clarification are preserved with their editable source and finite-check programs
- Formula-transcription maps and original-versus-corrected mathematical source records remain available for comparison
- Eleven subsequent conditional/provisional research branches are collected under `notes/`

## Editorial and privacy changes

- Current public-release status is stated in the navigation and status documents; preserved PDF/historical provenance wording remains a preparation-time record
- Research status is explicitly conditional, unreviewed and incomplete; the large-N objective remains unsolved
- Raw internal review reports are excluded. Their useful scientific findings, qualifications and corrections are rewritten into public branch `REVIEW_FINDINGS.md` summaries
- Local filesystem references are replaced by portable relative references. Private correspondence, conversation identifiers, credentials and operational instructions are not included
- Finite programs are rerun, their output paths are normalized for portability, and public integrity manifests are regenerated. Floating-point and timing differences do not constitute mathematical changes

These are archive-preparation changes, not new research or a proof certification. Historical checksums nested under `manuscript/provenance/original_v2/` describe an earlier version. Current `SHA256SUMS` files identify this public snapshot and exclude themselves.
