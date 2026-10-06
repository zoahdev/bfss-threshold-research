# BMN localization: scope and the positive-moment obstruction

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


Assessment date: 2026-10-06

## Conclusion

The established BMN localization formulas do not presently furnish an upper bound on the full positive equal-time BFSS observables \(q_h^2\) or \(\rho^2 q_h^2\). Two independent missing steps are the identification/control of a positive mixed correlator and convergence of a correctly selected BMN ground-state family as the mass vanishes. No claim of a uniform spectral gap, large-N factorization, or protected Hilbert-space norm is used here.

The representation-dependent spectral/energy-weighted bounds derived separately in the main audit are compatible with this conclusion: they supply genuine inequalities at nonzero mass. Localization does not, by itself, make their right-hand sides uniform or provide the weighted comparison to the BFSS state.

## 1. Precise localized operator and integral

In the conventions of Asano–Ishiki–Okada–Shimasaki, define \(\widetilde\phi=\phi_{\mathrm{paper}}/2\). The protected complex field is

\[
\widetilde\phi(\tau)=-X_4(\tau)+\sinh\tau\,X_9(\tau)+i\cosh\tau\,X_{10}(\tau).
\]

For the specified vacuum \(X_a=-2L_a\), their localization relation is

\[
\left\langle\prod_\alpha\operatorname{Tr} f_\alpha(\widetilde\phi(\tau_\alpha))\right\rangle
=\left\langle\prod_\alpha\operatorname{Tr} f_\alpha(2L_4+iM)\right\rangle_{\rm MM}.
\]

Here \(M=\bigoplus_s(M_s\otimes\mathbf1_{n_s})\), where the \(M_s\) have sizes equal to the vacuum multiplicities. Up to normalization, the eigenvalue measure is

\[
d\nu_{\mathcal R}(m)=\prod_{s,i}dm_{si}\,
\exp\!\left[-\frac{2}{g^2}\sum_{s,i} n_s m_{si}^2\right] Z_{\rm 1-loop},
\]

\[
Z_{\rm 1-loop}
=\prod_{s,t}\prod_{J=|n_s-n_t|/2}^{(n_s+n_t)/2-1}\prod_{i,j}'
\left[
\frac{((2J+2)^2+\Delta m^2)((2J)^2+\Delta m^2)}
{((2J+1)^2+\Delta m^2)^2}
\right]^{1/2},\qquad \Delta m=m_{si}-m_{tj}.
\]

The prime omits the zero numerator factor at \(s=t,J=0,i=j\). The formula includes products of traces; factorization is unnecessary. It does not equate \(M\) with an original Hermitian matrix's equal-time distribution. In particular, the operation of taking an adjoint cannot simply be moved through this localization substitution.

Source: [1401.5079, §2, Eqs. 2.5–2.10](https://arxiv.org/html/1401.5079v2).

## 2. Exactness and instanton qualification

The foundational calculation omits instanton/anti-instanton localization saddles at Euclidean infinity. It computes the perturbative contribution exactly and invokes appropriate ’t Hooft limits for suppression of the omitted effects. The displayed integral is therefore not an unconditional exact finite-N formula for arbitrary BMN ground-state expectations.

Source: [1211.0364, introduction and §3.2](https://arxiv.org/html/1211.0364v2).

The 2017 M5 paper retains the instanton qualification, including a warning that unsuppressed instantons might invalidate its M2-limit computation. Removal by fermion zero modes is left for further analysis. More directly, §4.2 explains that interpreting the localized eigenvalue density as a full SO(6) scalar density would yield a \(\lambda^{1/2}\) second moment, conflicting with the \(\lambda^{2/3}\) scale discussed using Polchinski's bound. The proposed interpretation is instead low-energy/time-averaged moduli, with large noncommuting-mode contributions cancelling in protected complex combinations. That interpretation does not give upper bounds on full positive equal-time moments.

Source: [1711.07681, §§4.1, 4.2 after Eq. 4.12, and final paragraphs of §5](https://arxiv.org/html/1711.07681).

The 2023 NS5 analysis establishes its scaling limit in a specified planar quarter-BPS sector and supports nonplanar existence numerically. It does not establish the BFSS ground-state limit.

Source: [2211.13716 / PTEP 2023, abstract and §4](https://academic.oup.com/ptep/article/2023/4/043B01/7085765).

## 3. Exact positive-norm mismatch

The following is an independent algebraic derivation, not a claim from the cited papers.

Set \(T_{ij}=\operatorname{tr} Z_iZ_j\) and \(q_h=h_{ij}T_{ij}\). Assume \(h\) is real symmetric and traceless with \(\operatorname{Tr}_9h^2=1\). Let \(W\) be any nonnegative SO(9)-invariant coordinate observable, such as \(1\) or \(\rho^2\). In an SO(9)-invariant state, whenever the relevant moments exist,

\[
\langle W T_{ij}T_{kl}\rangle
=A_W\delta_{ij}\delta_{kl}
+B_W(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
\]

It follows that

\[
\langle Wq_h^2\rangle=2B_W.
\]

Choose \(u=e_1+ie_2\) and \(O=\operatorname{tr}(Z_1+iZ_2)^2=u_iu_jT_{ij}\). Since \(u\cdot u=0\) and \(u\cdot u^*=2\),

\[
\langle WO^2\rangle=0,\qquad
\langle WO^\dagger O\rangle=8B_W.
\]

Consequently,

\[
\boxed{\langle q_h^2\rangle=\tfrac14\langle O^\dagger O\rangle},\qquad
\boxed{\langle\rho^2q_h^2\rangle=\tfrac14\langle\rho^2O^\dagger O\rangle}.
\]

The needed quantity is a mixed positive norm, whereas the holomorphic square vanishes. The weighted holomorphic identity is used only to show the mismatch; \(\rho^2O^2\) is not asserted to be localized.

If \(h\) is an arbitrary real traceless matrix, only \(h_s=(h+h^T)/2\) contributes, and the displayed right-hand sides acquire a factor \(\|h_s\|_F^2\). The equality with factor one assumes symmetric unit norm.

At finite mass, the simpler identity is already decisive. Write \(O=A+iB\), with \(A=T_{11}-T_{22}\), \(B=2T_{12}\). Because equal-time coordinate functions commute,

\[
\operatorname{Re}\langle O^2\rangle=\langle A^2\rangle-\langle B^2\rangle,
\qquad
\langle O^\dagger O\rangle=\langle A^2\rangle+\langle B^2\rangle.
\]

Control of the difference gives no upper bound on the sum. A positive measure for the auxiliary localized matrix does not remove that distinction. At finite mass, the preserved SO(3)×SO(6) symmetry also does not identify all components of the SO(9) quadrupole; different subgroup representations must be handled separately.

### Information-theoretic counterexample

Take \(Z_i=R n_i A_0\), where \(n\) is uniform on \(S^8\), \(R\ge0\) is independent, and \(A_0\) is any fixed nonzero traceless Hermitian matrix. All positive-degree same-null-polarization holomorphic moments vanish, including products of holomorphic traces, but

\[
\langle q_h^2\rangle
=\frac{2}{99}(\operatorname{tr}A_0^2)^2\langle R^4\rangle
\]

is arbitrarily large as the radial law varies. A radial weight gives the analogous sixth-moment freedom. This is not a BFSS ground-state counterexample. It shows why the protected moments plus rotational invariance cannot logically supply the bound without additional dynamical input.

## 4. Recent mass-flow work does not protect a positive norm or control the zero-mass tail

The June 2026 preprint derives the formal relation

\[
Q(\mu)=M(\mu,\mu_0)Q(\mu_0)M(\mu,\mu_0)^{-1},
\quad M=e^{(\mu-\mu_0)\mathcal K},
\]

\[
\mathcal K=\frac{1}{6R}\operatorname{Tr}X_i^2
-\frac{1}{12R}\operatorname{Tr}X_a^2.
\]

Its explicit qualification is that \(M\) is unbounded and nonunitary. The Gaussian-domain comparison gives a local criterion

\[
|\mu-\mu_0|<\min(|\mu_0|,|\mu|).
\]

The argument excludes \(\mu=0\), where flat directions return and the Gaussian decay used in the argument disappears. The explicit normal-mode checks use large-mass harmonic wavefunctions, not nonperturbative wavefunctions at zero mass. Cohomology preservation is not preservation of a Hermitian inner product or of matrix elements of a real SO(6) \(20'\) operator. No positive-norm protection theorem or uniform weighted-tail bound needed for the proposed BFSS application is established by these results.

Source: [2606.05314, §3, Eqs. 3.3–3.8, and §4 introduction](https://arxiv.org/html/2606.05314v1).

Komatsu et al. discuss a BFSS-like bound branch among the BMN vacua as a physical scenario needing first-principles confirmation. This does not select or prove convergence of the required finite-N state family.

Source: [2401.16471, §3.3.1](https://arxiv.org/html/2401.16471).

## 5. What the route still requires

A successful BMN-to-BFSS upper-bound argument needs:

1. A correctly selected family of normalized BMN ground states with a justified BFSS limit, after removing the decoupled center of mass where appropriate
2. A genuine positive mixed-correlator or coercive estimate, uniform in the chosen mass/rank regime, for the needed real observable
3. A justified transfer of that bound to the limiting BFSS state

For a nonnegative observable, lower semicontinuity can transfer a proved uniform upper bound once the requisite state or probability-measure convergence is established. Equality/convergence of unbounded moments requires additional tail control. The protected holomorphic moment identities alone establish neither the uniform positive bound nor the necessary convergence.
