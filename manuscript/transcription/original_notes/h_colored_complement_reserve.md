# Colored complementary reserve

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 1. Coordinate conventions and exact matrices

Use the intrinsic geometry note and the notation of the actual adapted source inventory:

    F=E*B_(Z+A), C=P_NB_A, L=E*B_Y, N_Y=P_NB_Y,
    I_Y=P_IB_Y, C_Y=P_CB_Y, K=R^−1C_Y*, J2=KC_Y,
    M=F+L−J2, W=I+KK*, g_C=I+K*K.

Let p_s=(g_C^−1/2 p_C,p_I), where p_C includes the exact normal connection. Define

    Ψ=[(C_Y*+(F+L)*K)g_C^−1/2,I_Y*],
    A=W^1/2M^−*Ψ,
    a=Bp_F=W^1/2M^−*(C+N_Y)*p_F,
    s=−W^1/2M^−*S_f.

The minus sign in s matches the original Gauss expression S_f−fast−slow after multiplying that whole stack by −1. The unshifted scalar kinetic stack is exactly

    |p_s v|²+|p_Fv|²+|a v+A p_s v+s v|².                 (1.1)

The scalar half-density term is added after this first-order identity. We never add the same Gauss square a second time to H_fast.

Throughout, T_cent[v]=||p_Cv||² with the exact normal connection. Its direct induced-metric coefficient obeys g_C^−1≥(1+Cσ²)^−1I; this small center-only loss is included in the final allocation.

Set D0=F^−1C\*p_F, P=L−J2, Z=F^−1P\*, T=(I+Z)^−1, n=F^−1N_Y\*p_F. Thus

    a=W^1/2 T(D0+n),   ||T||+||T^−1||≤C,   ||A||≤Cσ.   (1.2)

The frozen kinetic contribution in H_fast is p_F²+||D0||².


## 2. Oscillator estimates with the vacuum kept explicitly

The adapted bosonic Gaussian on edge e is exp(−Y_e·Ω_eY_e/2), with c r_e I≤Ω_e≤C r_e I. Let a_e=∂_e+Ω_eY_e be its annihilation gradient. Then ||a_ev||²≤C h_e[v], including arbitrary fermionic and spectator components. The shifted fermionic excitation form is nonnegative and only improves this inequality.

The following estimates are consequences of splitting each edge into its adapted full vacuum P_e and Q_e=1−P_e; see Appendix E for the first two:

    ||χY_ep_e/r_e v||²≤Cσ²h_e[v]+Cr_e^−2||v||²,         (2.1)

    ||χY_fp_e/r_g v||²≤C(σ²+r_*^−3)(h_e+h_f)[v]
                             +CΣ_(u in triangle)r_u^−2||v||². (2.2)

A useful sharpened two-coordinate version is

    ||χY_fY_gv||²≤Cσ²r_*²(h_f[v]/r_f²+h_g[v]/r_g²)
                             +C/(r_fr_g)||v||²,               (2.3)

for distinct edges f,g. To prove it, decompose into Q_f, P_fQ_g and P_fP_g. On the first two pieces use |χY_g|≤Cσr_\* or |χY_f|≤Cσr_\*, and ||Y_fQ_fv||²≤C h_f[v]/r_f² (similarly g). On the last use the exact Gaussian second moments. Finite-sum Cauchy–Schwarz supplies the displayed constant. The cutoff acts only on the left; it need not commute with P_f.

In every triangle e,f,g,

    r_*r_g/(r_er_f)≤2,    r_g/(r_e²r_f)≤C(r_e^−2+r_f^−2). (2.4)

These elementary triangle inequalities are what remove remote zero-point energies.


## 3. Direct cubic potential, with arbitrary fast vectors

Let e,f,g be a triangle, s_t=r_e+r_f+r_g, and let B_t be any fixed bounded trilinear contraction of the three real fast coordinate spaces, also allowing a bounded spectator matrix. Then

    |<v,s_t B_t(Y_e,Y_f,Y_g)v>|
      ≤Cσ(h_e+h_f+h_g)[v]+Cσ^−1Σ_(u in t)r_u^−2||v||². (3.1)

Choose e with largest r_e. For a scalar component, integration by parts gives exactly

    < v,Y_eY_fY_g v >
     =Re< a_ev, Ω_e^−1(Y_fY_g)v >.                           (3.2)

There is no derivative of Y_fY_g in the e coordinate. Equation (3.2) applies componentwise to the finite contraction, with Ω_e^−1 acting on its e index. Use s_t/r_e≤3, (2.3), r_\*≤r_f,r_g and Young with parameter σ. The source term is at most Cσ^−1/(r_fr_g), which is bounded by the triangle W2. This proves (3.1). No finite oscillator truncation is made.

Every actual cubic potential term has a bounded coefficient times s_t: its coefficient is a commutator with Z+A, whose norm is ≤C(r_e+r_f+r_g) under the pairwise-relative internal tube. Therefore (3.1) applies to the full V3. V4 remains positive and is not spent.


## 4. Signed triangle kinetic forms

For any bounded real coefficient contraction and three distinct triangle edges,

    |2Re<p_ev, (Y_f/r_e)p_gv>|
     ≤Cσ(h_e+h_f+h_g)[v]+Cσ^−1Σ_(u in t)r_u^−2||v||². (4.1)

The clean proof is the Gaussian ground-state transform. The real symmetric principal coefficient a_eg(Y)=Y_f/r_e has no divergence in either active derivative coordinate e,g. For the product Gaussian g_B,

    ∫(∂v)*a∂v
     =∫g_B²(∂(v/g_B))*a∂(v/g_B)
      +∫[div(aΩY)−(ΩY)·a(ΩY)]|v|².                         (4.2)

The first term is ≤CσΣh_e because |Y_f|/r_e≤Cσ on the support. The divergence term is zero since the three roots are distinct. The last term is a triangle cubic with coefficient bounded by C r_g, hence by C s_t, and (3.1) proves (4.1). An outer cutoff equal to one near the support contributes no derivative term there.

One may instead expand p=−i a+iΩY. Formula (2.3), together with (2.4), controls the apparently dangerous factor r_g/r_e in the mixed annihilator/quadratic term. This gives the same bound without ever estimating p_e² by h_e plus an unassigned r_e vacuum mass.


## 5. Exact inverse-M reduction: higher paths are products of errors

Let X=n−ZD0. The connection bounds imply

    ||Xv||²+||Z*D0v||²
     ≤C(σ²+r_*^−3)H_exc[v]+CW2[v].                          (5.1)

For X this is the displayed helper lemma. For Z\*D0=P F^−1D0 the linear L term is a triangle map Y_f p_e/r_e; the J2 term factors through C_YF^−1D0, a same-edge map, followed by bounded K. Thus the identical proof applies. Denominators stay on their actual input or output root.

Since W≥I and T−I=−ZT exactly,

    ||av||²≥||D0v+TXv||²
     ≥||D0v||²+2Re<D0v,Xv>−2|<Z*D0v,TXv>|.                 (5.2)

The last term is bounded by (5.1). The J2 part of the remaining cross factors as

    <D0,F^−1J2*D0>=<C_YF^−1D0,K*D0>,                       (5.3)

and both factors satisfy the same-edge bound. The two other terms are precisely

    2Re<D0,F^−1N_Y*p_F>−2Re<D0,F^−1L*D0>.                   (5.4)

Their root supports are triangles; their coefficients are bounded by Cκ/r_e and Cκ²/r_e. They obey (4.1). Consequently

    ||av||²≥||D0v||²−C(κσ+σ²+r_*^−3)H_exc[v]
                             −C(1+κ/σ)W2[v].                 (5.5)

This is an actual all-vector signed-form comparison for the coupled inverse-M fast column. It does not require a separate estimate of every higher Neumann path. Importantly, it never bounds the large D0 vacuum norm by the nearest complementary gap.


## 6. Exact slow completion and finite-spin payments

With s temporarily omitted, the identity

    ||p_s v||²+||a v+A p_s v||²
     =||(p_s+A*a)v||²+||av||²+||A p_sv||²−||A*a v||²         (6.1)

holds pointwise on the first-order stack. The final negative term is controlled by

    ||A*a v||²≤C(σ²+r_*^−3)H_exc[v]+CW2[v],                  (6.2)

because A\*a=A\*D0+A\*(a−D0), ||A||≤Cσ, and both helper norms are established. Equation (6.1) leaves the explicit nonnegative reserve ||A p_sv||². It does not reserve another copy of the full Gauss square.

The center component of the shifted square is compared to the original exact normal-covariant center kinetic by ordinary Young, costing εT_cent plus ε^−1 times (6.2). Internal components are treated by the complete averaged charges in Section 7; one must not apply this ordinary Young inequality to the internal kinetic square alone.

Restore s. Drop its positive norm square and expand its two cross terms. Put s0=−F^−1S_f, so ||s0||²≤CW2. The cross <s,a> differs from <s0,D0> by a quantity bounded by εH_exc+C_εW2. To verify this, expand T\*WT−I once: every factor moved onto D0 is ZD0, Z\*D0, or KK\*D0, all controlled by (2.1), (2.2), (5.1). The remaining factors are uniformly bounded. The n terms use (2.2). The leading <s0,D0> is a finite sum p_e times a Hermitian fast/slow Clifford matrix of norm Cκ/r_e. Its real form pairs with a_e, since the Gaussian drift has purely imaginary expectation against that Hermitian matrix. Hence it is bounded by εh_e+C_εκ²r_e^−2.

For the internal part of <s,A p_s>, define w_a=Σ_(e incident a)r_e^−3. Factoring M^−1=R^−1(MR^−1)^−1 gives, for its coefficient β_s,a,

    ||β_s,av||²/w_a
     ≤CW2 Σ_(e incident a)r_e||Y_ev||²
     ≤C r_*^−3H_exc[v]+CW2[v].                              (6.3)

Weighted Young loses γΣ_a w_at_a, plus γ^−1 times the right side. This is a vanishing loss of the complete colored internal forms because

    t_a≤H_a+c_a alpha_a,
    Σ_a w_a alpha_a≤CκW2.                                   (6.4)

The weights depend only on centers, so no internal derivative of a weight occurs. Center spin cross terms use ordinary center Young. The direct linear-Y Yukawa terms obey εH_exc+C_εW2 by (3.2) with one Y and a bounded Hermitian Clifford matrix.

All spin estimates remain on the whole colored internal module. They make no physical-sector assumption.


## 7. Complete differential-connection curvature payment

Write the internal component of β=A\*a as β_j=b_j(Y;Z,A)·p_F. This is real and fast-bosonic, hence commutes with internal coordinates and internal Clifford matrices. Its symmetric version is

    βhat_j=β_j−(i/2)div_F b_j.

The averaged sixteen internal charges can therefore be used with p_A+βhat. There is no additional internal-potential anticommutator; the only algebraic correction is a finite Clifford contraction of the fast-bosonic curvature

    F_jk=i[P_j,P_k]=p_sym(∂_j b_k−∂_k b_j+[b_j,b_k]),
    P_j=p_Aj+βhat_j.                                         (7.1)

The nonsymmetric-to-symmetric kinetic conversion also has the exact scalar correction

    (1/2)X_j(div_F b_j)+(1/4)(div_F b_j)²,
    X_j=∂_Aj+b_j·∂Y.                                        (7.2)

The companion proof Appendix G establishes the actual rootwise bound

    |<v,F_jkv>|+|<(7.2)v,v>|
     ≤C(σ²+r_*^−3)H_exc[v]+C W2[v].                          (7.3)

The proof does not infer (7.3) from a norm bound alone. Internal differentiation of the explicit rootwise source decomposition preserves the same-edge and triangle source classes and adds one factor at most C/r_\*. Thus ||r_\*∂Aβhat v||²≤C[(σ²+r_\*^−3)H_exc[v]+W2[v]]. Weighted Cauchy with ||r_\*^−1v||²≤W2[v] pays the derivative curvature. Symmetry bounds each commutator-curvature expectation by 2||βhat_jv||||βhat_kv||. The scalar divergence correction is bounded by CW2 from the actual first and second coefficient derivatives. Averaged-charge Cauchy–Schwarz therefore yields

    H_I(p+β)≥(1−ε)H_I−C_ε(σ²+r_*^−3)H_exc−C_εW2,           (7.4)

retaining the entire interacting H_I, not a fixed fraction of t_A alone.


## 8. Density, vacuum defect, and the final allocation

The density term is bounded by CW2 uniformly on the pairwise tube. Indeed M R^−1 and its inverse are uniformly bounded; each slow or fast derivative of their explicit normalized entries is ≤C/r_\*, and a second derivative is ≤C/r_\*². The principal co-metric and the required normal-covariant coefficient derivatives obey the same bounds. In d^−1div(a∂d), these give C/r_\*²≤CW2. This argument uses actual normalized matrices and does not compactify a set of gap ratios.

The frozen E0,total is paid separately by the incident commutator-square result Appendix B. Directly, |E0,total|≤CΣ_a w_aV_a≤Cr_\*^−3H_I+CκW2, with fixed endpoint multiplicities absorbed in C. This uses V_a≤H_a+c_a alpha_a and the incident bound w_a alpha_a≤CκW2. The first term is a vanishing complete-internal-form loss; the second remains in the allowed inverse-square remainder. Thus this local reserve does not require a separate center-Hardy argument. E0,total is never included in H_exc or a virtual excitation denominator.

Equations (7.3), (3.1), (5.5), (6.1)–(6.4), the density bound, and the exact Hamiltonian potential/Yukawa inventory give, for every desired δ>0, constants κ_δ, σ_δ, R_δ and C_δ, independent of all gap ratios,

    H_full[v]≥(1−δ)(H_I[v]+T_cent[v]+H_exc[v])−C_δW2[v],     (8.1)

on the tube with κ≤κ_δ, σ≤σ_δ and r_\*≥R_δ. Uniformity for nested smaller fast tubes follows by proving the estimate at the fixed positive width σ_δ and restricting its core; C_δ is not obtained by substituting a varying σ into σ^−1. A nonnegative fraction of ||A p_sv||² and V4 may also be retained by allocating their positive terms explicitly. This is not a reserve of the original full Gauss square.

For v fiberwise orthogonal to the adapted product vacuum, H_exc[v]≥c r_\*||v||². Since W2≤(#edges)r_\*^−2, increasing R_δ absorbs C_δW2 into δH_exc. The resulting complementary reserve is near-unit in the full colored H_I, center kinetic, and shifted excitation form. Starting (8.1) with δ/2 gives a final displayed coefficient 1−δ after this absorption.

For a projection-stable tube realization first fix a positive cutoff width σ0≤σ_δ, then choose the exterior radius so σ0²r_\*³ is large. Choose a smooth χ0 with support strictly inside the validity tube and equal to one on a smaller tube, using the smooth harmonic minimum of pair separations. Put Uσ=χ0U/||χ0U||. The fixed-rank Gaussian tail gives ||Uσ−U||≤τ≤C exp(−cσ0²r_\*³), uniformly in all gap ratios. For v fiberwise orthogonal to Uσ, |<U,v>|≤τ||v||, hence H_exc[v]≥cr_\*(1−τ²)||v||². Both Uσf and v=u−Uσf have Dirichlet form support. Thus the same complementary reserve holds for this cutoff projection once the exterior radius is enlarged. Gaussian derivative tails needed in a subsequent mixed-source calculation are separate estimates.

The reserve retains the actual normal-bundle center derivative, with no replacement by a bounded Berry coefficient. On the low vacuum line the scalar pure-internal and mixed center/internal Berry comparison is the rootwise full-charge lemma in source Section 4.2 in Appendix F: its costs are C_N(κ+ε^−1κ^4)W2. This does not require a flat determinant line.

No claim about mixed low/complement source estimates follows merely from (8.1), especially if those estimates spend the full original Gauss square instead of the actual reserve left by (6.1). The full inverse-square Feshbach conclusion remains separate from this complementary theorem.
