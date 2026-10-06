#!/usr/bin/env python3
"""Verify the original release bytes, not mathematical correctness.
SPDX-License-Identifier: MIT
"""
from pathlib import Path
import hashlib, sys
root=Path(__file__).resolve().parent
failures=[]; count=0
for line in (root/'SHA256SUMS').read_text().splitlines():
    expected,name=line.split('  ',1)
    p=root/name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:
        failures.append(name)
    count+=1
if failures:
    print('MISMATCH: '+'; '.join(failures)); sys.exit(1)
print(f'All {count} release file hashes match. This checks bytes only.')
