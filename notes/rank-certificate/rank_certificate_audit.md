# BFSS rank audit: radial susceptibility certificates lose too much

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


Research checkpoint, 6 October 2026. This is an audit of the conditional finite-rank estimate in [the interacting-threshold note](../interacting-threshold/interacting_threshold_bound.md), not a proof or disproof of the requested large-rank susceptibility bound. Every reference to an actual zero mode assumes its existence, normalization, singletness, and the compatible self-adjoint BFSS realization. The candidate exterior theorem is used only when quoting its susceptibility upper certificate and positive radial moments. No priority claim is made.

## Main conclusions

1. Even setting the exterior radius to zero cannot make the positive-radial-moment certificate establish the target. Its right side is at least order N², by the radius lower bound and Jensen.
2. Keeping the quadrupole exactly gives a much better conditional certificate, but it still requires a mixed moment at order N^(-8/3), stronger than the familiar planar N^(-2) expectation. This is not an innocent restatement of the earlier clipping condition.
3. There is a stronger obstruction using the actual BFSS kinetic and fermion terms: the right side of that exact-quadrupole Hardy certificate is bounded below by the explicit positive constant 2^(-5/4)/243. Consequently this certificate cannot establish any vanishing large-rank target. The result concerns a particular upper-certificate, not the susceptibility. It does not falsify the requested bound.
4. The centered source estimate W₀ ≤ 32N Σ_(a<b) n_a n_b/r_ab² has an unavoidable N factor in this uniform algebraic form: equality holds for two blocks. Changing to canonical relative coordinates moves, rather than removes, its rank dependence. The exact centered cancellation remains essential.

## 1. Definitions and the crude exponent test

Use

    H = P_Z²/(2N) + V + F,      V ≥ 0,
    d = N²−1,                  D = 9d,
    rho² = (1/N) Σ_(i,A) (Z_i^A)²,
    X = sqrt(N) Z,             r = |X| = N rho.

Let eta be a fixed real symmetric traceless 9 by 9 tensor with Tr eta²=1. Set

    q = tr(eta_ij Z_i Z_j),
    a = tr(Z_i (eta²)_ij Z_j),
    S = <rho²>,                A = <a> = S/9,
    Vq = <q²>,                 M = <rho² q²>.

The singlet expectation of q is zero. Here Vq is a variance, not the bosonic potential V.

The previous conditional theorem gives h₄₄ ≥ [2(R_N²+r²)]^(-1), where h=2H. For chi=2<qΩ,H^(-1)qΩ>, its crude consequence is

    A chi ≤ B_rad := 8 A [R_N² <rho⁴> + N² <rho⁶>].          (1)

The previously restored finite-N radius bound is

    S ≥ s_N := (27/16)(1−N^(-2))^(4/3).                     (2)

The underlying primary source is Lin, https://arxiv.org/html/2302.04416, section 2.3; its displayed large-N one-direction lower bound is 3/16. The finite-N factor in (2) is the existing project correction, not a theorem newly attributed to that article. All standard virial/domain assumptions remain in force.

Jensen gives <rho⁴> ≥ S² and <rho⁶> ≥ S³. Thus

    B_rad ≥ (8/9)[R_N² S³ + N² S⁴] ≥ (8/9)N² s_N⁴.        (3)

This is a lower bound on the proposed numerical upper bound, not on A chi. It rules out deriving A chi=O(N^(-2/3)) by making (1)'s right side small. No choice of R_N fixes this.

For exponent bookkeeping, if A=O(N^alpha), R_N=O(N^gamma), <rho⁴>=O(N^mu4), and <rho⁶>=O(N^mu6), sufficient powers for (1) would be

    alpha + 2gamma + mu4 ≤ −2/3,
    alpha + mu6 ≤ −8/3.                                    (4)

These are requirements on a successful positive-moment estimate, not independent BFSS hypotheses that can be chosen at will. In particular (2) and Jensen forbid them. If the physical radius S is order one and R_N is order N, (1) is order N² rather than N^(-2/3).

## 2. Keep the spatial quadrupole, including connected correlations

The exact inverse-form step, before replacing q by its radial maximum, is

    chi ≤ 8 <(R_N²+r²)q²>
        = 8N²[(R_N/N)² Vq + M].                            (5)

Hence the necessary and sufficient numerical condition for this particular RHS to have the target order is

    A[(R_N/N)² Vq + M] = O(N^(-8/3)).                       (6)

When A and R_N/N are bounded above and below by positive constants, both Vq and M must be O(N^(-8/3)). By contrast, the susceptibility target itself only implies Vq=O(N^(-4/3)), through the f-sum inequality

    A chi ≥ N² Vq².                                        (7)

Introduce the positive spatial Gram matrix G_ij=tr(Z_i Z_j), B=G−rho² I_9/9, and Q₂=Tr(B²). Rotational invariance gives for every integrable radial scalar w

    <w q²> = (1/44)<w Q₂>.                                 (8)

Thus the directional information discarded in (1) is the entire traceless Gram norm, not merely the numerical normalization of a fixed tensor. The exact form of (5) is

    A chi ≤ (2N² S/99) <[(R_N/N)²+rho²] Q₂>.                (9)

For N≥4, G can be proportional to I_9 at a single configuration, so no pointwise color-rank obstruction forces Q₂ to be large. This fact by itself does not control the zero-mode probability of such configurations.

The mixed moment decomposes as

    M = S Vq + Cov(rho²,q²).                                (10)

Since <q>=<rho² q>=0, that covariance is also the corresponding connected three-observable cumulant. Ordinary planar power counting would give Vq=O(N^(-2)) and the connected three-trace term O(N^(-4)), if valid uniformly for this threshold state. It would therefore make M=O(N^(-2)), yielding only an order-one bound in (5). Those planar rates are not proved here or assumed as facts. A proposed super-planar cancellation in (10) is constrained by Section 4 below.

Comparison with clipping: the earlier bounded-primitive criterion is satisfied if <a q²>=O(N^(-2)), by Markov at |q|~N^(-2/3). Since a≤rho², a bound M=O(N^(-2)) is sufficient for that clipping route. Equation (6) is substantially stronger and is not a relabeling of the clipping proposition.

### 2.1 Exact return to the clipping normalization

For one fixed real supercharge component, use Q_alpha²=H and

    b_alpha = (iN/2)[Q_alpha,q],
    b_alpha² = a/2,
    K_N(s) = s<b_alpha Ω,(H+s)^(-1)b_alpha Ω>.

The prior smooth clipping certificate is

    K_N(s) ≤ (1/2)<a 1_(|q|>L)> + sN²L².

If the unproved upper estimate M≤C_M/N² holds, then a≤rho² and Markov give, with L=kappa N^(-2/3) and s=sigma N^(-4/3),

    K_N(s) ≤ [C_M/(2kappa²)+sigma kappa²] N^(-2/3).

For sigma>0, choosing kappa⁴=C_M/(2sigma) gives

    K_N(s) ≤ sqrt(2 C_M sigma) N^(-2/3),
    ||1_((0,s))(H)b_alpha Ω||² ≤ 2sqrt(2 C_M sigma) N^(-2/3).

These constants use the earlier smooth clipping convention |T_L|≤2L and its one-component normalization; summing over 16 components multiplies the estimates by 16. They establish an implication, not M≤C_M/N². The new lower bound M≥v_0/(8N²) is compatible with precisely that proposed upper rate.

## 3. Actual BFSS input: fermion norm, virial, and a variance lower bound

Let D_f=Σ_i Gamma_i tensor ad(Z_i) on the 16d-dimensional one-particle Majorana space. With Tr(T_A T_B)=delta_AB and {psi,psi}=delta,

    Tr(D_f²) = 16 Σ_i Tr_ad(ad(Z_i)²)
             = 32N Tr Σ_i Z_i² = 32N² rho².

The eigenvalues of the pure-imaginary antisymmetric Hermitian matrix D_f come in ±lambda pairs. For F=−psi^T D_f psi/2, diagonalizing each Majorana pair gives

    ||F(Z)|| ≤ (1/4)Tr|D_f|
             ≤ 4 sqrt(2) N sqrt(d) rho =: C_N rho.          (11)

This is a pointwise operator norm on the full fermion module. It uses no factorization or spectral ansatz.

The usual dilation virial identity and zero energy give <T>=<V> and <F>=−2<T>. Therefore

    <T> ≤ (C_N/2)<rho>
        ≤ 2 sqrt(2) N sqrt(d) S^(1/2).                     (12)

The previously derived shear spectral moments are

    m₁ = 2A/N²,            m₃ ≤ 2<T>/N⁴.                   (13)

The inequality for m₃ is sufficient. It can be justified without assuming the double-commutator expression as an operator identity. For D_eta=eta_ij Z_i^A P_j^A, let U(t)=exp(itD_eta). The exact shear-transformed energy curve has, up to the immaterial replacement t→−t,

    T(t) = <T> Tr exp(−2t eta)/9,
    F(t) = <F> Tr exp(t eta)/9,
    V(t) = <V>[(Tr exp(2t eta))²−Tr exp(4t eta)]/72.

Its second derivative at zero is (4<T>+7<V>+<F>)/9=<T>. Since HΩ=0,

    H[(U(t)−I)Ω/t] = <U(t)Ω,H U(t)Ω>/t² → <T>/2.

D_eta Ω is in L²: the scalar ground-state identity with g=rho bounds its weighted first derivatives using <rho³><infinity. Strong convergence of the unitary difference quotients and closed-form lower semicontinuity then give H[D_eta Ω]≤<T>/2. Bounded clipped scalar multipliers first give qΩ in the closed form domain, using <q²><infinity and <|grad q|²><infinity. The distributional identity HqΩ=−2iD_eta Ω/N² on the physical form core has an L² right side. The representation theorem then gives qΩ in D(H), without assuming a separate maximal-realization theorem. This proves (13). Positive moments through degree four suffice for this source/domain step; the candidate theorem supplies them. Equivalently, one may retain the existing shear-sum-rule domain hypotheses explicitly.

Spectral Hölder m₁≤m₀^(2/3)m₃^(1/3) and (12) now give

    Vq ≥ 2A^(3/2)/(N sqrt(<T>))
       ≥ [2^(1/4)/27] S^(5/4)/(N^(3/2)d^(1/4))
       ≥ [2^(1/4)/27] S^(5/4) N^(-2).                     (14)

With R_N comparable to N, (14) alone already prevents the exact-q certificate from tending to zero. It does not contradict Vq=O(N^(-4/3)), which is the weaker necessary condition (7).

## 4. A radius-independent obstruction to the exact-q certificate

An inverse-radius bound prevents the variance required by (14) from being placed arbitrarily close to rho=0.

The ordinary ambient Hardy inequality in D=9(N²−1) real dimensions gives, on the physical subspace as well,

    T[u] ≥ (D−2)²/(8N²) ||rho^(-1)u||².                    (15)

The finite-dimensional fermion fiber and restriction to SU(N)-invariant vectors do not invalidate a scalar componentwise Hardy inequality.

For eta0>0 set g_eta0=(rho²+eta0²)^(-1/4). This is a bounded smooth multiplier with bounded gradient at each fixed eta0; approximations at infinity justify its use on Ω. The exact scalar ground-state identity and |grad_Z rho|²=1/N give

    H[g_eta0 Ω] = (1/(2N))<|grad_Z g_eta0|²>
                ≤ (1/(8N²))<rho^(-2)g_eta0²>.              (16)

Combining (11), (15), V≥0, and rho g_eta0²≤1 yields

    [(D−2)²−1]/(8N²) <rho^(-2)g_eta0²> ≤ C_N.

Monotone convergence as eta0↓0 proves the explicit bound

    I₃ := <rho^(-3)>
       ≤ 32 sqrt(2) N³ sqrt(N²−1)
          /[(9(N²−1)−2)²−1] =: J_N.                       (17)

For N≥2, J_N≤32 sqrt(2)/39, a convenient nonsharp uniform constant. No inverse moment was assumed to obtain it.

Pointwise, ||eta||_op²≤8/9 and G≥0 imply q²≤b rho⁴ with b=8/9. Hölder then gives

    Vq ≤ b^(2/9) M^(7/9) I₃^(2/9),
    M ≥ b^(-2/7) I₃^(-2/7) Vq^(9/7)
      ≥ b^(-2/7) J_N^(-2/7) Vq^(9/7).                     (18)

Combining (2), (14), and (18), there is an explicit constant c>0 independent of N≥2 such that

    M ≥ c N^(-18/7).                                       (19)

The RHS of the susceptibility certificate is therefore constrained by

    B_q := 8A[R_N² Vq + N² M] ≥ c' N^(-4/7),               (20)

regardless of R_N. Since N^(-4/7)/N^(-2/3)=N^(2/21) diverges, B_q cannot be O(N^(-2/3)). This excludes closing the desired target by (5), even if a rank-uniform radius and every needed connected-moment estimate were available. In particular the numerical requirement M=O(N^(-8/3)) cannot hold under these hypotheses.

Important direction: A chi≤B_q and B_q≥c'N^(-4/7) do not imply A chi≥c'N^(-4/7). An upper estimate can be much larger than the quantity being estimated. The true susceptibility target remains open.

### 4.1 Stronger conclusion: the certificate is bounded below by a constant

The regularized-power argument gives, for every integer k≥3 with D−2>k−2,

    I_k := <rho^(-k)>
        ≤ L_(N,k) I_(k−3),
    L_(N,k) := 8N² C_N/[(D−2)²−(k−2)²].                    (21)

Use g_eta0=(rho²+eta0²)^(-(k−2)/4). Its derivative loss is (k−2)²/(8N²), and rho g_eta0²≤rho^(-(k−3)); the same bounded-multiplier argument proves (21) recursively. No uniform-in-k domain assertion is needed: there are only finitely many steps at each fixed N.

Set

    k_N = 3 floor(D/6).

For N≥2, 3N²≤k_N≤D/2. For every 3≤k≤D/2,

    (D−2)²−(k−2)² ≥ D(3D/4−2) ≥ (2/3)D² ≥ 24N⁴,
    8N²C_N ≤ 32 sqrt(2) N⁴.

Here D≥27 and D≥6N². Consequently L_(N,k)≤4sqrt(2)/3<2. Iteration from I_0=1 gives

    I_(k_N) ≤ 2^(k_N/3),
    P(rho≤1/2) ≤ 2^(-k_N) I_(k_N)
                ≤ 2^(-2k_N/3) ≤ 2^(-2N²).                (22)

This is an actual zero-mode configuration-probability consequence of the stated BFSS hypotheses. It does not follow from rotational invariance alone.

The coarse I_3≤2 consequence of (17) and Jensen give S≥s_0:=2^(-2/3), independently of the prior Lin finite-N correction. Equation (14) thus supplies

    Vq ≥ v_0/N²,           v_0 := 2^(-7/12)/27.

Using q²≤b rho⁴, b=8/9, and the elementary N²2^(-2N²)≤1/64 for N≥2,

    <q² 1_(rho≤1/2)> ≤ (b/16)2^(-2N²)
                     ≤ b/(1024N²) < v_0/(2N²).

The remaining quadrupole variance is at rho>1/2. Hence

    M = <rho²q²>
      ≥ (1/4)<q²1_(rho>1/2)>
      ≥ v_0/(8N²).                                        (23)

The explicit conclusion is

    B_q = 8A[R_N²Vq+N²M]
        ≥ A v_0 ≥ 2^(-5/4)/243 > 0,                       (24)

for every N≥2 and every R_N≥0. This strengthens (20): the exact-q scalar Hardy certificate cannot prove any bound tending to zero. Its required mixed-moment premise in (6) is impossible under the same BFSS assumptions. The simpler fixed-k proof remains above because it already shows the target-rate mismatch without a growing-k iteration.

Again, (24) is not a lower bound on A chi. The actual susceptibility may be much smaller than this certificate. Nor does (23) contradict a planar upper bound M=O(N^(-2)); those rates are compatible.

## 5. Centered rank constants and why rescaling does not remove them

Use the independently checked centered coefficients from [the centered-coefficient findings](REVIEW_FINDINGS.md#centered-coefficient-cross-check). For an edge ab and a triangle abc,

    W_ab = 32 n_a n_b(n_a+n_b)/r_ab²,
    W_abc = n_a n_b n_c[32s/p−2(K²)²/(s p³)],

where s is the sum and p the product of the three side lengths. Since

    s/p = 1/(r_ab r_bc)+1/(r_bc r_ca)+1/(r_ca r_ab)
        ≤ 1/r_ab²+1/r_bc²+1/r_ca²,

and the area-dependent term is subtracted, summing every triangle once gives

    W₀ ≤ 32 Σ_(a<b) n_a n_b[(n_a+n_b)+Σ_(c≠a,b)n_c]/r_ab²
       = 32N Σ_(a<b) n_a n_b/r_ab².                       (25)

At two blocks, (25) is an equality. Thus an all-partition bound with an o(N) coefficient multiplying that same root sum is impossible.

For two blocks n and m, n+m=N, put mu=nm/N and canonical relative coordinate y=sqrt(mu)(z_a−z_b). Then

    T_cent = −Delta_y,
    W₀ = 32 (nm)²/|y|²,
    T_cent ≥ (49/4)|y|^(-2).

The ratio of the uncanceled coefficient to the relative Hardy coefficient is 128(nm)²/49. It grows as N⁴ for balanced blocks and N² for a 1+(N−1) split. This ratio is invariant under an overall coordinate rescaling. If a perturbation estimate only gives an error epsilon W₀, paying it by the two-block center Hardy term requires epsilon of order (nm)^(-2) or smaller. This is a statement about that particular error majorant; the actual perturbation might have better cancellation, which must be proved.

The original centered formula cancels exactly against S*H_f^(-1)S. It would be wrong to treat W₀ itself as a surviving repulsive/attractive BFSS potential. Equation (25) gives a useful polynomial rank inventory but does not bound the nonlinear off-center errors, partition derivatives, global exterior radius, or zero-mode susceptibility.

## 6. What information must replace this certificate

The loss is structural: at canonical radius r~N the all-vector radial coercivity assigns an energy scale N^(-2) to every 44-vector. The quadrupole's actual spectral distribution need not live at that scale. Its f-sum and shear moments constrain positive spectral moments, but do not supply an upper inverse moment. A source-specific low-energy bound, a sufficiently sharp source resolvent construction, or the earlier bounded primitive/clipping estimate can in principle retain the missing information.

Nothing here excludes planar-scale M=O(N^(-2)), the clipping target, or A chi=O(N^(-2/3)). What is ruled out is closing the susceptibility target solely by the global scalar radial inverse weight in (5), even after restoring the exact spatial quadrupole.
