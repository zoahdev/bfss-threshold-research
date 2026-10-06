#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
set -euo pipefail
# Fixed document timestamp; the same TeX installation can reproduce PDF bytes.
export SOURCE_DATE_EPOCH=1791244800
export FORCE_SOURCE_DATE=1
export TZ=UTC
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
mkdir -p .build
if ! kpsewhich xelatex.fmt >/dev/null 2>&1; then
  if [[ ! -d /usr/share/texlive/texmf-dist ]]; then
    echo 'A configured XeLaTeX installation is required.' >&2; exit 1
  fi
  export TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}'
  export TEXFORMATS="$ROOT/.build/texformats"
  export TEXMFVAR="$ROOT/.build/texmf-var"
  export TEXMFCONFIG="$ROOT/.build/texmf-config"
  export XDG_CACHE_HOME="$ROOT/.build/fontcache"
  mkdir -p "$TEXFORMATS" "$TEXMFVAR" "$TEXMFCONFIG" "$XDG_CACHE_HOME"
  if [[ ! -f "$TEXFORMATS/xelatex.fmt" ]]; then
    (cd "$TEXFORMATS" && xetex -ini -etex -interaction=nonstopmode -halt-on-error \
       -jobname=xelatex -progname=xelatex '\input xelatex.ini' > format.log 2>&1)
  fi
fi
for pass in 1 2 3; do
  xelatex -interaction=nonstopmode -halt-on-error -output-directory=.build manuscript.tex > ".build/pass-$pass.log" 2>&1
done
cp .build/manuscript.pdf manuscript.pdf
printf 'Built %s\n' "$ROOT/manuscript.pdf"
