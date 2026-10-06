# Differential connections and colored forms

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 1. Setting and result

Fix the rank and block partition. Assume only

    alpha_a+alpha_b <= kappa r_ab,     |Y| <= sigma r_*,
    r_* = min_e r_e >= 1,             W_2 = sum_e r_e^-2.

Constants depend on fixed rank and fixed sufficiently small upper bounds for kappa and sigma, never on r_max/r_\*. Work first on the compactly supported smooth residual-equivariant core in a normal-frame chart. No individual block-singlet assumption is imposed. Let

    H_exc = sum_e (H_fast,e-E_0,e) >= 0,
    lambda(Z) = sigma^2+r_*^-3,
    E[v] = (lambda H_exc)[v]+W_2[v].                       (1.1)

The weights are center-only and the excitation form acts in fast fibers. For the INTERNAL part of the completion connection write

    beta_j = b_j(Y,A,Z) dot p_F,
    beta = A_s^* B_F p_F,     A_s = B_s G_s^-1/2.

Here A_s is the normalized Gauss slow coefficient, not the internal matrix tuple. The internal block of G_s is exactly identity. Define the ordered shifted form inherited from the exact kinetic identity:

    H_I^raw(beta)[v]
      = sum_j ||(p_j+beta_j)v||^2+(V_I+Y_I)[v].             (1.2)

For every epsilon in (0,1),

    H_I^raw(beta)[v]
      >= (1-epsilon)H_I[v]
           -C_(N,epsilon)(lambda H_exc)[v]
           -C_(N,epsilon)W_2[v].                         (1.3)

This retains the ENTIRE interacting internal form, including its original potential and Yukawa terms. There is no epsilon times bare internal kinetic loss and no epsilon alpha_a mass remainder. No internal gap or physical-sector lower-rank Hardy estimate is used.

The proof gives the actual curvature expectation bound

    |R_beta[v]| <= C_N(lambda H_exc)[v]+C_N W_2[v].       (1.4)

The stronger possible coefficient C_N r_\*^-3 with sigma^2 absent is not needed and is not claimed. Fixing sigma sufficiently small and then taking the exterior radius large makes the excitation coefficient as small as desired. On fast-complement inputs W_2 is also paid by the gap.


## 2. Exact completion

Remove the finite fermionic Gauss source by the separate estimate chosen for that source. Its estimate is not part of this algebra. Let

    w=G_s^1/2 p_s v,   a=B_F p_F v,   A_s=B_s G_s^-1/2.

Exactly, as a first-order form identity,

    ||w||^2+||a+A_s w||^2
      =||w+A_s^*a||^2+||a||^2+||A_s w||^2-||A_s^*a||^2. (2.1)

Coefficients multiply the differentiated section in their original order. No integration by parts and no coefficient derivative occurs in this completion.

The internal components of w+A_s^\*a are p_j+beta_j. Its center components use the exact center metric and NORMAL-BUNDLE covariant momentum. The center square and ||A_s w||^2 may be retained or discarded as positive forms. They are not additional copies of the fast Gauss energy. The negative term is the connection norm already bounded in the rootwise lemma.

If the half-density was separated as in the intrinsic geometry note, its scalar V_d must still be included separately. The symmetrization below neither replaces nor duplicates that calculation.


## 3. Coefficients and differentiated rootwise bounds

Use intrinsic notation

    F=E^*B_(Z+A),   C=P_N B_A,   N_Y=P_N B_Y,
    I_Y=P_I B_Y,    M=F+L-J_2,   W=I+KK^*.

The internal coefficient is, with the common Gauss sign convention,

    beta_I=I_Y M^-1 W M^-* (C+N_Y)^*p_F.                   (3.1)

All coefficients are real in real trace-orthonormal frames. Normal frames depend on centers only; an internal derivative differentiates neither p_F nor the frame. The connection commutes with internal Clifford matrices and every internal potential-supercharge multiplication coefficient.

For a unit internal direction h,

    partial_h M=partial_h F,
    partial_h F and partial_h C are pair-block diagonal,
    ||partial_h F_e||+||partial_h C_e|| <= C_N,
    partial_h W=partial_h I_Y=partial_h N_Y=0.             (3.2)

Only pairs incident to the differentiated block contribute. The coarse r_\* estimate below does not convert any kinetic or Yukawa term, so it creates no unrelated alpha_a/r_\* error.

The cited rootwise connection proof gives

    sum_j ||beta_jv||^2 <= C_N E[v].                     (3.3)

Its explicit first-order decomposition also gives

    sum_(j,k)|| (partial_j beta_k)v ||^2
       <= C_N [ (r_*^-2 lambda H_exc)[v]
                     +(r_*^-2 W_2)[v] ].                 (3.4)

Here partial_j beta_k differentiates its coefficients only. The following proves (3.4); it is not inferred from the abstract bound (3.3).

### 3.1 Proof of the differentiated estimate

In the rootwise lemma put

    d_0=F^-1 C^*p_F,    T=(I+F^-1 P^*)^-1,    P=L-J_2.

The exact decompositions (5)-(7) and (12)-(15) in that lemma express beta as finite sums of bounded multiplication matrices times the source classes

    Y_e p_e/r_e,
    Y_f p_e/r_g,       when (e,f,g) is a triangle,
    Y_f p_e/r_e,       with the input-root denominator,

with bounded root-preserving factors between the displayed operators. Non-root-preserving inverse matrices remain bounded LEFT factors. Thus no unweighted spectator momentum is hidden.

Differentiate those exact decompositions. Y, r_e, W, K, I_Y, C_Y, L, J_2 and g_C have zero internal derivatives. The differentiated factors satisfy

    ||partial_j F_e^-1|| <= C_N/r_e^2,
    ||partial_j(F_e^-1 C_e^*)|| <= C_N/r_e,
    ||partial_j T||+||partial_j T^*|| <= C_N/r_*.

The inverse derivative formula and (3.2) prove these inequalities. All other bounded left factors in the displayed decompositions consequently have derivative at most C_N/r_\*. Differentiating F_e^-1 C_e^\* replaces its O(kappa) factor by O(1/r_e); use the source bound with its optional kappa gain omitted.

Every resulting term is therefore the SAME source class with one extra factor at most C_N/r_\*. Applying the proved same-root and mixed-root inequalities (2)-(4) of the cited lemma, and finite-sum Cauchy, proves (3.4). The argument is all-vector, does not bound internal momenta, and does not require a fast projection to preserve tube support.

### 3.2 Coarse pointwise derivatives for divergence

Only for the scalar divergence correction we need

    |b| <= C_N sigma(kappa+sigma),
    |partial_Y b| <= C_N/r_*,
    |partial_A partial_Y b|+|partial_Y^2 b| <= C_N/r_*^2. (3.5)

Indeed the internal normalized slow column is O(sigma), the full fast Gauss column is O(kappa+sigma), and ||M^-1||<=C_N/r_\*. First derivatives of M, I_Y and C+N_Y are O(1); second derivatives of M are O(1/r_\*), coming from J_2. First and second derivatives of W and its positive square root are O(1/r_\*) and O(1/r_\*^2). Differentiate the product B_I^\*B_F using the inverse derivative formula. The potentially large C is always kept inside F^-1 C^\* or the bounded full fast column, rather than estimated by kappa r_max. This proves (3.5); fixed coordinate dimensions absorb component sums.


## 4. Exact self-adjoint symmetrization

In flat fast-fiber measure, with p_F=-i partial_Y, put

    d_j=div_F b_j,
    beta_hat_j=(beta_j+beta_j^*)/2
              =b_j dot p_F-(i/2)d_j,
    P_j=p_j+beta_hat_j,
    X_j=partial_j+b_j dot partial_Y.

Then beta_j=beta_hat_j+(i/2)d_j and P_j=-i(X_j+d_j/2) is symmetric on the core. Direct integration by parts gives the EXACT identity

    ||(p_j+beta_j)v||^2
      =||P_jv||^2
          + integral [(1/2)X_j d_j+(1/4)d_j^2]|v|^2.     (4.1)

The cross term is (1/2) integral X_j(d_j)|v|^2; div X_j=d_j. Thus simply treating b dot p_F as symmetric would miss a scalar correction.

By (3.5),

    |d_j| <= C_N/r_*,
    |partial_A d_j|+|partial_Y d_j| <= C_N/r_*^2,
    sum_j |(1/2)X_j d_j+(1/4)d_j^2| <= C_N W_2.           (4.2)

Hence the full correction is inverse-square multiplication. Also

    sum_j ||beta_hat_jv||^2 <= C_N E[v],                  (4.3)

and (3.4) holds with beta_hat replacing beta: its extra multiplication derivative is O(r_\*^-2), whose squared norm is bounded by r_\*^-2 W_2.


## 5. Actual curvature expectation

Define the symmetric curvature operator

    F_jk=i[P_j,P_k]
        =partial_j beta_hat_k-partial_k beta_hat_j
                         +i[beta_hat_j,beta_hat_k].       (5.1)

Equivalently F_jk is the symmetrized momentum of the fast vector field

    partial_j b_k-partial_k b_j
      +(b_j dot partial_Y)b_k-(b_k dot partial_Y)b_j.

It is first order, not bounded multiplication.

The charge identity contracts (5.1) with fixed bounded internal-Clifford matrices. If L is any such matrix, it commutes with beta_hat and its coefficient derivatives. Symmetry gives exactly

    |<v,L i[beta_hat_j,beta_hat_k]v>|
       <=2||L|| ||beta_hat_jv|| ||beta_hat_kv||.           (5.2)

Thus (4.3) pays all beta-beta curvature terms. There is no need to bound the norm of a fast-differentiated curvature symbol.

For the derivative part, (3.4) and Cauchy give

    |<v,L(partial_j beta_hat_k)v>|
       <= C_N ||r_*^-1 v|| E[v]^1/2
       <= C_N E[v],                                     (5.3)

since ||r_\*^-1v||^2<=W_2[v]<=E[v]. To justify the first inequality with varying centers, apply the coefficient derivative bound at each center and then apply weighted Cauchy over centers. Summing the finitely many Clifford components proves (1.4).

This is an all-vector curvature EXPECTATION estimate. It derives the extra coefficient derivative from the actual rootwise expansion, not from a generic relative-norm assertion. It makes no oscillator-degree cutoff and loses no internal kinetic energy.


## 6. Averaged sixteen-supercharge comparison

Normalize the internal charges by

    H_I[v]=(1/16)sum_alpha ||Q_alpha v||^2,
    Q_alpha=sum_j c_(alpha,j)p_j+V_alpha(A).

The c_(alpha,j) are fixed internal Clifford matrices. The ordinary colored Gauss terms cancel in the spinor average. An individual Q_alpha^2 must not be identified with H_I on the colored core.

Replace p_j by P_j:

    Q_alpha^beta=Q_alpha+C_alpha(beta_hat),
    C_alpha(beta_hat)=sum_j c_(alpha,j) beta_hat_j.

The exact averaged expansion is

    (1/16)sum_alpha ||Q_alpha^beta v||^2
       =sum_j||P_jv||^2+(V_I+Y_I)[v]+R_beta[v].           (6.1)

Here R_beta is a finite-Clifford linear contraction of F_jk. The symmetric momentum products give the kinetic form, antisymmetric momentum products give curvature, and

    [P_j,V_alpha]=[p_j,V_alpha]

because beta_hat is fast-bosonic with scalar bosonic coefficients. The original potential and Yukawa terms are consequently unchanged. Spinor-averaged cancellation of the original Gauss term is unchanged too.

Finite-dimensional Clifford bounds and (4.3) imply

    (1/16)sum_alpha ||C_alpha(beta_hat)v||^2 <= C_N E[v].  (6.2)

Young's inequality on the COMPLETE charge stack now gives

    (1/16)sum_alpha ||Q_alpha^beta v||^2
       >=(1-epsilon)H_I[v]-C_N epsilon^-1 E[v].           (6.3)

Subtract curvature using (1.4), then apply (4.1)-(4.2). This proves (1.3). The loss is epsilon H_I, not epsilon t_I; that is why no large unrelated internal Yukawa mass is introduced.


## 7. Normal-bundle center connection and chart changes

The normal fast bundle N_Z depends on centers alone. Its orthogonal connection is already in p_C in the exact intrinsic formula. In a local frame its center generator may contain unbounded Y partial_Y operators. This argument never estimates those by H_exc.

Internal derivatives act in a center-dependent but A-independent frame, so (3.2) has no frame derivative. The internal supercharges contain no center momentum. Neither center normal-bundle curvature nor mixed center/internal curvature occurs in the INTERNAL square (6.1).

The completed center square remains a genuine positive covariant derivative form. Any subsequent center Hardy argument must use that actual connection with its domain justified. It may not replace its unbounded normal-frame generator by a bounded vacuum Berry coefficient. That separate comparison is not claimed here.

All identities intertwine under center-dependent orthogonal changes of fast normal frame and residual gauge changes. beta is an actual vector field on the fast fiber, beta_hat is its half-density action, and curvature is its commutator. The internal comparison is therefore intrinsic on a fixed projector branch.


## 8. Parameter order and exact scope

Choose the requested internal loss epsilon first, then sigma so C_(N,epsilon)sigma^2 fits the available fast reserve, then r_\* large enough for C_(N,epsilon)r_\*^-3 and the inverse-square multiplier.

On the global fast complement H_exc>=c_N r_\* and W_2<=m_N r_\*^-2, so

    W_2[v] <= C_N (r_*^-3 H_exc)[v].

This final payment is restricted to complementary inputs; (1.3) itself holds on arbitrary colored inputs. No internal Hamiltonian is inverted.

Still separate are the finite spin source, density multiplier, signed fast kinetic remainder, potential/Yukawa remainders, and branch/cutoff compatibility. The present lemma closes the complete internal-form and curvature step only.
