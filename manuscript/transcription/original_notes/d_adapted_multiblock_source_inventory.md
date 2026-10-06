# Actual adapted source inventory

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 1. Notation and exact origin

Use the kinetic-one normalization and the intrinsic slice in Appendix A. The only internal thinness hypothesis is

    alpha_a+alpha_b <= kappa r_ab,

with fixed sufficiently small kappa. Set `r_*=min r_ab`. All finite constants below depend on N but not on a ratio of unrelated gaps.

To avoid overloading center C, use these coefficient maps:

    F = E*B_(Z+A),             C = P_N B_A,
    L = E*B_Y,                 N_Y = P_N B_Y,
    I_Y = P_I B_Y,             C_Y = P_C B_Y,
    K = R^-1 C_Y*,             J_2 = K C_Y.

Thus `F` is pair-block diagonal, `C` is pair-block diagonal as a map from gauge parameters into normal fast coordinates, and

    M=F+L-J_2,   W=I+KK*.

The maps `L` and `N_Y` between distinct fast root pairs have triangle support. They have no same-pair block. The maps `I_Y` and `C_Y` use one root and its endpoints. The center metric is `g_C=I+K*K`; the internal and fast tangent metrics are exactly identity.

The definitive flattened kinetic form is

    ||(p_H+i rho)u||_(g_S^-1)^2 + ||D u||²,
    D=W^(1/2)M^-*[S_f-O*Sg_S^-1(p_H+i rho)],
    rho=d_H log d,       d=sqrt(det M).                     (1.1)

All products below inherit this ordering. Fast adjoints are taken in the flat fiber measure. The normal connection is retained in center derivatives. Nothing is obtained by substituting a momentum constraint into a squared operator.


## 2. Exact coefficients needed through H2

Use homogeneous weights

    (Z,A) -> L_scale (Z,A),  Y -> L_scale^-1/2 Y,
    p_s -> L_scale^-1 p_s,  p_F -> L_scale^1/2 p_F.

Here `s` comprises centers and all internal coordinates. Keep the internal potential and internal Yukawa terms in their complete internal Hamiltonians throughout.

Write

    log d = log d_0 + phi_2 + terms of Y-degree >=3,
    d_0=sqrt(det F),
    phi_2=-(1/2)tr(F^-1 J_2)
            -(1/4)tr(F^-1 L F^-1 L),                       (2.1)
    rho_0=d_s log d_0,    rho_F2=d_F phi_2,
    u_s=p_s+i rho_0.

There is no degree-one term because `tr(F^-1 L)=0` for every A, not only at A=0. The triangle term in (2.1) must be retained.

The Gauss derivative stack has coefficients

    D = D_0 + D_1 + D_2 + higher homogeneous orders,

of scaling degrees `1/2`, `-1`, and `-5/2`, respectively. They are

    D_0 = -F^-1 C* p_F,                                     (2.2)

    D_1 = F^-1(S_f-N_Y* p_F)
             +F^-1 L* F^-1 C* p_F,                         (2.3)

and

    D_2 = -F^-1[I_Y* u_I+(C_Y*+F K)u_C+i C* rho_F2]
          -F^-1 L* F^-1(S_f-N_Y* p_F)
          -F^-1 L* F^-1 L* F^-1 C* p_F
          -F^-1 J_2* F^-1 C* p_F
          -(1/2)KK* F^-1 C* p_F.                           (2.4)

These follow by expanding

    M^-*=F^-1-F^-1L*F^-1
             +F^-1L*F^-1L*F^-1+F^-1J_2*F^-1+...,
    W^(1/2)=I+(1/2)KK*+...,
    O*Sg_S^-1p_H
       =C*p_F+N_Y*p_F+I_Y*p_I+(C_Y*+F K)p_C+... .          (2.5)

For example `L*K p_C` first enters the next Gauss order, and `g_C^-1-I` first contributes to direct center kinetic energy at scaling degree -5; neither belongs to H2. The `F K` in (2.4) is essential and becomes `C_Y*` at A=0, so the centered center-orbital coefficient is twice `C_Y*`.

The exact leading fast Hamiltonian comprises the direct `p_F²`, `D_0*D_0`, the full adapted quadratic potential, and the fast fermion mass. Its product vacuum is `U(A)`, with energy `E_0,total`. Define

    H_exc = H_fast-E_0,total.

The vacuum-energy multiplier is handled by Appendix B. It is not inserted into a virtual excitation denominator.

The next two homogeneous form coefficients are exactly

    H_1 = V_3+Y_Y +D_0*D_1+D_1*D_0,                       (2.6)

    H_2 = ||u_s (.)||² +V_4
            +2 Re <p_F(.),i rho_F2(.)>
            +||D_1(.)||²+2 Re <D_0(.),D_2(.)>.             (2.7)

Here `Y_Y` is the Yukawa term linear in Y, including both slow-fast and fast-fast fermion terms. `V_3` is the cross term between `[Z+A,Y]` and `[Y,Y]`; `V_4` is the pure quartic fast potential. The internal potential term paired with `[Y,Y]` is already in the adapted quadratic potential. Equations (2.6)-(2.7) therefore include the terms which appear as anticommutators of the internal potential charge with higher inverse-Gauss charge coefficients; there is no permission to omit them in a charge derivation. This Hamiltonian derivation fixes them directly from the original scalar potential and the exact kinetic form.


## 3. Actual H1 source and its graph weights

Define the actual leading source

    S(A) = H_1 U(A).                                        (3.1)

It is complementary by boson parity. Each summand is a finite Gaussian-polynomial/Fock map on the full slow Clifford module. It has the graph decomposition

    S=sum_e S_e+sum_t S_t,

where an edge source has exactly two excitations on that edge (`N_e=2`) and a triangle source has exactly one excitation on every triangle edge (`N_e=N_f=N_g=1`). In the pair case these are one bosonic and one fast-fermionic excitation. Graph subspaces remain orthogonal and invariant under the adapted quadratic oscillator. Parity alone would not be the complete finite-sector statement.

The inventory is explicit:

* `Y_Y U`: a pair has `Y_e theta_e theta_s`; a triangle has `Y_e theta_f theta_g`.
* `V_3 U`: only three distinct triangle edges, one Y on each.
* `D_0*F^-1 S_f U` and its adjoint: pair terms have one `p_e` and one fast fermion; triangle terms have `p_e theta_f theta_g`.
* `D_0*F^-1 N_Y*p_F U` and its adjoint: a triangle has `p_e Y_f p_g`.
* The last term of D1 yields the same triangle support with one additional factor `F_f^-1 C_f*`.

A slow internal derivative does not occur in H1. Only the pair source contains internal/center Clifford generators; the triangle source acts trivially on the internal Clifford factors.

For a triangle let `s_t=sum_(e in t)r_e`, `w_t=sum_(e in t)r_e^-2`. Pairwise thinness gives

    ||F_e^-1|| <= C/r_e,    ||F_e^-1 C_e*|| <= C kappa.

On a fixed finite Gaussian degree, `Y_e` costs `C r_e^-1/2`, and `p_e` costs `C r_e^1/2`. Thus

    ||S_e||² <= C_N/r_e,
    ||S_t||² <= C_N s_t w_t.                               (3.2)

For the cubic potential, use

    s_t/(r_e r_f r_g)
       =1/(r_e r_f)+1/(r_f r_g)+1/(r_g r_e) <= w_t.

For the Gauss triangle `p_e Y_f p_g/r_e`, its norm is bounded by

    C kappa sqrt(r_g/(r_e r_f))
       <= C kappa sqrt(s_t) (r_e r_f)^-1/2.

The inverse-L correction has one additional bounded factor kappa. These are shape-independent estimates, including when one edge is much shorter than the other two.

Transporting only the finite oscillator coefficient spaces to their centered spaces by the actual pair functional calculus gives the coefficientwise perturbation estimates

    ||S_e(A)-S_e(0)|| <= C_N kappa r_e^-1/2,
    ||S_t(A)-S_t(0)|| <= C_N kappa sqrt(s_t w_t).             (3.3)

This is an estimate for the actual source (3.1), not a definition by transport. Every new Gauss H1 term has an explicit factor `F^-1 C*`, and the remaining actual coefficients have relative O(kappa) variation in the pair matrices and vacuum factors.


## 4. Compressed H2 and its actual scalar/Clifford multiplier

Separate the complete slow Berry-covariant form

    H_s^B=T_cent^B+sum_a(T_a^B+V_a+Y_a)

from the vacuum compression of (2.7). The remainder is a multiplication operator `W(A)` on the entire slow Clifford fiber. The following procedure is an exact specification of W:

1. In `||u_s(Uf)||²`, retain `||nabla_s^B f||²`; put the Born-Huang multiplier and `|rho_0|²+div rho_0` into W.
2. Put the vacuum expectations of V4, the displayed fast-density cross term, and `D_1*D_1` into W.
3. In `2 Re<D_0(Uf),D_2(Uf)>`, keep the written ordering. For the slow-orbital part put

       L_mu = component_mu{F^-1[I_Y*,C_Y*+F K]},
       <D_0 U,-L_mu U> = i j_mu,       j_mu real.            (4.1)

   This coefficient is purely imaginary: the bosonic Gaussian and the orbital coefficient maps are real, while D0 contains one fast momentum. The fermionic factor is its norm. Its first-order coefficient on f therefore integrates to the scalar multiplier `-div j`. All remaining terms, including derivatives on U and `i rho_0`, are placed in W. A scalar Berry term in `p_mu U` has zero real pairing with `i j_mu`, so this step is gauge covariant.

An equivalent exact scalar formula removes even the implicit derivative bookkeeping. Write `U=g(Y;s)v(s)`, with g real, put

    A_op=F^-1 C*,    a=A_op d_F log g,
    B_mu=component_mu{F^-1[I_Y*,C_Y*+F K]}.

Then `D_0 U=i a U`, and the entire slow-orbital compression is

    V_orb=-sum_mu <partial_mu(a dot B_mu)>_U
             -2 sum_mu rho_(0,mu)<a dot B_mu>_U.            (4.3)

The derivative acts on the displayed fast coefficient; Gaussian-density differentiation has already canceled the derivative of the fiber expectation. Fock/Berry derivative terms have zero real part. The direct fast-density term and the rho_F2 term in D2 combine exactly to

    V_fast-density=tr_F[(I+C F^-2 C*) Hess_Y phi_2].          (4.4)

Since phi2 is quadratic in Y, its Hessian is a coefficient matrix independent of Y. These formulas follow by one integration by parts and retain all ordering terms.

No slow derivative has been discarded or bounded by a momentum cutoff. In particular differentiating j, or the coefficient in (4.3), includes internal derivatives at A=0. Those terms participate in the centered cancellation.

### 4.1 Complete root support and coefficient bounds

Every surviving vacuum contraction in W is supported on one edge or the edges of a triangle. The following list accounts for all terms in (2.7):

* Born-Huang derivatives on two different pair vacua are orthogonal after removing the scalar Berry connection. Each remaining term is bounded by `C_N/r_e²`.
* `rho_0` is a sum of pair gradients. Their inner product vanishes for disjoint endpoint sets. A cross product on two incident edges has weight `1/(r_e r_f)` and belongs to their triangle. The divergence is pairwise.
* Wick contractions in V4 involve either one repeated root or two roots sharing an endpoint. Their weights are `r_e^-2` or `(r_e r_f)^-1`.
* The first term of phi2 is a sum of `Y_e²/r_e²` contractions. Its second term follows a root-space path `e -> f -> e` and has `Y_g²/(r_e r_f)`, where e,f,g form a triangle. A fast derivative and the momentum pairing remove the Y_g scale; the resulting weights are again `r_e^-2` or `(r_e r_f)^-1`.
* D1 contains a pair spin term with weight `r_e^-1`, and triangle terms with weights `r_e^-1` or `r_e^-1 sqrt(r_g/r_f)`. Squaring on the vacuum preserves graph orthogonality. The triangle inequality reduces the latter square to `C w_t`.
* The slow-orbital part of D2 paired with D0 gives `j_e=O(kappa/r_e)` on endpoint coordinates. Its derivative is `O(r_e^-2)` and varies from its centered value by `O(kappa/r_e²)`. Derivatives of spectator vacua are orthogonal in this compression; the products with rho0 have pair/triangle support.
* In `D_0*F^-1L*F^-1 S_f`, the two bosonic factors lie on distinct roots, so its vacuum compression is zero.
* In `D_0*F^-1L*F^-1 N_Y*p_F`, nonzero Wick contractions force the second root path to close the same triangle. The two possible pairings have weights `kappa/(r_f r_g)` and `kappa/(r_e r_f)`.
* In the two-L term of D2 the same closure gives the preceding weights with kappa squared.
* In the J2 and KK\* terms, the two orbital center maps vanish against each other for disjoint endpoint sets. Surviving weights are `kappa²/(r_e r_f)`, with the repeated-edge case included.
* The rho_F2 part of D2 has the density supports already listed and a prefactor bounded by kappa squared after pairing with D0.

For estimates on finite excited states, a root path need not close under Wick contraction. It still has a uniform inverse-square coefficient bound. For example a two-L path has normalized weight

    sqrt(r_h)/(sqrt(r_e) r_f sqrt(r_g r_j)).

The triangle relation `r_h<=r_f+r_j` bounds this by a sum of

    1/sqrt(r_e r_f r_g r_j),
    1/(sqrt(r_e) r_f sqrt(r_g)),

both bounded by a numerical multiple of the sum of inverse-square edge weights by weighted arithmetic-geometric mean. This observation is useful for mixed source terms and prevents an illicit global-frequency comparison.

All of these are finite coefficient expressions in pair matrices with external gaps comparable to their own r_e. Normalize each occurrence of an internal matrix by the incident r_e in that factor. Its norm is O(kappa). Functional calculus and its required derivatives have uniform convergent resolvent bounds on that fixed pair ball. Termwise product estimates in the above inventory therefore prove

    ||W(A)|| <= C_N W_2,
    ||W(A)-W(0)|| <= C_N kappa W_2,
    W_2=sum_e r_e^-2.                                      (4.2)

The derivative of j is included in the second estimate. It is not estimated merely by the small value of j, which would miss a nonzero centered internal derivative.


## 5. Actual shifted-fast correction and leading operator defect

On the pair source space the adapted excitation energy is at least `c r_e`; on the triangle source space it is at least `c s_t`. The finite matrix resolvent identity, applied to the actual sources (3.1), gives

    ||S_e*H_exc^-1 S_e-S_e(0)*H_f(0)^-1 S_e(0)||
          <= C_N kappa r_e^-2,

    ||S_t*H_exc^-1 S_t-S_t(0)*H_f(0)^-1 S_t(0)||
          <= C_N kappa w_t.                                (5.1)

Cross terms between distinct graph spaces vanish. The centered source lemma, including all internal vacuum derivatives and compression jets, gives

    W(0)=S(0)*H_f(0)^-1 S(0).

Consequently the actual leading operator defect satisfies

    ||W(A)-S(A)*H_exc(A)^-1 S(A)||
          <= C_N kappa W_2.                                (5.2)

This is an operator-norm estimate on the complete internal Clifford module. Its actual fast dressing is

    Z(A)=-H_exc(A)^-1 S(A),                                 (5.3)

and obeys the root-graph bounds and spectator-derivative correction from Appendix C. No interacting internal Hamiltonian occurs in (5.3). The fast energy E0 remains a separate multiplier with its proved commutator-square payment.


## 6. All-vector use and the remaining reserve requirement

The graph-local lemma now applies to the actual dressing (5.3): its coefficients are the explicit graph-local functions above. Smooth pair functional calculus gives active derivative weights `C r_e^-5` or `C(sum_t r_e^-1)²w_t/s_t`; spectator derivatives add `C m_g W_2`. Therefore

    H_s[Zf] <= C_N r_*^-3 H_s[f]
                 +C_N kappa W_2[f]+C_N W_5[f].              (6.1)

In fact triangle sources have no internal Clifford generator, so outside derivative commutators are the only issue for their internal potential charges. The more general graph bound is valid without using this improvement. All internal momenta in (6.1) are unrestricted.

The identity `H_exc Z+S=0` cancels the actual leading complementary source exactly. The complete internal/center form pairs involving Z can be controlled by Cauchy-Schwarz in H_s, using (6.1). The remaining derivative source from U is incident-edge weighted and has the same payment as Section 6 of the geometric lemma. These steps are valid form estimates on arbitrary complementary vectors in the corresponding control norm; they are not a finite oscillator truncation of those vectors.

What is not supplied here is an inequality extracting that control norm from the original complementary form while retaining the same Gauss square. In particular, the expression

    H_s[v]+H_exc[v]+||D_full v||²

cannot be added to the right side of the original Hamiltonian merely because its three terms are nonnegative. H_exc already uses the frozen piece of D_full. The desired actual all-vector comparison still needs a non-double-counted reserve, compatible with unrestricted slow momenta, and a complete mixed/remainder estimate in that reserve. Finite coefficient cancellation (5.2) cannot prove this coercivity.

Thus Sections 2–5 identify and estimate the actual leading H1/H2 source coefficients. Section 6 supplies their internal-momentum payment and states the precise remaining all-vector obstruction rather than silently assuming it away.
