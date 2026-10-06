#!/usr/bin/env python3
"""Run the two finite checks; neither substitutes for the analytic audit."""
from pathlib import Path
import subprocess,sys,os
root=Path(__file__).resolve().parent
for name in ('check_triangle_symbolic.py','check_centered_triangle.py'):
    subprocess.run([sys.executable,str(root/name)],check=True,env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
print('Both finite checks passed; see the audit for mathematical scope.')
