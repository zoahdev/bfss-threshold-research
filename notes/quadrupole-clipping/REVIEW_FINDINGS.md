# Review findings: quadrupole clipping and scalar capacity

Author: Yicheng Pan. Research checkpoint: 6 October 2026.

**Conditional/provisional. No independent human expert review has been supplied.** These findings summarize the existing analytical material and finite checks; they are not a new mathematical certification. The large-rank BFSS upper bound remains open.

## Conditional reduction

For one real supercharge component and a normalized physical singlet zero mode with finite second radial moment, the bounded scalar primitive gives

    K_N(s) ≤ ½ E[a_h 1_(|q_h|>L)] + sN²L².

Thus at s=N^(−4/3), an O(N^(−2/3)) bound on the gradient-weighted tail at L=κN^(−2/3) is sufficient. That concentration input is unproved. The graph-norm cutoff construction uses bounded clipping and a finite second moment; it does not silently assume a fourth moment.

The older variance condition and this particular fixed-threshold weighted-tail condition are not established to imply one another. The note's rotational Gram-law examples illustrate this kinematic distinction; they are not BFSS states. The stronger mixed-moment estimate E[a_h q_h²]=O(N^(−2)) would suffice by Markov, but is not derived.

## Restricted radial trial obstruction

For F=f(ρ)q_h, the isotropic conditional quadrupole profile obeys 0≤c_N(ρ)≤2ρ⁴/99. Square completion yields

    J[f] ≥ E[sN²ρ² c_N(ρ)/(4ρ²+22sN²c_N(ρ))].

The comparison x/(4+22x)≥min(1,x)/26 fixes the displayed necessary profile condition for a successful radial trial. This is a lower bound on the restricted trial objective, not on exact K_N(s). It neither disproves concentration nor establishes a general no-go for nonradial primitives.

## Check coverage and limits

The script checks the square completion and constants symbolically; the 44-dimensional projector and residual formulas on 500 seeded coordinate configurations; and the abstract resolvent variational identity in a finite self-adjoint matrix with a zero mode. These are algebraic consistency checks, not BFSS ground-state data or a proof of analytic domains.

The primary references, their stated applicability limits, and the historical literature comparison are preserved in the main note as of the research checkpoint. No new literature survey or priority claim is made for this publication. This reduction does not construct rank-changing soft emission or prove generic eleven-dimensional factorization.
