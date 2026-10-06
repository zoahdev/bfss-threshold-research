# BFSS mixed-moment audit: exact reductions, but no planar upper bound

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


Research checkpoint, 6 October 2026. This note attacks the actual finite-rank target

\[
M_N=\langle \rho^2q_h^2\rangle=O(N^{-2}),
\]

without assuming planar factorization. It does not prove that target, a large-rank soft theorem, or a general impossibility of a quantum bootstrap certificate. The mathematical progress is: an exact cubic Gram identity; equivalence of the two sixth moments previously treated only one-sidedly; stronger consequences of the existing BFSS small-radius estimate; and a precisely scoped coordinate-only obstruction. The source-specific upper estimate remains missing.

## 1. Definitions and assumptions

Use the normalization and compatible BFSS realization of `../bfss_new_rank_route_20261006/scalar_capacity_and_clipping.md`. Thus `tr=Tr/N`,

\[
G_{ij}=\operatorname{tr}(Z_iZ_j),\quad R=\rho^2=\operatorname{Tr}_9G,
\quad B=G-RI_9/9,
\]
\[
q_h=\operatorname{Tr}_9(hG),\quad a_h=\operatorname{Tr}_9(h^2G),
\quad \operatorname{Tr}_9h=0,\quad \operatorname{Tr}_9h^2=1.
\]

Here h is real symmetric. The bosonic configuration law of the normalized gauge- and Spin(9)-singlet zero mode is invariant under G→OGOᵀ. Put

\[
S=\langle R\rangle,\qquad V_q=\langle q_h^2\rangle,
\qquad A_6(h)=\langle a_hq_h^2\rangle.
\]

Section 2 needs only rotational invariance and G≥0. Section 3 additionally uses the actual-BFSS hypotheses and previously audited estimates in `../bfss_rank_certificate_audit_20261006/rank_certificate_audit.md`: normalization, zero energy, singletness, compatible quadratic forms, finite positive moments needed for the shear argument, and its virial/domain justifications. No candidate exterior theorem is promoted to an established theorem.

## 2. Exact cubic Gram identity

For m≥3, let C be a traceless symmetric m×m matrix, and average its rotational orbit C_O=OCOᵀ. For traceless symmetric A,D,E,

\[
\int \operatorname{Tr}(AC_O)\operatorname{Tr}(DC_O)
\operatorname{Tr}(EC_O)\,dO
=c_m\operatorname{Tr}(C^3)\operatorname{Tr}(ADE),
\]
\[
c_m=\frac{8m}{(m-2)(m-1)(m+2)(m+4)}.
\tag{1}
\]

The last trace is symmetric in A,D,E: cyclicity and transposition generate every permutation. To see uniqueness, an invariant cubic on traceless symmetric matrices is a symmetric homogeneous degree-three polynomial in the eigenvalues; with their sum zero it is a multiple of Tr(C³). Polarization supplies the trilinear statement. The orbit moment is separately an invariant cubic in C, so its coefficient is proportional to Tr(C³).

Calibrate on C=nnᵀ−I/m with n uniform on S^(m−1). Then

\[
\operatorname{Tr}C^3=\frac{(m-1)(m-2)}{m^2},\qquad
\mathbb E(n^TAn)(n^TDn)(n^TEn)
=\frac{8\operatorname{Tr}(ADE)}{m(m+2)(m+4)},
\]

which proves (1). At m=9, c₉=9/1001.

The quadratic orbit identity is

\[
\mathbb E_O q_h^2=\operatorname{Tr}B^2/44.
\tag{2}
\]

Since a_h=R/9+Tr[(h²−I/9)B], apply (1) with A=h²−I/9 and D=E=h to obtain

\[
\boxed{A_6(h)=\frac{M_N}{9}
+\frac9{1001}\left(\operatorname{Tr}h^4-\frac19\right)
\left\langle\operatorname{Tr}B^3\right\rangle.}
\tag{3}
\]

This is an exact finite-N identity. There is no independence or factorization hypothesis.

### 2.1 Uniform comparison of the two sixth moments

The eigenvalues of B lie in [−R/9,8R/9]. Consequently,

\[
-\frac R9\operatorname{Tr}B^2\le\operatorname{Tr}B^3
\le\frac{8R}9\operatorname{Tr}B^2.
\]

Also Tr h⁴≥1/9. Tr h=0 and Tr h²=1 imply ∥h∥op²≤8/9, hence

\[
0\le\operatorname{Tr}h^4-1/9\le7/9.
\]

Using ⟨R Tr B²⟩=44M_N in (3) gives the convenient nonsharp bounds

\[
\boxed{\frac1{13}M_N\le A_6(h)\le\frac5{13}M_N.}
\tag{4}
\]

In particular, A₆(h)=O(N^−2) is equivalent to M_N=O(N^−2), with constants independent of h and N. Replacing the radial weight by a_h does not bypass this sixth-moment concentration problem.

There is no hidden assumption that ⟨ρ⁶⟩ is finite. Prove (3) and (4) first with the rotationally invariant cutoff 1_(R≤T). Every term is then integrable. Monotone convergence gives (4) in the extended nonnegative reals. If either A₆ or M is finite, both are finite, and |Tr B³|≤(8/9)R Tr B² makes the untruncated signed term in (3) absolutely integrable. If both are infinite, only (4), rather than a signed infinity formula, is asserted.

## 3. The desired upper bound would also settle a radius upper bound

The prior actual-BFSS audit proves

\[
V_q\ge\frac{2^{1/4}}{27}S^{5/4}N^{-2},\quad
S\ge2^{-2/3},\quad
\mathbb P(\rho\le1/2)\le2^{-2N^2}.
\tag{5}
\]

It also has q_h²≤bρ⁴ with b=8/9. Thus

\[
\langle q_h^2\mathbf1_{\rho\le1/2}\rangle
\le\frac b{16}2^{-2N^2}.
\]

The constants checked in that audit imply this discarded variance is at most V_q/2, for every N≥2. Therefore the original argument actually gives the S-dependent estimate

\[
\boxed{M_N\ge\frac18V_q
\ge\frac{2^{1/4}}{216}S^{5/4}N^{-2}.}
\tag{6}
\]

Hence a uniform upper certificate M_N≤C_M/N² would imply

\[
\boxed{S\le(216\,2^{-1/4}C_M)^{4/5}.}
\tag{7}
\]

The proposed planar mixed-moment bound is therefore strong enough to prove a rank-uniform radius upper bound. The latter is not furnished by the elementary BFSS bootstrap estimates currently being used. This is an implication under the existing audited assumptions, not a proof that the mixed-moment upper bound is false.

### 3.1 A planar mixed-moment estimate would beat the clipping rate

The same split yields the useful upper comparison

\[
\boxed{V_q\le4M_N+\frac b{16}2^{-2N^2}.}
\tag{8}
\]

If M is finite, then V_q is finite even without an a priori fourth radial moment: on ρ>1 its integrand is controlled by ρ²q², and on ρ≤1 it is bounded. The direct primitive F=q_h is then available under the stated bounded-multiplier/core hypothesis. Indeed, take F_L=χ(ρ/L)q_h, with χ=1 near zero and compactly supported. Finite V_q gives F_LΩ→q_hΩ in L². In

\[
Q_α(F_LΩ)=-(2i/N)χ(ρ/L)b_{α,h}Ω+[Q_α,χ(ρ/L)]q_hΩ,
\]

the first term converges by ⟨a_h⟩≤S<∞. The second has squared norm at most ∥χ′∥∞²V_q/(2N²L²), since |∇ρ|²=1/N. Closedness therefore proves q_hΩ∈D(Q_α) and Q_αq_hΩ=−2ib_{α,h}Ω/N, without an additional unresolved domain assumption. The existing source certificate gives

\[
K_N(s)\le\frac{sN^2}{4}V_q
\le sN^2M_N+\frac b{64}sN^2 2^{-2N^2}.
\tag{9}
\]

At s=σN^−4/3, a planar M_N≤C_MN^−2 would therefore give K_N(s)=O(N^−4/3), stronger than the originally requested O(N^−2/3). Even M_N=O(N^−4/3) suffices for that original target via (9). This does not establish either upper estimate; it correctly calibrates what remains sufficient after retaining the small-radius information.

## 4. What the simplest exact supercharge Ward family does

Keep all 16 supercharges, and define

\[
b_{\alpha,h}=N^{-1/2}\operatorname{Tr}
(h_{ij}Z_i\Gamma^j_{\alpha\beta}\psi_\beta),\qquad
D_h=\sum_{ijA}h_{ij}Z_i^AP_j^A.
\]

D_h is symmetric because Tr h=0. Direct Clifford contraction gives the exact identities on the usual compactly supported smooth core

\[
\sum_{\alpha=1}^{16}\{Q_\alpha,b_{\alpha,h}\}
=\frac{16}{N}D_h,
\quad [Q_\alpha,q_h]=-\frac{2i}{N}b_{\alpha,h},
\quad b_{\alpha,h}^2=\frac{a_h}{2}.
\tag{10}
\]

The interaction contribution to the first identity vanishes because Tr(Γ^(ij)ᵀΓ^k)=0. In the kinetic derivative term, h_ijΓ^iΓ^j=(Tr h)I=0. For a smooth scalar f,

\[
\sum_\alpha\{Q_\alpha,f(q_h)b_{\alpha,h}\}
=\frac{16}{N}\bigl[f(q_h)D_h-i f'(q_h)a_h\bigr]
=\frac8N\{f(q_h),D_h\}.
\tag{11}
\]

Formally choosing f(q)=q³ gives

\[
\sum_\alpha\{Q_\alpha,q_h^3b_{\alpha,h}\}
=\frac{16}{N}\bigl[q_h^3D_h-3i a_hq_h^2\bigr].
\tag{12}
\]

Thus the candidate sixth-moment Ward identity is precisely a symmetrized shear-current identity. When its expectation is justified, it fixes the real part of ⟨q³D_h⟩ to zero; its imaginary part 3⟨a_hq_h²⟩ is already the canonical commutator [D_h,q_h³]=−6i a_hq_h². It provides no restoring term with a favorable sign that bounds A₆.

This is a failure of this specific Ward family, not a statement that supersymmetry is useless or that all quantum Ward identities are redundant. Higher fermion/commutator Ward identities introduce additional correlators whose positivity and rank dependence must still be controlled.

Domain caution matters: q³b grows as seventh coordinate degree, and its Hilbert norm can demand fourteenth moments. Therefore (12) must not be inserted into the zero-mode expectation just because a sixth moment exists. Equation (11) is an exact core identity; using it on Ω requires legitimate cutoffs/weak limits. Treating the unregularized polynomial as automatically admissible would be an additional error, rather than a closure of the estimate.

## 5. Explicit obstruction to coordinate-only trace/SOS arguments

For each N≥2 choose a traceless diagonal Hermitian D_N with tr D_N²=1 and ∥D_N∥op≤√(3/2). For even N take half its entries +1 and half −1. For odd N take (N−1)/2 entries of each sign ±√[N/(N−1)] and one zero.

Let n be uniform on S⁸, U be Haar in SU(N), and set

\[
Z_i=n_i U D_N U^\dagger.
\tag{13}
\]

This configuration law is gauge- and SO(9)-invariant, and obeys every exact finite-N coordinate trace identity and every coordinate-polynomial positivity inequality. Every normalized coordinate single-trace moment of fixed degree has a rank-uniform bound. Nevertheless,

\[
[Z_i,Z_j]=0,\quad \rho^2=1,\quad G=nn^T,
\quad \operatorname{Tr}B^2=\frac89,
\quad M_N=\frac2{99}.
\tag{14}
\]

Thus even a hard bounded radius, all coordinate trace-word positivity, and vanishing commutator potential do not imply any vanishing rank bound on M. No coordinate-only SOS/trace-inequality argument using just these properties can close the estimate, at degree six or at any higher degree. A putative pointwise inequality controlling the Gram anisotropy by the commutator potential is already contradicted by (13).

The limitation is important: (13) is not a BFSS quantum state. It does not satisfy the canonical momentum/fermion constraints and the zero-energy virial identities. It is not a counterexample to the desired BFSS estimate, and it is not a no-go theorem for finite-degree quantum SOS certificates that use those dynamical constraints.

## 6. Connected equations and the precise missing input

Spin(9) invariance gives ⟨q_h⟩=⟨Rq_h⟩=0, so the exact cumulant decomposition is

\[
M_N=S V_q+\kappa_N(R,q_h,q_h).
\tag{15}
\]

Uniform S=O(1), V_q=O(N^−2), and |κ_N|=O(N^−2) would suffice; the usual stronger topological expectation |κ_N|=O(N^−4) is not needed. Neither symmetry nor positivity establishes these upper estimates. Positivity fixes M≥0 but does not supply an upper sign or magnitude for the cumulant.

Finite-N trace-splitting identities generate precisely such connected multi-traces. Replacing them by products is a hypothesis, not a derivation of their required error. A leading factorization statement o(1), even if proved, would also be insufficient to identify the needed power. The currently available scalar Hardy source certificate cannot supply the missing estimate, because its numerical upper bound already has the positive floor established in the previous audit.

A successful next certificate must establish, with constants uniform in N, either:

1. the actual positive moment bound ⟨R Tr B²⟩≤C N^−4/3, which already suffices by (9), or its stronger planar rate;
2. the original weighted tail/capacity estimate, allowing the sixth moment to remain uncontrolled; or
3. a source-specific low-energy resolvent estimate that avoids these scalar moment requirements.

No such upper certificate was obtained in this pass. Continuing by adding uncontrolled high-degree Ward variables or reusing planar power counting would not be a proof.

## 7. Primary-source check, 6 October 2026

[Lin–Zheng, 2410.14647v2](https://arxiv.org/html/2410.14647v2), §§2.1–2.3 and 4, explicitly imposes factorization to close the single-trace hierarchy. Its displayed level-nine feasible region lacks an unconditional radius upper bound. Its discussion flags low-energy intermediate states, power-law tails, divergent higher finite-N moments, and regulator/order-of-limits problems. It does not establish the finite-N planar mixed-moment bound here.

The later [high-precision multimatrix result, 2507.21007](https://arxiv.org/abs/2507.21007) concerns bosonic models. [Lin’s TASI revision, 2508.20970v3](https://arxiv.org/html/2508.20970v3), reference 115, still lists BFSS Part II as in preparation. Targeted searches located no primary source proving this zero-mode weighted connected estimate. This is a bounded negative literature check, not a claim of exhaustive originality.

## 8. Verification and status

`check_cubic_constants.py` checks the exact rational coefficient, endpoint constants, and a rank-one spherical calibration. These are algebra checks, not numerical evidence for BFSS concentration. The cubic identity, S-dependent lower consequence, elementary Ward identity, and direct-primitive consequence were independently audited; the reports are included. The full BFSS upper bound remains open under the stated assumptions.
