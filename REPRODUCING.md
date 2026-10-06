# Reproducing the finite checks

Use normal Python, **not `python -O`**: assertions are part of the checks. The programs are local algebraic/numerical regressions, not an automated proof of the analytical claims.

Python 3.11+ is recommended. Tested dependencies are NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0 and mpmath 1.3.0; see `requirements-publication.txt`. A virtual environment is recommended. No script installs dependencies or downloads papers.

From the repository root:

```sh
python3 verify_publication.py
python3 check_threshold.py
python3 check_quadrupole.py
python3 check_rank_normalization.py
python3 check_descendant_cluster.py
python3 manuscript/run_checks.py
python3 coefficient-audit/prior_audit/run_checks.py
OPENBLAS_NUM_THREADS=1 python3 coefficient-audit/addendum/check_pair_clifford.py
```

Each `notes/` branch README provides its additional commands and exact scope. For stable resource usage set `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1` and `MKL_NUM_THREADS=1`.

To rebuild the preserved main PDF with an installed XeLaTeX/TeX Live toolchain, DejaVu and Noto Serif CJK SC fonts:

```sh
bash manuscript/build_pdf.sh
bash coefficient-audit/prior_audit/build_pdf.sh
```

The clarification source is `coefficient-audit/addendum/addendum_standalone.tex`; compile it from its directory with XeLaTeX. Neither build route downloads or installs software. Exact PDF bytes depend on the documented TeX/font toolchain.

Run integrity verification before rerunning checks or building PDFs. Regenerated numerical outputs, timing fields and PDFs can legitimately change hashes. A zero exit code confirms only the checks actually implemented. It does not establish operator-domain hypotheses, inventory completeness, arbitrary-rank inequalities, a nonperturbative upper bound or a large-N limit.
