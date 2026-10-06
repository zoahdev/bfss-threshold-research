# BMN mass deformation: an actual finite-mass bound and the unresolved BFSS transfer

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


Research checkpoint: 6 October 2026. This note proves a finite-mass representation-theoretic inequality, gives a conditional compactness obstruction to using all BMN vacua, and checks a separated-cluster model quantitatively. It does **not** prove the requested large-rank BFSS upper bound. The surviving sufficient conditions are not claimed as a breakthrough or as easier than the original problem.

## 1. Normalization and the precise deformation

The target lives in the physical SU(N) Hilbert space, with the free U(1) center of mass removed. Use

\[
H_0=\frac1{2N}\operatorname{Tr}P^2-\frac N4\operatorname{Tr}[Z_I,Z_J]^2
-\frac12\operatorname{Tr}\psi\Gamma^I[Z_I,\psi],\qquad
\operatorname{tr}=\operatorname{Tr}/N.
\]

Let \(\Omega_N\) be the hypothesized normalized Spin(9)-singlet BFSS zero mode. Set

\[
\rho^2=\operatorname{tr}\sum_{I=1}^9Z_I^2,\quad
\rho_6^2=\operatorname{tr}\sum_{a=4}^9Z_a^2,\quad
q_h=\operatorname{tr}h_{IJ}Z_IZ_J,\quad
a_h=\operatorname{tr}Z_I(h^2)_{IJ}Z_J,
\]

where \(h\) is real symmetric, traceless, and \(\operatorname{Tr}_9h^2=1\). The targets are \(\langle q_h^2\rangle=O(N^{-4/3})\) or \(\langle\rho^2q_h^2\rangle=O(N^{-4/3})\).

Write the dimensionless BMN mass as \(m>0\):

\[
H_m=H_0+\frac N2\operatorname{Tr}\left[
\frac{m^2}{9}\sum_{i=1}^3Z_i^2+\frac{m^2}{36}\sum_{a=4}^9Z_a^2\right]
+\frac{imN}{3}\epsilon_{ijk}\operatorname{Tr}Z_iZ_jZ_k
+\frac{im}{8}\operatorname{Tr}\psi^T\Gamma^{123}\psi.
\tag{1}
\]

The conventional sign of the Myers term can be changed together with the fuzzy-sphere orientation. Nothing below uses that sign. It is essential, however, that both the Myers and fermion mass terms are present. This is not \(H_0+\varepsilon\rho^2\), and positivity comparisons valid for that simpler regulator do not apply.

Starting from physical matrices \(X=\ell N^{1/3}Z\), the energy unit and mass relation are

\[
E_N=RN^{1/3}/\ell^2,\qquad m=\mu/E_N,
\qquad g_{\rm BMN}^2=\frac{R^3}{\mu^3\ell^6}=\frac1{Nm^3},
\qquad \lambda_{\rm BMN}=Ng_{\rm BMN}^2=m^{-3}.
\tag{2}
\]

Thus \(m=cN^{-2/3}\) means \(\mu=cR\ell^{-2}N^{-1/3}\), \(g_{\rm BMN}^2=N/c^3\), and \(\lambda_{\rm BMN}=N^2/c^3\). Weak-mass-oscillator perturbation theory is not justified there.

The full finite-N BMN Hamiltonian has compact resolvent at nonzero mass. The proof in [Boulton–García del Moral–Restuccia, §3](https://arxiv.org/html/1011.4791#S3) explicitly has rank-dependent confinement constants. It does not give the needed uniform mass/rank estimate. Ordinary finite-mass eigenfunctions have the decay needed for the moments and integrations below; alternatively state the displayed moment/domain hypotheses explicitly and use smooth radial cutoffs.

## 2. A concrete finite-mass theorem from SU(2|4)

Choose \(h\) supported on the last six directions and traceless there. A convenient example is \(h_{45}=h_{54}=1/\sqrt2\). Let \(\Psi_{N,m}\) be any normalized BMN zero-energy vector. Its ground multiplet is an SO(3)×SO(6) singlet; the proof applies also to a singlet ground-space mixture.

The quadrupole \(q_h\Psi_{N,m}\) lies in the \((\mathbf1,\mathbf{20}')\) isotypic subspace. A positive supercharge anticommutator is

\[
\Delta=H_m-\frac m3J_{12}-\frac m6(J_{45}+J_{67}+J_{89})\ge0.
\tag{3}
\]

This is [Chang, *Witten index of BMN matrix quantum mechanics*, Eq. (2.4), July 2026 revision](https://arxiv.org/html/2404.18442v2#S2.SS2), rescaled by (2). The \(\mathbf{20}'\) has highest weight \((J_{45},J_{67},J_{89})=(2,0,0)\). Because every spectral projection of \(H_m\) commutes with SO(6), every nonzero spectral slice in this isotypic subspace includes that highest weight. Therefore

\[
H_m\big|_{(\mathbf1,\mathbf{20}')}\ge m/3.
\tag{4}
\]

This is a sector bound proportional to the mass, **not a mass-independent spectral gap**. Degenerate singlet vacua do not cause a zero-energy contribution to \(q_h\Psi\).

For a real gauge-invariant coordinate multiplier \(f\), the ground-state quadratic-form identity is

\[
\langle f\Psi,H_m f\Psi\rangle
=\frac1{2N}\langle|\nabla f|^2\rangle_\Psi.
\tag{5}
\]

All potential terms, including the fermion matrix potential, commute with \(f\). In raw color coordinates,

\[
|\nabla q_h|^2=4a_h/N.
\]

Combining (4)–(5) and SO(6) invariance gives the first actual upper bound:

\[
\boxed{\langle q_h^2\rangle_{N,m}
\le\frac{6\langle a_h\rangle_{N,m}}{N^2m}
=\frac{\langle\rho_6^2\rangle_{N,m}}{N^2m}.}
\tag{6}
\]

The mean is zero in this sector, so this is also a variance bound. The equality uses \(\operatorname{Tr}_6h^2=1\).

### The weighted target can be bounded directly

The scalar \(\rho\) preserves the same representation. For \(f=\rho q_h\),

\[
|\nabla\rho|^2=1/N,\quad
\nabla\rho\cdot\nabla q_h=2q_h/(N\rho),\quad
|\nabla(\rho q_h)|^2=(4\rho^2a_h+5q_h^2)/N.
\]

The origin causes no difficulty after replacing \(\rho\) by \(\sqrt{\rho^2+\eta}\) and passing to the form limit. Applying (4)–(5), then SO(6) invariance with the scalar weight \(\rho^2\), yields

\[
\boxed{\begin{aligned}
M_{N,m}:=\langle\rho^2q_h^2\rangle_{N,m}
&\le\frac{\langle\rho^2\rho_6^2\rangle_{N,m}
+\tfrac{15}{2}\langle q_h^2\rangle_{N,m}}{N^2m}\\
&\le\frac{\langle\rho^4\rangle_{N,m}}{N^2m}
+\frac{15\langle\rho_6^2\rangle_{N,m}}{2N^4m^2}.
\end{aligned}}
\tag{7}
\]

No factorization, localization, Born–Oppenheimer expansion, or uniqueness of the BMN vacuum was used in (6)–(7). The calculations have been independently audited; the symbolic checks include the coefficient 5 in the weighted gradient.

At \(m_N=cN^{-2/3}\), a selected family with \(\langle\rho^2\rangle\le C_2\) and \(\langle\rho^4\rangle\le C_4\) would satisfy

\[
\langle q_h^2\rangle_{N,m_N}\le(C_2/c)N^{-4/3},
\quad
M_{N,m_N}\le(C_4/c)N^{-4/3}
+\frac{15C_2}{2c^2}N^{-8/3}.
\tag{8}
\]

These are BMN estimates. Establishing the radius hypotheses and passing them to the actual BFSS zero mode remain separate open inputs.

## 3. Why fixed-rank regulator removal does not finish this mechanism

Suppose a chosen \(\Psi_{N,m}\) converges strongly, at fixed \(N\), to \(\Omega_N\). Lower semicontinuity gives

\[
\liminf_{m\downarrow0}\langle\rho_6^2\rangle_{N,m}
\ge\langle\rho_6^2\rangle_{\Omega_N}>0.
\]

The last strict inequality follows because a nonzero L² wavefunction cannot be supported on the measure-zero locus with all six matrices zero. Thus the certificate on the right of (6) diverges at fixed N. This does not assert that the actual variance diverges; it shows that this mass-gap certificate alone cannot transfer it. The same problem occurs in (7).

The following sufficient conditions precisely delimit a possible scaled-mass route. Choose phases and \(m_N=cN^{-2/3}\). In addition to the radius bounds in (8), require one of

\[
\|q_h(\Omega_N-\Psi_{N,m_N})\|\le C_*N^{-2/3}
\tag{9a}
\]

or, for the weighted target,

\[
\|\rho q_h(\Omega_N-\Psi_{N,m_N})\|\le C_*N^{-2/3}.
\tag{9b}
\]

The triangle inequality then transfers the corresponding \(O(N^{-4/3})\) estimate. These are sufficient weighted comparison conditions, not facts proved by the mass deformation. They are strong, and may be as difficult as the original target. Unweighted state convergence with no rate or tail information does not imply them.

Only one fixed SO(6)-sector polarization is needed: in a Spin(9)-singlet BFSS state the quadratic form \(h\mapsto\langle Wq_h^2\rangle\), for \(W=1\) or \(\rho^2\), is scalar on the irreducible traceless-symmetric \(\mathbf{44}\). A transferred estimate therefore extends to all normalized real traceless \(h\).

A different, nonquantitative transfer would be enough if one independently proved a uniform small-mass bound on the desired nonnegative observable and a tight fixed-N state family. Strong convergence and Fatou would then transfer the upper bound without fourth-/sixth-moment convergence. Equations (6)–(7) do not supply that uniform small-mass bound.

## 4. Vacuum degeneracy gives a genuine conditional escape theorem

The protected zero-energy BMN states are indexed by partitions of N. Let \(d_N\) denote their dimension (conventionally \(p(N)\) after the independent U(1) oscillator is removed), and \(P_{N,m}\) their projector. The index paper above explicitly distinguishes nonzero mass from the singular zero-mass limit. Its invariance is not a statement about a selected normalized BFSS vector.

Assume, explicitly, that the physical SU(N) BFSS operator has a one-dimensional L² kernel \(\mathbb C\Omega_N\), and use the usual self-adjoint realization with compactly supported smooth gauge-invariant spinors as an operator core. At each fixed N:

1. For any sequence \(m_j\downarrow0\), normalized zero modes have uniform local H² bounds, since \(H_{m_j}\) is a fixed elliptic kinetic operator plus locally uniformly bounded matrix coefficients.
2. Weak L² subsequential limits are BFSS zero modes: test the zero-mode equation on the core, where \(H_m\phi\to H_0\phi\).
3. Rellich compactness gives strong L² convergence on every compact region. A tight family consequently converges strongly globally to \(\Omega_N\), up to phases.

Apply this simultaneously to an orthonormal basis \(\psi_{a,m}\), \(a=1,\ldots,d_N\), of the BMN ground space. Along a subsequence its local limits are \(c_a\Omega_N\). Bessel's inequality gives \(\sum_a|c_a|^2\le1\). Therefore, for every compactly supported scalar multiplier \(0\le\chi\le1\),

\[
\boxed{\limsup_{m\downarrow0}\frac1{d_N}\operatorname{Tr}(P_{N,m}\chi)
\le\frac1{d_N}\langle\Omega_N,\chi\Omega_N\rangle.}
\tag{10}
\]

It follows that there cannot be two mutually orthogonal, individually tight normalized BMN zero-mode families. This is a statement about tight directions, not a canonical partition label: several basis vectors may each retain a fractional overlap with \(\Omega_N\), while their other norm escapes.

Taking \(\chi\) equal to one on \(\rho\le R\) gives, for every R,

\[
\liminf_{m\downarrow0}\frac1{d_N}\operatorname{Tr}(P_{N,m}\rho^2)
\ge R^2(1-1/d_N).
\]

Thus the full ground-space mixture has diverging radius whenever \(d_N>1\). Averaging over all protected vacua cannot supply the tight bounded-radius state needed in (8). This does not exclude one well-selected tight branch, nor prove its existence. The proof also makes clear why keeping the U(1) center of mass would invalidate the assumed BFSS normalizable vacuum.

There is no automatic canonical ground-state branch from the fact that its energy is protected: the entire zero eigenspace remains degenerate. A protected count or a nonunitary cohomology isomorphism supplies neither a norm-preserving branch selection nor control of its tails.

## 5. Quantitative separated-block check

The following calculation is exact in the leading decoupled-cluster oscillator model; it is **not** asserted to be a uniform-N theorem for the interacting BMN wavefunction. [Komatsu et al., §§1, 3.2.3, 3.3.1](https://arxiv.org/html/2401.16471v1) derive a fixed-N strong-coupling separated-particle effective Hamiltonian and explain that it breaks down at collisions. The bound-cluster completion is an additional physical scenario.

For k clusters of sizes \(n_\alpha\), \(\sum n_\alpha=N\), let \(K=k-1\) and remove the total center of mass. Mass-normalized Jacobi coordinates \(s_\ell\in\mathbb R^9\) have covariance

\[
D=\operatorname{diag}\left(\frac3{2m}I_3,\frac3m I_6\right),
\quad
q_{\rm cen}=N^{-2}\sum_{\ell=1}^K s_\ell^Ths_\ell,
\quad
\rho_{\rm cen}^2=N^{-2}\sum_{\ell=1}^K|s_\ell|^2.
\tag{11}
\]

For two blocks of sizes n and N−n with relative displacement r,
\(s=\sqrt{n(N-n)}r\), so \(q_{\rm cen}=n(N-n)r^Thr/N^2\). The dependence on the split cancels after taking the oscillator expectation.

For \(h_{45}=h_{54}=1/\sqrt2\), exact Wick contraction yields

\[
\boxed{\begin{aligned}
\langle\rho_{\rm cen}^2\rangle&=\frac{45K}{2N^2m},\\
\langle q_{\rm cen}\rangle&=0,\\
\langle q_{\rm cen}^2\rangle&=\frac{18K}{N^4m^2},\\
\langle\rho_{\rm cen}^2q_{\rm cen}^2\rangle
&=\frac{405K^2+216K}{N^6m^3}.
\end{aligned}}
\tag{12}
\]

For K=1 the last numerator is 621. Equation (6) is exactly saturated by the center quadrupole in this model: \(\langle\rho_{6,\rm cen}^2\rangle=18K/(N^2m)\), and the quadrupole creates an oscillator excitation of energy \(m/3\). An improvement must use information excluding or suppressing these low-energy cluster components, not merely the superalgebra.

If a disjoint cluster channel, or an incoherent/independent product approximation, has weight \(p_{N,m,K}\) and controlled subleading errors, its center contribution forces the necessary bounds

\[
p_{N,m,K}\lesssim\frac{N^{8/3}m^2}{18K}
\quad\hbox{for the variance target},
\qquad
p_{N,m,K}\lesssim\frac{N^{14/3}m^3}{405K^2+216K}
\quad\hbox{for the weighted target}.
\tag{13}
\]

These formulae specify missing amplitude information. Arbitrary coherent superpositions cannot be treated as classical channel probabilities without controlling cross terms/localization errors. At fixed N, unsuppressed K≥1 channels make the moments diverge as m⁻² and m⁻³. Tightness alone forces their probability to vanish but supplies no necessary rate for moment convergence. Existing asymptotic block falloffs or protected degeneracy counts do not give the rates in (13).

At a double-scaled mass the fixed-N approximation itself needs uniform error control. For example, substituting \(K=N-1\) or \(m=cN^{-2/3}\) into (12) is power counting only unless the collision regions and rank-dependent off-diagonal corrections are bounded. In particular, this note does not infer a BFSS bound from that substitution.

## 6. Why protected localization does not provide the missing positive estimate

The localized observable is a complex supersymmetric combination of an SO(3) matrix and time-dependent SO(6) matrices, not the full real equal-time radius distribution. The detailed formulas and instanton qualifications are recorded in `localization_scope.md`. The primary references are [Asano et al., 1211.0364](https://arxiv.org/html/1211.0364v2), [1401.5079](https://arxiv.org/html/1401.5079v2), and [1711.07681, §4.2](https://arxiv.org/html/1711.07681). The last paper explicitly discusses cancellation of heavy-mode contributions in protected combinations and the failure of identifying its eigenvalue density with the full scalar extent.

An elementary invariant-tensor calculation makes the mismatch precise. For \(T_{ij}=\operatorname{tr}Z_iZ_j\), \(O=\operatorname{tr}(Z_1+iZ_2)^2\), and any Spin(9)-scalar nonnegative weight W,

\[
\langle WT_{ij}T_{kl}\rangle=A_W\delta_{ij}\delta_{kl}
+B_W(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}),
\]

so, whenever moments exist,

\[
\langle Wq_h^2\rangle=2B_W=\tfrac14\langle WO^\dagger O\rangle,
\qquad\langle WO^2\rangle=0.
\tag{14}
\]

Holomorphic moments can vanish while the desired positive norm is arbitrarily large. No inference from those moments alone controls \(W=1\) or \(W=\rho^2\). This is an algebraic insufficiency result, not a counterexample to concentration in the BFSS ground state.

The recent [*Mass-Flow Invariance of Q-Cohomology in BMN Matrix Quantum Mechanics*, June 2026, §3](https://arxiv.org/html/2606.05314v1#S3) gives a formal similarity multiplier \(e^{(\mu-\mu_0)\mathcal K}\). It explicitly requires domain control because the multiplier is unbounded and nonunitary, and excludes the zero-mass endpoint from its Gaussian small-step argument. It therefore does not establish (9), a tight branch, or preservation of positive moment norms.

## Bottom line

The tested BMN mechanism does yield exact finite-mass inequalities (6)–(7), and the natural mass scale for the desired exponent is \(m\asymp N^{-2/3}\). Its unresolved inputs are a bounded-radius selected state and a quantitative comparison to the BFSS normalizable zero mode. Protected degeneracy, localized holomorphic moments, finite-mass compactness, and cohomological mass flow do not supply those inputs. A simultaneous compactness theorem for all vacua is actually impossible under the one-dimensional BFSS-kernel hypothesis, and the separated-block calculation quantifies the tail amplitudes that must be controlled. The original BFSS large-N upper bound remains unproved.
