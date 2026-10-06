# Findings on the BMN mass limit

Author: Yicheng Pan  
Date: 6 October 2026  
Status: Provisional research summary with explicitly conditional conclusions

The mass-deformation calculation supports finite-mass quadrupole inequalities, a conditional obstruction to tightness of the full BMN ground-space mixture, and exact coefficients in a separated-cluster oscillator model. It does not establish the proposed large-rank BFSS bounds. No human expert review was supplied. Finite algebra checks are not independent human certification and do not establish the missing operator-domain, tail, or uniform-limit hypotheses.

## Setting and assumptions

The setting is the physical SU(N) Hilbert space with the free U(1) center removed, normalized trace \(\operatorname{tr}=\operatorname{Tr}/N\), and kinetic operator \(-\Delta/(2N)\). Write

\[
\rho^2=\operatorname{tr}\sum_{I=1}^9Z_I^2,\qquad
\rho_6^2=\operatorname{tr}\sum_{a=4}^9Z_a^2,\qquad
q_h=\operatorname{tr}h_{IJ}Z_IZ_J,\qquad
a_h=\operatorname{tr}Z_I(h^2)_{IJ}Z_J.
\]

Here \(h\) is real symmetric and traceless, with \(\operatorname{Tr}_9 h^2=1\). The BMN Hamiltonian includes both the Myers term and the fermion mass. It is not a purely positive quadratic regulator of BFSS.

The compactness argument assumes the standard self-adjoint realization with a common smooth compactly supported physical core and local elliptic regularity. Kernel dimension and BFSS existence are separate hypotheses. Fixed-parameter polynomial-moment regularity requires coercivity of the full matrix potential and a weighted eigenfunction argument; spectral discreteness alone does not imply it. None of these fixed-parameter facts gives uniform constants as \(m\downarrow0\) or \(N\to\infty\).

## Finite-mass inequalities

For an SO(3)×SO(6)-singlet BMN zero mode and \(h\) in the symmetric traceless SO(6) sector, the positive supercharge combination

\[
H_m-\frac m3J_{12}-\frac m6(J_{45}+J_{67}+J_{89})\ge0
\]

gives a lower energy bound \(m/3\) in the \((\mathbf1,\mathbf{20}')\) sector. The highest SO(6) weight is \((2,0,0)\), and spectral projections commute with the rotations. This is a sector bound, not a mass-independent gap of the full Hilbert space. The algebra input is [Chang, equation (2.4)](https://arxiv.org/html/2404.18442v2).

For real scalar multipliers in the requisite form domain,

\[
\langle f\Psi,H_m f\Psi\rangle
=\frac1{2N}\langle|\nabla f|^2\rangle,\qquad
|\nabla q_h|^2=\frac{4a_h}{N},\qquad
|\nabla(\rho q_h)|^2=\frac{4\rho^2a_h+5q_h^2}{N}.
\]

SO(6) invariance then yields

\[
\langle q_h^2\rangle_{N,m}
\le\frac{\langle\rho_6^2\rangle_{N,m}}{N^2m},
\]

\[
\langle\rho^2q_h^2\rangle_{N,m}
\le\frac{\langle\rho^2\rho_6^2\rangle_{N,m}}{N^2m}
+\frac{15\langle\rho_6^2\rangle_{N,m}}{2N^4m^2}
\le\frac{\langle\rho^4\rangle_{N,m}}{N^2m}
+\frac{15\langle\rho_6^2\rangle_{N,m}}{2N^4m^2}.
\]

Smooth radial cutoffs justify the weighted identities when the stated moments are finite. The coefficient 5 in the weighted gradient and the resulting constants are consistent with the stated kinetic and trace normalizations.

At \(m=cN^{-2/3}\), uniform second- and fourth-radius bounds on a selected family would give the respective \(O(N^{-4/3})\) BMN estimates. Such radius bounds and transfer to BFSS are not proved. At fixed N, even strong convergence to a nonzero BFSS state leaves the right side of the unweighted certificate divergent as \(m\downarrow0\); this says nothing by itself about divergence of the actual variance.

## Conditional escape of the full ground-space mixture

Assume \(\ker H_0=\mathbb C\Omega_N\), with \(\|\Omega_N\|=1\), and let the finite-mass ground projector \(P_{N,m}\) have fixed rank \(d_N>1\). Local elliptic estimates and the common core imply that subsequential weak zero-mode limits lie in \(\ker H_0\), with strong convergence on compact coordinate sets. Applied to an orthonormal basis, Bessel's inequality gives, for compactly supported \(0\le\chi\le1\),

\[
\limsup_{m\downarrow0}\frac{\operatorname{Tr}(P_{N,m}\chi)}{d_N}
\le\frac{\langle\Omega_N,\chi\Omega_N\rangle}{d_N}.
\]

Consequently the full ground-space mixture has

\[
\frac{\operatorname{Tr}(P_{N,m}\rho^2)}{d_N}\longrightarrow\infty.
\]

Two mutually orthogonal normalized branches cannot both remain tight along the same sequence. This conclusion concerns tight directions, not preferred partition labels: several basis vectors may retain fractional overlap with the same BFSS zero mode while the rest of their norm escapes. The argument alone neither constructs a tight branch nor makes every branch's radius divergent. More generally, a BFSS kernel of finite rank \(r<d_N\) gives the corresponding \(r/d_N\) local-mass obstruction.

## Cluster calculation and its limited scope

For \(k\) separated clusters, set \(K=k-1\). Mass-normalized Jacobi coordinates satisfy

\[
\sum_{\ell=1}^K|s_\ell|^2
=N\sum_\alpha n_\alpha|R_\alpha|^2,\quad
\rho_{\rm cen}^2=N^{-2}\sum_\ell|s_\ell|^2,\quad
q_{\rm cen}=N^{-2}\sum_\ell s_\ell^Ths_\ell.
\]

In the decoupled oscillator model the covariance is
\(D=\operatorname{diag}(3I_3/(2m),3I_6/m)\). For \(h_{45}=h_{54}=1/\sqrt2\), exact Gaussian contractions give

\[
\langle\rho_{\rm cen}^2\rangle=\frac{45K}{2N^2m},\quad
\langle q_{\rm cen}\rangle=0,\quad
\langle q_{\rm cen}^2\rangle=\frac{18K}{N^4m^2},\quad
\langle\rho_{\rm cen}^2q_{\rm cen}^2\rangle
=\frac{405K^2+216K}{N^6m^3}.
\]

The last numerator is 621 for one Jacobi vector. The center quadrupole saturates the finite-mass unweighted inequality in this model. Internal-block contributions and center/internal cross terms are not included in these expressions.

The physical conversion \(m=\mu/E_N\), \(E_N=RN^{1/3}/\ell_P^2\), gives \(g_{\rm BMN}^2=1/(Nm^3)\). The cited strong-coupling description is at fixed N and requires collision/cluster qualifications. Substituting a growing cluster count or \(m=cN^{-2/3}\) is only power counting until approximation errors are controlled uniformly. Classical channel weights also require separated or incoherent channels with controlled cross terms. See [Komatsu et al., equations (1)–(4) and Sections 3.2–3.3](https://arxiv.org/html/2401.16471v1).

## Localization and positive moments

Protected localization concerns a complex supersymmetric combination. It does not identify the auxiliary eigenvalue density with the full positive equal-time scalar distribution. For a Spin(9)-invariant state, a scalar nonnegative weight W, and \(O=\operatorname{tr}(Z_1+iZ_2)^2\), the invariant-tensor identities are

\[
\langle Wq_h^2\rangle=\tfrac14\langle WO^\dagger O\rangle,
\qquad \langle WO^2\rangle=0.
\]

Thus holomorphic information alone does not bound the required positive mixed norm. The localization sources retain qualifications about omitted instanton sectors, and the later scalar-extent discussion distinguishes protected combinations from full scalar fluctuations. The nonunitary, unbounded cohomological mass-flow similarity likewise does not preserve these norms and excludes the zero-mass endpoint from its stated Gaussian-domain argument.

Relevant primary sources are [1211.0364v2](https://arxiv.org/html/1211.0364v2), [1401.5079v2](https://arxiv.org/html/1401.5079v2), [1711.07681, Section 4.2](https://arxiv.org/html/1711.07681), [the NS5 limit analysis](https://academic.oup.com/ptep/article/2023/4/043B01/7085765), and [2606.05314v1, Section 3](https://arxiv.org/html/2606.05314v1). These references concern distinct observables or limits and are not invoked as BFSS concentration theorems.

## What remains open

The route needs a selected state with uniform positive-moment control and a justified weighted comparison to the BFSS state in the chosen joint mass/rank regime. Fixed-N convergence, protected degeneracy, and finite-mass compact resolvent do not supply that comparison. A weighted error of order \(N^{-2/3}\) in \(q_h\) or \(\rho q_h\) would suffice, but is an additional dynamical hypothesis. The compactness reference is [Boulton, García del Moral and Restuccia, Section 3](https://arxiv.org/html/1011.4791#S3); its confinement constants are parameter dependent. The BFSS upper bound remains unresolved.
