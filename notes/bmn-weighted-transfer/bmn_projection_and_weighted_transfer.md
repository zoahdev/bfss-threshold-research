# BMN branch selection and weighted BFSS transfer

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


Research checkpoint 6 October 2026. This note advances the mass-deformation calculation by proving a fixed-rank branch-selection lemma and identifying its quantitative large-rank limitation. It is a separate research supplement, not a revision of the canonical manuscript. Existence and uniqueness of a physical BFSS zero mode are not proved here. The requested large-rank quadrupole upper bound remains open.

## 1 What is established

Let P_{N,m} be the orthogonal projection onto the complete zero-energy BMN space, after removal of the free U(1) center of mass. Let Ω_N be any normalized physical Spin(9)-singlet BFSS zero mode. In the normalization below, set R_{2,N}=⟨ρ²⟩_{Ω_N}.

The superalgebra gives an actual spectral gap on the complement of the entire BMN kernel. In the SO(3)×SO(6) singlet sector the gap is at least m/3. Consequently, when R_{2,N} is finite,

\[
\epsilon_{N,m}:=1-\|P_{N,m}\Omega_N\|^2
\le \frac{N^2mR_{2,N}}{12}.
\tag{1}
\]

For ε_{N,m}<1 the normalized projected vector

\[
\Phi_{N,m}=\frac{P_{N,m}\Omega_N}{\|P_{N,m}\Omega_N\|}
\tag{2}
\]

is well defined, is a BMN zero mode, and satisfies

\[
\|\Phi_{N,m}-\Omega_N\|^2
=2\bigl(1-\sqrt{1-\epsilon_{N,m}}\bigr)
\le2\epsilon_{N,m}\le\frac{N^2mR_{2,N}}6.
\tag{3}
\]

A cutoff argument removes the second-moment hypothesis for qualitative fixed-N convergence. Thus, conditional on a BFSS zero mode, a tight BMN direction does exist and converges to it. This improves the preceding audit's conclusion that at most one orthogonal direction could remain tight under BFSS uniqueness.

The quantitative control parameter is t=N²m. The mass m≈N^{-2/3} used by the earlier BMN quadrupole certificate gives t≈N^{4/3}, outside the regime guaranteed by (1) from an order-one radius bound alone. This is a limitation of the proved comparison estimate, not proof that the actual states fail to be close at that mass.

## 2 Normalization and spectral input

Use physical SU(N) matrices, normalized trace tr=Tr/N, and

\[
H_0=\frac1{2N}\operatorname{Tr}P^2-\frac N4\operatorname{Tr}[Z_I,Z_J]^2
-\frac12\operatorname{Tr}\psi\Gamma^I[Z_I,\psi],\qquad
\rho^2=\operatorname{tr}\sum_{I=1}^9Z_I^2.
\]

The BMN Hamiltonian is H_m=H_0+mV_1+m²V_2, with

\[
V_2=\frac N2\operatorname{Tr}\left(\frac19\sum_{i=1}^3Z_i^2+
\frac1{36}\sum_{a=4}^9Z_a^2\right).
\tag{4}
\]

V_1 contains both the Myers cubic and the fermion mass. No comparison H_m≥H_0+m²V_2 is made.

The primary representation-theory input is [Dasgupta, Sheikh-Jabbari and Van Raamsdonk, hep-th/0207050, Eqs. (3), (5)](https://arxiv.org/pdf/hep-th/0207050). The lowest energy of a unitary multiplet with labels (a₁,a₂,a₃|a₄|a₅) is

\[
\frac{E_0}{m}=\frac13\left(\frac{a_1}4+\frac{a_2}2+\frac{3a_3}4+a_4-\frac{a_5}2\right),
\quad
\begin{cases}
a_4\ge a_5+1,&a_5\ge1,\\
a_4\in\{0\}\cup[1,\infty),&a_5=0.
\end{cases}
\tag{5}
\]

Here a₁,a₂,a₃,a₅ are nonnegative integers. Descendant energy increments are km/12, 0≤k≤8. Minimization gives

\[
H_m\ge\frac m{12}(1-P_{N,m}).
\tag{6}
\]

Indeed, a₅≥1 gives E₀≥m/2; a₅=0,a₄≥1 gives E₀≥m/3; and a₄=a₅=0 gives E₀=mB/12, B=a₁+2a₂+3a₃. B=0 is the trivial zero-energy multiplet; every other multiplet has B≥1. Typical multiplets have continuously variable energies, but cannot approach zero at fixed m. Degenerate zero modes are all included in P_{N,m}.

### The relevant singlet gap

Let S be the SO(3)×SO(6) singlet subspace. Then

\[
H_m\big|_{S\ominus\ker H_m}\ge m/3.
\tag{7}
\]

To check descendants as well as lowest states, suppose E<m/3. Only the a₄=a₅=0 series is possible. Its lowest SU(4) representation has B boxes modulo four, and a putative descendant has B+k<4. An SU(2) singlet requires k even. At k=0 a nontrivial lowest SU(4) representation is not a singlet. At k=2 one has B≤1, whose SU(4) center charge cannot cancel the two fundamental or antifundamental supercharge factors. The B=0 multiplet is already trivial. This exhausts the possibilities below m/3.

The standard finite-N BMN realization has compact resolvent: see [Boulton, García del Moral and Restuccia, 1011.4791, §3](https://arxiv.org/html/1011.4791#S3). This allows an eigenmultiplet decomposition. All superalgebra statements concern its physical gauge-invariant domain. The cited compactness theorem is finite-rank; it is not a rank-uniform confinement estimate.

A rank-growing singlet gap is unavailable on the whole singlet complement. The protected multiplet (0,2,0|0|0), present for N≥2, contains a singlet at E=2m/3. Its 2-by-2 supertableau has an all-SU(2)-index component, with SU(2) determinant-squared symmetry. This follows from the protected traceless two-SO(6)-oscillator multiplet in §6.1 of the same primary representation paper. Thus an N-dependent improvement must exclude this and other low-energy components from the specific BFSS source, rather than assert a larger gap for the whole singlet sector.

## 3 The Rayleigh error really is quadratic in mass

One can avoid separate integrability assumptions on the cubic Myers term. Use the standard sixteen self-adjoint real supercharges on physical states, with trace-normalized sum of squares equal to the Hamiltonian form. At fixed time,

\[
Q_{m,\alpha}=Q_{0,\alpha}+mL_\alpha,
\]

where L_α is linear in Z and in fermions. The trace over supercharge indices cancels the rotation terms in the BMN anticommutator, and the squared mass contribution is exactly (4). Since Q_{0,α}Ω_N=0, finite ⟨ρ²⟩ suffices to put Ω_N in every deformed charge domain and gives

\[
\mathfrak h_m[\Omega_N]=m^2\langle V_2\rangle_{\Omega_N}
=\frac{N^2m^2}{36}R_{2,N}.
\tag{8}
\]

For the last equality, Spin(9) invariance gives one third of R₂ in the first three coordinates and two thirds in the last six. Equivalently, on radial cutoffs the two linear mass expectations vanish because they transform as a nontrivial Spin(9) three-form. The charge-form proof remains valid when an uncut cubic expectation has not been defined. The explicit mass-linear matrix supercharges and their real-basis anticommutator appear in [Dasgupta, Sheikh-Jabbari and Van Raamsdonk, hep-th/0205185, Appendix B, printed pp. 40–41](https://arxiv.org/pdf/hep-th/0205185). [Kim and Park, hep-th/0207061, §2](https://arxiv.org/pdf/hep-th/0207061) provide an independent algebra convention.

The spectral theorem applied to (7) and (8) proves (1). Since P_{N,m} commutes with SO(3)×SO(6), projection preserves the singlet sector. No BMN ground-state uniqueness or partition label is needed. Equation (3) is a squared-norm estimate; the norm error is generally O(N√(mR₂)), not O(N²mR₂).

## 4 Qualitative projection convergence without a moment assumption

Assume the compatible self-adjoint supersymmetric realizations with the usual smooth compactly supported physical core. Fix N. Let Ω be a normalized Spin(9)-singlet BFSS zero mode, with no radial moment assumed. Choose a smooth radial cutoff χ_L(ρ)=χ(ρ/L), equal to one below L, zero above 2L, with |χ′|≤C. The zero-mode ground-form identity and Spin(9) cancellation give

\[
\mathfrak h_m[\chi_L\Omega]
=\frac1{2N^2}\langle |\partial_\rho\chi_L|^2\rangle_\Omega
+\frac{N^2m^2}{36}\langle\rho^2\chi_L^2\rangle_\Omega.
\tag{9}
\]

The singlet gap implies, with t=N²m,

\[
\|(1-P_m)\chi_L\Omega\|^2
\le\frac{3C^2}{2tL^2}\Pr_\Omega(\rho\ge L)
+\frac t{12}\langle\rho^2\chi_L^2\rangle_\Omega.
\tag{10}
\]

Take L=t^{-1/2}. The first term tends to zero by the L² tail property. The integrand tρ²χ_L² is bounded by 4 and tends pointwise to zero, so the second term tends to zero by dominated convergence. Finally,

\[
\|(1-P_m)\Omega\|
\le\|(1-\chi_L)\Omega\|+\|(1-P_m)\chi_L\Omega\|\longrightarrow0.
\tag{11}
\]

Therefore Φ_m in (2) exists for all sufficiently small m and converges strongly to Ω. This argument does not use the candidate radial-moment theorem from the preceding BFSS work. Its conclusion is conditional on existence of Ω, not on a mass-flow or cohomology identification.

## 5 A branch selection that does not require knowing Ω explicitly

Now additionally assume ker H₀=ℂΩ. The projections converge strongly on the whole Hilbert space:

\[
P_m\longrightarrow P_0=|\Omega\rangle\langle\Omega|.
\tag{12}
\]

For any fixed f, every weak subsequential limit of P_mf lies in ker H₀: test H_mP_mf=0 against the common compact core, on which H_m converges to H₀. Equation (11) gives ⟨Ω,P_mf⟩→⟨Ω,f⟩ and identifies that weak limit as P₀f. Projection idempotence yields ||P_mf||²=⟨f,P_mf⟩→||P₀f||², hence strong convergence.

Choose any fixed smooth, compactly supported radial weight 0≤χ≤1 with a=⟨χ⟩_Ω>0. The zero-mode equation has fixed elliptic kinetic part and locally uniformly bounded matrix potential as m→0. Interior elliptic estimates followed by Rellich compactness make the family χP_m collectively compact. Combined with (12) and self-adjointness, this gives

\[
\|\chi(P_m-P_0)\|\to0,
\qquad
\|P_m\chi P_m-aP_0\|\to0.
\tag{13}
\]

A direct norm proof is useful: if unit f_m converge weakly to f, then P_mf_m converge weakly to P₀f by (12); local elliptic compactness makes χP_mf_m converge strongly to χP₀f. This contradicts any sequence violating the first limit. The second limit follows by taking adjoints and multiplying by norm-one projections.

For sufficiently small m, P_mχP_m has exactly one eigenvalue near a; every other eigenvalue is near zero. Its normalized top eigenvector, with a consistent phase, converges to Ω. Thus one may select the BMN branch by maximizing probability in a fixed compact radial region within the complete BMN ground space. No preferred fuzzy-sphere partition must be guessed.

This is an intrinsic finite-rank selection prescription, not an explicit computation of the unknown wavefunction. Its proof gives no uniform-in-N threshold or rate. In the absence of a BFSS zero mode, the local eigenvalues could all tend to zero. Under uniqueness, every BMN direction orthogonal to the selected one escapes all fixed compact regions uniformly at fixed N; the earlier vacuum-degeneracy obstruction is consistent with this surviving direction.

## 6 Quantitative weighted transfer

For a normalized symmetric traceless h, q_h=tr(h_{IJ}Z_IZ_J) obeys |q_h|≤ρ². Set A₂=q_h and A₃=ρq_h, so |A_k|≤ρ^k. Let Φ=P_mΩ/||P_mΩ|| be specifically the projected branch from (2), δ=||Φ−Ω||, and M_p(u)=⟨ρ^p⟩_u. The compact-localization maximizer in §5 has qualitative convergence but has not been given the quantitative bound (3).

For any p>2k for which both moments are finite, weighted Hölder interpolation gives

\[
\|A_k(\Phi-\Omega)\|
\le\delta^{1-2k/p}
\bigl(\sqrt{M_p(\Phi)}+\sqrt{M_p(\Omega)}\bigr)^{2k/p}.
\tag{14}
\]

A cutoff proof displays the missing tail input. For every L>0,

\[
\|A_k(\Phi-\Omega)\|
\le L^k\delta+
L^{k-p/2}\bigl(\sqrt{M_p(\Phi)}+\sqrt{M_p(\Omega)}\bigr).
\tag{15}
\]

The first term controls the compact region; the last two contributions control the two independent tails. A moment bound on Ω alone cannot control the Φ tail. A uniform sixth moment by itself is not uniform integrability of the degree-six observable; p>6, or an explicit sixth-moment tail modulus, is needed for this argument. At each fixed m, the cited BMN theorem supplies quadratic coercivity of the full matrix potential after domination of its linear fermion part. Weighted eigenfunction bootstrapping then gives finite polynomial moments. These fixed-mass constants may diverge as m decreases; discreteness by itself would not suffice for this moment claim.

Combining (3) and (14), for small enough tR₂,

\[
\|A_k(\Phi-\Omega)\|^2
\le \left(\frac{tR_2}{6}\right)^{1-2k/p}
\bigl(\sqrt{M_p(\Phi)}+\sqrt{M_p(\Omega)}\bigr)^{4k/p}.
\tag{16}
\]

The candidate BFSS exterior estimate in the preceding research would give M_p(Ω_N)<∞ for p<9 at each fixed N if its analytical proof is valid. It gives neither uniform N control nor M_p(Φ_{N,m}). Even granting both uniform p-moment bounds, (16) is too weak at the proposed scaled mass.

To guarantee that the square of the transfer error is O(N^{-4/3}) using (16) with only O(1) upper bounds on R₂ and both p-moments, write m=N^{-α}. This certificate requires

\[
\alpha\ge2+\frac{4p}{3(p-2k)}.
\tag{17}
\]

For the weighted observable k=3 and any fixed available p<9, this requires α>6; for k=2 it requires α>22/5 in the limiting p→9 regime. These are sufficient thresholds for this particular interpolation certificate, not necessary laws for the actual states.

The earlier finite-mass estimate was

\[
\langle\rho^2q_h^2\rangle_\Phi
\le\frac{M_4(\Phi)}{N^2m}
+\frac{15\langle\rho_6^2\rangle_\Phi}{2N^4m^2}.
\tag{18}
\]

With only O(1) moment upper bounds inserted, its leading certified power reaches N^{-4/3} only for α≤2/3. The parameter regions guaranteed by (17) and (18) do not overlap. Equation (1) guarantees qualitative unweighted comparison from a bounded R₂ alone when t=N²m→0, whereas the same O(1)-only reading of (18) asks for t of order N^{4/3} or larger. Moments that themselves shrink with N could change the power count; such shrinkage is an additional input. No missing numerical constant fixes these opposite scales.

This does not rule out a much sharper Ω-specific comparison, positive-moment cancellation, or a dynamical estimate at m≈N^{-2/3}. It identifies what a new argument must improve. The global singlet gap itself cannot provide a rank gain, because of the protected singlet at 2m/3 discussed above.

## 7 An explicit warning about weighted inference

The following abstract model is not BMN and is not a counterexample to BFSS concentration. It shows that a linear gap, a quadratic Rayleigh error, compact resolvent at positive regulator, and even norm convergence of the ground projections do not imply weighted convergence.

On ℓ²({0,1,2,…}), let Ω=e₀, Re₀=e₀, Re_k=ke_k, and H₀e₀=0, H₀e_k=k^{-2}e_k for k≥1. Along m=j^{-2}, define a diagonal A_m by A_me₀=0 and A_me_k=(k^{-2}+m²k²)e_k. A_m has compact resolvent and all nonzero energies are at least 2m. Rotate only e₀ and e_j so that

\[
\phi_m=\sqrt{1-m}\,e_0+\sqrt m\,e_j
\]

is the new ground vector, and set H_m=U_mA_mU_m*. Then H_m tends to H₀ in strong resolvent sense, ||P_m−P₀||=√m, and

\[
\langle\Omega,H_m\Omega\rangle=2m^2,
\qquad
\langle R^p\rangle_{\phi_m}=1-m+m^{1-p/2}.
\tag{19}
\]

Ω has every moment finite, while the selected state's sixth moment diverges as m^{-2}. Even the second moments stay bounded yet fail to converge to Ω's second moment. For an endpoint variant, replace the mixing probability m by m³ while keeping the same A_m and escaping index j. Then the Rayleigh error is 2m⁴, the sixth moment is 2−m³, and ||R³(φ_m−Ω)||² tends to 1. Thus even a uniform sixth moment does not guarantee convergence of the degree-six weighted norm. The extra algebraic and differential structure of actual BMN must therefore be used if one wants to deduce the missing weighted estimates; spectral overlap alone is insufficient.

## 8 Precise conclusion

The fixed-rank branch obstacle is resolved conditionally on the BFSS zero mode: projection onto the whole BMN kernel converges, and under uniqueness a compact-localization eigenvector gives an intrinsic branch prescription. The linear nonzero BMN gap is real, including the singlet sector; arbitrary low-energy typical multiplets do not invalidate it.

The quantitative transfer obstacle survives. The rigorously derived overlap scale is N²m, and weighted transfer requires a BMN tail estimate in addition to BFSS moments. The candidate p<9 BFSS decay range does not provide that estimate, and the current gap-plus-Rayleigh-plus-interpolation certificate has no mass window compatible with the earlier N^{-4/3} BMN certificate. Any successful continuation must control the specific low-energy spectral/tail components of the projected BFSS state, rather than reapply the same mass gap.

## References and verification scope

1. K. Dasgupta, M. M. Sheikh-Jabbari, M. Van Raamsdonk, Protected Multiplets of M-theory on a Plane Wave, hep-th/0207050. https://arxiv.org/pdf/hep-th/0207050
2. N. Kim, J.-H. Park, Superalgebra for M-theory on a pp-wave, hep-th/0207061. https://arxiv.org/pdf/hep-th/0207061
3. L. Boulton, M. P. García del Moral, A. Restuccia, Spectral properties in supersymmetric matrix models, 1011.4791. https://arxiv.org/html/1011.4791#S3
4. K. Dasgupta, M. M. Sheikh-Jabbari, M. Van Raamsdonk, Matrix Perturbation Theory for M-theory on a PP-Wave, hep-th/0205185, Appendix B. https://arxiv.org/pdf/hep-th/0205185
5. Prior research supplement, BFSS_BMN_Mass_Limit_Audit_2026-10-06.zip: normalization and Eq. (18), already independently checked. The present note does not re-prove the prior candidate BFSS exterior theorem.

The attached finite checks verify the representation-label exclusion, coefficients, interpolation powers, and abstract example. They do not certify the unproved existence/uniqueness or a rank-uniform BMN tail theorem. The independent audit gives a separate derivation of the gap, form-domain argument, and cutoff selection result.
