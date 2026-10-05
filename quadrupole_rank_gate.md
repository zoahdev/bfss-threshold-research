# BFSS quadrupole rank gate: physical normalization and what is still missing

Date checked: 2026-10-05. This is a conditional analytic reduction, not a proof of the BFSS soft theorem or of a rank-uniform bound.

## Result

The physical, unprojected tensor `O^{ij}=R^{-1}Tr(x^i x^j)` cannot obey the proposed rank-uniform Hilbert norm bound in decompactification `R=N/p^+`: its scalar expectation already grows at least as `N^{2/3}` under the usual ground-state Ward/domain hypotheses. This objection does **not** apply to a traceless graviton contraction or to the minimal preimage with the entire zero-energy kernel projected out.

For real symmetric traceless `h`, `sum_ij h_ij^2=1`, the exact condition for the **full-norm route** is

`sup_N N^{4/3} <[tr(h_ij Z_i Z_j)]^2>_N < infinity`,

where `tr=Tr/N`, `x=ell N^{1/3} Z`, and `ell` is a fixed Planck-length convention specified below. This is a sufficient, not necessary, connected spin-2 **double-trace** estimate for the spectral objective (see §8). It is a bound in the finite-rank zero-energy state. It is weaker than an `O(N^{-2})` planar connected-correlator estimate, but such a uniform estimate is not supplied by the BFSS bootstrap results checked here.

## 1. Fixed physical conventions, without a normalization chosen to force the result

Use the center-of-mass-subtracted SU(N) matrices and physical transverse coordinates `x_i`. Set `ell^3=2 pi l_p^3` in the convention `x=2 pi alpha' Y`, `alpha'=l_p^3/R`. Equivalently one may absorb this fixed numerical factor into the definition of Planck length. The bosonic physical Hamiltonian is

`H_b = (R/2) Tr P_x^2 - R/(4 ell^6) Tr[x_i,x_j]^2`.

With `Y=(R/ell^3)x`, `g^2=R^3/ell^6`, this becomes

`H = (1/2)Tr[g^2 P_Y^2 - (1/(2g^2))[Y_i,Y_j]^2 - psi gamma^i[Y_i,psi]]`.

The dimensionless 't Hooft variables are

`lambda=g^2 N`, `Z=lambda^{-1/3}Y`, hence **exactly** `x=ell N^{1/3}Z`.

The full energy unit is `lambda^{1/3}=R N^{1/3}/ell^2`. Thus a fixed physical energy interval in decompactification corresponds to dimensionless energies of order `N^{-4/3}`. Fixed dimensionless energy control is not automatically control of the physical soft threshold.

The current convention is the standard zero-longitudinal-mode moment

`T^{++(ij)}=(1/R)STr(x_i x_j)=(1/R)Tr(x_i x_j)`.

Consequently

`O_h=(ell^2 N^{5/3}/R) tr(h_ij Z_i Z_j)`

and, for `R=N/p^+`,

`||O_h Omega_N||^2=ell^4 (p^+)^2 N^{4/3} <[tr(h_ij Z_i Z_j)]^2>_N`.

The factors `N`, `R`, and the two matrix powers are retained. For a hard block of rank `n` inside a larger matrix, replace `N` by `n` in its intrinsic bound-state scaling, while keeping the common `R`; then `p_block^+=n/R`.

Sources for conventions: [Taylor, matrix theory review, Eqs. (4), (56)](https://arxiv.org/html/hep-th/0101126); [Van Raamsdonk, current moments](https://arxiv.org/html/hep-th/9803003); [Lin, Hamiltonian Eq. (3)](https://arxiv.org/html/2302.04416).

## 2. Explicit finite-N lower-radius inequality from the actual Hamiltonian

Assume a normalized zero-energy state, SO(9) invariance, finite displayed moments, and valid stationary/virial identities as quadratic forms. Let `D=N^2-1`, `a=<Tr Y_1^2>`, `k=<K>`. Write the fermionic term as `F=Tr B_i Y_i`. Virial and zero energy give `K=V`, `<F>=-2k`. The Gram matrix of `B_1,Y_1,P_1` has entries

`[[b,-2k/9,0],[-2k/9,a,iD/2],[0,-iD/2,2k/(9g^2)]] >= 0`,

with the finite-N fermion bound `b<=64N^3`. Its Schur complement yields

`a >= k^2/(1296N^3) + 9g^2D^2/(8k)`.

Minimizing at `k=9(g^2)^{1/3}N D^{2/3}` gives

`<tr Z_1^2> >= (3/16)(1-N^{-2})^{4/3}`.

This restores the finite-N commutator omitted in the large-N presentation of [Lin, §2.3 and Appendix C](https://arxiv.org/html/2302.04416). No large-N factorization enters this derivation. Algebra was checked symbolically in the companion script.

It follows that, for `S=sum_i Tr x_i^2`,

`<S>/R >= (27/16)ell^2 (N^{5/3}/R)(1-N^{-2})^{4/3}`,

and `||(S/R)Omega|| >= <S>/R` if this vector exists. Therefore a uniform norm bound on all **raw** tensor components is inconsistent with this inequality when `R~N`.

Important limits: this is conditional on the stated moment/domain/Ward assumptions. It does not prove existence or uniqueness of `Omega_N`, nor prove those assumptions from normalizability alone. If the required position norm is infinite, the raw uniform norm assertion fails even earlier.

## 3. Why this is not a no-go for the graviton source

The source identity under investigation is `T_h Omega=-(1/2)H^2 O_h Omega`. The canonical minimal preimage is obtained by removing the whole kernel of `H`, not merely a guessed unique vacuum. A scalar expectation is killed by `H^2`, so the preceding raw-tensor obstruction must not be transferred to this projected preimage.

For traceless `h`, rotational invariance gives `<O_h>=0`. More strongly, if every normalizable zero-energy state is a Spin(9) singlet, `P_0 O_h Omega=0`: a spin-2 operator has no matrix element between singlets. [Sethi–Stern](https://arxiv.org/abs/hep-th/0001189) prove the relevant invariance statement conditional on normalizable ground states; their abstract singles out the two-D0 case when combining it with index results for uniqueness. We assume no general-rank uniqueness theorem here.

## 4. Exact spin-2 reduction to two gauge-invariant double traces

Put `M_ij=tr(Z_i Z_j)`, and define

`A_N=<sum_ij M_ij M_ij>`, `B_N=<(sum_i M_ii)^2>`, `D_N=A_N-B_N/9`.

`M` is a positive-semidefinite nine-dimensional Gram matrix at each configuration. SO(9) invariance and the dimension `44` of symmetric traceless rank-two tensors give the exact identity

`<[h_ij M_ij]^2>=D_N/44`.

Thus the physical uniform bound is **equivalent** to

`sup_N N^{4/3}D_N < infinity`

when `p^+` is fixed and nonzero. It is neither an upper bound on `<tr Z^2>` alone nor an ordinary single-trace quartic estimate.

Positivity gives only

`0<=D_N<=(8/9)B_N`,

or, in physical variables,

`||O_h Omega||^2 <= (2/(99R^2)) <S^2>`.

Even a hypothetical `B_N=O(1)` bound would give only `||O_h Omega||^2=O(N^{4/3})`. It does not prove the desired estimate. A quantitative connected suppression is needed. Ordinary planar factorization with a controlled `O(N^{-2})` variance would be more than sufficient, giving `||O_h Omega||^2=O(N^{-2/3})`; merely saying that the variance tends to zero is insufficient because its rate matters.

The lower bound on the scalar size does not imply any lower bound on `D_N`: a Gram matrix can be proportional to the nine-dimensional identity while having arbitrarily large trace. This is an algebraic nonimplication, not a proposal for a BFSS wavefunction.

## 5. What a Hamiltonian Ward identity actually controls

For a real scalar multiplication operator `f(x)`, the quadratic-form identity in a zero-energy state is

`<f Omega,H f Omega>=(R/2)<|grad f|^2>`,

provided cutoff integration by parts and the limit are justified. The matrix-valued fermion potential commutes with scalar `f`. Applied to the physical quadrupole,

`<O_h Omega,H O_h Omega>=(2/R)<Tr x_i(h^2)_ij x_j>=(2/(9R))<S>`.

This is a first **energy-weighted** spectral moment. It does not give an upper bound on the unweighted norm in a gapless spectrum. For dimensionless `q_h=tr(hZZ)` and `H_hat=H/lambda^{1/3}`, the same identity is

`<q_h Omega,H_hat q_h Omega>=(2/N^2)<tr Z_1^2>`.

Therefore a low-energy spectral component of weight `N^{-alpha}` at energies of order `N^{-beta}` is not bounded by this sum rule unless `alpha+beta` is controlled. Taking a mass-deformed spectral gap and then dropping the mass loses precisely the needed uniformity. These formulas specify what a proposed bootstrap certificate would have to add; they are not a new upper-bound theorem.

## 6. Literature audit relevant to this gate

- [Lin–Zheng, BFSS ground-state bootstrap, 2410.14647v2, §§3–4](https://arxiv.org/html/2410.14647v2): the level-9 feasible region is noncompact; there is no unconditional upper bound on the quadratic or radial quartic bosonic moment. The construction imposes infinite-N factorization. The authors explicitly discuss low intermediate energies, power-law tails, and a possible failure of factorization in higher multitraces, together with the noninterchangeable BMN-mass and large-N limits. Those observations do not show divergence of the degree-four quadrupole variance, but they do prevent treating it as a proved, uniform finite-N estimate. Their thermal comparison includes BMN-regulated finite-temperature data; it is not an exact zero-temperature BFSS bound. The paper’s reported scalar lower bound is not a bound on `D_N`.
- [Lin–Zheng, 2507.21007v3](https://arxiv.org/html/2507.21007v3): the later high-precision islands concern **bosonic** multimatrix quantum mechanics. Its text describes high-precision supersymmetric BFSS as future work and cites Part II as in preparation. Its adjoint-gap discussion does not give the gauge-singlet spin-2 covariance needed here.
- [Biggs–Herderschee, 2503.14685v2](https://arxiv.org/html/2503.14685v2): holographic Witten-diagram correlators supply predictions in the gravitational regime, not a finite-rank Hamiltonian inequality on the equal-time quadrupole norm.
- [Polchinski, hep-th/9903165v2, §7](https://arxiv.org/html/hep-th/9903165v2): the lower size argument and `r^{-9}` two-cluster tail support the known fixed-rank power counting; they do not control its rank-dependent coefficient, onset, or all-channel sum.

## 7. Precisely delimited next analytic target

A useful actual-BFSS certificate must bound the finite-N spin-2 double trace `D_N` by `C N^{-4/3}` (or bound the appropriately restricted low-energy spectral measure sufficiently for the source argument), with constants uniform in the physical decompactification and any infrared regulator. A certificate for a planar single-trace moment, an assumed planar factorization law, or a BMN bound with coefficients diverging as the mass vanishes does not meet that target.

No such certificate was established in this pass. The substantive progress is the physical normalization, an explicit conditional lower-bound obstruction for the raw tensor, and the exact connected spin-2 condition for the full-norm route. The energy-form alternative in §8 is weaker and avoids the fourth moment.


## 8. Stronger follow-up: the full quadrupole norm is unnecessary, but a radius upper bound does not close uniformity

Let `mu_O` be the spectral measure of `O_h Omega` when this vector exists, and `u=-(1/2)H_phys^2 O_h Omega`. For the **physical** cutoff `delta`,

`W_N(delta)=integral_(0,delta) E^{-1} dmu_u(E)`

`= (1/4) integral_(0,delta) E^3 dmu_O(E)`

`<= (delta^2/4) <O_h Omega,H_phys O_h Omega>`.

This is valid and uses an energy-form norm rather than the quadrupole Hilbert norm. In fact it has a useful domain extension. Suppose `<S>` is finite and compact-cutoff ground-state form identities are valid. Set `f_L=chi(sqrt(S)/L) O_h`, with `chi` a smooth compact cutoff equal to one near zero. Since `|grad f_L|^2 <= C S/R^2`, cutoff differences have energy norm tending to zero by dominated convergence. Consequently

`v_N=lim_(L->infinity) H_phys^{1/2}(f_L Omega_N)`

exists in the Hilbert space even if `O_h Omega_N` does not. It satisfies

`||v_N||^2=(2/(9R))<S> = (2 ell^2 N^{5/3}/R) a_N`,

where `a_N=<tr Z_1^2>`. On a finite energy interval define

`u_(N,delta)=-(1/2) 1_(0,delta)(H_phys) H_phys^{3/2} v_N`.

This is a well-defined bounded spectral construction, with

`W_N(delta)=(1/4) integral_(0,delta) E^2 dmu_v(E) <= (delta^2/4)||v_N||^2`.

Identifying it with the physical stress source still requires the source identity in this cutoff/form sense; this construction does not establish that missing identification by itself.

### Exact rank factors

Writing `c_N=ell^2 N^{5/3}/R`, `Lambda_N=R N^{1/3}/ell^2`, `O_h=c_N q_h`, `H_phys=Lambda_N H_hat`, one obtains

`W_N(delta)=(R N^{13/3}/(4 ell^2)) integral_(0,delta/Lambda_N) e^3 dmu_q(e)`

whenever `mu_q` exists. The exact dimensionless Ward sum rule is `integral e dmu_q(e)=2a_N/N^2`.

At `R=N/p^+`,

`W_N(delta) <= (delta^2 ell^2 p^+/2) N^{2/3} a_N`.

A hypothetical uniform upper radius bound `a_N<=C` therefore leaves a growing `N^{2/3}` coefficient. Making this **full first-moment bound** uniform would require `a_N=O(N^{-2/3})`, incompatible with the positive finite-N lower bound in §2. Thus the energy-form route genuinely removes the fourth-moment/domain requirement, but an ordinary O(1) radius upper bound alone cannot certify physical rank-uniform integrability.

This does **not** disprove the desired low-energy conclusion: the divergent total first moment might be carried by high physical energies. Nor should one use the dimensionless cutoff in place of the physical cutoff: the latter becomes `delta/Lambda_N=delta ell^2 p^+ N^{-4/3}`.

### A weaker sufficient target than the full-norm bound

For a fixed physical `delta_0>0`, it would suffice to prove

`sup_N ||1_(0,delta_0)(H_phys) v_N||^2 < infinity`.

Then `sup_N W_N(delta)<=C delta^2/4` for `delta<=delta_0`. Where `mu_q` exists, this localized estimate is equivalent to

`integral_(0,delta_0 ell^2 p^+ N^{-4/3}) e dmu_q(e) = O(N^{-8/3})`,

because its physical prefactor is `ell^2 p^+ N^{8/3}`. The total Ward moment is only `2a_N/N^2`; it does not provide the extra low-energy suppression. This is a precise finite-N infrared spectral target, with a shrinking dimensionless window, rather than a global position-moment bound.

If one assumes `a_N<=C` and chooses a diagonal cutoff `delta_N=epsilon N^{-1/3}`, the crude Ward estimate becomes `W_N(delta_N)<=C ell^2 p^+ epsilon^2/2`. This is a restricted joint scaling. It cannot replace a uniform-in-N estimate at fixed physical delta or justify exchanging the limits.

All of this remains confined to the established **zero longitudinal Fourier mode** current identity. No extension to a rank-changing/nonzero-longitudinal soft source, full scattering-state factorization, or complete soft theorem has been shown.
