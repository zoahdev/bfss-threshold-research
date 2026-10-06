# Rootwise all vector connection estimates

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 1. Assumptions and the excitation energy

Fix the rank and a partition. For every root/pair e=(a,b), let r_e=|z_a-z_b| and assume alpha_a+alpha_b <= kappa r_e, with kappa sufficiently small. Write r_\*=min_e r_e and W_2=sum_e r_e^-2. No ratio r_max/r_\* is restricted.

Freeze the slow variables. Let

    H_fast,e = H_B,e + H_F,e,
    E_0,e = E_B,e + E_F,min,e,
    h_e = H_fast,e - E_0,e
        = (H_B,e-E_B,e) + (H_F,e-E_F,min,e).

Here H_B,e is the exact kinetic-aware bosonic oscillator. The uniform pair-matrix bounds give

    c(p_e^2+r_e^2 Y_e^2) <= H_B,e <= C(p_e^2+r_e^2 Y_e^2),
    E_B,e <= C r_e,
    h_e >= c r_e Q_e,

where P_e is its full boson/fermion vacuum projection and Q_e=1-P_e. In particular

    ||p_e Q_e v||^2 <= C h_e[v],
    ||Y_e v||^2 <= C r_e^-2 h_e[v] + C r_e^-1 ||v||^2,
    ||p_e P_e v||^2 <= C r_e ||P_e v||^2,
    ||Y_e p_e P_e v||^2 <= C ||P_e v||^2.                 (1)

The last two statements also hold with any uniformly bounded finite color/spatial matrices between the displayed operators. Constants depend only on rank and the fixed small pair-matrix neighborhood. h_e, rather than H_B,e or a centered oscillator, is essential.

Let chi be any multiplication cutoff with |chi|<=1 supported in |Y|<=sigma r_\*. Derivatives of chi are not used below. Every estimate is a fast-fiber estimate for arbitrary vectors, with arbitrary spectator fast modes and arbitrary slow/Clifford coefficient vectors. It can be integrated over the slow variables. No internal momentum or oscillator-degree cutoff is imposed. No individual internal singlet condition is imposed; the estimates remain valid on the total residual-equivariant space.


## 2. Same-root and mixed-root lemmas

For any pair e and any positive denominator scale r_g drawn from the retained roots,

    ||chi Y_e p_e v/r_g||^2
      <= C sigma^2 (r_*^2/r_g^2) h_e[v]
           + C r_g^-2 ||v||^2.                           (2)

Proof: split the INPUT as P_e v+Q_e v. On Q_e use |chi Y_e|<=sigma r_\* and the first inequality in (1). On P_e use the last inequality in (1), dropping chi. The factor two from the split is harmless. P_e v need not be supported in the tube. No argument asserts that P_e preserves tube support.

For distinct roots e and f,

    ||chi Y_f p_e v/r_g||^2
      <= C sigma^2 (r_*^2/r_g^2) h_e[v]
       + C r_e/(r_g^2 r_f^2) h_f[v]
       + C r_e/(r_g^2 r_f) ||v||^2.                      (3)

Indeed the Q_e input is as above. On the P_e input, drop chi, commute Y_f with P_e, and use ||p_e P_e||^2<=C r_e followed by the Y_f bound in (1). Equivalently split the remaining f input into P_f and Q_f. This is the step that cannot be omitted from a mixed-root claim.

If e,f,g are the three edges of a triangle, r_e<=r_f+r_g, so

    r_e/(r_g^2 r_f^2) <= 2 r_*^-3,
    r_e/(r_g^2 r_f) <= r_g^-2+(r_g r_f)^-1 <= C W_2,t.

Consequently

    ||chi Y_f p_e v/r_g||^2
      <= C (sigma^2+r_*^-3) (h_e[v]+h_f[v])
           + C W_2,t ||v||^2.                            (4)

For the input-root denominator g=e, the same conclusion follows directly, without any triangle hypothesis, with residual (r_e r_f)^-1. In (2)-(4), Y and p can be contracted with any bounded root-preserving finite matrices. Finite sums of such sources obey the same bounds after enlarging the rank-dependent constant.

A triangle hypothesis (or another restriction on r_e relative to r_f,r_g) is genuinely necessary to replace (3) by (4): the P_e P_f input has squared size comparable to r_e/(r_g^2 r_f). An arbitrary unrelated r_e cannot disappear from this expression.


## 3. Exact inverse-M factorization for the fast column

Use the notation of the intrinsic geometry and adapted source inventory:

    M=F+P,   P=L-J_2,   J_2=K C_Y=R^-1 C_Y* C_Y,
    W=I+K K*,   K=R^-1 C_Y*,
    T=(I+F^-1 P*)^-1,
    M^-*=T F^-1,
    d_0(v)=F^-1 C* p_F v.

F is self-adjoint pair-block diagonal; ||F_e^-1 C_e\*||<=C kappa. On the tube,

    ||P F^-1||+||F^-1 P*|| <= C sigma,
    ||T||+||W^(1/2)|| <= C,
    ||K|| <= C sigma.

Let B p_F=W^(1/2) M^-\*(C\*+N_Y\*)p_F be the exact fast column of the Gauss stack. Algebraically, with the indicated operator ordering,

    B p_F-d_0
      =(W^(1/2)-I)d_0
       +W^(1/2)T[
          F^-1 N_Y* p_F
          -F^-1 L* d_0
          +F^-1 J_2* d_0].                               (5)

There are no derivatives of inverse matrices in this first-order form identity.

The first two bracketed expressions are finite triangle sources Y_f p_e/r_g, with respectively bounded and O(kappa) root-preserving factors. The last expression factors as

    F^-1 J_2* d_0
      =F^-1 C_Y* [C_Y R^-1 d_0],                         (6)

where ||F^-1 C_Y\*||<=C sigma and C_Y R^-1 d_0 is a sum of same-root terms Y_e p_e/r_e with O(kappa) coefficients. Also

    (W^(1/2)-I)d_0
      =(W^(1/2)+I)^-1 K [K* d_0],
    K* d_0=C_Y R^-1 d_0.                                 (7)

Thus all potentially troublesome inverse-M matrices remain bounded left factors. Equations (2)-(7) prove

    ||chi (B p_F-d_0)v||^2
      <= C (sigma^2+r_*^-3) sum_e h_e[v]
           + C W_2 ||v||^2.                              (8)

The estimate holds for arbitrary fast vectors. It is not an estimate restricted to vacuum or a finite excited coefficient space.

The spin column obeys separately

    ||chi W^(1/2)M^-* S_f v||^2 <= C W_2 ||v||^2,          (9)

because the finite fermionic Gauss matrices are bounded and F^-1 retains the individual output-root denominators.


## 4. Exact slow-square coefficient and its Schur loss

Let G_s=diag(g_C^-1,I_I), so the direct slow kinetic stack is w=G_s^(1/2)p_s. The exact normalized slow column in the Gauss square is

    A=W^(1/2)M^-* Psi,
    Psi=[(C_Y*+(F+L)*K)g_C^-1/2, I_Y*].                  (10)

This follows directly from O\*Sg_S^-1. In particular the F K term must be retained. One has

    ||Psi*F^-1|| <= C sigma,
    ||A|| <= C sigma.                                    (11)

The adjoint coefficient acting on the frozen fast column has the exact expression

    A* d_0=Psi*F^-1 T*W^(1/2)d_0.                        (12)

Expand

    T*W^(1/2)-I=(T*-I)+T*(W^(1/2)-I),
    T*-I=-T* P F^-1.                                    (13)

The leading term Psi\*F^-1 d_0 is the stack of

    I_Y F^-1 d_0,
    g_C^-1/2[C_Y F^-1 d_0+K* d_0+K* L F^-1 d_0].         (14)

The first three contractions are same-root Y_e p_e/r_e. L F^-1 d_0 is a triangle source with INPUT-root denominator r_e, so (3) applies even without using a frequency ratio. The J_2 part of P F^-1 d_0 factors as

    J_2 F^-1 d_0=R^-1 C_Y* [C_Y F^-1 d_0],               (15)

again a bounded O(sigma) left factor times a same-root contraction. Equations (7), (11), and (13)-(15) therefore prove the sharper estimate

    ||chi A* d_0(v)||^2
      <= C kappa^2 (sigma^2+r_*^-3) sum_e h_e[v]
           + C kappa^2 W_2 ||v||^2.                      (16)

Combining (8), (9), and ||A||<=C sigma also controls A\* applied to the full fast-plus-spin stack, with a coefficient C(kappa^2+sigma^2) multiplying the right side of (8), and a harmless C sigma^2 W_2 spin term.

For completeness, for any vectors w,b and eta>0,

    eta||w||^2+||b-Aw||^2
      =||(eta I+A*A)^(1/2)
          [w-(eta I+A*A)^-1 A*b]||^2
          +<b,(I+eta^-1 A A*)^-1 b>.

The difference between ||b||^2 and the final term is at most eta^-1||A\*b||^2. Thus (16) controls the frozen-column Schur loss by exact excitation energies and W_2, with no delta sum_e r_e zero-point cost. This is a first-order form identity: variable coefficients create no omitted ordering terms at this stage.


## 5. What this lemma does and does not close

It closes the all-vector rootwise CONNECTION-NORM sublemma, including mixed roots, exact inverse-M left factors, and the coefficient occurring after slow-square completion. It remains valid with unrestricted internal momenta because none of its steps estimates those momenta or differentiates a fast projection in a slow direction.

At the connection-norm stage, two additional arguments are necessary. Section 6 below supplies the first for the fast kinetic column:

1. Bounding a squared connection norm is not a bound for the bilinear pairing with d_0. The direct Young estimate against ||d_0 v||^2 introduces its frozen vacuum energy C kappa^2 sum_e r_e. The odd H1 source / normal-ordering or graph-local form argument must be used instead; (8) alone does not perform it.
2. Completing all slow squares leaves shifted slow derivatives. Splitting off eta times ordinary internal kinetic energy is not the same as splitting eta times the colored internal supersymmetric form: an unweighted Yukawa remainder eta C alpha_a may be large for a far block. One must retain a suitable full slow-supercharge form or prove an incident-weighted conversion of the shifted slow squares. Equations (10)-(16) do not silently supply that conversion.

Accordingly these results are compatible with, but do not establish, a near-sharp complementary lower bound in the original Hamiltonian. They provide the rootwise estimate that avoids a global-frequency substitution at the connection stage.


## 6. Addendum: signed fast kinetic terms without a vacuum-frequency loss

The first obstruction listed in Section 5 can also be removed for the exact fast kinetic column. The following statements concern a smooth core vector v supported in the fast tube; an outer cutoff equal to one near its support may always be used in Sections 2-4. Only that support requirement, not a restriction on the oscillator content of v, is imposed.

### 6.1 All-vector triangle multiplication

For distinct triangle roots e,f,g, write s_t=r_e+r_f+r_g. Any uniformly bounded real coefficient tensor that may depend on the slow variables but is independent of the fast variables Y obeys

    |<v,s_t Y_e Y_f Y_g v>|
       <= C sigma sum_(j in t) h_j[v]
          + C sigma^-1 W_2,t ||v||^2.                   (17)

First, splitting inputs into Q_f, P_f Q_g, and P_f P_g gives

    ||chi Y_f Y_g v||^2
       <= C sigma^2 r_*^2 [r_f^-2 h_f[v]+r_g^-2 h_g[v]]
          + C/(r_f r_g) ||v||^2.                        (18)

On the first component bound chi Y_g by sigma r_\* and use the excited Y_f oscillator bound; on the second use chi Y_f and the excited Y_g bound; on the last use both Gaussian widths. The splitting is for estimation only; the projected pieces need not have tube support.

Choose e to be a largest triangle root. If U_B,e=constant exp(-Y_e·Omega_e Y_e/2), put a_e=partial_e+Omega_e Y_e. The exact bosonic excitation form controls ||a_e v||^2. Since the other two factors do not depend on Y_e, integration by parts gives, componentwise,

    <v,Y_e Y_f Y_g v>
       =Re<a_e v,Omega_e^-1(Y_f Y_g)v>.

Using ||Omega_e^-1||<=C/r_e, s_t/r_e<=3, and (18) gives (17) by Young with parameter sigma. The proof is valid for arbitrary fermionic and slow vector coefficients.

### 6.2 Leading triangle differential forms

Let a(Y) be a real symmetric fast coefficient matrix supported only in the off-diagonal root blocks (e,g) and (g,e), with each entry a bounded linear contraction of Y_f divided by r_e, multiplied by a coefficient O(kappa) that is independent of the fast variables Y (it may depend on the slow variables). For the product bosonic Gaussian U_B, writing v=U_B u gives the exact identity

    integral (partial v)* a (partial v)
      =integral U_B^2 (partial u)* a (partial u)
       +integral [div(a Omega Y)-(Omega Y)·a(Omega Y)] |v|^2.
                                                                    (19)

This identity does not project onto the fermionic vacuum. The excitation form satisfies

    sum_e (H_B,e-E_B,e)[v]
       =integral U_B^2 (partial u)*G(partial u),

with G uniformly positive. On tube-supported v, the first term in (19) is bounded in absolute value by C kappa sigma sum_e h_e[v]. The divergence term in (19) vanishes: a connects distinct roots, depends on the third root, and Omega is pair-block diagonal. The remaining scalar is a triangle cubic with coefficient O(kappa r_g), hence is bounded by (17). Consequently

    |integral (partial v)* a (partial v)|
      <= C kappa sigma sum_(j in t) h_j[v]
          + C kappa sigma^-1 W_2,t ||v||^2.              (20)

The same proof applies to O(kappa^2) coefficients. Equation (20) applies to both leading triangle forms from

    2 Re<d_0,F^-1 N_Y* p_F-F^-1 L* d_0>.

No derivative cutoff is needed: (19) is applied to the original polynomial coefficient and v itself has tube support. If one instead wants a globally cut-off form on arbitrary unsupported inputs, cutoff derivatives must be included; an even radial cutoff generates additional triangle cubics, with coefficient smaller by O((sigma^2 r_\*^3)^-1).

### 6.3 Full inverse-M reduction

There is a short exact reduction avoiding an infinite expansion. Set

    Z=F^-1 P*,   T=(I+Z)^-1,
    n=F^-1 N_Y* p_F,
    X=n-Z d_0.

Then

    B p_F=W^(1/2)(d_0+T X).

Because W>=I and T-I=-ZT,

    ||B p_F v||^2
      >=||d_0 v||^2+2 Re<d_0 v,Xv>
          -2 |<Z* d_0 v,T Xv>|.                         (21)

Both X and Z\* d_0=P F^-1 d_0 are covered by the rootwise connection estimates. The last pairing is therefore bounded by

    C(sigma^2+r_*^-3) sum_e h_e[v]+C W_2||v||^2.

Inside <d_0,X>, the J_2 term factors exactly as

    <d_0,F^-1 J_2* d_0>
       =<C_Y F^-1 d_0,C_Y R^-1 d_0>,                    (22)

and has the same bound. Only the two linear triangle forms in Section 6.2 remain. Combining (20)-(22) gives

    ||B p_F v||^2
      >=||d_0 v||^2
         -C[kappa sigma+sigma^2+r_*^-3] sum_e h_e[v]
         -C(1+kappa/sigma) W_2||v||^2.                  (23)

Thus direct p_F^2 plus the exact Gauss FAST column, the adapted quadratic potential, and its fast fermion mass have a lower bound

    E_0,total ||v||^2
       +(1-C[kappa sigma+sigma^2+r_*^-3]) H_exc[v]
       -C(1+kappa/sigma) W_2||v||^2,                    (24)

with the frozen E_0 multiplier understood pointwise in the slow variables. This is a fast-column comparison only; the slow derivatives in the full Gauss square have not been dropped or independently counted.

### 6.4 Frozen spin-linear term

The leading spin cross is a finite sum A_e p_e/r_e, with Y-independent Hermitian Clifford matrices ||A_e||<=C kappa. Since the Omega_e Y_e part of a_e=partial_e+Omega_e Y_e contributes a real expectation against A_e,

    |<v,A_e p_e v/r_e>|
      <= C kappa r_e^-1 sqrt(h_B,e[v]) ||v||
      <= epsilon h_e[v]+C kappa^2/(epsilon r_e^2)||v||^2. (25)

Here h_B,e=H_B,e-E_B,e. This also avoids any bosonic vacuum-frequency cost. The inverse-M corrections to this frozen spin cross pair rootwise connection errors with the bounded spin column (9), and are bounded by epsilon H_exc+C_epsilon W_2.


## 7. Final scope after the addendum

Equations (2)-(16) prove the connection and Schur-loss norm statements for arbitrary fast vectors. Equations (17)-(25) additionally prove the signed fast-column comparison on an unrestricted oscillator core supported in the fast tube. These estimates remove the need for a delta sum_e r_e loss at the fast-connection stage.

They still do not convert the completed, shifted slow derivative form into a nonnegative colored internal supersymmetric form. One must control its connection curvature/full-supercharge terms or use another incident-weighted argument. In particular a constant loss of internal kinetic energy cannot simply be identified with the same loss of H_a. That slow-form issue, the other physical potential/Yukawa terms, and the final allocation of one non-double-counted reserve belong to the full complementary theorem, not to this helper lemma.
