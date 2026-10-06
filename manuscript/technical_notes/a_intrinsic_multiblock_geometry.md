# Intrinsic multiblock geometry

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 1. Setting and precise scope

Fix N and a partition N=n_1+...+n_k, k>=2. Hermitian matrix tuples have the real trace inner product. Retain the residual group K=S(U(n_1)x...xU(n_k)), including its action on the fermions; do not divide by any internal nonabelian orbit. Write

    X_i=Z_i+A_i+Y_i,
    Z_i=diag(z_1i I_(n_1),...,z_ki I_(n_k)),
    sum_a n_a z_a=0,   Tr A_i^(a)=0,
    b_ab=z_a-z_b,   r_ab=|b_ab|,   r_*=min_(a<b) r_ab>0.

A is block diagonal and Y is off block. Put alpha_a^2=sum_i ||A_i^(a)||_F^2. Assume only

    alpha_a+alpha_b <= kappa r_ab  for every a<b.             (1)

There is no hypothesis alpha_a << r_\* for a block unrelated to a shortest pair. Set kappa<=1/100. For the fast tube use

    |Y| <= sigma r_*,   sigma<=1/100.                         (2)

Condition (2) is deliberately a fast-coordinate condition. It is compatible with the Gaussian widths at sufficiently large r_\* and does not impose the forbidden common scale on A. A smooth smaller cutoff may use the harmonic minimum of the r_ab instead of the nonsmooth literal minimum.

Let C be the Euclidean block-center tuple space, I the space of blockwise traceless internal tuples, and m the off-block Hermitian gauge-parameter space. Its real dimension is

    q=2 sum_(a<b) n_a n_b.

For a Hermitian tuple Q let B_Q xi=(i[xi,Q_i])_i. Define

    R=(B_Z^* B_Z)^(1/2)=direct_sum_(a<b) r_ab I_(2n_an_b),
    E=B_Z R^(-1),   E^*E=I_m,
    N_Z=ker B_Z^* in the off-block tuple space.

The intrinsic normal constraints are B_Z^\*Y=0, equivalently b_ab dot Y_ab=0 for every pair. The slice S consists of the triples (Z,A,Y) satisfying these constraints. Statements below are tensor identities on this slice and its local gauge-saturated image. A simultaneous smooth projector branch exists locally by the nonsingular Hessian proved below. This does not assert a globally unique branch across incompatible cluster partitions.


## 2. Horizontal differential and the exact internal coefficient

Use the normal connection obtained by orthogonal projection onto N_Z. For h=(delta Z,delta A,delta Y_N) in H=C direct_sum I direct_sum N_Z, horizontal differentiation of B_Z^\*Y=0 gives

    delta Y=delta Y_N+E K h,
    K h= -R^(-1) B_(delta Z)^*Y.                             (3)

K vanishes identically on I and N_Z. The slice embedding differential, in the orthogonal ambient splitting H direct_sum range E, is

    S h=(h,K h),
    g_S=S^*S=I_H+K^*K
       =g_C direct_sum I_I direct_sum I_(N_Z).                (4)

Thus the induced slice has internal kinetic coefficients **exactly one**, and there are no internal/center or internal/fast induced-metric cross terms. The full reduced co-metric additionally contains the positive orbital contribution from the Gauss square; it is not claimed that its total AA block equals I. The coefficient-one t_A summand is retained before that square is estimated. This is an exact identity for every A and Y in the coordinate domain, not an oscillator expectation.

Skew-adjointness of the gauge action gives a useful equivalent identity. For O=B_X, O_C=P_C O and O_H=P_H O,

    O_C=P_C B_Y,   K=R^(-1) O_C^*.                            (5)

The elementary commutator bound ||B_Y||<=2|Y| proves

    ||K||<=2s,   s=|Y|/r_*,
    (1+4s^2)^(-1) I_C <= g_C^(-1) <= I_C.                    (6)

All normal-frame connections remain inside the covariant center momentum. Their unbounded Y partial_Y generators are never estimated by oscillator energy on arbitrary vectors.


## 3. Faddeev-Popov matrix, explicit noncircular invertibility, and density

The differential of the normalized slice constraint is N^\*=(-K,I_m); thus

    N=(-K^*,I_m),   W=N^*N=I_m+K K^*.

The full transverse-orbit matrix is

    M=N^*O=E^*B_X-K O_C
     =E^*B_(Z+A)+E^*B_Y-R^(-1)O_C^*O_C.                     (7)

Put F=E^\*B_(Z+A). F is pair-block diagonal. Under the canonical complex identification of a pair, its block is unitarily equivalent to

    r_ab I+T_(ab,n),
    T_(ab,n) V=A_n^(a)V-V A_n^(b),  n=b_ab/r_ab.

Consequently

    (1-kappa)R <= F <= (1+kappa)R,   FR=RF.                  (8)

The transverse-frame convention E=B_Z R^(-1) has absorbed the fixed real root-plane complex structure; that is why F is positive here. In a fixed real root frame the corresponding matrix carries that orthogonal complex structure.

Equations (5)-(8) give the explicit bound

    ||M R^(-1)-I|| <= kappa+2s+4s^2 <=0.0304.                (9)

No r_max/r_\* or unrelated internal radius enters (9). The full differential from (h,xi) to ambient coordinates has block matrix

    T=[ I_H   O_H ]
      [ K     E^*O].

Its determinant is det M. Equivalently the induced slice volume is sqrt(det W), while the normalized-normal orbit contraction is |det(W^(-1/2)M)|. They cancel. The physical measure after the compact off-block gauge integration is therefore

    J dZ dA dY_N,   J=det M>0,                              (10)

up to one constant orbit normalization. This is physical measure including orbit volume, not bare quotient Riemannian volume.

At Y=0,

    J_0=det F=product_(a<b) det_C(r_ab I+T_(ab,n))^2,
    d_0=sqrt(J_0)=product_(a<b) det_C(r_ab I+T_(ab,n)).        (11)

The determinant is positive by (1). Internal coincidences introduce no singularity.

There is no linear-Y density term, even for nonzero internal A. Indeed L=E^\*B_Y has zero diagonal pair blocks: acting on an ab gauge parameter, an off-block Y produces block-diagonal output or a different pair. Since F^(-1) is pair-block diagonal,

    tr(F^(-1)L)=0.                                         (12)

The remaining correction -K O_C is quadratic in Y. In fact the absolutely convergent logarithm series gives, for the stated kappa and sigma,

    |log(J/J_0)| <=8 q s^2.                                 (13)

For verification: ||F^(-1)L||<=2s/(1-kappa), ||F^(-1)K O_C||<=4s^2/(1-kappa). The linear trace vanishes, and the sum of powers >=2 is bounded by q e^2/[2(1-e)], where e=(2s+4s^2)/(1-kappa). Together with the quadratic trace this is <8q s^2.


## 4. Intrinsic projectors and transition law

For an ordered orthogonal family of projectors P_a of ranks n_a define the gauge-invariant function

    Phi_X(P)=sum_(a,i) n_a^(-1) (Tr(P_a X_i))^2.

Stationarity under off-block variations is precisely B_Z^\*Y=0. At such a point its Hessian in a gauge parameter xi is

    Hess Phi_X[xi,xi]
      =2||O_C xi||^2-2<B_Z xi,B_X xi>
      =-2<xi,R M xi>.                                      (14)

Thus RM is symmetric. In the normalized orbit variable eta=R xi, the negative half-Hessian is M R^(-1), which by (9) lies between 0.9696 I and 1.0304 I. Every such stationary decomposition is a strict local maximum with a nonsingular transverse Hessian. The implicit function theorem therefore gives a unique smooth nearby projector branch, equivariant under SU(N), with no internal eigenvalue gap assumption.

On overlap of charts describing the same branch, the ordered P_a agree. Their block frames differ by K and, when the labels are changed consistently, by a permutation of equal-rank blocks. Normal frames differ by orthogonal maps on N_Z. These are exact unitary bundle changes on bosonic fibers and the fermionic module. J is invariant; no extra nonunit half-density amplitude appears. All expressions (3)-(14) and the kinetic identity below intertwine under these changes. One may prove them in local frames without introducing scalar angular IMS cutoffs.

This is a **same-branch** transition theorem. Comparing different nested partitions, proving that their selectors agree with all commuting-tree choices, and uniformly transporting every decision-tree cutoff off the commuting cone remain separate obligations. Local nonsingularity alone does not prove any of those global claims.

### 4.1 Smooth fast projection on the same branch

The frozen pair matrices G_ab, K_ab and D_ab of the general fast-energy lemma are obtained at Y=0 from (15)-(16) and the exact quadratic potential. Their bosonic frequencies and fermionic spectral gaps are bounded below by fixed positive multiples of r_ab under (1). Functional calculus therefore gives a smooth positive Gaussian and a smooth negative-energy occupied subspace, including at every internal eigenvalue collision. The resulting rank-one fast-vacuum projection P is gauge equivariant. Local vacuum frames may have a nonflat scalar Berry connection; none is declared parallel here.

A same-branch chart change acts on every finite pair matrix by its actual orthogonal/color/spin unitary representation. Spectral functional calculus and the positive Gaussian construction commute with that action. Hence P'=V P V^\* exactly. The same is true after a smooth invariant radial cutoff, for example with h=(sum_(a<b)r_ab^(-2))^(-1/2) and chi(|Y|/(sigma h)), followed by fiberwise normalization. There is no angular scalar partition in this construction. Since r_\*/sqrt(k(k-1)/2)<=h<=r_\*, the cutoff tail bounds differ only by fixed N-dependent constants.

For the uncut product U, an internal derivative in A_a differentiates only the pair factors incident to a. For U_sigma the derivative also differentiates its global scalar normalization; this term is bounded by the same derivative norms, and its difference from the uncut normalization is exponentially small in the indicated tail scale. The resolvent formula for their spectral projections and the Gaussian square-root formula give norm bounds C_(N,j) r_ab^(-j) for each fixed number j of such derivatives, after the natural fast dilation. These follow from external pair gaps, never from an internal Hamiltonian resolvent. Mixed derivatives have the corresponding products of inverse incident scales. Global phase choices are unnecessary because the projection and its induced connection are intrinsic.


## 5. Exact all-vector kinetic plus Gauss form

Let p_H be the slice coordinate momentum stack, with the normal connection in its center component and ordinary internal and fast components. Let S_f denote the off-block fermionic Gauss generator, in the same sign convention as O^\*p=S_f. Residual K-equivariance remains imposed. The orthogonal tangential projection of the orbit is

    O_T=S g_S^(-1) S^*O.

For a raw equivariant section phi define

    D phi=W^(1/2) M^(-*)[S_f phi-O^*S g_S^(-1)p_H phi].      (15)

Then the exact ambient reduced kinetic form, in coefficient-one units, is

    t_raw[phi]=integral J {
       <p_H phi,g_S^(-1)p_H phi>+||D phi||^2 }.              (16)

Proof: write an ambient covector as its slice-tangent projection plus N beta. Its tangential restriction is p_H; the Gauss equation fixes M^\* beta=S_f-O^\*S g_S^(-1)p_H. Tangent and normal parts are orthogonal, and ||N beta||^2=<beta,W beta>. This proves (16) for arbitrary covectors, arbitrary spinor values, and unrestricted momenta. It is a first-order identity, not substitution into a squared differential operator.

For the flat measure put d=sqrt J and psi=d phi. The exact flattened formula is obtained from (15)-(16) by

    p_H -> p_H+i d_H log d.                                 (17)

This fixes every ordering. Equivalently integration of the real density cross terms gives the unshifted quadratic stack plus the scalar multiplication

    V_d=d^(-1) div_H(a d_H d),                              (18)

where a is the complete scalar principal co-metric, including the orbital part of D. Divergence is that of the flat bundle measure. The finite Hermitian spin terms have zero real cross pairing with the purely imaginary scalar density shift. No separate spin connection is appended. Formula (17) remains the definitive expression if a convention for momenta is changed.

On a fixed-shape regular region r_\*>=delta rho_C with rho_C^2=sum_a n_a|z_a|^2, and a closed smaller tube, V_d and all coefficient derivatives needed at any fixed order are bounded by constants times their homogeneous powers. In particular |V_d|<=C_(N,delta,kappa,sigma) rho_C^(-2). These are bounds from explicit smooth finite matrices and compact shape sets; they do not use a full Hamiltonian inequality.

Combining the exact internal kinetic coefficient with the exact internal potential and Yukawa pieces retains

    sum_a [t_(A_a)+V_a+Yukawa_a]=sum_a h_(n_a)

with coefficient one, also on colored internal sections. The averaged-supercharge nonnegativity of these internal forms is the usual algebraic statement, not a physical-sector Hardy inequality or an internal spectral gap.

Equation (16) does **not** justify adding a separately extracted adapted fast kinetic matrix and the whole same Gauss square. The frozen adapted kinetic matrix is already part of that square.


## 6. Incident-edge reserve for unrestricted low internal derivatives

Let U(Z,A) be the normalized product of the pairwise kinetic-aware Gaussian and occupied fermionic determinant from the frozen-pair lemma. Interpret it as an isometric injection of its vacuum line; no flat Berry connection is assumed. On each pair its covariance obeys

    E_U |Y_ab|^2 <= C n_a n_b ell^3/r_ab,

with an absolute C on the stated kappa tube. Use a smooth invariant cutoff strictly inside (2), normalize fiberwise, and call the resulting injection U_sigma. At fixed finite N and sufficiently large r_\*, the same covariance bound holds with twice C; cutoff errors are bounded by polynomial factors times exp(-c sigma^2 r_\*^3/ell^3), uniformly in unrelated A and r_max. Derivatives can have fixed shape-dependent prefactors if expressed in rho_C units.

The internal orbital map in (15) is exactly

    O_(T,A)=O_A=P_I B_Y.                                    (19)

There is no Y-independent internal orbital derivative and no contribution from an unrelated pair. For an internal covector p=(p_a), the ab component satisfies

    |(O_A^*p)_ab| <= C |Y_ab| (|p_a|+|p_b|).                 (20)

Write M=F+P. The elementary bound

    ||P F^(-1)|| <=(2s+4s^2)/(1-kappa)<0.021

shows that M^(-\*)=(I+F^(-\*)P^\*)^(-1)F^(-\*) has a uniformly bounded left factor. W^(1/2) is uniformly bounded too. Thus (20) gives the pointwise estimate

    ||W^(1/2)M^(-*)O_A^*p||^2
        <=C sum_(a<b) |Y_ab|^2/r_ab^2 (|p_a|^2+|p_b|^2).    (21)

This is valid for every internal covector, not just bounded internal momenta. Compressing only its coefficients in U_sigma yields

    ||D_A(U_sigma nabla_A f)||^2
        <=sum_a w_a |nabla_(A_a) f|^2,
    w_a=C sum_(b!=a) n_a n_b ell^3 r_ab^(-3).                (22)

The derivatives here are the covariant derivatives on the possibly nonflat vacuum line. The expression in (22) denotes the part where the derivative acts on f; derivatives acting on U_sigma are separate coefficient sources. Estimate (22) records the incident-weighted low-leg coefficient bound. Its use in the mixed form must follow the complete-charge and postcompletion estimates of Appendix I, Sections 4 and 5.2-5.4; it does not authorize retaining or spending a second copy of the original Gauss square.

Most importantly, the loss is incident-edge weighted. For an ordinary untwisted internal derivative, both t_(A_a)<=h_a+C_(n_a) ell^(-3) alpha_a and V_a<=h_a+C_(n_a) ell^(-3) alpha_a follow from the finite-Clifford Yukawa bound. Independently of that form comparison, (1) gives

    w_a alpha_a <=C kappa sum_(b!=a)n_a n_b ell^3 r_ab^(-2). (23)

The weighted derivative error has a direct payment that does not require a new weighted full-supercharge theorem. Use the internal-radial gauge constructed in source Section 4.2 in Appendix F: each pair connection obeys |a_ab|<=C_N kappa^2/r_ab, and its A_a component vanishes unless that pair is incident to a. In the resulting identification with the flat A=0 center line,

    sum_a w_a ||nabla_(A_a)f||^2
       <=2 sum_a w_a t_(A_a)[f]
          +C_N kappa^4 ell^3 r_*^(-3)
                         integral sum_(a<b)r_ab^(-2)|f|^2
       <=2 sum_a w_a h_a[f]
          +C_N [kappa+kappa^4 ell^3 r_*^(-3)]
                         integral sum_(a<b)r_ab^(-2)|f|^2.   (26)

All rank-dependent Clifford and endpoint factors are included in C_N. The first inequality is the elementary |partial f+i a f|^2<=2|partial f|^2+2|a|^2|f|^2; the second uses (23). The weights depend only on centers, so multiplying the internal form creates no omitted internal weight derivative. At large r_\* their h_a coefficients vanish. The inverse-square term is arbitrarily small in kappa and has a shape-independent pair-center Hardy payment. This argument pays only the small derivative error (22); it does not replace the full-supercharge comparison needed for the principal Berry-coupled slow form. A cruder replacement w_a<=C r_\*^(-3), followed by r_\*^(-3) alpha_a, would destroy this conclusion for a far extended block and is not used.

The variable induced center metric is also paid as a genuine derivative-form pairing against a retained covariant center kinetic square. Its correction is exactly

    g_C^(-1)-I_C=-K^*(I+K K^*)^(-1)K.

Its Gaussian coefficient norm is O_N(ell^3 r_\*^(-3)), so the squared cost in that direct pairing is O_N(ell^6 r_\*^(-6)) times the low center derivative form. This step involves only center derivatives; it cannot create an internal kinetic loss. Derivatives of U_sigma supply further coefficient sources, which still require their own full source inventory.
