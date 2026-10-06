# Local Schur comparison on the form domain

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 1. Statement and inputs

Fix a partition of a finite N. Put

    r_* = min_e r_e,    W_p = sum_e r_e^(-p),
    H_s = H_I + T_C,    H_exc = sum_e(H_fast,e-E_0,e).

The internal tube is alpha_a+alpha_b <= kappa r_ab. The fast tube has |Y| < sigma r_\*. There is no bound on ratios of unrelated r_e and no internal spectral-gap assumption. H_I is the complete interacting colored internal form. T_C on the full fiber retains the intrinsic normal connection. On the slow bundle, H_s denotes the center-plus-internal model identified by internal radial transport with the A=0 vacuum line. Its unperturbed internal forms are the colored ones; no lower-rank physical-sector Hardy theorem is used.

For every epsilon>0, there are positive kappa, sigma, R and a smooth even normalized cutoff vacuum U_sigma supported strictly inside the fast tube such that, for r_\*>=R,

    (1-epsilon) H_s[f] - epsilon W_2[f]
       <= F_sigma[f]
       <= (1+epsilon) H_s[f] + epsilon W_2[f],              (1.1)

where the actual zero-energy variational Hamiltonian Schur form is

    F_sigma[f] = inf_{v in Q(H), U_sigma^*v=0}
                          H[U_sigma f+v].                 (1.2)

Here Q(H) denotes the CLOSED QUADRATIC-FORM DOMAIN of the Hamiltonian, not its operator domain D(H). Orthogonality is fiberwise over the slow variables. For every f in Q(H_s), the infimum is attained by a unique v_f in Q(H) with U_sigma^\*v_f=0. The form is closed on the slow model's form domain, interpreted with Dirichlet support on the selected branch. The constants depend on the fixed partition and epsilon, never on r_max/r_\*.

Inputs proved in the companion notes are:

1. The exact intrinsic kinetic identity and normalized matrices from Appendix A.
2. The rootwise all-vector connection estimates in Appendix E and differential-curvature identities in Appendix G.
3. The actual H1/H2 inventory, finite source graph grading, and operator identity

       ||W-S^*H_exc^(-1)S|| <= C_N kappa W_2,              (1.3)

   from Appendix D . Here S=H1 U is the actual source, not a transported replacement.
4. The graph-local complete-slow-form bound for Z=-H_exc^(-1)S:

       H_s[Zf] <= C R^(-3)H_s[f]+C kappa W_2[f]+C W_5[f], (1.4)

   including spectator-vacuum derivatives, from Appendix C and the actual-source continuation.
5. The colored complementary reserve. A fixed positive part of the actual square J[v]=||A p_s v||^2 can be retained:

       H[v] >= (1-delta)(H_s[v]+H_exc[v])+c_0 J[v]         (1.5)

   on the cutoff complement, after choosing the parameters and exterior radius. For example c_0=1/2 is allowed. This is NOT another copy of the original full Gauss square.

This note supplies the mixed and diagonal-remainder estimates needed to assemble these inputs. It never inverts H_I or expands a resolvent in internal momenta.


## 2. Exact error-column factorization, including spin

Use the common positive-fast/positive-slow convention

    H_kin = ||p_s u||^2+||p_F u||^2+||a u+A p_s u+s u||^2,
    p_s=(g_C^(-1/2)p_C,p_I),
    a=W^(1/2)M^(-*) (C+N_Y)^*p_F,
    s=-W^(1/2)M^(-*)S_f.

The scalar density term is added separately. Set

    d_0=F^(-1)C^*p_F,  P=L-J_2,  Z_m=F^(-1)P^*,
    T=(I+Z_m)^(-1),  n=F^(-1)N_Y^*p_F,
    X=n-Z_m d_0,  s_0=-F^(-1)S_f,
    q=X+s_0,  X_1=n-F^(-1)L^*d_0,  X_2=F^(-1)J_2^*d_0.

The symbol Z_m is an inverse-matrix error, distinct from the dressing Z. Exactly,

    a+s = W^(1/2)(d_0+Tq),

and, as ordered first-order forms,

    ||(a+s)u||^2-||d_0u||^2
      =2 Re<d_0u,(X_1+s_0)u> + 2 Re<d_0u,X_2u>
       -2 Re<Z_m^*d_0u,Tq u> +||Tq u||^2
       +||K^*(d_0+Tq)u||^2.                              (2.1)

The first line's first term is exactly the fast-orbital/spin part of H1. No derivative has been moved through an inverse matrix. The remaining apparently dangerous d_0-X_2 product factors exactly:

    <d_0u,X_2u>
       =<C_Y F^(-1)d_0u,C_Y R^(-1)d_0u>.                 (2.2)

Every factor on the right of (2.1)-(2.2), after removing the displayed H1 term, belongs to the finite error-column list

    X_1, X_2, Z_m^*d_0, K^*d_0,
    C_Y F^(-1)d_0, C_Y R^(-1)d_0, s_0,

followed by uniformly bounded left multiplication matrices. Their all-vector estimates are

    ||E u||^2 <= C[(lambda H_exc)[u]+W_2[u]],
    lambda=sigma^2+r_*^(-3).                              (2.3)

For the spin column the stronger bound ||s_0u||^2<=CW_2[u] holds. On the uncut vacuum, and on each fixed-degree Gaussian/Fock coefficient vector normalized in its own roots,

    ||E U f||^2 <= C W_2[f].                              (2.4)

For (2.4), a same-edge Y_ep_e/r_e costs C/r_e; a triangle Y_fp_e/r_g costs C sqrt(r_e/r_f)/r_g, whose square is bounded by C W_2,t by r_e<=r_f+r_g. Root-preserving pair matrices have uniformly bounded normalized coefficients. All inverse matrices in the exact expressions remain bounded LEFT factors. The same proof therefore works on a fixed finite excited degree, with a degree-dependent constant, and does not introduce r_max.

For a complementary v, W_2[v]<=C R^(-3)H_exc[v]. Polarization of each product in (2.1)-(2.2) consequently gives, for any eta>0,

    |R_fast[Uf,v]| <= eta H_exc[v]
                         +C_eta(sigma^2+R^(-3)) W_2[f].   (2.5)

This includes spin-fast and spin-square remainders. It is the central reason a finite inverse-square constant is not left unpaid: no Taylor remainder is ever paired directly with an unassigned d_0 vacuum norm.

For diagonal matching, retain the quadratic terms in (2.1), replace T by I, q by X_1+s_0, Z_m by F^(-1)L^\*, and retain (2.2) and ||K^\*d_0||^2. These are precisely the corresponding H2 terms. Each discarded product has one additional uniformly O(sigma) factor and two low error columns. Hence

    |R_fast[Uf]-R_fast,H2[Uf]| <= C sigma W_2[f].          (2.6)

One may obtain an additional inverse-radius improvement from Gaussian moments, but it is unnecessary. The order of the two operations matters: first perform the exact error-column factorization, then bound the inverse difference. Doing them in reverse would expose the forbidden remote vacuum mass.


## 3. Other nondifferential fast terms

The actual V3 and linear-Y Yukawa are exactly the remaining H1 terms; there is no omitted higher polynomial potential. They are boson-odd, so their diagonal expectation on U or an even cutoff U_sigma is zero.

The quartic potential is a sum of squares of quadratic fast-coordinate contractions. In addition to the distinct-root Q/P estimate already proved, the repeated-root estimate is

    ||chi Y_e^2 u||^2 <= C sigma^2 h_e[u]+C r_e^(-2)||u||^2. (3.1)

Split the input into Q_e and P_e, bound one Y_e by sigma r_\* on Q_e, use ||Y_e Q_eu||^2<=Cr_e^(-2)h_e[u], and use the exact fourth Gaussian moment on P_e. This gives

    0<=V4[u]<=C sigma^2 H_exc[u]+C W_2[u],
    V4[Uf]<=C W_2[f].                                    (3.2)

Thus its low/complement cross obeys the same bound as (2.5). Its full diagonal expectation belongs to W and is retained there.

The density multiplier satisfies |V_d|<=CW_2. Its mixed term is paid by the complementary L2 gap:

    |<Uf,V_d v>|<=eta H_exc[v]+C_eta R^(-3)W_2[f].         (3.3)

The leading coefficient V_d,2 is the one specified by the exact H2 inventory, including the slow density, fast Hessian, and orbital ordering terms. Differentiating the normalized matrices in the exact density formula and subtracting their zero-fast-coordinate jets gives

    |V_d-V_d,2|<=C sigma W_2                              (3.4)

on the tube. Each normalized inverse and its required derivatives are bounded in its own root scale. More explicitly, V_d uses two coefficient derivatives, and one additional fast derivative of that finite rational expression is bounded by C/r_\*^3; integrating it from Y=0 gives C|Y|/r_\*^3<=C sigma W_2. The leading zero-fast-coordinate coefficient includes the quadratic determinant jet before fast differentiation. This is a density-coefficient estimate, not a bound on d_0^2. Equations (3.3)-(3.4) settle both density uses.

The frozen E_0 is a separate scalar multiplier. It has zero U-v cross because it commutes with the vacuum projection. Its incident payment is

    |E_0[u]|<=C R^(-3)H_I[u]+C kappa W_2[u].              (3.5)

It is never included in H_exc or in a virtual denominator.


## 4. Scalar fast-slow orbit cross: complete charges instead of bare t_I

Write beta=A^\*a, with internal components beta_j=b_j(Y;s) dot p_F. The b_j are real, scalar in internal Clifford factors, and commute with all internal potential-charge coefficients. Let

    d_j=div_F b_j,    beta_hat,j=beta_j-(i/2)d_j,
    C_alpha(beta_hat)=sum_j c_(alpha,j) beta_hat,j.

The differentiated connection lemma and its explicit rootwise decomposition imply

    sum_j ||beta_hat,j v||^2 <= C(lambda H_exc[v]+W_2[v]),
    sum_j ||beta_hat,j U f||^2 <= C(kappa^2+sigma^2)W_2[f], (4.1)

and

    sum_jk ||(partial_Aj beta_hat,k)U f||^2
                           <= C r_*^(-2)W_2[f].          (4.2)

The SMALL low-leg divergence estimate in (4.1) is essential. Directly, b=A^\*B with A=O(sigma), B=O(kappa+sigma), partial_Y A=O(r_\*^(-1)) and partial_Y B=O(r_\*^(-1)). Hence

    |div_F b|<=C(kappa+sigma)/r_*.

Together with the stronger rootwise estimate for A^\*d_0 and the O(sigma) factor multiplying a-d_0, this proves the second line of (4.1). It is not inferred from a coarse O(1/r_\*) divergence bound.

### 4.1 Exact linear charge identity

Polarize the following identity, initially on the smooth core:

    2 Re sum_j <p_j u,beta_j u>
      =2 Re (1/16)sum_alpha <Q_alpha u,C_alpha(beta_hat)u>
         -R_der[u]+(1/2)sum_j <u,(partial_Aj d_j)u>.      (4.3)

Here R_der is the fixed bounded-Clifford contraction of
partial_j beta_hat,k-partial_k beta_hat,j. To verify it, expand the exact shifted averaged-charge identity and subtract the beta-square. The beta-beta curvature in C_alpha(beta_hat)^2 cancels the beta-beta curvature in the full shifted charge identity. Only the derivative curvature remains. The raw-versus-symmetric cross contributes +(1/2)partial_A d, with this sign. No anticommutator with the internal potential survives the spinor average.

The first term in the polarized identity contains

    <Q(Uf),C(beta_hat)v>  and  <C(beta_hat)Uf,Qv>.

The first is bounded using (4.1), the complementary gap, and

    (1/16)sum ||Q_alpha(Uf)||^2 <= C(H_s[f]+W_2[f]).

The second uses the full H_I[v] reserve and the small low-leg estimate in (4.1). No constant fraction of bare t_I is spent. Since each derivative-curvature operator is symmetric, it can be moved onto U in a mixed pairing. Equation (4.2) and the complementary gap then give a C_eta R^(-3)W_2 cost. The scalar term has the same payment.

Consequently the complete internal scalar-orbit mixed form obeys

    |R_orb,I[Uf,v]| <= eta(H_I[v]+H_exc[v])
       +C_eta lambda H_s[f]
       +C_eta(kappa^2+sigma^2+R^(-3))W_2[f].              (4.4)

This is uniform over unrestricted internal momenta and colored internal states. The center component obeys the same inequality by ordinary center-kinetic Cauchy-Schwarz, with its actual normal connection retained. Normal-frame generators are not estimated by a vacuum Berry scalar on arbitrary v.

### 4.2 Independent incident-row verification

There is a second direct check of the high-momentum issue. With U=g times its fermion vacuum and real Gaussian g,

    (beta_j+beta_j^*)U
        =i(2 b_j dot Omega Y-div_F b_j)U.

Ground-state integration by parts therefore gives

    ||H_exc^(-1/2)(beta_j+beta_j^*)U||^2
                              <=C||b_jU||^2.            (4.5)

For an internal row belonging to block a, factor the exact coefficient as

    b_a=I_Y,a F^(-1)[T^* W M^(-*)(C+N_Y)^*].

The bracket is uniformly O(kappa+sigma), while I_Y,a F^(-1) contains only Y_e/r_e on edges incident to a. Thus

    ||b_aU||^2<=C(kappa+sigma)^2 w_a,
    w_a=sum_(e incident a)r_e^(-3).                       (4.6)

This proves directly that integrating the single slow derivative in the orbit cross cannot create an unrelated internal-radius loss. It also accounts for the adjoint fast divergence, rather than dropping it. Either (4.3) or (4.5)-(4.6) supplies the needed first-derivative estimate; the proof above uses (4.3).

### 4.3 Diagonal orbit remainder

Let beta_1 be the first homogeneous slow-orbit coefficient: use the linear slow column with F^(-1), the leading C_Y^\*+FK center term, and d_0. Its raw diagonal compression, including derivatives of its coefficient at A=0, is retained in W. Together with the corresponding V_d,2 orbital-density term, it equals the V_orb in the density-shifted inventory. In particular the inventory term -2 sum_mu rho_(0,mu) j_mu belongs to V_d,2 in the present unshifted-kinetic convention; it is counted exactly once, not inserted a second time in the raw beta_1 compression. Only the SUM of these contributions is identified with the H2 scalar. The raw beta_1 contribution is NOT discarded on the grounds that beta_1 vanishes at A=0.

The exact identities for A^\*d_0 in the rootwise helper express beta-beta_1 as a sum with one extra O(sigma) factor multiplying a controlled error column. They give

    ||(beta-beta_1)U||^2+||(div(b-b_1))U||^2<=C sigma^2 W_2,
    ||partial_A(beta-beta_1)U||<=C sigma r_*^(-1) W_2^(1/2).

Differentiate those identities, not an abstract norm bound: the extra fast-degree factor remains when F or F^(-1)C^\* is differentiated. Applying (4.3) to this difference gives, for any eta>0,

    |R_orb,diag[f]|<=eta H_s[f]
                             +C_eta(sigma+sigma^2)W_2[f]. (4.7)

This retains the exact leading coefficient while paying only its true higher-order remainder.


## 5. Spin-slow, slow-orbit square, and induced center metric

### 5.1 Spin-slow cross

Put c=A^\*s. Its internal row a satisfies the exact incident coefficient bound

    |c_a|^2<=C W_2 sum_(e incident a)|Y_e|^2/r_e^2,
    ||c_a U||^2<=C w_a W_2.                              (5.1)

For the mixed form, integrate its single slow derivative onto the smooth coefficient cU f. This is legitimate for the complete matrix c, with no commutation claim about internal Clifford matrices. The coefficient of partial_Aa f has norm squared bounded by C w_a W_2. The complementary gap therefore gives the weighted derivative cost

    C(W_2/r_*) sum_a w_a t_a[f]
       <=C R^(-3)[R^(-3)H_I[f]+kappa W_2[f]].             (5.2)

The exact inverse derivative formula, incident left factor I_Y,a F^(-1), and finite Gaussian derivative moments give

    sum_a ||partial_Aa(c_aU)||^2
       <=C r_*^(-2)(sum_a w_a)W_2+C(sum_a w_a)W_2^2
       <=C R^(-5)W_2.                                   (5.3)

Spectator-vacuum derivatives are included in the W_2^2 term. Center derivatives have the same or better bound and are paid by T_C. After the complementary gap, (5.2)-(5.3) are smaller than the mixed budget in (4.4).

For the DIAGONAL, (5.1) alone would leave a fixed W_2 constant and is insufficient. The leading coefficient c_1 is boson-odd: its internal part is -I_Y F^(-2)S_f, with the corresponding linear center row. U, its slow derivatives, and the even cutoff are boson-even. Its diagonal cross is exactly zero. Every term of c-c_1 has an additional inverse/metric difference of size O(sigma), so

    ||(c_a-c_1,a)U||^2<=C sigma^2 w_a W_2.

Weighted Young and sum_a w_a alpha_a<=C kappa W_2 yield only

    eta R^(-3)H_s[f]+C_eta(kappa+sigma^2)W_2[f].          (5.4)

This is the specific parity use that prevents an unpaid diagonal constant.

### 5.2 The positive square actually retained by completion

Let J[u]=||A p_su||^2. Its low-leg estimate is

    J[Uf]<=C R^(-3)H_s[f]+C kappa W_2[f]+C W_5[f].        (5.5)

For derivatives on f, the exact incident factorization gives sum_a w_a t_a and the analogous center coefficient. Convert only these incident weights using

    sum_a w_a t_a<=C R^(-3)H_I+C kappa W_2.

Derivatives on U are finite degree-two Gaussian/Fock vectors. Their rootwise moments give W_5, including spectator products W_3W_2<=C_NW_5. The Berry connection adds its already proved smaller incident contribution. Thus

    |<A p_sUf,A p_sv>|
       <=eta J[v]+C_eta[R^(-3)H_s[f]+kappa W_2[f]+W_5[f]]. (5.6)

Equation (5.6) uses only the true postcompletion reserve J. No original full Gauss square is used.

### 5.3 Center metric

The direct center coefficient differs from identity by

    g_C^(-1)-I=-K^*(I+KK^*)^(-1)K.

It is O(sigma^2) on arbitrary tube vectors. On a Gaussian low leg its squared coefficient norm is O(R^(-6)); derivatives on U have the corresponding W_5-or-smaller moments. Ordinary center-form Young controls the mixed term by eta T_C[v]+C_eta R^(-6)T_C[f]+C_etaW_5[f]. Its diagonal has bound C R^(-3)T_C[f]+CW_5[f]. No internal derivative is involved.

### 5.4 Direct slow kinetic cross

The preceding orbit estimates do not replace the cross from the DIRECT center and internal kinetic forms. For v perpendicular to U, differentiate U^\*v=0 and integrate the remaining slow derivative once. In a covariant vacuum-line frame the complementary source is

    -2 sum_j (1-P)(nabla_j U) nabla_j f
          -(1-P)sum_j nabla_j^2 U f.                    (5.7)

This is a form identity and contains no second derivative of f. Internal potential and Yukawa terms commute with the vacuum injection and have zero mixed compression. The same is true of E_0. Normal-bundle derivatives are kept covariantly in (5.7).

An internal derivative in block a differentiates only incident pair vacua. After removing its scalar Berry part, each term has a fixed excited sector on that pair, norm C/r_e, and gap at least c r_e. Its squared H_exc-dual norm is therefore at most C w_a. The center derivative satisfies the analogous sum of pair weights. Second derivatives have active-pair and two-pair finite excitation terms, of norm at most C/r_e^2 or C/(r_e r_f). Their dual squared norm is bounded by C W_5; spectator products are included using W_3W_2<=C_NW_5. Thus ordinary source/gap Young gives

    2|H_s[Uf,v]| <= eta H_exc[v]
           +C_eta[R^(-3)H_s[f]+kappa W_2[f]+W_5[f]].    (5.8)

The conversion on the right is incident: sum_a w_a t_a<=C R^(-3)H_I+C kappa W_2. It is performed before replacing w_a by its maximum. The cutoff version gains only the source-specific exponentially small errors in Section 7. This explicitly includes the direct slow derivative source in the mixed ledger.


## 6. Summary of the mixed and diagonal estimates

Let B[v]=H_s[v]+H_exc[v]+J[v]. After a fixed finite allocation of eta to the preceding terms, for every eta>0 the exact mixed form has the decomposition

    H[Uf,v]=<Sf,v>+R_mix[f,v],

with

    2|R_mix[f,v]|
       <=eta B[v]+a_(eta)(kappa,sigma,R)H_s[f]
                         +b_(eta)(kappa,sigma,R)W_2[f],  (6.1)

where one can choose finite constants such that

    a_(eta)<=C_eta(sigma^2+R^(-3)),
    b_(eta)<=C_eta(kappa+kappa^2+sigma^2+R^(-3)).          (6.2)

The exact diagonal is

    H[Uf]=H_s^B[f]+E_0[f]+W[f]+R_diag[f],                (6.3)

and for an independently chosen theta>0,

    |R_diag[f]|<=theta H_s[f]
         +C_theta[kappa+sigma+sigma^2+R^(-3)]W_2[f]
         +C R^(-3)H_s[f].                               (6.4)

The H_s^B comparison is the full averaged-charge Berry comparison from source Section 4.2 of Appendix F:

    |H_s^B[f]-H_s[f]|
       <=theta H_s[f]+C(theta^(-1)kappa^4+kappa)W_2[f].  (6.5)

Equations (3.5), (6.3)-(6.5) keep every internal potential and Yukawa term. No frozen slow-momentum resolvent has appeared.


## 7. Cutoff vacuum, derivative tails, and source parity

Fix sigma>0 before increasing R. Let h=(sum_e r_e^(-2))^(-1/2), and choose a smooth even radial chi=chi_0(|Y|^2/(sigma_0^2h^2)), with 0<sigma_0<c_N sigma fixed, equal to one on an inner tube and supported strictly inside the validity tube. Put

    U_sigma=chi U/n,    n=||chi U||.

This is intrinsic and residual-equivariant. Its support is projection-stable. The normalized Gaussian coordinates xi_e=r_e^(1/2)Y_e have uniformly positive bounded covariance matrices. On the cutoff transition region,

    sum_e |xi_e|^2 >= c sigma_0^2 r_*^3.

Consequently any fixed-degree root-normalized Gaussian polynomial has a tail bounded by

    tau_R=C_(N,sigma_0) exp(-c_N sigma_0^2 R^3),           (7.1)

after absorbing fixed powers of R into the exponential. These estimates do not contain r_max. They apply after the rootwise error-column factorization, and to finite graph source/dressing coefficients with their own graph weights.

One must not claim that ||p_F(U_sigma-U)|| has a root-independent bound: a far vacuum derivative can indeed carry an arbitrarily large zero-point norm. Instead use the excitation ground-state transform. Since

    H_exc U=0,
    H_exc[chi U]=integral |grad_F chi|_G^2 |U|^2,

no spectator vacuum energy occurs. In the operator cutoff commutator, grad_e chi is a scalar multiple of Y_e/h^2; its product with Omega_eY_e has a root-normalized quadratic coefficient of order h^(-2), because Omega_e/r_e is bounded. The same observation applies to the active finite graph states in Z and to H1: replacing a p_e by grad_e chi adds a factor bounded by C/(r_e h^2), with a Gaussian tail. Thus the only cutoff errors required here satisfy, uniformly in all root ratios,

    |delta diagonal|<=tau_R(H_s[f]+W_2[f]),
    |delta mixed|<=eta B[v]+C_eta tau_R(H_s[f]+W_2[f]),
    H_exc[chi Zf/n]=H_exc[Zf]+O(tau_R W_2[f]),             (7.2)

with the analogous graph-local H_s and J estimates. Slow cutoff derivatives use |partial h|/h<=C/r_\*; internal derivatives of h vanish. Derivatives of n are controlled by the same normalized tail calculation. The normal connection preserves |Y|^2, so it creates no extra radial-cutoff generator.

S and Z are boson-odd. The cutoff is even, hence chi Z/n is EXACTLY orthogonal to U_sigma. The leading cutoff H1 source is also odd and is orthogonal to the uncut U, so its shifted-fast inverse never encounters the vacuum kernel. Replacing it by S in the mixed identity costs only (7.2). In the lower bound the source completion with the uncut H_exc is valid for every v, whether or not v is exactly orthogonal to U: S is orthogonal to its kernel.

Finally v perp U_sigma has ||Pv||<=tau_R||v|| and therefore

    H_exc[v]>=c r_*(1-tau_R^2)||v||^2.                   (7.3)

All estimates (6.1)-(6.4) consequently hold for U_sigma and its genuine Dirichlet complement after adding the vanishing tau_R terms.


## 8. Lower Schur comparison

Choose the reserve loss delta and the mixed allocation eta small. A fixed positive fraction of J is available, so eta can be chosen below c_0. Equations (1.5) and (6.1) leave

    H[U_sigma f+v]
      >=H[U_sigma f]+c_s H_s[v]+c_J J[v]
           +(1-delta-eta)H_exc[v]+2Re<Sf,v>
           -a_eta H_s[f]-b_eta W_2[f],                  (8.1)

where c_s and c_J are positive after the finite allocation. Completing only the shifted fast form gives

    (1-delta-eta)H_exc[v]+2Re<Sf,v>
      >=-(1-delta-eta)^(-1)<f,S^*H_exc^(-1)Sf>.          (8.2)

The virtual multiplier is <=CW_2. Therefore replacing its coefficient by one costs only C(delta+eta)W_2. Use (1.3), (3.5), and (6.3)-(6.5). Their total error is made smaller than epsilon(H_s+W_2) in the parameter order below. Taking the infimum proves the lower half of (1.1). One may retain a further small positive fraction of H_s[v]+H_exc[v]+J[v] for the form-domain argument, at an additional O(eta W_2) cost.


## 9. Upper trial and the complete internal-source graph bound

Use the genuine complementary trial

    v_f=chi Zf/n,   Z=-H_exc^(-1)S.

The actual graph components obey

    ||Z_e||^2<=C r_e^(-3),
    ||Z_t||^2<=C w_t/s_t,
    w_t=sum_(e in t)r_e^(-2),  s_t=sum_(e in t)r_e,

and their full derivatives include the spectator term m_gW_2. The complete interacting internal estimate is (1.4). At a graph vertex, alpha_a m_g<=C kappa W_2,g; outside the graph the potential charge commutes with the even graph map, and only differentiated spectator vacua remain. This is why no alpha_a from an unrelated far block can multiply a nearest-root dressing norm. The rootwise graph proof covers arbitrary momenta of f.

There is also a direct incident estimate for the retained orbit square:

    J[Zf]<=C R^(-6)H_s[f]
                      +C kappa R^(-3)W_2[f]+C sigma^2 W_5[f]. (9.1)

Indeed each fixed-degree graph state has the same Y_e second-moment scale C/r_e on active and spectator roots. The coefficient of t_a[f] is at most C w_a sum_g m_g. Convert w_a t_a BEFORE using sum_g m_g<=CR^(-3). Derivatives on Z use the full active-plus-spectator derivative bound and the pointwise coefficient ||A||<=C sigma, giving C sigma^2 W_5. This proves (9.1) without a global internal kinetic loss.

The same absolute estimates used in the reserve proof, with the upper Young inequality for the complete shifted charges, give

    H[w]<= (1+delta)(H_s[w]+H_exc[w])
                        +C_delta W_2[w]+C J[w]+V4[w].   (9.2)

For the fast part this is immediate from the exact identity (2.1), whose leading signed terms have two-sided bounds. The internal shifted-charge comparison is also two-sided; density, E0 and spin estimates are absolute. If desired V4 can be absorbed using (3.2). Thus (9.2) uses no unproved upper control of the full original Gauss square.

Apply (9.2) to v_f. Since H_exc[Zf]=<f,S^\*H_exc^(-1)Sf>, (1.4), (9.1), (3.2), and the cutoff estimates give

    H[v_f]<= (1+delta+C sigma^2)H_exc[Zf]
       +C R^(-3)H_s[f]+C kappa W_2[f]
       +C_delta R^(-3)W_2[f]+O(tau_R(H_s+W_2)).          (9.3)

The mixed remainder (6.1) applied to this trial is small by the same graph estimates. Meanwhile

    2Re<Sf,Zf>=-2<f,S^*H_exc^(-1)Sf>.

Together with the diagonal expansion, this leaves W-S^\*H_exc^(-1)S and only the displayed arbitrarily small errors. Equation (1.3) therefore proves the upper half of (1.1). The graph trial is used only for this upper bound; arbitrary complementary vectors remain unrestricted in the lower bound.


## 10. Simultaneous parameter order

There is no circular order and no unattached constant C W_2:

1. Fix the partition and desired epsilon. Choose the finite Young allocations theta, eta and reserve loss delta so the coefficients they alone contribute, including C(delta+eta) from (8.2), use less than epsilon/10 each.
2. Choose kappa small enough for the fixed pair functional-calculus neighborhood, C_eta kappa, C kappa from the source defect and E0 payment, and C theta^(-1)kappa^4 to fit their assigned W_2 budgets.
3. Choose a FIXED positive sigma small enough for the reserve, C_theta sigma, C_eta sigma^2 and the complete-charge mixed costs to fit their budgets. Choose a fixed smaller sigma_0 for the radial cutoff.
4. Increase R until every constant now fixed times R^(-3), all complementary W_2 absorptions, and all cutoff-tail quantities fit the remaining budgets.

Constants such as C_delta or 1/sigma are finite before R is chosen. No estimate uses a later inverse power of a parameter to undo an earlier smallness requirement without allowing that earlier parameter to be chosen in the stated order. All estimates are uniform on nested smaller supports at the selected fixed widths.


## 11. Closed domains and variational meaning

First work on compact slow supports strictly inside the chosen branch and tube. The exact first-order coefficients and density are smooth there, with uniformly positive principal kinetic form and bounded local matrix potentials. The associated Dirichlet form is closed after a scalar shift, with its ordinary local H1 core. U_sigma has smooth compact fast support; P_sigma and Q_sigma map this core into the same form domain. No assertion is made that the uncut P preserves Dirichlet support.

The estimates above imply, after adding a bounded scalar multiple of ||u||^2,

    H[u]+C_R||u||^2 >= c H_s[f]+c B[v],
    u=U_sigma f+v,

with c>0; W_2<=C R^(-2) is bounded. Conversely the diagonal upper estimate bounds H[U_sigma f] by C(H_s[f]+||f||^2). Hence P_sigma extends boundedly in the closed quadratic-form norm, equivalently the graph norm of the averaged supercharge stack for the stated supersymmetric realization. This proves P_sigma Q(H) subset Q(H); preservation of the Hamiltonian operator domain D(H), or boundedness in its operator graph norm, is not asserted. Exhaustion by compact slow supports gives the same identification on an unbounded selected branch, using these UNIFORM estimates rather than local ellipticity constants that might depend on r_max.

The restriction of the closed quadratic form of H to Q(H) intersect ker(U_sigma^\*) is closed and strictly L2-coercive by (1.5) and (7.3). For f in the slow form domain, the mixed functional is continuous in that complementary form norm by (6.1) and the exact source dual estimate. Riesz representation gives a unique minimizing v_f in Q(H) intersect ker(U_sigma^\*) for each f in Q(H_s). This is form-domain attainment only; no operator-domain regularity of v_f is inferred. The resulting Schur form is continuous in the shifted H_s form norm, and (1.1) makes the shifted quadratic-form norms equivalent after a bounded scalar shift. It is therefore closed.

These are form statements. They do not claim a bounded operator B or a second-slow-derivative operator identity on arbitrary f, and do not assume an inverse for H_I. All cutoffs, projections, graph dressings, and estimates intertwine under the same-branch residual/color/normal-frame unitaries. Different cluster branches and off-cone selector transport remain outside this local theorem.


## 13. Explicit module and differentiated-tail checks

The following coefficient identities make the retained-module and differentiated-tail steps explicit.

### 13.1 Internal potential/Yukawa commute with the actual injection

At a fixed intrinsic branch, the orthogonal Lie-algebra splitting into off-block and retained block/center directions gives the graded tensor product of the fast and slow Clifford modules. The injection is

    U(A,Z)f = g_(A,Z)(Y) v_F(A,Z) tensor f,

with the identity map on the ENTIRE slow Clifford module. There is no projection onto an internal singlet or internal eigenstate. Each complex bifundamental fast mass has 8 n_a n_b occupied negative modes, an even number. This remains constant under the gapped continuation, so the product determinant v_F is even. In particular its graded tensor injection intertwines the internal odd Clifford generators with the same retained representation. The internal Hamiltonian's Yukawa term is even in any case: it is a sum of bilinears in retained internal fermions only.

Pointwise in (A,Z), V_I is scalar multiplication and Y_I(A) acts only on those retained Clifford factors. Therefore, as actual maps,

    V_I U=U V_I,    Y_I U=U Y_I,
    U^*Y_I v=Y_I U^*v.

This proves their zero mixed compression for U^\*v=0. The cutoff is a scalar bosonic multiplier, so the identities hold exactly for U_sigma as well.

The pair negative-projector radial transport is implemented on the fast Fock module by a fast-fermion even unitary; its bosonic covariance transport also acts only on the fast module. Both commute with the retained Clifford action. The line may carry a nontrivial scalar Berry connection, but this does not rotate the slow Clifford representation. Differentiation gives

    p_A(Uf)=U nabla_A^B f+(1-P)(p_A U)f.

The transverse term is retained in (5.7); the Berry term is retained in H_s^B and compared by the full charge estimate (6.5). Nothing in the radial identification sets the full derivative of U to zero. Residual color transformations act simultaneously on the fast determinant line and the retained module, and U is the corresponding equivariant intertwiner. These pointwise tensor identities therefore descend to the residual-equivariant/physical subspace without requiring individual block singlets.

### 13.2 Exact beta-tail decomposition before internal differentiation

Use the notation of Section 2, and set

    B=Psi^*F^(-1),
    B_1=[C_Y F^(-1)+K^* ; I_Y F^(-1)],
    R_m=T^*WT-I.

The center row of B is

    B_C=g_C^(-1/2)[C_Y+K^*(F+L)]F^(-1),

and the internal row is B_I=I_Y F^(-1). Direct substitution into beta=A^\*a gives the exact identities

    beta=B T^*WT(d_0+n),      beta_1=B_1d_0,

    beta-beta_1=(B-B_1)d_0+B R_m d_0+B T^*WT n.           (13.1)

The internal part of B-B_1 is zero, and its center part has the exact factorization

    (B-B_1)_C d_0
      =(g_C^(-1/2)-I)(C_Y F^(-1)d_0+K^*d_0)
         +g_C^(-1/2)K^* L F^(-1)d_0.                    (13.2)

The metric difference is O(sigma^2), and the last term has the explicit O(sigma) left factor K^\*. The other factors in (13.2) are same-root or input-root-denominator triangle columns.

To expand the middle term of (13.1) without exposing a bare frozen vacuum norm, use T-I=-Z_m T and the fact that T commutes with Z_m. Exactly,

    R_m d_0
      =-T^* Z_m^*d_0 -T^*T Z_m d_0
         +T^*K(K^*d_0)-T^*KK^*T(Z_m d_0).              (13.3)

Thus it contains only uniformly bounded left factors multiplying Z_m^\*d_0, Z_m d_0, or K^\*d_0. These are the controlled rootwise columns. For example

    Z_m d_0=F^(-1)L^*d_0
                 -F^(-1)C_Y^*[C_Y R^(-1)d_0],
    Z_m^*d_0=L F^(-1)d_0-K[C_Y F^(-1)d_0],
    K^*d_0=C_Y R^(-1)d_0.

The last term of (13.1) has the same explicit O(sigma) outer B multiplying the triangle column n. This proves the extra small factor by an exact finite identity, not by a formal infinite series.

For an INTERNAL derivative partial_j, Y, K, L, N_Y, I_Y, C_Y, W and g_C are independent of A. Consequently

    ||partial_j B||<=C sigma/r_*,
    partial_j Z_m=-F^(-1)(partial_j F)Z_m,
    ||partial_j T||<=C sigma/r_*.

Every derivative of a root-preserving coefficient F_e^(-1) adds 1/r_e. A derivative of F_e^(-1)C_e^\* can remove its optional O(kappa) factor, but replaces it by O(1/r_e). The same-root or triangle column therefore still has an extra 1/r_e<=1/r_\* in its low Gaussian norm. Crucially the outer B, K^\*, or g_C^(-1/2)-I displayed in (13.1)-(13.3) remains, or its derivative has the SAME sigma gain and another 1/r_\*.

Applying the finite Gaussian rootwise bounds to these differentiated identities gives

    ||(beta-beta_1)U||<=C sigma W_2^(1/2),
    ||[partial_A(beta-beta_1)]U||
                        <=C sigma r_*^(-1)W_2^(1/2).    (13.4)

The derivative in the second line acts on the operator coefficient, exactly as required by the curvature term, not on U. Derivatives of U are already present in the complete-charge cross. At A=0, partial_A d_0 need not vanish; (13.1)-(13.3) explicitly retain its contribution with the same extra fast factor. The non-small derivative of beta_1 itself is not included in the tail estimate and remains in the leading H2 scalar.

Finally the coefficients of beta-beta_1 have at least two fast-coordinate factors before p_F. A fast divergence removes at most one. Differentiating the displayed normalized coefficients therefore gives |div_F(b-b_1)|<=C sigma/r_\*; an additional internal derivative costs at most 1/r_\* and leaves this sigma factor. This proves the divergence portions of Section 4.3 with the required gain as well.

### 13.3 Form domain convention

The infimum, projection bound, and Riesz minimizer are statements about Q(H), the closed quadratic-form domain. They do not establish invariance of the Hamiltonian operator domain D(H). The minimizing complement is asserted only in Q(H), for f in Q(H_s). The global lower bound does not require attainment.
