# BFSS Spin9 interference and polarization audit

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


6 October 2026. Target: M_N = ⟨ρ² q_h²⟩ = O(N^(-4/3)).

## Result

No upper bound for the actual fixed-coupling BFSS zero mode was obtained. The off-diagonal interference decomposes exactly into the 36 and 84 irreducible Spin(9) channels. In each channel separately, the averaged squared descendant reduces to the previous diagonal current norm. Expanding that identity leaves an unsigned mixed fermion-bivector term.

A full isotropic average over the 44 real traceless-symmetric polarizations does not remove that term: an explicit exact coefficient of its cubic-interaction part is nonzero. The calculation retains the BFSS interaction coefficient and the physical Gauss constraint. The coordinate evaluation used to check noncancellation is an algebraic operator test, not a quantum state, a ground-state approximation, or a counterexample to an actual-BFSS bound.

This closes the proposed simple spinor/polarization averaging test. A genuinely new estimate is still required. It does not rule out higher-degree certificates, source-dependent weights, or analytic control of the actual zero mode.

## 1 Conventions and domain qualifications

Use Tr(T_A T_B)=δ_AB, tr=Tr/N, [Z_i^A,P_j^B]=iδ_ijδ_AB, and {ψ_α^A,ψ_β^B}=δ_αβδ_AB. Real symmetric 16 by 16 gamma matrices satisfy {Γ_i,Γ_j}=2δ_ij. Products Γ_I have increasing, distinct spatial indices.

Fix real h=hᵀ with Tr_9 h=0 and Tr_9 h²=1. Write

    X_i = h_ij Z_j,
    q = tr(Z_i h_ij Z_j),
    a = tr(Z_i (h²)_ij Z_j),
    D = Σ_Aij h_ij Z_i^A P_j^A,
    A = {q,D}/2 = qD − ia.

The letter A in the last line is an operator; a superscript A on a component is a color index. Put

    Q_α = N^(-1/2) Tr(P_i Γ_i,αβ ψ_β)
          − (i√N/2) Tr([Z_i,Z_j] Γ_ij,αβ ψ_β),
    b_α = N^(-1/2) Tr(X_i Γ_i,αβ ψ_β),
    R_αβ = {Q_α,b_β}.

The physical Hilbert space has the Gauss constraint. All the multipliers used here are gauge invariant, so their descendants stay in that sector, where {Q_α,Q_β}=2δ_αβ H. Assume a normalized Spin(9)-singlet zero mode Ω with Q_αΩ=0 and the required domains and moments.

The polynomial identities first hold on a common smooth core. The norm identities additionally require, for example, q²Ω∈D(H), the displayed projected descendants, and the indicated mixed forms, or justified cutoff limits. Finiteness of M_N alone does not establish these requirements. Existence, uniqueness, and uniform-in-N domain control are not proved here.

The basic relations are

    {b_α,b_β}=aδ_αβ,
    R_αβ+R_βα=2δ_αβ D/N,
    [R_αβ,q]=0  for α≠β,
    [Q_α,q]=−2ib_α/N.

## 2 Explicit fixed-coupling tensor decomposition

The real antisymmetric 16 by 16 spinor matrices have the orthogonal basis

    E_I = Γ_ij  (i<j; 36 matrices),
    E_I = Γ_ijk (i<j<k; 84 matrices),
    Σ_αβ (E_I)_αβ (E_J)_αβ = 16δ_IJ.

Thus Λ²(16)=36⊕84. Define Hermitian coefficients

    r_I = (1/16)Σ_αβ (E_I)_αβ R_αβ,
    F_I = −(i/16)Σ_αβ (E_I)_αβ b_α b_β.

Then, with B_αβ=[b_α,b_β]/2,

    R_αβ = δ_αβ D/N + Σ_I (E_I)_αβ r_I,
    −iB_αβ = Σ_I (E_I)_αβ F_I.

In a spatial basis diagonalizing h, let h=diag(λ_1,…,λ_9), Σ_iλ_i=0. Put Ψ_I=Σ_A ψ^A Γ_I ψ^A. Direct anticommutation gives

    r_ij = [λ_j Z_j·P_i − λ_i Z_i·P_j]/N
           + i(λ_i+λ_j) Ψ_ij/(8N),                       (2.1)

    r_ijk = −i(λ_i+λ_j+λ_k)
            [Tr([Z_i,Z_j]Z_k) + Ψ_ijk/(8N)].             (2.2)

The dot contracts color components. There is no sum over the displayed i,j,k in these formulas.

To check the fermionic factors, the kinetic derivative term before projection is

    −(i/N)Σ_Aij h_ij (Γ_iψ^A)_α(Γ_jψ^A)_β.

For traceless diagonal h,

    Σ_s λ_s Γ_s Γ_ij Γ_s = −2(λ_i+λ_j)Γ_ij,
    Σ_s λ_s Γ_s Γ_ijk Γ_s = +2(λ_i+λ_j+λ_k)Γ_ijk.

Together with the projection factor 1/16, these give exactly the signs and factors in (2.1)–(2.2).

The interaction term before projection is

    −(i/2)Σ_ijk Tr([Z_i,Z_j]X_k)(Γ_ijΓ_k)_αβ.

Its one-form component vanishes because Σ_j Tr([Z_i,Z_j]X_j)=0 for symmetric h. Its three-form coefficient in an arbitrary basis is

    r^V_ijk = −i[Tr([Z_i,Z_j]X_k)
                  + Tr([Z_j,Z_k]X_i)
                  + Tr([Z_k,Z_i]X_j)].                  (2.3)

For diagonal h this is the cubic part of (2.2). In particular it retains the fixed BFSS coupling.

Let

    L_ij = Z_i·P_j − Z_j·P_i − iΨ_ij/4,
    T_ij = Z_i·P_j + Z_j·P_i.

Equation (2.1) is equivalently

    r_ij = −(λ_i+λ_j)L_ij/(2N)
           +(λ_j−λ_i)T_ij/(2N).                         (2.4)

Singletness kills L_ijΩ, but leaves the symmetric shear. The 84 channel retains the independent cubic interaction and its fermion bilinear. Neither channel disappears merely because Ω is a Spin(9) singlet.

## 3 Each irreducible norm sum collapses to diagonal current data

For either gamma sector separately, with dimension d=36 or d=84, the exact Bianchi identity is

    Σ_I [(E_I)_αβ(E_I)_γδ − (E_I)_αγ(E_I)_βδ
          +(E_I)_αδ(E_I)_βγ] = 0.                        (3.1)

An explicit integer Clifford construction and a second independent construction verify all components. It is also the vanishing of the fully alternating four-spinor invariant in the corresponding contraction.

Applying (3.1) to the b Clifford algebra cancels the grade-four Clifford part and gives the operator identity

    Σ_I F_I² = d a²/32.                                 (3.2)

The values are 9a²/8 and 21a²/8.

For α≠β the Hermitian descendant is

    S_αβ = qR_αβ − 2i b_αb_β/N,
    S_αβΩ = Q_α(qb_β)Ω.

Its projected coefficient is

    S_I = q r_I + 2F_I/N.                               (3.3)

Let χ=q²Ω. Exact zero-mode relations give

    qb_βΩ = (iN/4)Q_βχ,
    S_IΩ = (iN/64)Σ_αβ(E_I)_αβ Q_αQ_βχ,
    Hχ = −4iAΩ/N².                                     (3.4)

By (3.1), the fully antisymmetric four-supercharge part in the norm sum vanishes. Its scalar part gives

    Σ_I ||S_IΩ||² = (dN²/128)||Hχ||²
                   = d⟨A²⟩/(8N²).                     (3.5)

This is an exact reduction, not a Cauchy estimate. It is valid separately for 36 and 84, not only for their sum.

Expanding (3.3), retaining the full interference, yields

    ⟨q²Σ_I r_I²⟩ + (2/N)⟨qΣ_I{r_I,F_I}⟩
      = d[⟨A²⟩−⟨a²⟩]/(8N²).                          (3.6)

The unsquared coefficients of q commute with r_I and F_I. The second term is real but has no positivity established here. Summing both sectors gives d=120 and reproduces exactly the previous total off-diagonal identity divided by 16.

Explicitly, if

    I = Σ_{α≠β}⟨q{R_αβ,b_αb_β}⟩,

then

    I = 16i⟨qΣ_I{r_I,F_I}⟩.

I itself is imaginary; the norm contribution −2iI/N is real. A change of sign convention F→−F changes both occurrences consistently.

### What can be removed by a linear combination

A Spin(9)-equivariant positive weight on antisymmetric spinor pairs has the form c_2P_36+c_3P_84, c_2,c_3≥0. Any nonzero such combination of (3.5) retains a positive multiple of the uncontrolled ⟨A²⟩.

The signed combination of (3.6) that cancels both diagonal terms is

    ⟨q²[Σ_84 r_I² − (7/3)Σ_36 r_I²]⟩
      +(2/N)⟨q[Σ_84{r_I,F_I}
                     − (7/3)Σ_36{r_I,F_I}]⟩ = 0.       (3.7)

It is an exact potential/shear balance, with a negative square coefficient and surviving mixed terms. It is not a positive upper-bound certificate. This conclusion concerns the stated invariant scalar weights; it does not cover new coordinate-dependent matrix weights or higher multipliers.

## 4 Cubic Ward contractions do not cancel the interference

The same-source Clifford reduction is

    Σ_β b_β b_α b_β = −7a b_α.

Consequently, summing the most direct cubic Ward identity only reduces to the scalar-dressed linear-fermion identity already audited. Expanding the cubic word produces commutators [R_αβ,b_αb_β]; the norm interference contains anticommutators {R_αβ,b_αb_β}. They cannot be interchanged.

For example, the exact operator expansion is

    {Q_α,b_βb_αb_β}
      = R_αβ b_αb_β − b_β R_αα b_β
         + b_βb_α R_αβ
      = [R_αβ,b_αb_β] − b_β(D/N)b_β  (α≠β).

This shows directly which combination the Ward identity controls.

## 5 Full polarization averaging leaves a nonzero interaction coefficient

Let h be uniform on the unit sphere in the 44-dimensional space Sym_0(9), with Tr h²=1. For the auxiliary Gaussian with covariance

    P_ij,kl = (δ_ikδ_jl+δ_ilδ_jk)/2 − δ_ijδ_kl/9,

the unit-sphere fourth moment is its Gaussian Wick fourth moment divided by 44·46. This Gaussian is only an exact polarization integration device. It is not a proposed bosonic BFSS probability distribution.

Use a fixed coordinate point

    Z_1=T_1, Z_2=T_2, Z_3=T_3, Z_4=…=Z_9=0,

where T_1,T_2,T_3 are normalized embedded SU(2) generators with Tr(T_aT_b)=δ_ab and [T_a,T_b]=i√2 ε_abc T_c. This works at every N≥2 by embedding. Evaluate the polynomial multiplication coefficients, keeping the full fermion Clifford operators.

At this point write

    q = q_0/N,          q_0=h_11+h_22+h_33,
    r^V_I = √2 u_I,

where the only nonzero u_I are

    u_123=q_0,
    u_12k=h_k3, u_13k=−h_k2, u_23k=h_k1  (k=4,…,9).

Also

    F_I = −i/(16N) Σ_ABmn h_mA h_nB
                         ψ^A Γ_m E_I Γ_n ψ^B,

with color A,B=1,2,3 at this coordinate point. The A=B=1 spinor-matrix kernel in the Gaussian average of Σ_I q_0u_I h_mA h_nB Γ_mE_IΓ_n is

    (8/3)Γ_123.

A short hand calculation gives the same coefficient. The I=123 contribution is −4Γ_123/3. Each of the six I=23k contributions is +2Γ_123/3; all other channels contribute zero to this color-diagonal block. Dividing by 44·46 gives

    (1/759)Γ_123.

Therefore the full polarization average contains the nonzero Clifford-bilinear component

    E_h Σ_{I∈84} q r^V_I F_I
       contains −i√2/(12144 N²) ψ^1Γ_123ψ^1.             (5.1)

Equivalently, the real interference (2/N)E_h Σ_I q{r^V_I,F_I} contains

    −i√2/(3036 N³) ψ^1Γ_123ψ^1.                         (5.2)

Both factors in the anticommutator commute for the potential contribution, which explains the extra factor two. The corresponding Hermitian Clifford multiplication operator is nonzero and traceless, so that contribution has both signs on the full fermion module. This is not a claim about its expectation in Ω.

Upon replacing Z by tZ, this contribution has degree t^7. The fermionic part of r_I contributes degree t^4 instead. Thus those multiplication pieces cannot cancel (5.1) as a polynomial identity. The 36 channel has no cubic-interaction multiplication term. In particular an invariant positive combination with nonzero 84 weight does not erase this term merely by adding the 36 channel.

The averaged expression is a permitted Spin(9) scalar. Its nonzero coefficient refutes an operator-level cancellation by this full polarization average. No claim is made that the example is a quantum state, that the actual zero-mode expectation is nonzero, or that every specially weighted polarization identity has been excluded. A full sphere average is stronger than a single orbit average in the relevant sense: its nonzero result also shows that cancellation cannot hold identically on every polarization orbit.

## 6 What changed and what remains missing

The unsigned term has now been identified in irreducible fixed-coupling variables, with exact 36 and 84 norm coefficients and a checked noncancellation under the natural full polarization average. These are finite-N identities; no planar factorization, guessed quantum state, or coupling-changing dilation was used.

The actual upper estimate has not improved. The averaged squared descendants return the uncontrolled current moment ⟨A²⟩ and mixed terms in (3.6), rather than an upper bound on M_N or its comparable moment ⟨a q²⟩. Eliminating ⟨A²⟩ by subtraction produces the indefinite balance (3.7).

To turn this route into an upper certificate requires genuinely new control of the mixed current or of the shear norm, tied to the fixed-coupling zero mode with uniform rank dependence. Alternatively, a different higher-degree/localized certificate could supply a coercive term. Neither input is derived here. Simply repeating the spinor, cubic-Ward, or isotropic-polarization sums does not supply it.

## 7 Reproducibility and source

Run `python3 check_spin9.py`. It uses integer matrices and exact rational arithmetic for its asserted identities; NumPy integer arrays perform the finite matrix products. It checks the Clifford relations, both orthogonal gamma bases, both Bianchi identities, the diagonal-h projection factors, both exact Clifford square sums, and the polarization coefficient 1/759. `checks.json` records the output. `independent_verify_bianchi.py` is a separate implementation of the finite gamma identity.

The BFSS charge and Gauss algebra conventions were cross-checked against Lin and Zheng, *Bootstrapping Ground State Correlators in Matrix Theory, Part I*, Section 1.1, equations (3)–(5), and the real gamma convention in Appendix C.2: https://arxiv.org/html/2410.14647v3 . The factors of N here are the established rescaled conventions of the preceding audit. The reductions and noncancellation check in this note are derived above, rather than attributed to that paper.

This is a finite algebra audit, not a numerical BFSS ground-state calculation, an SDP solution, a literature priority claim, or a proof of the large-N bound.
