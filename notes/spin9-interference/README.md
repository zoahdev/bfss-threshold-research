# Spin(9) interference

Author: Yicheng Pan  
Research checkpoint: 6 October 2026

## Status

**Conditional/provisional. Exact finite algebra with conditional operator interpretation; polarization averaging does not identically remove interference.**

No independent human expert review has been supplied. Symbolic, algebraic and finite numerical consistency checks are not human peer review or proof-assistant certification. This branch does not establish existence or uniqueness of a physical BFSS zero mode, the full candidate exterior theorem, a large-rank quadrupole upper bound, or a soft theorem.

## Read first

- [Scientific note](spin9_interference_audit.md)
- [Public review findings and caveats](REVIEW_FINDINGS.md)
- [Machine-readable status](CHECK_STATUS.json)

## Dependencies

- Physical supercharge normalization and stated operator domains
- Quantum-Gram descendant framework
- No actual zero-mode expectation supplied by configuration checks

Related branches: [quantum-gram](../quantum-gram/README.md), [mixed-moment](../mixed-moment/README.md).

## Reproduction

Run from this directory with Python 3:

```sh
python3 check_spin9.py
python3 independent_verify_bianchi.py
```

Dependencies: numpy.

Recorded check outputs are retained. `VALIDATION.json` and `validation_outputs/` record the publication rerun. These checks establish only their explicitly described finite identities, not the analytical assumptions.

## Editorial provenance

The scientific note, code, primary-source links and attribution are preserved from the dated source package. Changes here are limited to publication status, privacy-safe references and navigation. Raw review reports have been replaced by the public scientific summary in `REVIEW_FINDINGS.md`. Duplicate background notes are linked to their canonical copy in this archive. This is a research archive, not a replacement for the main manuscript.
