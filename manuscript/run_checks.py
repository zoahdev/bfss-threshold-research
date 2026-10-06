#!/usr/bin/env python3
"""Run the included finite regressions; successful runs are not proof verification.
SPDX-License-Identifier: MIT
"""
from pathlib import Path
import subprocess, sys, os, json, platform, time, hashlib
ROOT=Path(__file__).resolve().parent
RESULTS=ROOT/'results'; RESULTS.mkdir(exist_ok=True)
CASES=[
 ('bfss_global_induction_20261005','check_global_budget.py','exact rational scalar budgets'),
 ('bfss_multiblock_geometry_20261005','check_multiblock_geometry.py','finite ambient metric and density identities'),
 ('bfss_all_rank_induction_20261005','check_general_fast_energy.py','finite frozen pair energy identities'),
 ('bfss_all_rank_induction_20261005','check_multiblock_root_sources.py','finite source and graph bookkeeping'),
 ('bfss_all_rank_induction_20261005','check_adapted_source_inventory.py','finite adapted Gauss Taylor coefficients'),
 ('bfss_complementary_reserve_20261005','check_colored_reserve.py','finite square completion identities'),
 ('bfss_complementary_reserve_20261005','check_local_schur.py','finite mixed and variational identities'),
 ('bfss_offcone_partition_20261005','check_regularized_tree.py','sampled regularized cluster tree'),
 ('bfss_offcone_partition_20261005','check_offcone_ims.py','finite difference incidence IMS examples'),
 ('bfss_sharp_decay_20261005','check_sharp_singlet_budget.py','exact rotation normalization and singlet scalar budgets'),
 ('bfss_sharp_decay_20261005','check_angular_gate_clifford.py','exact integer Clifford rotation identities'),
]
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONHASHSEED='0')
rows=[]
for directory,name,scope in CASES:
    path=ROOT/'checks'/directory/name
    start=time.monotonic()
    p=subprocess.run([sys.executable,str(path)],cwd=path.parent,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (RESULTS/(path.stem+'.log')).write_text(p.stdout)
    rows.append({'program':str(path.relative_to(ROOT)),'scope':scope,'exit_code':p.returncode,'seconds':round(time.monotonic()-start,3),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    print(name, 'completed' if p.returncode==0 else 'FAILED',flush=True)
import numpy, scipy
report={'meaning':'Programs completed with the recorded exit codes. Floating outputs are finite regressions, not a proof certificate. Read each log for its exact scope.','python':sys.version,'platform':platform.platform(),'numpy':numpy.__version__,'scipy':scipy.__version__,'runs':rows}
(RESULTS/'run_summary.json').write_text(json.dumps(report,indent=2)+'\n')
sys.exit(any(r['exit_code'] for r in rows))
