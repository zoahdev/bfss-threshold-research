# Off cone incidence localization

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 1. A slightly regularized commuting tree

Write a traceless ordered commuting configuration as lambda=(lambda_1,...,lambda_N), with rho^2=sum |lambda_i|^2. For a proper subset B with at least two members put

    c_B=|B|^(-1) sum_(i in B) lambda_i,
    a_B^2=sum_(i in B)|lambda_i-c_B|^2,
    d_B^(-2)=sum_(j outside B) (|lambda_j-c_B|^2+a_B^2)^(-1).

The extra a_B^2 in the denominator is deliberate. It removes inverse-matrix singularities from the off-cone extension whenever a_B>0, without changing the clustering mechanism. For 0<kappa<1/20, L>1 and delta=kappa exp(-L), use

    theta_B=Theta(log(a_B/(delta d_B))/L),
    C_B=cos(theta_B), S_B=sin(theta_B),

where Theta is a fixed smooth nondecreasing function, 0 on (-infinity,0] and pi/2 on [1,infinity). Every derivative of the trigonometric factors is flat at the constant-tail boundaries. If a_B=0 and all exterior points are separated, C_B=1 locally. Coincident unused nodes are handled by the same identically zero-prefix mechanism as in the decision tree.

The regularization retains a uniform derivative bound

    |d a_B|<=1, |d d_B|<=C_N,
    |d theta_B|^2 <= C_N ||Theta'||_infinity^2 L^(-2) a_B^(-2)

on delta d_B<a_B<kappa d_B. The constant is independent of delta and L. For example a conservative C_N can be obtained by taking |d d_B|<=4N and then squaring 1+4N kappa.

For crossing subsets B,C, the same three-point argument gives

    d_B <= 2a_B+2a_C, d_C <= 2a_B+2a_C.

Thus C_B C_C=0 if kappa<1/4. All simultaneously selected clusters are laminar. The decreasing-cardinality decision tree and its exact pathwise IMS identity therefore still apply.

### Symmetric raw leaf formula

For an unordered partition pi into at least two final blocks, its tree leaf multiplier is exactly

    q_pi = product_(B in pi, |B|>=2) C_B
           product_(B proper union of >=2 pi-blocks) S_B.       (1)

This is not a claim that all visited nodes are unions on their entire domain. Rather, any omitted rejected crossing node has S_B=1 on a neighborhood of the nonzero final-block selection support, by laminarity. Nodes strictly inside a selected final block are skipped. Thus (1) equals the original leaf product as a smooth function, including its derivatives. In particular

    sum_pi q_pi^2=1,
    sum_pi |d q_pi|^2 = sum_pi q_pi^2 E_pi,                  (2)

where E_pi sums |d theta_B|^2 for the final nontrivial blocks and the proper unions in (1). Terms that were skipped or crossing contribute zero on that leaf. No arbitrary ordering of equal-cardinality clusters remains in (1).


## 2. Intrinsic matrix extension on one stationary flag

Use the notation and associated-bundle coordinates of the intrinsic multiblock geometry note. On an ordered flag of ranks n_1,...,n_k, write

    X=Z+A+Y, B_Z^*Y=0, alpha_a^2=sum_i ||A_i^(a)||_F^2,
    r_ab=|z_a-z_b|, r_*=min r_ab.

For a union I of flag blocks define

    n_I=sum_(a in I)n_a,
    c_I=n_I^(-1)sum_(a in I)n_a z_a,
    a_I^2=sum_(a in I)alpha_a^2 + sum_(a in I)n_a|z_a-c_I|^2,
    H_(b,I)=sum_i(A_i^(b)+(z_b-c_I)_i I)^2+a_I^2 I,
    d_I^(-2)=sum_(b outside I)Tr H_(b,I)^(-1).                (3)

For a single nontrivial final block, a_I=alpha_a. Formula (3) ignores Y, as it must for the desired leading slow localization. It uses traces, positive matrix inverses, and projector compressions; it chooses no internal eigenbasis. If a_I>0 every H is positive. If a_I=0 for a selected final block, exterior separation keeps every H positive and its angle has a constant select tail. A union of at least two blocks has a_I>0 when r_\*>0.

The inverse-trace differentiation estimate remains uniform. If H=sum_i T_i^2+a^2 I, then Cauchy-Schwarz and sum_i||T_i H^(-2)||_F^2<=Tr H^(-3) bound the derivative of Tr H^(-1). The inequality sum eigenvalues(H)^(-3)<=(sum eigenvalues(H)^(-1))^3 gives a dimension-controlled Lipschitz bound for d. Center subtraction only introduces the fixed factors from n_I and N. Hence the theta derivative estimate of Section 1 holds for the canonical (Z,A) metric.

For any gauge-invariant scalar f(Z,A), the exact co-metric identity gives

    |grad_X f|^2 <= (1+C_N sigma^2)|d_(Z,A)f|^2              (4)

on a thin fast tube. Indeed put p=(d_Z f,d_A f,0). Solving the full coordinate differential and scalar gauge constraint gives the ambient covector (p-K^\* beta,beta), where beta=-M^(-\*)O_H^\*p and O_H^\*p=O_C^\*d_Z f+O_A^\*d_A f. Both O_C and O_A are projections of B_Y. Factoring M^(-\*) with F^(-\*) on the right gives |beta|<=C|Y| |p|/r_\*. Since ||K||<=2|Y|/r_\*, the full squared covector norm is at most (1+C_N sigma^2)|p|^2. This argument includes the full orbital contribution and has no unrelated internal-radius loss.


## 3. Support margins and an explicit center-gap bound

If q_pi is nonzero, all nontrivial final blocks satisfy alpha_a<kappa d_a. From

    d_a^2 <= r_ab^2+alpha_b^2+alpha_a^2

and the analogous inequality with a,b interchanged, obtain

    alpha_a+alpha_b <= beta r_ab,
    beta=2 kappa/sqrt(1-2 kappa^2).                          (5)

Singleton radii are zero. Choose the tree kappa so beta is strictly smaller, for example by a factor four, than the endpoint constant allowed by the geometric lemma.

Every proper union I of at least two final blocks has been rejected, so a_I>=delta d_I on q_pi's support. Suppose the currently included centers have diameter D. Equation (5) implies

    a_I <= sqrt(N(1+beta^2)) D.

From d_I<=a_I/delta, at least one eigenvalue of some exterior H_(b,I) is <=N a_I^2/delta^2. Evaluating its unit eigenvector and using the triangle inequality yields

    |z_b-c_I| <= sqrt(N) a_I/delta + alpha_b.

Using alpha_b<=beta|z_b-z_a| for an included a and adjoining this center grows D by at most M_N/delta, where

    M_N=[N sqrt(1+beta^2)+1]/(1-beta).

Starting from a closest pair and making at most k-2 additions proves

    r_* >= Delta_N R,
    R^2=r_pi^2+sum_a alpha_a^2,
    Delta_N=[N(1+beta^2)]^(-1/2)(delta/M_N)^(N-2).            (6)

Since rho_X^2=R^2+|Y|^2 and |Y|<=sigma r_\*, this also gives

    r_* >= Delta_N rho_X/sqrt(1+2sigma^2).                  (7)

All nonzero raw weights, and the closures of their derivative supports, have this margin. This is the key quantitative substitute for an unspecified finite cover.

For a selected-block angle transition,

    d_a >= (1-beta) r_*/sqrt(N),
    alpha_a >= delta(1-beta)r_*/sqrt(N).                    (8)

For a proper-union angle, a_I dominates its center-relative radius. Thus all nonconstant cutoff factors live at a fixed positive multiple of rho, once N,kappa,L have been fixed. Internal coincidences never cause an unbounded derivative of a surviving multiplier.


## 4. All branches, finite count, and smooth zero extension

For every ordered composition N=n_1+...+n_k, k>=2, take the incidence set of stationary ordered orthogonal projector flags for Phi_X. Admit branches inside a padded domain with:

- endpoint bound strictly larger than beta, but still inside the stated geometric regime
- center gap strictly smaller than the lower bound (7), for example one fourth of that bound
- fast width strictly larger than the support of an invariant smooth fast cutoff

Use a smooth cutoff chi_Y=1 for |Y|<=sigma h/4 and chi_Y=0 for |Y|>=sigma h/2, with h=(sum_(a<b)r_ab^(-2))^(-1/2). The geometric domain can allow |Y|<sigma r_\*. Put

    b_j=(k!)^(-1/2) chi_Y q_pi                             (9)

on each stationary flag sheet j. Extend it by zero outside the padded support. Equations (5)-(7), the flat cutoff tails, and the strict fast margin make this a smooth finite-cover section. There is no cutoff associated with a choice of coordinate chart or block frame.

The Hessian estimate from the geometry note makes each admitted stationary flag a nondegenerate critical point. In particular it is locally a smooth branch, and no branch can be born or disappear inside the nonzero support. Branches can have monodromy; chart transitions merely permute direct-sum components.

### Explicit N-only multiplicity bound

A crude bound is sufficient. A flag of type (n_a) has real dimension m=N^2-sum n_a^2<=N^2. It is covered by at most N! pivot charts. In a complex block-lower-unipotent chart, every cumulative orthogonal projector is

    V(V^*V)^(-1)V^*.

A common denominator for all projectors has degree at most 2N^2 in real chart coordinates. Phi has numerator and denominator degree at most 4N^2; clearing denominators from each first derivative gives polynomial equations of degree at most 8N^2. Nondegenerate real critical points are isolated complex zeros as well. The elementary Bezout isolated-zero bound therefore gives at most (8N^2)^m per chart. Summing the at most 2^(N-1) ordered compositions gives the conservative bound

    D_N=2^(N-1) N! (8N^2)^(N^2).                           (10)

The bound is deliberately huge and only used to ensure constants do not secretly depend on the logarithmic inner scale. It counts ordered sheets; (9) corrects their actual multiplicity.

### Why commuting admitted sheets are exactly cluster partitions

Let B(X)=sum_(i<j)||[X_i,X_j]||_F^2. On a stationary thin flag, the transverse linear commutator has norm

    ||L_Z Y||^2=sum_(a<b) r_ab^2 |Y_ab|^2

with the corresponding fixed real-block normalization. Endpoint perturbations are bounded by C times the padded geometric endpoint constant times this norm (and by C beta on the raw-weight support), and the quadratic Y term by C sigma times it. With the fixed small geometric constants,

    B(X)^(1/2) >= c_N (sum r_ab^2|Y_ab|^2)^(1/2).          (11)

Consequently a commuting admitted sheet has Y=0. Its projectors group common eigenspaces; a repeated joint eigenvalue cannot be split between two selected thin blocks, by (5). Each unordered particle partition appears exactly k! times among all ordered compositions and flags. Thus on the commuting cone

    Q=sum_j b_j^2=1.                                      (12)

No extra N! multiplier belongs in (9).

Equation (11) also ensures that on a sufficiently small near-commuting region the fast cutoff is identically one on every contributing sheet. Using (7) and h>=r_\*/sqrt(k(k-1)/2), it suffices to take

    t=B(X)/rho_X^4 <= c_N sigma^2 Delta_N^4.                (13)

The constant in (13) can be reduced to include every fixed geometric margin. There is then no fast-cutoff derivative in the near-cone localization; outside it, its usual cost could instead be paid by a retained fast reserve.


## 5. The exact cone identity and the small off-cone defect

Where Q>0 define w_j=b_j/sqrt(Q). Then sum_j w_j^2=1. Let

    E(X)=sum_j |grad_X w_j|^2,
    R(X)=sum_j w_j^2 E_j(X),                               (14)

where E_j is the sum of the ambient |grad theta_I|^2 for the single-block select factors and proper-union reject factors of that sheet. All expressions are taken before any slow/fast projection.

At a commuting X on an admitted sheet, Y=0. A pointwise common diagonalization verifies that the first derivative of every scalar in (3) in an off-diagonal internal direction is zero. This is a calculation of an invariant Frechet derivative, not a choice of smoothly varying eigenvectors. It remains true at repeated joint eigenvalues: trace derivatives of inverse matrices against off-diagonal perturbations vanish, and the radius-zero select factor is constant on a neighborhood. Further, K=O_C=O_A=0 at Y=0 in the exact kinetic identity. Therefore the ambient gradients of all raw weights equal their commuting-base gradients, including at singular strata. The same statement holds for the angles wherever their derivatives matter.

The whole symmetric commuting identity (2) therefore implies

    Q=1, dQ=0, E=R                                      (15)

at every nonzero commuting tuple. This is stronger than just equality of the weight values.

On the unit sphere, all supported branch sums and their first two derivatives are bounded: the incidence Hessian is uniformly invertible after (7), the flag multiplicity is bounded by (10), all nonconstant cutoff transition scales a_I obey fixed positive lower bounds, and the support stays strictly inside the padded branch domain. Accordingly Q and E-R are smooth scalar functions in a neighborhood of the compact commuting unit locus. There is a finite explicitly defined derivative bound K_(N,kappa,L,sigma,Theta), obtained as the supremum of their first derivatives on a closed smaller padded neighborhood, such that

    |Q(X)-1|+|E(X)-R(X)| <= K dist(X,K_comm)                (16)

for unit X close enough to that locus. This constant can grow with Delta_N^(-1); it is not asserted uniform in the shape gap. Its role is to determine a later near-cone thickness, never to appear as an unpaid inverse-square coefficient.

For every epsilon>0 choose a neighborhood thickness eta>0 small enough that Q>=1/2 and K eta<=epsilon. Homogeneity then proves

    E(X) <= R(X)+epsilon rho_X^(-2)                        (17)

on that conical neighborhood. If desired, the elementary estimate of Section 6 makes the choice in terms of t: take t_1<=(eta/(2 C_N))^4, together with (13) and the branch-continuation radius. This is a concrete order of choices, not a simultaneous assumption kappa=kappa(Delta_N).

### Why direct leafwise normalization was insufficient

For a single select factor, |d cos theta|^2=sin^2 theta |d theta|^2 cannot be bounded by cos^2 theta times the same cost near its zero. Hence one cannot bound |dw_j|^2 by w_j^2 E_j separately. Nor may one charge every nested transition to every final leaf: a tiny subcluster transition inside a larger selected block is not controlled with a shape-independent coefficient by the latter's total-radius Hardy estimate. Only the summed defect argument (15)-(17) repairs this issue.


## 6. An elementary almost-commuting distance certificate

There is no need to assume a smooth retraction onto the singular commuting cone. For a traceless Hermitian nine-tuple X of norm one, put epsilon_0=max_(i<j)||[X_i,X_j]||_F<=sqrt(t). An elementary spectral-block construction produces a commuting traceless tuple Z with

    ||X-Z|| <= C_N sqrt(epsilon_0) <= C_N t^(1/4),
    C_N=729 sqrt(N^3+9)                                   (18)

as a conservative choice.

To see this, process one component at a time inside the already constructed invariant blocks. In each current block, group consecutive eigenvalues across gaps at most eta=sqrt(epsilon_j). Distinct groups have spectral distance greater than eta. Replace the processed component on each new spectral block by its trace-average; its tuple error is at most N^(3/2) eta. Delete interblock entries of all remaining components. The Frobenius norm of each deleted part is at most epsilon_j/eta, by its commutator with the processed component. The new block-diagonal commutator differs from the compressed old commutator only by two products of deleted off-block parts. Hence epsilon_(j+1)<=epsilon_j+2(epsilon_j/eta)^2<=3epsilon_j. At most nine steps give (18); all changes preserve traces. Previously processed components are scalar on their blocks and stay commuting with subsequent steps.

This proof uses spectral subspaces only to establish a distance inequality. The actual localization never uses this approximate tuple, its ordering, or any internal eigenbasis. If the right side of (18) is at most 1/2, normalize Z to norm one; its distance from X is at most 2C_N t^(1/4). Thus (16) can be converted into an explicit t^(1/4) modulus with the finite derivative constant K.


## 7. Payment and physical measure

The first term R in (17) has the original leafwise payments:

1. A selected-block transition costs at most C_N L^(-2) alpha_a^(-2), with alpha_a>=c_N delta Delta_N r_pi by (8). On the physical low coefficient the lower-rank soft Hardy estimate pays this from an arbitrarily small internal-form fraction, with faster-than-inverse-square exterior defect.
2. A proper-union transition has a_I^2=sum alpha_a^2+s_I^2, where s_I is the canonical relative-center radius of that union. Therefore a_I^(-2)<=s_I^(-2), paid by ordinary Hilbert-valued relative-center Hardy in dimension 9(l-1). There are at most 2^N such terms per sheet. Their coefficient C_N/L^2 can be made arbitrarily small before delta and Delta_N are fixed.
3. On the colored complementary coefficient all scalar costs are bounded by C_(N,kappa,L) r_pi^(-2), using (6)-(8), and are paid by a retained fast gap at sufficiently large radius. The physical lower-rank Hardy theorem is not applied to colored vectors.
4. The additional epsilon rho_X^(-2) in (17) is at most epsilon r_pi^(-2). On the low coefficient it uses an arbitrarily small fraction of the center Hardy reserve; on the complement it is absorbed by the fast reserve at large radius. If the near-cone region is set by t, the existing outer cutoff has its separately paid commutator-potential IMS cost.

The only form inputs in this payment are the previously identified internal soft-Hardy estimates and the separately supplied all-vector multiblock comparison with sufficient retained reserves. This construction does not manufacture those reserves.

On each flag sheet the physical density is the exact J=det M from the intrinsic geometry note. Same-sheet frame changes are unitary residual-block/normal-frame transitions and introduce no scalar chart partition. Distinct sheets remain distinct summands. Pull back the physical section to the incidence cover and multiply by w_j. Then

    ||u||^2=sum_j ||w_j u||^2,
    h[u]=sum_j h[w_j u]-integral E(X)|u|^2                  (19)

with sheet integration against the pulled-back physical measure, equivalently J dZ dA dY after gauge integration. The k! factor in (9) and normalization, rather than discarding branches, enforce single counting. Local form estimates can therefore be integrated chart-free on every sheet. No globally smooth projector, angular gauge-fixing multiplier, or internal bound-state projector is used.


## 8. Noncircular parameter order

For each fixed N and target loss epsilon:

1. Fix the necessary fractions of center/internal/fast reserves in the conditional local form theorem.
2. Choose the geometric endpoint and fast constants; choose tree kappa so beta in (5) lies strictly inside the endpoint bound. Any analytic requirement on these constants must itself be shape-independent, as required by the local comparison.
3. Choose L so the sum of at most 2^N logarithmic costs is paid by the allocated slow reserves.
4. Set delta=kappa e^(-L), Delta_N from (6), padded incidence domains, and the finite derivative/continuation constants K.
5. Choose the near-commuting threshold t_1 using (13), (16)-(18), so the added IMS defect is at most epsilon rho^(-2).
6. Choose the outer cutoff parameters and finally the exterior radius large enough to pay all fixed-shape constants, complementary inverse-square costs, and soft-Hardy remainders.

No rank-uniform statement or effective small radius is asserted. The point is that every large delta-dependent constant is either multiplied by a later freely chosen cone thickness or absorbed at a later exterior radius.
