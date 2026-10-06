"""Exact algebra checks only; no BFSS large-rank numerical evidence."""
from fractions import Fraction as F
m = 9
dim = (m-1)*(m+2)//2
c = F(8*m, (m-2)*(m-1)*(m+2)*(m+4))
assert dim == 44 and c == F(9,1001)
p3_rank_one = F((m-1)*(m-2),m*m)
sphere_traceless_cubic = F(8,m*(m+2)*(m+4))
assert c*p3_rank_one == sphere_traceless_cubic
kappa_max = F(7,9)
lo = F(1,9) - c*kappa_max*dim/F(9)
hi = F(1,9) + c*kappa_max*8*dim/F(9)
assert lo == F(1,13) and hi == F(5,13)
# h=diag(1,-1,0,...)/sqrt(2), G=nn^T.
# Exact spherical moments yield E[a q²]=(30−6)/(4*9*11*13).
mixed_sphere = F(24,4*9*11*13)
M_rank_one = F(2,99)
mixed_formula = M_rank_one/F(9) + c*(F(1,2)-F(1,9))*p3_rank_one
assert mixed_sphere == mixed_formula == F(2,429)
# For the optional sharper h^4 bound Trh4≤19/24.
assert F(1,9)-c*(F(19,24)-F(1,9))*dim/F(9) == F(19,234)
print('Exact checks passed: c_9=9/1001; bounds [1/13,5/13]; rank-one calibration 2/429.')
