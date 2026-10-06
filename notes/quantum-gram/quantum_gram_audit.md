# BFSS quantum-Gram audit: two finite-family obstructions

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


6 October 2026. Target: M_N = <rho^2 q_h^2> = O(N^(-4/3)). No upper bound for the actual fixed-coupling BFSS zero mode was obtained. This note gives two precisely scoped quantum obstructions and identifies the first omitted terms. It does not prove an impossibility theorem for higher-degree BFSS bootstrap certificates.

## 1. Setup and assumptions

Use the conventions of the preceding mixed-moment and rank-certificate audits:

- tr = Tr/N; [Z_i^A,P_j^B] = i delta_ij delta_AB; {psi_alpha^A,psi_beta^B} = delta_alpha_beta delta_AB
- R = rho^2 = tr(sum_i Z_i^2), q = tr(h_ij Z_i Z_j), a = tr(Z_i (h^2)_ij Z_j)
- h is real symmetric, Tr_9 h = 0, Tr_9 h^2 = 1
- D = sum_Aij h_ij Z_i^A P_j^A
- Q_alpha = K_alpha + V_alpha, where K is linear in P and psi and V is quadratic in Z and linear in psi
- H = P^2/(2N) - (N/4) sum_ij Tr[Z_i,Z_j]^2 - (1/2)Tr psi Gamma^i[Z_i,psi]

A use of zero-mode expectations assumes a normalized physical gauge- and Spin(9)-singlet Omega, Q_alpha Omega = 0, in a compatible self-adjoint realization. Existence, uniqueness, uniform rank control, and unbounded-multiplier domain limits are not supplied here. Every displayed polynomial identity is first an identity on the smooth core. An expectation additionally requires the indicated forms and moments to exist, or a justified cutoff limit. In particular, M finite alone does not license every high-degree polynomial Gram entry.

The earlier result gives, under its explicit second-moment and domain hypotheses,

    K_N(s) <= s N^2 M_N + (b/64) s N^2 2^(-2N^2),   b = 8/9.

Thus M_N = O(N^(-4/3)) already suffices for K_N(s) = O(N^(-2/3)) when s is proportional to N^(-4/3). The stronger planar O(N^(-2)) moment is not the target of this pass.

## 2. A concrete small quantum Gram

For a fixed alpha define b_h = (iN/2)[Q_alpha,q], and define b_0 by replacing h with I_9. Then

    [Q_alpha,q] = -2i b_h/N,
    b_h^2 = a/2,   b_0^2 = R/2,   {b_0,b_h} = q,
    {Q_alpha,b_h} = D/N,
    [D,q] = -2i a.

The individual, rather than merely spinor-summed, anticommutator follows without an interaction calculation:

    {Q,[Q,q]} = [Q^2,q] = [H,q] = -2i D/N^2.

A concrete seed is the even-word list (1,q,D,q^2) and odd-word list

    (b_0, b_h, q b_0, q b_h, Q_alpha).

Use their full Hermitian Gram matrices and the exact null vector Q_alpha Omega = 0. The objective appears directly as

    ||q b_0 Omega||^2 = M_N/2,
    ||q b_h Omega||^2 = <a q^2>/2.

The latter mixed moment is comparable to M_N by the previous exact rotational identity: M_N/13 <= <a q^2> <= 5M_N/13. This comparison does not provide an upper estimate.

The 2-by-2 odd principal block for (b_h,q b_h) is

    (1/2) [[<a>, <a q>], [<a q>, <a q^2>]].

Its determinant yields only <a q^2> >= <a q>^2/<a>. The even block (q,D), using the current Ward identity, similarly yields

    <q^2><D^2> >= <a>^2.

Adding the first apparently dynamical descendant does not insert a restoring term:

    Q_alpha(q b_h) Omega = (qD - i a)Omega/N
                           = {q,D}Omega/(2N).

Consequently its squared norm is a higher shear-current moment. Also

    ||Q_alpha(q^2 Omega)||^2 = 8<a q^2>/N^2.

This is an energy identity, not an upper bound on that energy.

## 3. Fixed-coupling obstruction for a specified weighted polynomial dual

This is an operator-level BFSS statement, not a substitute classical probability law.

Assign the BFSS weights

    weight(Z)=1,   weight(P)=2,   weight(psi)=0.

All Clifford words are allowed, so fermion degree is not artificially truncated. At each finite N the Clifford algebra is finite-dimensional. Q is homogeneous of weight 2. H has its bosonic principal part of weight 4 and its fermionic part of weight 1. A canonical reordering [P,Z]=-i lowers weight by 3.

Consider any polynomial dual identity of the following precise form:

    C_N I - Rq^2
      = sum_j S_j^* S_j
        + sum_alpha (Q_alpha O_alpha + O_alpha^* Q_alpha)
        + H B + B^* H
        + sum_A (G_A C_A + C_A^* G_A)
        + sum_ij (L_ij E_ij + E_ij^* L_ij).

Here G_A and L_ij are the usual gauge and full spatial-rotation generators. Their orbital parts have weight 3 and their fermionic parts weight 0. The allowed coefficient bounds are

    weight(S_j) <= 4,
    weight(O_alpha) <= 6,
    weight(B) <= 4,
    weight(C_A), weight(E_ij) <= 5.

Coefficients may depend arbitrarily on N. The sum of squares may equivalently be any positive semidefinite Gram form in all words of weight at most 4. Exact finite-N matrix trace and Clifford identities are retained. The ordering of the null terms makes their expectation zero in a legitimate singlet zero mode. The bounds are on the raw factors before cancellations, not merely on the reduced degree of a nested commutator.

### Theorem

No such identity exists for any N >= 2 and any finite scalar C_N.

### Proof

Normal-order every differential operator with all canonical momenta to the right. Pick a real unit n in R^9 and a traceless diagonal Hermitian D_N with tr D_N^2=1. Evaluate its polynomial coefficient symbol at

    Z_i = t n_i D_N,   P_i^A = 0.

Keep the fermions as matrices in their exact Clifford representation. This is an algebraic symbol test of a proposed operator identity; it is not asserted to be a quantum state.

At this commuting phase-space point the principal Q symbol, the bosonic H symbol, and the orbital G and L symbols all vanish. Reordering corrections in each displayed null term have weight at most 8-3=5. The lower fermionic H term has weight at most 1+4=5; the lower fermionic G,L terms have weight at most 0+5=5. Therefore none of the null terms contributes a power t^6,t^7, or t^8 at this point.

Write the evaluated symbol of S_j as sum_(k=0)^4 t^k s_(j,k). Reordering corrections to S_j^*S_j also have weight at most 5. The t^8 coefficient of the identity is therefore

    0 = sum_j s_(j,4)^* s_(j,4).

Positivity in the finite Clifford representation forces every s_(j,4)=0. The t^6 coefficient then reads

    -(n^T h n)^2 I = sum_j s_(j,3)^* s_(j,3),

because R=t^2 and q=t^2 n^T h n, and the possible s_4^*s_2 terms vanish. Since nonzero h admits n with n^T h n != 0, the left side is strictly negative and the right side nonnegative. Contradiction.

A gauge/spatial orbit average gives the same contradiction with the explicit coefficient -2/99, since the spherical average of (n^T h n)^2 is 2/99. Thus imposing those singlet symmetries does not remove the test.

### What the theorem does and does not say

It rules out this entire finite polynomial family, including momentum words, arbitrary Clifford words, fixed BFSS coefficients, and the displayed zero-mode/singlet null relations. It rules out even a fixed-N constant upper certificate in this family, so optimizing its coefficients cannot generate the desired rank power.

It does not exclude higher raw-degree multipliers whose leading terms cancel, localizing/rational weights, a larger moment hierarchy, or analytic zero-mode estimates. It does not prove an unbounded primal optimum for every possible truncated SDP representation; the explicit conclusion is nonexistence of the displayed exact dual identity.

## 4. The first omitted quantum order, and its actual content

The first raw product order capable of contributing a degree-six canonical correction is 9, since canonical reordering lowers weight by 3. For example q^3 b_h has weight 7, so Q(q^3 b_h) has raw weight 9. Its exact anticommutator is

    {Q_alpha,q^3 b_h} = (q^3 D - 3i a q^2)/N
                       = {q^3,D}/(2N).

The apparent sixth-moment term is exactly the commutator correction needed to make the shear current symmetric. Its vanishing expectation supplies no upper sign on <a q^2>. Thus the first natural escape from the theorem is the current identity already audited, rather than a successful certificate.

More generally, a Hermitian stationary multiplier A={f(q),D}/2 produces

    (1/2)<{f(q),W}> = (2/N^2)<D f'(q)D - c f''(q) - a^2 f'''(q)>,

where W=i[D,H]=-2T_h+delta_h(V_bos+F), and c=tr(Z h^3 Z). The weighted stress on the left has no established upper sign or bound: T_h is traceless and indefinite, the commutator potential is sheared with coefficients of both signs, and the fermionic stress is indefinite. Positivity of D f'D for f'>=0 does not reverse this into concentration.

## 5. A separate dilation obstruction for the diagonal-supercharge family

If one keeps the q,a,R,D,b_alpha,Q_alpha relations of Section 2 and their polynomial consequences, but does not separately retain the fixed coefficient of the interaction in Q, those relations have the exact dilation

    q,a,R -> lambda^2(q,a,R),
    b_alpha -> lambda b_alpha,
    D -> D,
    Q_alpha -> lambda^(-1) Q_alpha.

After expanding polynomial vectors into homogeneous words, every finite Gram matrix transforms by diagonal congruence; positivity, the zero-mode null vectors and these relations survive, while M transforms to lambda^6 M. This is a quantum obstruction to that restricted algebra, not just coordinate positivity.

It can be realized explicitly conditional on a zero mode. Let

    (U_lambda psi)(Z) = lambda^(-d/2) psi(Z/lambda),
    d = 9(N^2-1).

Put Omega_lambda=U_lambda Omega and

    Q_(alpha,lambda) = lambda^(-1) U_lambda Q_alpha U_lambda^*
                    = K_alpha + lambda^(-3) V_alpha.

These are self-adjoint supersymmetric charges on the transported domains and kill Omega_lambda. The same canonical commutation relations, Clifford relations, and singlet symmetries hold. Their diagonal descendant/shear identities have exactly the same constants. The interaction coefficient, however, is changed. Therefore this family is expressly not a counterexample to fixed-coupling BFSS. It identifies precisely the fixed-coupling information that this restricted Gram fails to retain.

## 6. Cubic fermions and finite-N trace corrections

The same-source Clifford algebra obeys {b_alpha,b_beta}=a delta_alpha_beta, for 16 components. Therefore

    sum_beta b_beta b_alpha b_beta = -7 a b_alpha.

Delta-contracted cubic words reduce to scalar-dressed linear fermions. Genuinely antisymmetric cubic words survive, but their Ward identity is

    {Q_alpha,b_beta b_gamma b_delta}
      = R_(alpha,beta) b_gamma b_delta
        - b_beta R_(alpha,gamma) b_delta
        + b_beta b_gamma R_(alpha,delta),

where R_(alpha,beta)={Q_alpha,b_beta}. The supersymmetry algebra fixes only

    R_(alpha,beta)+R_(beta,alpha) = 2 delta_alpha_beta D/N

on the physical sector. There is a more explicit finite identity that exposes the missing term. Put A={q,D}/2 and, for alpha != beta, define

    S_(alpha,beta) = q R_(alpha,beta) - 2i b_alpha b_beta/N.

Here [R_(alpha,beta),q]=0, S is Hermitian, and

    Q_alpha(q b_beta)Omega = S_(alpha,beta)Omega,
    ||S_(alpha,beta)Omega||^2 = <A^2>/N^2.

The second equality uses Q_alpha^2=Q_beta^2=H. Expanding the square gives

    <q^2 R_(alpha,beta)^2> + <a^2>/N^2
      - (2i/N)<q {R_(alpha,beta),b_alpha b_beta}>
      = <A^2>/N^2.

The displayed interference term is real but unsigned. Dropping it is not a positive estimate. This is the exact additional term encountered by the first off-diagonal extension.

Delta-contracted cubic words also expose a definite missing operator. Define c_alpha=b_(alpha,h^2) and t=tr(h^3 G), so {c_alpha,b_alpha}=t. For a real scalar f(q),

    {Q_alpha,a f(q)b_alpha}
      = [{a f(q),D}/2 - i f(q)[c_alpha,b_alpha]]/N.

The new term is a Hermitian fermion bivector with no established sign. Thus reducing a cubic word to a b_alpha does not reduce it to the old f(q)b_alpha family unless the remaining a-dependence is also treated. All these identities require their graph domains or justified cutoff limits. No rank-uniform upper estimate for the interference or bivector term was obtained.

For normalized momentum Pi=P/N, exact SU(N) cyclicity for coordinate words U,V is

    <tr(Z^I U Pi^J V) - tr(U Pi^J V Z^I)>
      = i delta_IJ [<tr U tr V> - N^(-2)<tr(UV)>].

The double trace on the right must remain a joint expectation. Its explicit subtraction of N^(-2) times a single trace does not imply that the connected double trace is O(N^(-2)). Treating it as such would reinstall the factorization assumption under another name.

## 7. Primary-source check and status

- Lin and Zheng, *Bootstrapping BFSS Matrix Theory*, https://arxiv.org/html/2410.14647v3: the planar cyclicity constraint displayed around Eq. (12) factorizes; finite-N connected terms must instead be retained. The published calculation does not supply the present upper bound.
- Lin, *Bootstrap bounds on D0-brane quantum mechanics*, https://arxiv.org/html/2302.04416: Appendix C gives exact finite-N Clifford trace corrections, including Tr psi_alpha^2=(N^2-1)/2 and Tr psi_alpha^4=(2N^4-3N^2+1)/(4N). These sharpen fermionic caps but their established radius implication is a lower bound.
- Cho, Gabai, Lin, Yeh and Zheng, https://arxiv.org/html/2511.08560v3: continuous-time two-point positivity, revised June 2026, with examples in ungauged one-matrix quantum mechanics. Reference [6] still lists BFSS Part II as in preparation. No rank-uniform BFSS mixed-moment certificate is supplied.
- The June 2026 version https://arxiv.org/html/2507.21007v3 remains a bosonic large-N calculation and also lists BFSS Part II in preparation.

This was a targeted primary-source check, not an exhaustive priority search. The desired upper bound remains missing. A viable next calculation must retain fixed-coupling information and escape the bounded class proved here. Cross-supercharge tensors are one possible extension; higher-weight single-charge identities are not excluded. Any such attempt must actually control the unsigned terms it introduces. The note does not propose an unlimited formal hierarchy as a result.
