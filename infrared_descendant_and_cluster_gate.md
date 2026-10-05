# BFSS infrared gate: a fermionic certificate and a two-cluster calculation

Checked 2026-10-05. This note does not establish a rank-uniform BFSS threshold theorem. It identifies a simpler actual-Hamiltonian observable that would certify the desired estimate, computes the favorable leading free-channel power with its angular coefficient, and records the BFSS-specific missing ingredients.

## 1. Result first

The missing infrared bound is exactly a bound on the low-energy spectral weight of a **linear boson–fermion descendant**, not necessarily on a fourth position moment. In dimensionless 't Hooft variables define

\[
b_{h,\alpha}=N^{-1/2}\operatorname{Tr}(h_{ij}Z_i\Gamma^j_{\alpha\beta}\psi_\beta),\qquad
G_{N,h,\alpha}(t)=\langle b_{h,\alpha}\Omega_N,e^{-t\widehat H_N}b_{h,\alpha}\Omega_N\rangle.
\]

Here \(h=h^T\), \(\operatorname{Tr}_{9}h=0\), and \(\operatorname{Tr}_{9}h^2=1\). A sufficient, genuinely dynamical certificate is

\[
G_{N,h,\alpha}\!\left(\frac{N^{4/3}}{\delta_0\ell^2p^+}\right)=O(N^{-2/3}).
\]

A stronger but transparent sufficient condition is a uniform long-time bound \(G_N(t)\le C t^{-1/2}\), for \(t\ge1\). Its exponent \(1/2\) is the exact critical exponent for this sufficient route. Supersymmetry gives \(G_N(0)=a_N/2\); it does **not** establish the required decay.

In a leading free two-cluster channel the actual quadrupole source has a nonzero threshold coefficient and favorable powers

\[
F_v(\delta)\sim \frac{\sqrt2}{735\pi^5}\mu^{9/2}|A|^2\delta^{7/2},\qquad
W(\delta)\sim \frac{\sqrt2}{4620\pi^5}\mu^{9/2}|A|^2\delta^{11/2}.
\]

Neither the coefficient nor the energy interval on which this approximation holds is currently controlled uniformly in rank by the sources checked.

## 2. Exact descendant identity from the BFSS Hamiltonian

Use traceless generators \(\operatorname{Tr}T_AT_B=\delta_{AB}\), \([Z_i^A,P_j^B]=i\delta_{ij}\delta^{AB}\), \(\{\psi^A_\alpha,\psi^B_\beta\}=\delta^{AB}\delta_{\alpha\beta}\), and

\[
\widehat Q_\alpha=\operatorname{Tr}\left[N^{-1/2}P_i\Gamma^i_{\alpha\beta}\psi_\beta-
\frac{i\sqrt N}{2}[Z_i,Z_j]\Gamma^{ij}_{\alpha\beta}\psi_\beta\right].
\]

On gauge singlets, \(\widehat Q_\alpha^2=\widehat H\), with no sum on \(\alpha\). For \(q_h=N^{-1}\operatorname{Tr}(h_{ij}Z_iZ_j)\),

\[
[\widehat Q_\alpha,q_h]=-\frac{2i}{N^{3/2}}\operatorname{Tr}(h_{ij}Z_i\Gamma^j_{\alpha\beta}\psi_\beta)
=-\frac{2i}{N}b_{h,\alpha}.
\]

The commutator part of the supercharge is a multiplication operator and drops out. Let \(\chi=[\widehat Q_\alpha,q_h]\Omega\). Spectral commutation of \(\widehat Q_\alpha\) and \(\widehat H\) gives

\[
\|1_{(0,\varepsilon)}(\widehat H)\chi\|^2
=\int_{(0,\varepsilon)}e\,d\mu_q(e)
=\frac4{N^2}\|1_{(0,\varepsilon)}(\widehat H)b\Omega\|^2.
\]

This identity extends through compact position cutoffs under the finite-radius and quadratic-form assumptions of the existing gate note: \([Q,f_L]\Omega\) converges in Hilbert norm even if \(q\Omega\) does not. The limit is orthogonal to the entire zero-energy kernel. It has the same spectral measure as the homogeneous-energy-space vector \(\widehat H^{1/2}q\Omega\). Thus the displayed left side remains meaningful without pretending that \(d\mu_q\) exists as a finite measure.

There is an operator-level Clifford simplification:

\[
b_{h,\alpha}^2=\frac1{2N}\operatorname{Tr}(Z_i(h^2)_{ij}Z_j).
\]

Indeed the coordinate coefficients commute and \((\Gamma^i\Gamma^j)_{\alpha\alpha}=\delta_{ij}\). SO(9) invariance then gives

\[
\|b\Omega\|^2=a_N/2,\qquad \|\chi\|^2=2a_N/N^2.
\]

This shows explicitly why the elementary supersymmetric sum rule reproduces the radius Ward identity instead of improving it. Further positive energy moments of this descendant are higher moments of the same spectral measure; a suppression of its low-energy fraction remains dynamical information.

The Hamiltonian/supercharge conventions are those of [Lin–Zheng, Eqs. (3–5)](https://arxiv.org/html/2410.14647v3), after the 't Hooft rescaling. The formulas above are derived here, rather than quoted bounds from that work.

## 3. Positive Euclidean certificate at the exact required scale

For every \(t>0\), positivity implies

\[
\|1_{(0,\varepsilon)}(\widehat H)b\Omega\|^2\le e^{t\varepsilon}G_N(t).
\]

Choose \(\varepsilon_N=\delta_0\ell^2p^+N^{-4/3}\) and \(t=1/\varepsilon_N\). Then

\[
\int_0^{\varepsilon_N}e\,d\mu_q(e)\le\frac{4e}{N^2}G_N(1/\varepsilon_N).
\]

Thus the bound in §1 implies precisely \(O(N^{-8/3})\). It involves one positive correlator of a degree-two operator and bypasses a divergent equal-time quadrupole norm. If the uniform estimate \(G_N(t)\le Ct^{-1/2}\) holds for \(t\ge1\), then at sufficiently small fixed physical \(\delta\)

\[
\|1_{(0,\delta)}(H_{\rm phys})v_N\|^2
\le4eC(\ell^2p^+)^{3/2}\delta^{1/2},
\]

and consequently

\[
W_N(\delta)\le eC(\ell^2p^+)^{3/2}\delta^{5/2}.
\]

More generally a bound \(G_N(t)\le Ct^{-\beta}\) leaves the rank factor \(N^{(2-4\beta)/3}\). Hence \(\beta\ge1/2\) is sufficient; claiming a decay exponent without its uniform rank and time range would miss the main issue.

A resolvent alternative is \(K_N(s)=s\langle b\Omega,(\widehat H+s)^{-1}b\Omega\rangle\), since \(\|1_{(0,s)}b\Omega\|^2\le2K_N(s)\). A rigorous finite-N upper bound \(K_N(\varepsilon_N)=O(N^{-2/3})\) also suffices. This is a proposal for a non-polynomial spectral certificate, not an estimate already supplied by ordinary finite-level static moment bootstrap.

## 4. Actual leading two-cluster source

Consider a split into ranks \(n,m\), \(n+m=N\), with physical relative coordinate \(r=x_1-x_2\). The exact center-of-mass decomposition of the free channel gives

\[
\mu=\frac{nm}{NR}=\frac{p_1^+p_2^+}{p_1^++p_2^+},\qquad
H_{\rm rel}=-\frac{\Delta_r}{2\mu},\qquad O_{h,\rm rel}=\mu r^Thr.
\]

Normalize the reduced-channel tail by

\[
\Psi_{\rm tail}(r)=A\,\partial_i\partial_jG_9(r)|ij\rangle,\quad
G_9(r)=\frac{r^{-7}}{7|S^8|},\quad -\Delta G_9=\delta_0,
\]

where \(\langle ij|kl\rangle=\tfrac12(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})-\delta_{ij}\delta_{kl}/9\). This defines the convention for \(A\); it should not be equated numerically to coefficients in other wavefunction normalizations.

With unitary Fourier transform, the tail yields

\[
\widetilde{O_h\Psi}(k)\sim\frac{\mu A}{(2\pi)^{9/2}|k|^2}T_{ij}(\hat k)|ij\rangle,
\]

\[
T(n)=2h-4[(hn)n^T+n(hn)^T]+8(n^Thn)nn^T=2R_nhR_n,
\quad R_n=I-2nn^T.
\]

The reflection formula shows that \(T\) is symmetric traceless and \(\|T(n)\|_F^2=4\) for every direction. There is no angular cancellation of this leading quadrupole amplitude.

Integrating the free spectral shell gives

\[
\rho_O(E)=K\mu^{9/2}|A|^2E^{3/2},\qquad
K=\frac{2^{3/2}\,4|S^8|}{(2\pi)^9}=\frac{\sqrt2}{210\pi^5}.
\]

Therefore

\[
F_v(\delta)=\int_0^\delta E\rho_O(E)dE=\frac{2K}{7}\mu^{9/2}|A|^2\delta^{7/2},
\]

\[
W(\delta)=\frac14\int_0^\delta E^3\rho_O(E)dE=\frac{K}{22}\mu^{9/2}|A|^2\delta^{11/2},
\qquad \frac{W}{F_v}=\frac7{44}\delta^2.
\]

The tensor algebra, shell Jacobian, powers, and constants were checked symbolically and by a separate analytic check. The equalities for the density and moments refer to the pure leading homogeneous term. For a cut-off tail they are leading asymptotic formulas; in particular the ratio becomes \(7\delta^2/44\,[1+O(\delta)]\) at fixed channel parameters when \(A\ne0\). These are free-channel asymptotics, not a theorem about the full BFSS distorted spectral transform.

For an exact exterior tail cut off near the origin, the change in \(O\Psi\) is compactly supported and integrable, so its Fourier transform is bounded; it cannot cancel the \(|k|^{-2}\) coefficient. A subleading tail needs a quantitative decay/regularity bound before making the analogous claim. Most importantly, replacing the full interacting spectral transform by the free Fourier transform also needs proof.

## 5. What would actually close the cluster route

A sufficient all-rank theorem would combine:

1. A normalized, non-overcounting scattering-channel resolution or an equivalent quadratic-form inequality covering the relevant spectral subspace
2. Uniform low-energy distorted-wave matching of the quadrupole/descendant matrix element to the displayed tail, including threshold resonances and channel mixing
3. A bound on the physical weighted coefficient sum \(\sum_c\mu_c^{9/2}|A_c|^2\), or a direct integrated substitute, with a rank-independent energy window and a uniformly integrable remainder
4. Control of channels containing more than two clusters, including overlapping/nested threshold regions

If these hold with bounded sum and a suitable remainder, the favorable \(\delta^{7/2}\) localized-energy power closes the target. A two-cluster power count alone does not prove any of the four.

For canonical mass-normalized coordinates \(y=\sqrt\mu\,r\), the coefficient is \(B=\mu^{9/4}A\), so the required sum is simply \(\sum_c|B_c|^2\). This removes an apparent dependence on the mass convention; it does not bound the coefficients. In dimensionless coordinates \(y_0=\sqrt{nm/N}\,r/\ell\), a correspondingly normalized tail amplitude \(C_c\) obeys \(\mu_c^{9/2}|A_c|^2=\ell^9R^{-9/2}|C_c|^2\). At fixed \(p^+\), a sufficient coefficient condition becomes \(\sum_c|C_c|^2=O(N^{9/2})\), still accompanied by the uniform matching/onset requirement.

[Lin–Yin, Eq. (3.16) and the following paragraph](https://arxiv.org/pdf/1402.0055) gives the proposed \(r^{-9}\) two-cluster tail and explicitly leaves its two-body coefficients undetermined. Its asymptotic expression is not globally normalizable; normalization of the full state cannot by itself set all tail coefficients to one. This is a concrete BFSS-specific missing datum, beyond a generic moment-problem limitation. In the normalization above an exact exterior tail beyond radius \(L\) has probability \(8|A|^2/(|S^8|L^9)\). Normalization therefore bounds \(|A|^2\) only by a constant times the ninth power of the unknown onset radius. It cannot supply the required uniform amplitude bound without quantitative onset control. Channel quotient measures and multiplicities must also be fixed consistently.

## 6. Literature update relevant to an executable next step

- [Lin–Zheng, 2410.14647v3](https://arxiv.org/html/2410.14647v3): the updated genuine BFSS result remains an infinite-N static bootstrap and does not supply the finite-N upper control needed here
- [Bootstrapping Euclidean Two-point Correlators, 2511.08560v2](https://arxiv.org/html/2511.08560v2): provides a relevant methodology, but its worked model is ungauged one-matrix quantum mechanics; BFSS applications are future work. It does not prove the §3 certificate
- [Biggs–Herderschee, 2503.14685v2, Eqs. (2–3)](https://arxiv.org/html/2503.14685v2#S1): the stated IIA window implies dimensionless separations much smaller than \(N^{10/21}\). The present certificate probes \(N^{4/3}\), well outside it
- [Hanada et al., 1108.5153, Eqs. (3.8),(3.16), Appendix A](https://arxiv.org/pdf/1108.5153): the holographic \(T^{++}_{\ell=2}\) behavior formally corresponds to \(d\mu_q(E)\propto E^{-6/5}dE\). Its infrared Fourier transform requires analytic continuation; it is not a finite positive equal-time ground-state measure. Weighting by \(E\) would give the promising exponent \(G_b(t)\propto t^{-4/5}\), but extending that behavior uniformly to \(t\sim N^{4/3}\) is precisely unproved
- [Hasler–Hoppe, hep-th/0206043](https://arxiv.org/pdf/hep-th/0206043): asymptotic factorization when eigenvalues are widely separated is not a bound on the all-rank threshold coefficients or onset

## 7. Recommendation and stopping point

The sharper next certificate is the positive fermionic two-point function in §3, retaining finite-N double traces and taking time \(t_N\sim N^{4/3}\) explicitly. A calculation at fixed time followed by assumed planar factorization does not address it. The analytic alternative is a uniform cluster-threshold theorem with the coefficient sum and remainder specified in §5.

No rank-uniform upper bound, no exact BFSS threshold law, no nonzero-longitudinal/rank-changing source identity, and no full soft theorem have been proved in this pass. The positive result is an exact lower-complexity observable for the missing estimate, plus a nonvanishing and favorable source-specific leading channel calculation that identifies exactly what a BFSS proof must supply.
