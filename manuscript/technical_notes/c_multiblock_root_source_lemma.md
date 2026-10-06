# Centered sources and graph estimates

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 0. Result and scope

For any fixed partition `(n_1,...,n_k)`, the centered coefficient calculation has an exact root-graph resolution:

* Each two-block charge source occupies two quanta of one root pair and has fast energy `4r_ab`.
* Each genuine three-block charge source occupies one quantum on every edge of a triangle and has fast energy `2(r_ab+r_bc+r_ca)`.
* On residual block-center-neutral states, the leading inverse-square Schur multiplication cancels as an operator on the entire internal Clifford module. Internal derivatives of the adapted vacuum are included in this statement; freezing the internal coordinates is not permission to discard those derivatives.
* The associated finite dressing has pair weight `C_N r_ab^-3` and triangle weight `C_N [r_ab^-2+r_bc^-2+r_ca^-2]/(r_ab+r_bc+r_ca)`. The latter summed denominator is essential beside a far large block and a close opposite pair.
* A graph-local multiplier lemma turns these weights into a small multiple of the complete slow supersymmetric form plus a small pairwise center-Hardy multiplier, without expanding an inverse around an internal Hamiltonian and without applying physical internal Hardy to colored vectors.

The nonzero internal coefficient continuation is supplied in Appendix D; analyticity of the oscillator matrices alone would not supply that continuation.


## 1. Fibers, neutral sector, and the correct fast inverse

Write `b_ab=z_a-z_b`, `r_ab=|b_ab|`, and `d_ab=n_a n_b`. Centers have mass metric `sum_a n_a |dz_a|²`. Internal matrices `A^(a)` are traceless Hermitian, with radii

    alpha_a² = sum_i ||A_i^(a)||_F².

The hypotheses used in graph estimates are genuinely pairwise:

    alpha_a <= kappa r_ab  for every b != a,
    r_ab >= r_* > 0.

No comparison of one gap with an unrelated gap is made.

At `A=0` the fast vacuum is a product `U_0= tensor_(a<b) U_ab`. Each pair has `16d_ab` real transverse bosonic coordinates and `16d_ab` complex fermionic modes, with `8d_ab` occupied modes. The reverse block is the adjoint, not a second independent pair. The vacuum is invariant under the residual `S(product U(n_a))` group and is even in boson parity and fast fermion parity.

For any one normalized real supercharge let `q_0` be its centered fast part. Before imposing the block-center Gauss constraints, its square contains the center-weighted gauge term:

    q_0² = H_f + sum_i (Gamma_i)_(alpha alpha)
                         sum_a z_a^i G_(a,center,fast),

up to the common gauge-generator normalization. The background `z_a I_(n_a)` annihilates all traceless internal generators in this term. Consequently

    q_0² = H_f

on the residual block-center-neutral fast space. This includes fast states carrying nontrivial internal `SU(n_a)` representations. It does not assert the identity on arbitrary block-center-charged vectors. Physical total residual equivariance implies this center neutrality because traceless internal coordinates and internal adjoint fermions carry no block-center charge.

Every source below is center neutral: a pair contracts opposite root charges, while a triangle follows an oriented root cycle. On this space `P=U_0 U_0*` is the kernel of `H_f` and of `q_0`, and

    q_0^-1 = q_0 H_f^-1

is a genuine inverse on `1-P`. This is not the inverse of an interacting internal Hamiltonian.


## 2. The internal vacuum jet cannot be omitted

Let `U(z,A)` be the normalized adapted product vacuum from the gapped quadratic matrices in Appendix B. At one pair, rotate `n=b/r` to direction 9 and write

    T_i = A_i^(a) tensor I - I tensor (A_i^(b))^T,
    F = rI + T_9,
    D = Gamma_9 r + sum_i Gamma_i T_i.

At `A=0`, the bosonic kinetic correction `G-I` has no linear term and the bosonic frequency has first variation `delta Omega_ij=delta_ij delta T_9`. The fermionic negative projector has first variation

    delta P_- = -(1/(2r)) sum_(i perpendicular n) Gamma_i tensor delta T_i.

In a local unitary frame with zero scalar Berry connection at this point, the vacuum derivative is orthogonal to `U_0` and obeys the exact norm identity

    ||delta U_ab||² = (2/r_ab²) sum_i Tr_(d_ab)(delta Q_i²),       (2.1)

where `delta Q_i=delta b_i I+delta T_i`. The longitudinal contribution is the Gaussian variation; the transverse contributions are the occupied-determinant variation. Formula (2.1) is a norm in the fast fiber, leaving the entire slow Clifford module untouched.

For example, summing over all canonical center and endpoint-internal coordinate directions gives

    sum_mu ||partial_mu U_ab||²
       = 18 n_a n_b (n_a+n_b) / r_ab².                         (2.2)

Indeed the center contribution is `18(n_a+n_b)/r²`, while the internal contributions are `18[n_b(n_a²-1)+n_a(n_b²-1)]/r²`. Thus the adapted vacuum has nonzero internal derivatives even at `A=0`.

### 2.1 Zero first jet of the frozen-charge defect

Let `q_f(z,A)` be the frozen linear fast charge, with the exact frozen eliminated-Gauss kinetic coefficient. It need not annihilate the adapted vacuum at nonzero internal commutators. Nevertheless

    R(z,A)=q_f(z,A)U(z,A),
    R(z,0)=0,   partial_A R(z,0)=0.                            (2.3)

Here is the algebra behind the first derivative. In the frozen superalgebra the discrepancy between `q_f²` and the quadratic Hamiltonian consists of the residual internal gauge term and background-commutator terms. The latter are quadratic in `A`. The derivative of the former annihilates `U_0`, since `U_0` is internal-gauge invariant. Differentiating the adapted ground equation and using `E_0'(0)=0` therefore gives

    q_0 [q_f'(0)U_0 + q_0 U'(0)] = 0.

The vector in brackets is center neutral and odd in boson parity: a linear fast charge maps an even Gaussian to an odd Gaussian-polynomial vector. The kernel of `q_0` is the even vacuum line, so the bracket is zero. This parity step is required; the differentiated square alone does not rule out a vacuum component.

There is also a direct commuting-axis proof. Vary one canonical internal coordinate `A_i^(a)=t T`, with all other internal matrices zero. This whole one-parameter background is commuting. A unitary diagonalizing the single Hermitian `T` splits the adapted fast system into scalar color-pair oscillators at shifted relative vectors. The kinetic-aware Gaussian is the scalar transverse vacuum written in the chosen oblique slice, and the filled fermion vacuum is neutral for each color-pair phase. The frozen charge annihilates this product exactly. Thus every canonical internal partial derivative of `R` at zero vanishes, and linearity gives the full first jet. This argument is only along commuting coordinate axes; it does not incorrectly extend annihilation to noncommuting internal tuples.

Center derivatives of `R` vanish as well because `R(z,0)=0` identically in `z`. Equation (2.3), rather than a false assertion that the adapted fast charge has an exact kernel for all `A`, is what the centered homological calculation uses.


## 3. Exact centered coefficient identity, including internal derivatives

Under the simultaneous coefficient dilation

    z=L zeta,  A=L a,  Y=L^(-1/2) xi,

the exact reduced charge has the formal homogeneous inventory

    q(L) = L² Q_I^V(a) + L^(1/2) q_0(zeta,a)
           + L^-1 q_1 + L^(-5/2) q_2 + L^-4 q_3 + ... .      (3.1)

This is a coefficient expansion near the zero section, not a claim that the internal interacting charge is bounded or small. In an intrinsic multiblock chart the inverse Gauss matrix can create further terms; one must not copy the finite three-term axial expansion without checking this. All charge coefficients are first order in slow momenta. Since `Q_I^V(a)` and its first derivative vanish at `a=0`, its anticommutators with `q_2` and `q_3` vanish there. Thus the relevant centered Hamiltonian coefficients are exactly

    H_1 = {q_0,q_1},
    H_2 = q_1² + {q_0,q_2},                                  (3.2)

when evaluated at the centered internal jet. Terms from the quadratic density of the intrinsic Gauss determinant belong to this inventory. The fact that its linear-in-Y trace vanishes does not permit omitting its quadratic triangle terms.

Put

    D_s = U* q_1 U,
    B = (1-P) q_1 U.

The derivative of a coefficient section `f` in `q_1(Uf)` lies in the vacuum line. Therefore `B` is a multiplication map, but it includes the internal derivatives in (2.1):

    q_1(Uf) = U D_s f + Bf.

Equation (2.3) gives the centered off-diagonal source and diagonal compression

    (1-P) H_1 U = q_0 B,
    U* H_2 U = D_s² + B*B.                                  (3.3)

These are differential-operator/form identities on the common smooth coefficient core. There is no projection onto internal bound states or restriction of the spectator Clifford module.

The exact neutral fast inverse then gives

    B* q_0 H_f^-1 q_0 B = B*B.                               (3.4)

Consequently the centered effective coefficient is `D_s²`, and the entire additional multiplication coefficient cancels. It is important to identify `D_s` with its first jet before replacing `D_s²` by a free slow Laplacian.

### 3.1 Compression and its first jet

The following checks supply that last identification at `A=0`.

1. The scalar Berry curvature is zero at `A=0`, including pure internal and mixed center/internal components. A local gauge therefore has zero connection and zero first jet there.
2. The expectation of the quadratic-Y commutator charge is zero to first order in `A`. The centered covariance and its first variation are spatial-diagonal, so contraction with `Gamma_ij` vanishes.
3. The triangle orbital term and the fast-fast spin-Gauss term have an odd number of fast fermions and have zero vacuum compression. The same remains true after one internal derivative.
4. The delta part of the mixed slow-fast fermion covariance cancels the half-density derivative. The remaining sign-covariance term is, up to the fixed charge sign and factors of `i`, a linear combination of

       Gamma_n Im Tr_color[T_c F^-1 sign(D)],                 (3.5)

   where `T_c` is the Hermitian bifundamental action of a slow color generator. The trace leaves the spin matrix untraced. At the centered point it vanishes. Its first variation is a linear combination of

       r^-2 Im Tr(T_c delta T_n) Gamma_n,
       r^-2 Im Tr(T_c delta T_i) Gamma_i.

   Both are zero because the trace of a product of two Hermitian matrices is real. This is why the compression must be checked as a jet, not only by its value at `A=0`.

In a realification of the complex pair space, the covariance is `I/2` plus the complex structure times the realification of `sign(D)`, multiplied by `i/2`. The contracted mixed Gauss coefficient is the realification of `F^-1 T_c`. Its delta trace gives the density derivative, and its complex-structure trace is exactly the imaginary color trace in (3.5). This verifies the color mechanism without assuming that `F` commutes with the internal generators.

It follows that `D_s` has the centered free slow Dirac value and first jet, so the coefficient in (3.3)-(3.4) is the full free center-plus-internal kinetic operator. At nonzero internal coordinates, the complete internal potential charge must of course be retained; (3.1) never authorizes discarding it from an all-vector estimate.


## 4. Root graph grading and exact virtual denominators

Use a root edge `e={a,b}` and a triangle `t={a,b,c}`. For a root oscillator let `N_e` count bosonic excitations plus fermionic particles and holes relative to its vacuum. At the centered point

    H_f = 2 sum_e r_e N_e.

The leading complementary charge map has the decomposition

    B = sum_e B_e + sum_t B_t.                               (4.1)

Every `B_e` has `N_e=2` and every other `N_f=0`. Its terms are the Gaussian and determinant derivatives, the two-fast-variable commutator with slow fermion output, and the complementary mixed spin-Gauss contraction. Removing `P` removes their only possible zero-quantum part.

Every `B_t` has one excitation on each of its three edges. Its possible charge monomials are exactly of these types, with color contractions along an oriented cycle:

    Y_e Y_f theta_g,
    r_g^-1 Y_e p_f theta_g,
    r_h^-1 theta_e theta_f theta_g.                          (4.2)

Here `e,f,g` are the three distinct triangle edges, while `h` is one of them. A fast Majorana applied once to the filled vacuum creates one particle or hole. Different edges have independent Gaussian and Fock factors, so no within-edge vacuum contraction occurs in a triangle monomial.

Thus

    H_f B_e = 4r_e B_e,
    H_f B_t = 2s_t B_t,       s_t=sum_(e in t) r_e.           (4.3)

Distinct graph summands are orthogonal as fast-space maps. Pair sources are nonvacuum on only their own edge. Triangle sources are odd in combined excitation parity on exactly their three edges. The centered charge preserves each combined excitation parity and annihilates vacuum factors, so the orthogonality survives application of `q_0` and `H_f^-1`.

The finite dressing has the explicit graph resolution

    Z_e = -(4r_e)^-1 q_0 B_e,
    Z_t = -(2s_t)^-1 q_0 B_t.                               (4.4)

In particular, as positive operators on the full slow Clifford module,

    Z_e* Z_e = (4r_e)^-1 B_e*B_e,
    Z_t* Z_t = (2s_t)^-1 B_t*B_t.                           (4.5)

Replacing the second denominator by one arbitrarily selected root frequency is incorrect. Replacing every denominator by the unrelated global minimum throws away exactly the information needed for large far-away blocks.


## 5. Explicit coefficient seminorms and shape-independent graph estimates

All constants below are finite at fixed N. They can be calculated from the normalized Lie structure constants, gamma matrices, and the displayed source monomials; no compact global gap-ratio chart occurs in their definition.

One precise conservative convention is the following. Write each pair source as a sum of elementary maps after factoring `1/r_e`; evaluate the elementary Hermite/Fock monomials on unit-frequency normalized vacua and include their operator norms and absolute scalar coefficients in a sum `K_e`. Include the derivative contribution using (2.1). For a triangle, group the monomials (4.2) into the three types, factoring respectively

    (r_e r_f)^-1/2,
    r_g^-1 (r_f/r_e)^1/2,
    r_h^-1.

Let `K_t` be the sum of their unit-frequency Hermite/Fock norms times absolute coefficients. Gamma matrices have norm one, a real Majorana has norm `1/sqrt(2)`, and degree-two normalized Gaussian monomials have norms at most `sqrt(3)/2`. The remaining coefficients are normalized color brackets and unit spatial-direction contractions. This is a finite, explicit coefficient seminorm, not an unspecified supremum over gap ratios. For example (2.2) and Cauchy-Schwarz give a derivative-source contribution no larger than

    K_(e,derivative)² <= 162 N² n_a n_b(n_a+n_b).

Enlarge `K_t`, if necessary, by a factor two to account for the following weight reduction. Triangle geometry gives `r_f<=r_e+r_g`, and hence

    r_g^-1 sqrt(r_f/r_e)
       <= r_g^-1 + (r_e r_g)^-1/2
       <= (3/2)r_g^-1+(1/2)r_e^-1.

Also `(r_e r_f)^-1/2 <= (r_e^-1+r_f^-1)/2`. Therefore

    ||B_e|| <= K_e/r_e,
    ||B_t|| <= K_t sum_(e in t) r_e^-1.                     (5.1)

Set `w_t=sum_(e in t) r_e^-2`. Equations (4.5) and (5.1) imply

    ||Z_e||² <= K_e²/(4r_e³),
    ||Z_t||² <= 3 K_t² w_t/(2s_t).                          (5.2)

The centered map by itself has only center derivatives; an internal derivative requires an extension. For the following internal derivative bounds, choose smooth gapped pairwise Gaussian/Fock transport of the centered graph coefficient from `A=0`, for example transport along internal radial rays. This gives a concrete graph-factorized extension, but it is not asserted to equal the actual nonzero-internal homological source. The center derivative statement is unconditional. For these derivatives, the same graph coefficients and one differentiated vacuum factor give, with another computable coefficient seminorm `K'_g`,

    ||nabla Z_e||² <= K'_e² r_e^-5,
    ||nabla Z_t||² <= K'_t² (sum_(e in t) r_e^-1)² w_t/s_t. (5.3)

In (5.3), `nabla` differentiates the active graph coefficient and its active oscillator factors. The full map also contains a vacuum factor on every spectator edge. Its full derivative has the corrected bound

    ||nabla Z_g||² <= C_N[d_(g,active)+m_g W_2],
    W_p=sum_e r_e^-p,                                       (5.4)

where `m_g` is the right side of (5.2). The extra term is necessary when a spectator edge is much shorter. For adapted vacua it includes internal derivatives of spectator factors as well as center derivatives. The active triangle right side in (5.3) is at most a fixed numerical multiple of `K'_t² sum_(e in t) r_e^-5`, by Holder and `s_t>=max r_e`. Moreover

    W_3 W_2 <= (#edges) W_5.

Thus the full derivatives still have a summed `C_N W_5` majorant. Graph-resolved weights must nevertheless be kept when an internal Yukawa multiplier is to be paid.

### 5.1 Perturbed finite source spaces

The Gaussian/Fock statement also has a useful conditional continuation. On the adapted pairwise-relative tube, unitary/symplectic transport identifies the finite degree-at-most-three source spaces with their centered spaces. Frequencies have fixed positive bounds `c r_e <= omega_(e,j) <= C r_e`. A source odd in each triangle edge therefore has complementary excitation energy at least `c s_t`, even when modes within one pair split or coincide.

If the exact leading Hamiltonian graph source `S_g(A)` has the coefficient bounds

    ||S_e(A)||² <= C_N/r_e,
    ||S_t(A)||² <= C_N s_t w_t,

then the inverse of the shifted excitation operator

    H_exc = H_fast - E_(0,total)

on the relevant excited sector satisfies precisely the graph dressing bounds (5.2), with enlarged constants. The vacuum-energy defect is handled separately by the general frozen-energy lemma. An unshifted inverse of the full fast Hamiltonian need not have these denominators, because unrelated pair vacuum-energy defects would enter it. This is solely the finite-source fast excitation inverse. No internal momentum appears in its denominator.

To deduce a small adapted inverse-square remainder from the centered identity, one additionally needs the exact diagonal `H_2` inventory, including its density, ordering, and internal-potential cross terms. Under coefficientwise perturbation bounds of order `kappa`, the finite resolvent identity gives a defect at most `C_N kappa W_2`. Establishing all those hypotheses from the full reduced Hamiltonian is separate from the graph calculation.


## 6. A graph-local complete slow form lemma

This is an all-vector statement, not a finite-Gaussian approximation to an internal wavefunction.

Let

    H_s = T_cent + sum_a H_a,
    H_a = T_a + V_a + Y_a,
    V_a >= 0,     ||Y_a(A)|| <= c_(n_a) alpha_a.

The averaged sixteen-charge identity makes `H_a` nonnegative also on colored internal vectors. The ordinary physical lower-rank Hardy estimate is not being invoked. For a graph-local multiplication map `Z_g`, suppose

* it is an active-graph coefficient, depending on internal coordinates at graph vertices only, tensored with the vacua on spectator edges;
* it acts on internal Clifford factors only at these vertices;
* it is even in total fermion parity, as is `q_0^-1 B_g`;
* `||Z_g||² <= m_g(z)` and the full derivative obeys the center-only majorant `d_g` in (5.4).

For a block `a` outside `g`, its internal potential charge commutes exactly with the map. The complete internal charge satisfies

    Q_(a,alpha) Z_g = Z_g Q_(a,alpha)+C_(a,alpha,g),

where `C_(a,alpha,g)` is bounded multiplication coming only from derivatives of spectator vacua. Its squared norm is bounded by the corresponding derivative majorant, with the finite Clifford contraction factor. Averaging the exact charge squares and applying Young gives

    H_a[Z_g f] <= 2 integral m_g(z) [H_a-density of f]
                  + C_N integral d_(a,g)(z)|f|².            (6.1)

In particular no unrelated `alpha_a m_g` loss appears. It would be incorrect to assert exact commutation while differentiating a moving spectator vacuum. For a graph vertex use the elementary uncompressed estimate, with no internal spectral assumptions,

    H_a[Z_g f]
      <= 2 integral m_g(z) [H_a-density of f]
         + 3c_(n_a) integral alpha_a m_g(z)|f|²
         + 2 integral |partial_Aa Z_g|² |f|².               (6.2)

The notation for a weighted internal density is harmless here because its weight depends only on centers; it is the nonnegative internal form on every fixed-center fiber. The center kinetic estimate has the same derivative-product bound with no Yukawa term.

For pair and triangle dressings from (5.2),

    sup m_g <= C_N r_*^-3.

At a pair endpoint, `alpha_a<=kappa r_e` gives

    alpha_a m_e <= C_N kappa r_e^-2.

At any triangle vertex, `alpha_a<=kappa min(incident r_e)<=kappa s_t`, and hence

    alpha_a m_t <= C_N kappa w_t.                           (6.3)

This remains true when the opposite edge is arbitrarily shorter than the two incident edges. The factor `s_t` from the virtual denominator is doing essential work.

Combining (6.1)-(6.3), then using positivity of `H_s` to sum the finitely many graph maps, proves

    H_s[sum_g Z_g f]
      <= C_N r_*^-3 H_s[f]
         + C_N kappa integral W_2 |f|²
         + C_N integral W_5 |f|².                           (6.4)

The constants can be chosen from the finite sums of `K_g²`, `K'_g²`, vertex counts, and `c_(n_a)`. For instance a direct Cauchy-Schwarz sum multiplies their sum by the number of graphs `binom(k,2)+binom(k,3)`. This gives an explicit finite-N recipe, without a global ratio parameter.

The full derivative terms in this argument include spectator factors; their product weight is controlled by `W_3 W_2 <= (#edges) W_5`. The same argument applies to a genuinely adapted dressing if its active-graph coefficients and spectator factors satisfy the hypotheses. In particular, (6.4) retains arbitrary internal momenta. No absolute-value inverse expansion of `H_f+H_I` has been used. It also explains why the coarse estimate `||Z||²<=C W_3` should not first be multiplied by `sum alpha_a`: that would incorrectly charge a distant large block against an unrelated short root.

### 6.1 Direct center-Hardy payment

For each pair, in the mass center metric,

    integral r_ab^-2 |f|²
       <= (4/49)(1/n_a+1/n_b)^-1 T_cent[f].                 (6.5)

The inequality holds for Hilbert-valued coefficients and unitary connections. Also `W_5 <= r_*^-3 W_2`. Hence the last two terms in (6.4) are bounded by an arbitrarily small center kinetic fraction by first choosing `kappa` small at fixed N and then `r_*` large. The first term is a small fraction of the entire interacting slow form, not a fixed internal kinetic loss.
