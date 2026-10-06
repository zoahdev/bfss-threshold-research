# Pairwise Berry connection comparison

Technical derivation for review. Equation and subsection numbers in this appendix are local to the source derivation. Plain-text formulas retain their source notation to avoid an unverified algebraic transcription.

## 4.1 Complete charge comparison

A naive kinetic comparison

    |(partial+iA)f|² >= (1−epsilon)|partial f|²−epsilon^(-1)|A|²|f|²

loses a fixed part of internal kinetic energy. Replacing it by h_I incurs the unwanted O(epsilon kappa r) internal Yukawa mass. This is the wrong comparison.

Instead, normalize the sixteen internal charges so h_I is their averaged squared norm on the core. Replace each momentum by its scalar Berry-covariant momentum. Direct Clifford expansion gives

    h_I(A)= average_alpha ||Q_(I,alpha)+C_alpha(A)||²
             − a finite Clifford contraction of F_A.

The difference C_alpha(A) is a bounded multiplication matrix, with norm <=C_N|A|. Consequently

    h_I(A) >= (1−epsilon) h_I
               −C_N[epsilon^(-1)|A|²+|F_A|].

This retains the complete interacting h_I, rather than its kinetic part, and uses no gap. Spinor averaging eliminates the ordinary gauge-term obstruction to positivity even on the unrestricted internal module; the low coefficient additionally has the physical residual equivariance required by the inductive Hardy input.

On a two-block small-ratio tube the gapped finite matrix is analytic. All determinant curvatures vanish at internal A=0: the two-projector derivative calculation contains a Spin(9) trace of at most three Clifford matrices. Homogeneity and smoothness therefore give

    |F_A| <= C_N kappa/r².

Use equivariant radial gauge in the internal coordinates, based on the flat center vacuum at A=0. The radial-gauge curvature formula gives |A_A|<=C_N kappa²/r for internal components. Mixed relative components must also be kept: in this gauge they are the flat A=0 base connection plus the integral of F_(A,b) contracted with A. The same vanishing-at-A=0 argument and homogeneity give their bound C_N kappa²/r. Thus, after this separate mixed-component check,

    |A_Berry| <= C_N kappa²/r.

It follows that the preceding comparison costs only

    C_N[kappa+epsilon^(-1) kappa^4] r^(-2),

which can be made arbitrarily small after fixing epsilon. A gauge-equivariant radial trivialization preserves ordinary residual SU(n) physicality of the coefficient. Weyl/center flat identifications remain part of the bundle.

This establishes a viable repair of the flatness step provided the local Hamiltonian comparison really identifies the covariant internal form and retains its curvature terms. The following rootwise construction avoids an artificial dependence on the global minimum-gap ratio.

## 4.2 Pairwise relative multiblock Berry bound

At quadratic order the fast fermionic space is a direct sum over bifundamental block pairs. Its one-particle matrices are

    D_ab=Gamma dot b_ab tensor I
           +sum_i Gamma_i tensor (A_i^(a) tensor I−I tensor (A_i^(b))^T).

If each endpoint internal norm is at most kappa times r_ab=|b_ab|, the gap is a positive fixed multiple of r_ab after reducing kappa by the fixed nine-dimensional norm factor. The adapted determinant line is the tensor product of the occupied pair determinants. On each pair, choose the preceding internal-radial gauge from the flat A=0 center line. The Clifford trace calculation at A=0 is independent of bifundamental dimension, so every pure/mixed curvature component vanishes there.

Smoothness on the compact dimensionless pair tube and homogeneity give, in canonical block/center coordinates,

    |F_ab|<=C_N kappa r_ab^(-2),
    |a_ab|<=C_N kappa² r_ab^(-1).

The relative-component bound follows from its own mixed-curvature integral, not from simply declaring it gauged away. Product connections add, and Cauchy–Schwarz over the finitely many pairs gives

    |F_total|<=C_N kappa sum_(a<b) r_ab^(-2),
    |a_total|²<=C_N kappa^4 sum_(a<b) r_ab^(-2).

The full slow averaged charge stack includes all internal interacting charges and free center charges. Its comparison therefore loses only epsilon times the entire slow supersymmetric form and the inverse-square multiplier

    C_N(kappa+epsilon^(-1)kappa^4) sum_(a<b) r_ab^(-2).

This multiplier has a direct shape-independent center-kinetic payment. In the mass metric sum n_a|dz_a|², the linear map z->z_a−z_b has squared norm l_ab²=1/n_a+1/n_b. Let T_ab be kinetic energy in its nine-dimensional orthogonal relative subspace. Then

    T_ab >= (49/4) l_ab² integral r_ab^(-2)|f|²,
    T_ab <= T_centers.

Thus sum integral r_ab^(-2)|f|² <=(4/49) sum l_ab^(-2) T_centers. The finite rank-dependent coefficient contains no inverse shape gap delta_N. Choose epsilon, then kappa, before L and the global radius. Nonflatness therefore causes no parameter-order circle in this Berry comparison.

This is a lemma about the finite adapted vacuum connection and the full slow charge forms. It does not prove that all remaining full-Hamiltonian compression and Schur terms match that covariant slow model, nor does it prove the adapted bosonic/fermionic energy-defect estimate.
