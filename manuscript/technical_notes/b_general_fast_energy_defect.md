# Frozen fast energy defect

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

This appendix writes the frozen energy in physical units. Multiply E_0 by 2/R_BFSS to use the kinetic-one form of the main text; set ell=1 after the stated fixed dilation.

## 1. Statement and normalization

Let n,m be positive integers, d=nm, and let A_i and B_i, i=1,...,9, be Hermitian internal matrices of the two blocks. Rotate the spatial coordinates so that their center difference is b=r e_9, r>0. On Hom(C^m,C^n), with its Hilbert–Schmidt metric, put

    T_i Z=A_i Z−Z B_i,
    Q_i=r δ_i9 I_d+T_i,
    H=sum_i Q_i²,     C_ij=[Q_i,Q_j]=[T_i,T_j].

Assume each ||T_i||op≤r/100. A coordinate-invariant sufficient condition is

    (sum_i ||A_i||F²)^(1/2)+(sum_i ||B_i||F²)^(1/2)≤r/100.

Thus it suffices that each endpoint radius is at most r/200. No relation to any unrelated pair's separation is imposed. Each pair may use its own orthonormal spatial frame; a common global axial direction for all pairs is unnecessary. All traces below are finite ordinary, unnormalized traces.

On the slice Z_9=0 define 8-by-8 matrices with d-by-d blocks:

    G_ij=δ_ij I_d+Q_i Q_9^(-2) Q_j,
    K_ij=δ_ij H−Q_i Q_j+2 C_ij,       i,j≤8.

The kinetic-aware bosonic frequency matrix is B=G^(1/2) K G^(1/2). For Hermitian Spin(9) matrices satisfying {Γ_i,Γ_j}=2δ_ij I_16 put

    D=sum_i Γ_i⊗Q_i.

Both K and B are positive, and D has precisely 8d negative and 8d positive eigenvalues. The frozen ground energy, in physical units, is

    E_0=(R/ell³)[Tr_(8d) sqrt(B)−(1/2)Tr_(16d)|D|].

The following explicit, deliberately non-sharp constant is valid for every n,m:

    |E_0| ≤ 150002 (R/ell³) r^(-3)
                  sum_(i<j)||[T_i,T_j]||F².                    (1)

The constant in (1) is independent of d; endpoint weights below carry the finite-rank dependence. The proof neither diagonalizes internal matrices nor invokes an internal Hamiltonian gap, internal eigenvalue gap, regularity of the commuting variety, or a nearest-commuting-tuple estimate.


## 2. Why these are the correct frozen matrices

The eliminated off-block Gauss principal equation is

    Q_9 p_9+sum_(i≤8)Q_i p_i=0.

Its positive kinetic square gives G exactly. It must not be dropped or treated as a separate small bounded perturbation.

For V(X)=(R/(2ell^6))sum_(i<j)||[X_i,X_j]||F², the quadratic part in one off-block pair is (R/ell^6) Z\* K Z. The square of the linear off-block commutator gives δ_ij H−Q_j Q_i. The internal-background commutator paired with [Y_i,Y_j] contributes C_ij. Their sum is

    δ_ij H−Q_j Q_i+C_ij=δ_ij H−Q_i Q_j+2C_ij.

This works for two arbitrary internal blocks. The second block contributes with the minus sign in T_i, including in its induced commutator. At quadratic order other block pairs do not couple into this pair's Hessian. Interactions involving three distinct blocks begin in the higher-degree cross terms and are not estimated here.

The 8d complex bosonic coordinates are 16d real oscillators. Their ground energy is (R/ell³)Tr sqrt(B). The fast fermionic sector has 16d complex annihilators; filling the 8d negative eigenmodes gives −(R/(2ell³))Tr |D|. The reverse block is the adjoint, not an independent second copy.


## 3. Uniform cross gaps

Scale r to one and write κ=1/100. Then Q_9=I+T_9, Q_i=T_i for i≤8. Block norm row sums give

    ||K−I|| ≤ p(κ),        p(t)=2t+29t²,
    0≤G−I,   ||G−I||≤g(κ), g(t)=8t²/(1−t)².

For K, a diagonal block has 2T_9 plus eight squares, and each of its seven off-diagonal blocks is T_i T_j−2T_j T_i. This explains the coefficient 29. Consequently

    K≥0.9771 I,     G≥I,     B≥0.9771 I.

Also ||D−Γ_9⊗I||≤sum_i||T_i||≤9κ, so min|D|≥0.91. Continuous scaling of T to zero preserves its signature. H≥Q_9²≥0.9801 I. Restoring r multiplies K,B,H,D² by r² and D by r.


## 4. The real-trace two-commutator lemma

Let X_1,...,X_s be Hermitian matrices with ||X_i||≤κ. Set F²=sum_(i<j)||[X_i,X_j]||F². For any words w and w' of length q having the same multiset of letters,

    |Re Tr w−Re Tr w'|
       ≤ ((q)_4/8) κ^(q−4) F²,                  q≥4,          (2)

where (q)_4=q(q−1)(q−2)(q−3). The left side is zero for q≤3.

Proof. At most q(q−1)/2 adjacent swaps transform one ordering into another. The trace difference from one swap is Tr U[X_i,X_j]V. By cyclicity this is Tr C W, with C=[X_i,X_j] anti-Hermitian and W=VU a word of length q−2. Exactly,

    Re Tr(CW)=(1/2)Tr(C(W−W*)).                              (3)

Reversing W takes at most (q−2)(q−3)/2 adjacent swaps. Each resulting term contains a second commutator and q−4 other letters. Hilbert–Schmidt Cauchy–Schwarz bounds its trace by κ^(q−4)F². Equation (3), followed by the first sequence of swaps, proves (2). If q≤3, W is constant or Hermitian and (3) is zero.

In particular, take a real-coefficient homogeneous noncommutative trace polynomial whose commutative polynomial is zero. Sort every word to the same canonical word for its multiset. The sorted contributions cancel coefficient by coefficient; (2) bounds the original real trace by the sum of absolute coefficients times (q)_4 κ^(q−4)F²/8. This is an explicit algebraic estimate; it does not divide by an ideal on a singular algebraic variety.


## 5. Bosonic functional calculus and an explicit coefficient majorant

Continue at r=1. Put L=GK−I. Since GK is similar to B,

    Tr sqrt(B)=Tr sqrt(I+L)
              =8d+sum_(j≥1) binom(1/2,j) Tr L^j.            (4)

The binomial series converges in operator norm: ||L||≤l(κ)<1, where

    l(t)=p(t)+g(t)(1+p(t)).

The expansion Q_9^(-2)=sum_(j≥0)(−1)^j(j+1)T_9^j converges as well. Thus (4), and the corresponding expansion of 8Tr sqrt(H), define absolutely convergent noncommutative power series with real coefficients.

Here is a coefficientwise majorant, not just a bound on evaluations. Replace every letter T_i by a common nonnegative variable t, every scalar coefficient by its absolute value, and take maximum block row sums before taking the eight spatial diagonal traces. The series for K−I is majorized by p(t), for G−I by g(t), for L by l(t), and for H−I by

    h(t)=2t+9t².

Since sum_(j≥1)|binom(1/2,j)|z^j=1−sqrt(1−z), the sum of absolute trace-word coefficients of

    F_B(T)=Tr sqrt(B)−8Tr sqrt(H)

is majorized degree by degree by

    A(t)=8[2−sqrt(1−l(t))−sqrt(1−h(t))].                     (5)

The eight is the spatial trace multiplicity; there is no hidden factor d, because the color trace is retained inside each word and estimated by (2).

For scalar commuting variables, G K=H I_8 exactly, by the rank-one identity

    (I+vv*/q_9²)(H I−vv*)=H I,      H=q_9²+v*v.

It follows that the commutative specialization of F_B vanishes identically as a convergent power series. Each homogeneous polynomial therefore has zero commutative polynomial. Apply (2) termwise, which is allowed by the absolute majorant.

For a wholly explicit bound use t_0=1/10. Direct arithmetic gives

    p(t_0)=49/100,
    g(t_0)=8/81,
    l(t_0)=5161/8100<1,
    h(t_0)=29/100,
    A(t_0)<5.

If A(t)=sum a_q t^q, all a_q are nonnegative and

    sum_(q≥4) a_q (q)_4 κ^(q−4)
       ≤24 t_0^(-4) A(t_0),             κ≤1/100.

Indeed (q)_4(κ/t_0)^(q−4) is maximized at q=4: the consecutive-term ratio is at most 1/2. Combining with (2) gives

    |Tr sqrt(B)−8Tr sqrt(H)|
        ≤150000 sum_(i<j)||C_ij||F².                        (6)

Restoring r adds r^(-3). This establishes the needed bosonic quadratic-commutator estimate without a claim that vanishing on commuting matrices alone implies it.


## 6. Fermionic resolvent cancellation

Exactly,

    D²=I_16⊗H+S,
    S=sum_(i<j)Γ_iΓ_j⊗C_ij.

The Clifford trace gives

    Tr[(I⊗H)^(-1/2)S]=0,
    ||S||F²=16 sum_(i<j)||C_ij||F².                          (7)

For positive matrices A,A+S≥λI, the square-root resolvent identity gives

    Tr sqrt(A+S)−Tr sqrt(A)−(1/2)Tr(A^(-1/2)S)
      =−(1/π)integral_0^infinity t^(1/2)
         Tr[(A+t)^(-1)S(A+t)^(-1)S(A+S+t)^(-1)] dt.

The absolute value is bounded by

    ||S||F²/(8λ^(3/2)),

using integral_0^infinity t^(1/2)(λ+t)^(-3)dt=π/(8λ^(3/2)). Take A=I⊗H and λ=(0.91r)². Equations (7) prove

    |(1/2)Tr |D|−8Tr sqrt(H)|
       ≤(0.91)^(-3) r^(-3)sum_(i<j)||C_ij||F²
       <2 r^(-3)sum_(i<j)||C_ij||F².                        (8)

Combining (6) and (8) proves (1). The first-order fermionic term cancels exactly under the Clifford trace; the bosonic first-order-in-commutators term cancels by (3) and commutative specialization.


## 7. Endpoint commutators, pair weights, and absorption

In a matrix representation of Hom(C^m,C^n),

    T_i=A_i⊗I_m−I_n⊗B_i^T,
    [T_i,T_j]=[A_i,A_j]⊗I_m−I_n⊗[B_i,B_j]^T.

There is no mixed term [A_i,B_j]: the two endpoint actions commute. Since traces of commutators vanish, exactly

    ||[T_i,T_j]||F²
       =m||[A_i,A_j]||F²+n||[B_i,B_j]||F².                 (9)

For a partition with block sizes n_a and separations r_ab, summing (1) gives the pairwise-relative statement

    |sum_(a<b) E_0,ab|
      ≤C (R/ell³)sum_a F_a² sum_(b≠a)n_b r_ab^(-3),
    F_a²=sum_(i<j)||[A_i^(a),A_j^(a)]||F²,   C=150002.      (10)

The sum of absolute pair defects obeys the same bound. Defining the internal bosonic potential V_a=R F_a²/(2ell^6), its multiplier is

    2C ell³ sum_(b≠a)n_b r_ab^(-3).                         (11)

This tends to zero once all retained pair separations tend to infinity. Its constants have no dependence on a ratio involving the smallest unrelated center gap. At fixed finite N, r_ab≥r_\* gives the explicit upper bound 2C ell³(N−n_a)r_\*^(-3).

For clarity about full-form absorption, V_a by itself is not bounded by H_a with coefficient one without a Yukawa remainder. If the elementary finite-Clifford estimate is written as

    ||Y_a(A)||≤c_(n_a) (R/ell³) alpha_a,
    alpha_a²=sum_i ||A_i^(a)||F²,

then V_a≤H_a+c_(n_a)(R/ell³)alpha_a, since the internal kinetic form is nonnegative. One explicit choice in these conventions is c_n=24(n²−1), with c_1=0. Indeed, on the 16(n²−1) real Majoranas, the internal mass is D_ad=sum_i Γ_i⊗ad(A_i), and Y_a=(R/(2ell³))theta^T D_ad theta. In a real Hermitian generator basis D_ad is purely imaginary antisymmetric. Pairing its ±lambda eigenvalues gives ||Y_a||=(R/(4ell³))Tr|D_ad|, while

    ||D_ad||≤2sum_i||A_i||op≤6alpha_a.

This proves the stated c_n without an internal spectral gap. Hence (10) is bounded by an arbitrarily small multiple of sum_a H_a, after taking r_\* large, plus

    2C R sum_a c_(n_a)alpha_a sum_(b≠a)n_b r_ab^(-3).

Under the endpoint condition alpha_a≤κ r_ab, this last expression is at most

    2C R κ sum_(a<b)(c_(n_a)n_b+c_(n_b)n_a)r_ab^(-2).

It is an arbitrarily small center-Hardy cost by reducing κ before choosing the final exterior radius. This is a precise way to use the defect; replacing V_a by H_a with no remainder would be incorrect.

For an explicit finite-N allocation, write T_cent=(R/2)t_cent in the mass metric sum_a n_a|dz_a|². The nine-dimensional relative Hardy inequality gives

    R integral r_ab^(-2)|f|²
      ≤(8/49)(1/n_a+1/n_b)^(-1) T_cent[f].

The preceding residual multiplier is therefore bounded by

    (16Cκ/49) sum_(a<b)
      (c_(n_a)n_b+c_(n_b)n_a)(1/n_a+1/n_b)^(-1) T_cent[f]
      ≤(192C/49)N^4 κ T_cent[f].

The last bound uses c_n=24(n²−1) and
sum_(a<b)n_a²n_b²≤N^4/2. Thus, for any ε>0, the choices

    κ≤min(1/200, 49ε/(192C N^4)),
    r_*≥[2C ell³ N/ε]^(1/3),
    alpha_a≤κ r_ab for every incident pair,
    r_ab≥r_* for every pair,

give the form bound

    integral sum_(a<b)|E_0,ab| |f|²
      ≤ε sum_a H_a[f]+ε T_cent[f].                         (12)

Here the standard nonnegative internal supersymmetric forms are used on their common core, and the center Hardy estimate is valid also for Hilbert-valued coefficients and unitary connections. The multiplier of each H_a depends only on the centers, so no derivative of an internal-dependent weight has been omitted. Equation (12) is a bound on this defect multiplier, not a claim that the full Hamiltonian has already been compared with the slow forms on its right.
