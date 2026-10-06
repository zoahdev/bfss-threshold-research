#!/usr/bin/env python3
"""Check public archive bytes. This is not mathematical verification.
SPDX-License-Identifier: MIT
"""
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parent
bad = []
checked = 0
for line in (root / 'SHA256SUMS').read_text().splitlines():
    digest, name = line.split('  ', 1)
    path = root / name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        bad.append(name)
    checked += 1
if bad:
    print('Integrity mismatch:', *bad, sep='\n')
    sys.exit(1)
print(f'All {checked} public archive hashes match; bytes only, not proof correctness.')
