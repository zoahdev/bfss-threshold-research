#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
export SOURCE_DATE_EPOCH=1791244800 FORCE_SOURCE_DATE=1 TZ=UTC
mkdir -p .build
if ! kpsewhich xelatex.fmt >/dev/null 2>&1; then
  export TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}'
  export TEXFORMATS="$ROOT/.build/texformats"
  export TEXMFVAR="$ROOT/.build/texmf-var"
  export TEXMFCONFIG="$ROOT/.build/texmf-config"
  export XDG_CACHE_HOME="$ROOT/.build/fontcache"
  mkdir -p "$TEXFORMATS" "$TEXMFVAR" "$TEXMFCONFIG" "$XDG_CACHE_HOME"
  if [[ ! -f "$TEXFORMATS/xelatex.fmt" ]]; then
    (cd "$TEXFORMATS" && xetex -ini -etex -interaction=nonstopmode -halt-on-error -jobname=xelatex -progname=xelatex '\input xelatex.ini' > format.log 2>&1)
  fi
fi
for pass in 1 2; do
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=.build audit.tex > ".build/pass-$pass.log" 2>&1
done
cp .build/audit.pdf BFSS_Leading_Coefficient_Audit_2026-10-06.pdf
