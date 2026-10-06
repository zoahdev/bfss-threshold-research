# Review findings: rank-certificate obstruction

Author: Yicheng Pan. Research checkpoint: 6 October 2026.

**Conditional/provisional. No independent human expert review has been supplied.** These findings summarize the existing analytical material and finite checks; they are not a new mathematical certification. The large-rank BFSS upper bound remains open.

## Assumptions and the direction of the obstruction

Take the actual displayed BFSS Hamiltonian on the compatible physical self-adjoint form realization, a normalized Spin(9)-singlet zero mode, a real symmetric traceless spatial tensor h with Tr(h²)=1, and the stated finite radial moments. A fourth radial moment suffices for the source-domain and shear steps in the main note. Symmetry of h is essential: an antisymmetric tensor would give q=0 and invalidate the intended positivity of a.

Write S=⟨ρ²⟩, A=S/9, Vq=⟨q²⟩ and M=⟨ρ²q²⟩. The explicit numerical upper-certificate is

    B_N(R)=8N²[(R/N)² Vq+M].

The conditional result is

    B_N(R) ≥ v₀=2^(−7/12)/27,
    A B_N(R) ≥ 2^(−5/4)/243 > 0

for N≥2 and R≥0. These are lower bounds on a particular proposed upper-certificate. From χ≤B_N(R) and B_N(R)≥v₀, no lower bound χ≥v₀ follows. The actual susceptibility may be much smaller, and the desired susceptibility decay is not disproved.

## Form-domain and coefficient findings

For d=N²−1 and D=9d, the full fermion-fiber norm satisfies

    ||F(Z)|| ≤ C_N ρ,     C_N=4√2 N√d.

Radial compact cutoffs and the finite first moment give finite kinetic and potential energies. The dilation form curve then gives T=V and F=−2T. Weighted derivative bounds and fourth-moment cutoff approximation put qΩ in D(H), with HqΩ=−2iD_hΩ/N². The exact shear-energy curve has second derivative T at the origin. Closed-form lower semicontinuity supplies the sufficient inequality

    m₁=2A/N²,     m₃≤2T/N⁴.

An exact m₃ equality requires stronger differentiability/domain justification and is unnecessary for the obstruction. Spectral Hölder has the direction m₁≤m₀^(2/3)m₃^(1/3), yielding

    Vq ≥ (2^(1/4)/27) S^(5/4) N^(−2).

For the regularized multipliers (ρ²+η²)^(−(k−2)/4), ambient Hardy gives the recurrence

    I_k ≤ [8N²C_N / ((D−2)²−(k−2)²)] I_(k−3),
    I_k=⟨ρ^(−k)⟩.

The bounded-multiplier argument establishes each inverse moment before its use; it does not assume the conclusion. For k_N=3 floor(D/6), the recurrence coefficients are uniformly below 2 and 3N²≤k_N≤D/2. Hence P(ρ≤1/2)≤2^(−2N²). Combining this with q²≤(8/9)ρ⁴ and the variance lower bound gives M≥v₀/(8N²). The earlier k=3 interpolation already gives the weaker obstruction N^(−4/7); the tracked higher inverse moments give the positive floor above.

The argument for this floor does not need the candidate exterior theorem. Interpreting B_N(R) as an upper bound on susceptibility does depend on the exterior/operator assumptions in the [interacting-threshold note](../interacting-threshold/interacting_threshold_bound.md). Existence of the zero mode and the needed positive moments are not established unconditionally here.

## Centered-coefficient cross-check

In the corrected manuscript normalization, centered pair and triangle terms act as scalar multiples of the identity on the full retained slow Clifford module. For a pair of sizes n,m, d=nm and distance r,

    W_e=32d(n+m)/r²,
    S_e* S_e=128d(n+m)/r,
    excitation energy=4r.

The pair compression inventory, in units r^(−2), is 18d(n+m) from Born–Huang, 8(n+m) from slow half-density, 14d(n+m) from quartic potential, 8d(n+m) from mixed Gauss spin square, −16(n+m) from fast density, and −8(d−1)(n+m) from the internal orbital derivative. Their sum is 32d(n+m). Omitting the internal derivative creates a spurious defect.

For a triangle let d_t=n_a n_b n_c, s=a+b+c, p=abc and K²=|b_e∧b_f|², four times its Euclidean area squared. Then

    W_t=d_t[32s/p−2(K²)²/(s p³)],
    S_t* S_t=d_t[64s²/p−4(K²)²/p³],
    excitation energy=2s.

Graph-source orthogonality and these exact denominators give W(0)=S(0)*H_f(0)^(−1)S(0), without assuming comparability of unrelated gaps. The canonical pair-orbital term c_C K*F^(−1)C*p_F has zero centered value and zero first internal compression jet because the relevant color trace is traceless. This statement concerns the centered jet, not an off-center estimate.

The two-block case saturates W₀≤32N∑_(a<b)n_a n_b/r_ab², so the coefficient N cannot be removed from this particular uniform bound merely by rescaling. The centered cancellation is essential: W₀ is not a surviving physical potential. See the [leading-coefficient audit](../../coefficient-audit/prior_audit/BFSS_Leading_Coefficient_Audit_2026-10-06.pdf), its [clarification](../../coefficient-audit/addendum/BFSS_Coefficient_Audit_Clarification_2026-10-06.pdf), and the [corrected manuscript](../../manuscript/manuscript.pdf). None of these centered contractions alone certifies nonzero-internal continuation, all-vector coercivity, or the global exterior theorem.

## Reproducibility and remaining target

The original script checks exact exponent arithmetic, the shear coefficient, finite rank samples through N=10000, inverse-moment recurrence coefficients, and 10000 seeded pair/triangle consistency samples. Those samples are not a universal proof or BFSS simulation. The analytical argument carries the universal claims, conditionally on its hypotheses.

The primary radius/virial context remains [Lin, 2302.04416](https://arxiv.org/html/2302.04416); the finite-N correction is an existing project calculation, not newly attributed to that paper. A planar-scale upper bound M=O(N^(−2)) remains compatible with the lower bound and would suffice for the separate [clipping route](../quadrupole-clipping/scalar_capacity_and_clipping.md). It is not proved here.
