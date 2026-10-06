# BFSS weighted-quadrupole estimate: actual-Hamiltonian route audit

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


6 October 2026. This note does not prove or disprove the requested rank-uniform ground-state estimate. It identifies the exact unsupplied sign in a localized Ward identity, and proves why two natural source-energy routes do not automatically supply it. No finite-rank Hardy claim is used.

## Target and conventions

Write

\[
H=T+V+F=\frac1{2N}\operatorname{Tr}P^2
-\frac N4\operatorname{Tr}[Z_i,Z_j]^2
-\frac12\operatorname{Tr}\psi\Gamma^i[Z_i,\psi],
\]

on the physical SU(N)-singlet Hilbert space. Let \(\Omega_N\) be a normalized Spin(9)-singlet zero mode. Set \(\operatorname{tr}=\operatorname{Tr}/N\),

\[
q=\operatorname{tr}(h_{ij}Z_iZ_j),\quad
a=\operatorname{tr}(Z_i(h^2)_{ij}Z_j),\quad
c=\operatorname{tr}(Z_i(h^3)_{ij}Z_j),
\]

where \(h\) is real symmetric traceless and \(\operatorname{Tr}_9 h^2=1\). The open target is

\[
\mathbb E_N[a\,\mathbf1_{|q|>\kappa N^{-2/3}}]\le C N^{-2/3}.
\]

The existing clipping certificate then gives the desired resolvent-source estimate at \(s\asymp N^{-4/3}\). The certificate itself does not prove the concentration assumption.

## 1. The nonlinear shear Ward identity and its missing sign

Use raw real color coordinates \(Z_i^A\), let \(d=N^2-1\), and put

\[
u_{iA}=h_{ij}Z_j^A,\qquad
v=f(q)u,\qquad
A_v=\tfrac12(v\cdot P+P\cdot v).
\]

For smooth cutoffs for which the commutators are defined, stationarity gives the exact identity

\[
0=\left\langle
\frac1N P\cdot f(q)hP
+\frac2{N^2}P\cdot f'(q)uu^T P
-f(q)\,\delta_h(V+F)
-\frac1{N^2}\left[d f'(q)+4c f''(q)+2a^2 f'''(q)\right]
\right\rangle.
\tag{1}
\]

Here \(h\) acts on the spatial index and as the identity on color, \(\delta_h=u\cdot\nabla\), and all kinetic terms are in their displayed divergence-form ordering. Removing radial cutoffs requires convergence of the corresponding weighted kinetic and potential integrals; finite \(\mathbb E\rho^2\) alone does not justify every term of (1).

The coefficient check is elementary:

\[
\nabla q=2u/N,\quad |\nabla q|^2=4a/N,\quad
\Delta q=0,\quad \Delta a=2d/N,\quad
\nabla a\cdot\nabla q=4c/N.
\]

Thus \(\operatorname{div}v=2af'\) and

\[
\Delta\operatorname{div}v=
\frac4N[df'+4cf''+2a^2f'''].
\]

Combining these with

\[
i[T,A_v]=N^{-1}P\cdot(\nabla v)_{\rm sym}P
-(4N)^{-1}\Delta\operatorname{div}v,
\qquad i[V+F,A_v]=-v\cdot\nabla(V+F)
\]

proves (1).

For \(f'\ge0\), the \(uu^T\) kinetic term is positive. The term with \(f h\) is indefinite, however, and so is the weighted shear stress \(f\delta_h(V+F)\). Neither virial nor Spin(9) invariance provides the sign of their localized expectations. The derivative correction cannot generally repair those terms.

A concrete bosonic configuration rules out the tempting pointwise inequality \(q\delta_h V\ge0\). In SU(3), take

\[
Z_1=R\operatorname{diag}(1,1,-2),\quad
Z_2=\operatorname{diag}(\sigma_1,0),\quad
Z_3=\operatorname{diag}(\sigma_2,0),\quad Z_{4,\ldots,9}=0,
\]

and \(h=\operatorname{diag}(8,-1,\ldots,-1)/\sqrt{72}\). The large first matrix commutes with the others; only \([Z_2,Z_3]\) contributes to \(V>0\). For large \(R\), \(q>0\), whereas

\[
\delta_h V=2(h_2+h_3)V<0.
\]

This is a counterexample to that pointwise sign, not a BFSS ground-state counterexample. Closing (1) would require a genuinely new ground-state weighted-stress estimate.

## 2. Linear and bounded tail sources

### Proposition: the unstabilized quadratic source is unstable

For every fixed \(N\ge2\), nonzero normalized traceless \(h\), and real \(J\ne0\), the quadratic form \(H-Jq\) on physical gauge-singlet states is unbounded below.

Choose a unit eigenvector \(e\) of \(h\) with \(J(e^The)>0\), and a fixed regular traceless diagonal matrix \(A\). Around the compact gauge orbit of the commuting configuration

\[
Z_i=R e_i A
\]

choose normalized smooth gauge-invariant packets supported in tubes of transverse width \(\delta_R=R^{-1/2}\). Such packets can be constructed from smooth normal-coordinate cutoffs on the orbit; the orbit geometry is the dilation by \(R\) of a fixed compact homogeneous space. Multiply by any fixed normalized gauge-singlet fermionic state. At fixed \(N\),

\[
\langle T\rangle=O_N(\delta_R^{-2})=O_N(R),
\]

\[
\langle V\rangle=O_N(R^2\delta_R^2+\delta_R^4)=O_N(R),
\qquad |\langle F\rangle|=O_N(R+\delta_R),
\]

where the fermionic estimate follows because the fermion Hilbert space is finite dimensional and its potential is linear in \(Z\). Meanwhile

\[
\langle q\rangle
=R^2(e^The)\operatorname{tr}A^2+O_N(R\delta_R+\delta_R^2).
\]

Therefore \(\langle H-Jq\rangle\to-\infty\). No Born–Oppenheimer expansion or zero-mode existence is used in this proof.

The same construction shows that for fixed \(L\),

\[
H-t\,a\mathbf1_{|q|>L}
\]

is unbounded below for every \(t>0\). In particular, an all-state coercive form inequality of the type

\[
a\mathbf1_{|q|>L}\le C+\varepsilon H
\]

is false even at a fixed rank. This does not rule out an estimate in the specific zero mode.

### Bounded-source version: the needed inequality points the right way but is trivial at infinity

If \(0\le W\le1\), then a lower bound

\[
\inf\operatorname{spec}(H-tW)\ge-t\eta
\]

would imply \(\langle\Omega_N,W\Omega_N\rangle\le\eta\), by testing the lower bound on \(\Omega_N\). Thus the sign of this strategy is correct.

For the natural bounded tail observable

\[
W_L=\frac a{1+a}\,\chi_L(q),
\]

with \(0\le\chi_L\le1\) equal to one outside \(|q|\ge2L\), however, \(W_L\to1\) in open commuting escape cones. Standard BFSS zero-energy escape packets in those cones give

\[
\inf\operatorname{spec}(H-tW_L)=-t.
\tag{2}
\]

The lower inequality is immediate from \(H\ge0\). The upper inequality uses the same separated-eigenvalue low-energy packets as in the continuous-spectrum construction, supported in a fixed angular cone; their angular kinetic cost vanishes at large radius. Unlike the previous proposition, (2) uses supersymmetric cancellation in the escape construction. It is not inferred from the merely \(O(R)\)-energy packets above.

Equation (2) yields only \(\langle W_L\rangle\le1\). Moreover, \(W_L<1\) at every finite configuration, so the spectral bottom \(-t\) is not attained by a normalized state: equality would require both \(H\Psi=0\) and \((1-W_L)^{1/2}\Psi=0\). Thus the energy derivative at \(t=0+\) is \(-1\), whereas the expectation in any normalized zero mode is strictly greater than \(-1\). Applying the ordinary isolated-eigenvalue Hellmann–Feynman theorem at this threshold would be wrong even for this bounded source.

An isotropic regulator also exposes the noncommuting limits. For \(H+\varepsilon\rho^2-tW_L\), taking \(\varepsilon\downarrow0\) at fixed \(t>0\) gives spectral bottom \(-t\): the lower bound is immediate, and each fixed escape packet supplies the upper bound before its radius is sent to infinity. The limit selects the escaping sector, not the normalized threshold zero mode. A compact radial cutoff removes this particular escape obstruction, but controlling its removal uniformly in \(N\) is an additional ground-state tail problem.

The standard physical low-energy escape construction is the one underlying [de Wit–Lüscher–Nicolai, *The Supermembrane Is Unstable*](https://doi.org/10.1016/0550-3213(89)90214-9). The source perturbations and derivative conclusion above are direct deductions, not claims attributed to that paper.

## 3. Positive regulator and susceptibility: what would actually suffice

Consider the explicitly different Hamiltonian

\[
H_{\varepsilon,J}=H+\varepsilon\rho^2-Jq,
\qquad \rho^2=\operatorname{tr}\sum_i Z_i^2.
\]

For \(|J|\|h\|_{\rm op}<\varepsilon\), the added quadratic form is positive, so the source family is stable. This is an ordinary positive mass regulator, not the supersymmetric BMN deformation. Its stable source interval collapses when \(\varepsilon\downarrow0\).

Suppose, at a fixed \(\varepsilon,N\), its \(J=0\) ground state is isolated and nondegenerate and the differentiations are justified. With \(E_\varepsilon(J)\) its ground energy and the inverse on the orthogonal complement,

\[
\chi_{\varepsilon,N}:=-E_\varepsilon''(0)
=2\langle q\Omega_{\varepsilon,N},
(H_{\varepsilon,0}-E_\varepsilon(0))^{-1}
q\Omega_{\varepsilon,N}\rangle.
\tag{3}
\]

Spin(9) gives \(\langle q\rangle=0\). The unchanged kinetic double commutator gives the exact f-sum rule

\[
\langle q\Omega_{\varepsilon,N},
(H_{\varepsilon,0}-E_\varepsilon(0))q\Omega_{\varepsilon,N}\rangle
=2\langle a\rangle_{\varepsilon,N}/N^2.
\]

Cauchy–Schwarz in the spectral measure then gives an upper variance inequality,

\[
\operatorname{Var}_{\varepsilon,N}(q)^2
\le \frac{\langle a\rangle_{\varepsilon,N}}{N^2}
\chi_{\varepsilon,N}.
\tag{4}
\]

Consequently uniform bounds \(\langle a\rangle=O(1)\), \(\chi_{\varepsilon,N}=O(N^{-2/3})\), together with valid regulator removal, would suffice for the older variance route \(\operatorname{Var}_N(q)=O(N^{-4/3})\).

Neither stability nor concavity of \(E_\varepsilon(J)\) supplies the susceptibility upper bound. Secant differences control averages of \(-E''\), not its value at zero, and the available source interval has width \(O(\varepsilon)\). A spectral-gap estimate at fixed regulator also degenerates upon removal. Thus (4) identifies a genuine upper-bound route, but does not close it; claiming otherwise would replace one unproved uniform infrared estimate with another.

### Recoverable part: fixed-rank removal needs no fourth-moment convergence

Assume separately that, at each fixed \(N\), the physical zero eigenspace is one dimensional and its normalized vector \(\Omega_N\) has finite \(M_N=\langle\rho^2\rangle_{\Omega_N}\). This is a stated extra hypothesis, not a theorem proved here. Let \(\Omega_{\varepsilon,N}\) be a normalized ground state of \(H+\varepsilon\rho^2\). Its spectrum is discrete: at fixed \(N\), the fermionic potential is bounded below by \(-C_N\rho\), while the positive quadratic term confines.

The variational principle and \(H\ge0\) give

\[
0\le E_{\varepsilon,N}\le\varepsilon M_N,\qquad
\langle\rho^2\rangle_{\varepsilon,N}\le M_N,\qquad
\|Q_\alpha\Omega_{\varepsilon,N}\|^2
=\langle H\rangle_{\varepsilon,N}\le\varepsilon M_N.
\tag{5}
\]

The second bound makes the family tight in configuration space. On every compact set, the first-order elliptic estimate for \(Q_\alpha\) gives a uniform local \(H^1\) bound, because \(Q_\alpha\)'s principal symbol squares to \(|\xi|^2/(2N)\). Rellich compactness and tightness yield a strongly \(L^2\)-convergent subsequence with norm-one limit. Closedness of \(Q_\alpha\), using the last bound in (5), puts the limit in the zero eigenspace. Uniqueness identifies it with \(\Omega_N\) up to phase. Hence the full family converges after phases are fixed.

The same argument applied to two orthogonal regulated ground states shows that the regulated ground level is nondegenerate for all sufficiently small \(\varepsilon\) at this fixed \(N\): otherwise subsequences of two orthogonal vectors would both converge into a one-dimensional kernel. Spin(9) invariance then makes this ground state a singlet. The required smallness threshold may depend on \(N\).

Now suppose one can prove, for \(0<\varepsilon<\varepsilon_0(N)\) with a constant \(C\) independent of \(N\),

\[
\langle a\rangle_{\varepsilon,N}\,
\chi_{\varepsilon,N}\le C N^{-2/3}.
\tag{6}
\]

Equation (4) gives \(\langle q^2\rangle_{\varepsilon,N}\le\sqrt C\,N^{-4/3}\). Strong convergence and Fatou, or bounded multiplication by \(\min(q^2,M)\) followed by \(M\to\infty\), transfer exactly the same upper bound to \(\Omega_N\). No uniform rate of convergence in \(N\), and no pre-existing fourth moment of \(\Omega_N\), are needed; one first removes \(\varepsilon\) at each fixed rank.

Under uniqueness and the second moment, regulator removal is therefore recoverable. The unproved quantitative input is (6), not a blanket requirement to control every regulator limit. This does not rescue the fixed-negative-bounded-source limit in section 2, which follows a different order of perturbations and selects the escape sector. Condition (6) is only sufficient and may be stronger than the original variance or clipping target: the inverse energy in \(\chi\) amplifies exceptionally low-energy spectral weight. No claim is made that proving it is easier.

## 4. Known shear sum rules are not an independent closure

For

\[
D_h=\tfrac12\sum_{i,j,A}h_{ij}(Z_i^A P_j^A+P_j^A Z_i^A),
\]

the previously used identities are

\[
[H,q]=-2iD_h/N^2,\qquad [D_h,q]=-2ia.
\]

Under the virial and commutator domain hypotheses,

\[
\langle[D_h,[H,D_h]]\rangle=\langle T\rangle.
\]

For the spectral measure of \(q\Omega_N\), this gives

\[
m_1=2\langle a\rangle/N^2,\qquad m_3=2\langle T\rangle/N^4.
\]

These are the descendant-shifted version of the source second-moment identity already present in the project, not a new independent input. Hölder gives

\[
\operatorname{Var}(q)=m_0\ge
\frac{m_1^{3/2}}{m_3^{1/2}}
=\frac{2\langle a\rangle^{3/2}}{N\sqrt{\langle T\rangle}}.
\]

The direction is a lower bound. No upper tail estimate follows from these moments alone.

The elementary supersymmetry enlargement does not add an independent constraint. With \(b_\alpha=(iN/2)[Q_\alpha,q]\), one has on the physical sector

\[
\{Q_\alpha,b_\alpha\}=D_h/N,\quad
\{b_\alpha,b_\beta\}=a\delta_{\alpha\beta},\quad
\{Q_\alpha,b_\alpha f(q)\}=\{f(q),D_h\}/(2N).
\]

Thus these scalar dressings return to the same shear family. Including the radial companion \(b_0\) gives \(\{b_0,b_h\}=q\) and only \(q^2\le\rho^2a\). No claim is made that all higher-degree fermionic bootstrap identities have been exhausted.

## 5. Primary-literature check: no established planar variance rate

Lin–Zheng explicitly impose factorization and discuss low-energy intermediate-state and regulator-order loopholes. Their work does not prove finite-rank \(O(N^{-2})\) quadrupole variance. See [2410.14647, section 4](https://arxiv.org/html/2410.14647v2#S4). Lin's earlier bounds constrain mainly one-point moments from below: [2302.04416](https://arxiv.org/abs/2302.04416).

The directly relevant off-diagonal operator in [1108.5153](https://arxiv.org/html/1108.5153) is \(T^{++}_{2,12}=\operatorname{Tr}(X_1X_2)/N\), at \(\lambda=1\). Taking \(h_{12}=h_{21}=1/\sqrt2\) gives \(q_h=\sqrt2 T^{++}_{2,12}\). Its reported \(|p|^{-6/5}\) frequency law is not an equal-time large-rank variance measurement. The simulations use \(N=2,3\), finite Euclidean period, phase quenching, and an explicit radial cutoff (Appendix B, equation 102). The paper itself flags the infrared nonintegrability of the quadrupole inverse Fourier transform.

Conditional holographic power counting gives

\[
G_{h,N}(p)\sim A_hN^{-2}|p|^{-6/5},
\qquad N^{-10/21}\ll |p|\ll1.
\]

A dyadic band \([\eta,2\eta]\) would contribute order \(N^{-2}\eta^{-1/5}\) to equal-time variance. At \(\eta=N^{-\alpha}\), \(0<\alpha<10/21\), the power is \(N^{-2+\alpha/5}\). The formal endpoint power is \(N^{-40/21}\), smaller than \(N^{-4/3}\); reaching the latter by this extrapolation requires \(\eta\sim N^{-10/3}\), outside the IIA window. Thus this evidence does not contradict the desired estimate.

There is also a useful conditional caution. If the genuine positive ground-state Fourier correlators obeyed

\[
N^2G_{h,N}(p)\longrightarrow A_h|p|^{-6/5}
\]

for arbitrarily small fixed \(p>0\), then positivity and Fatou would imply \(\liminf N^2\operatorname{Var}(q_h)=\infty\). This rules out a strict uniform planar equal-time bound under that extra assumption, but gives neither the corrected rank exponent nor a contradiction to the weaker target.

[2503.14685v2, section 2.1](https://arxiv.org/html/2503.14685v2#S2.SS1) explicitly distinguishes its IIA double-scaling regime from exact finite-rank ground-state projection. [Lin–Yin, 1402.0055, equations 3.10–3.16](https://arxiv.org/html/1402.0055#S3) leave the cluster-tail normalization coefficients undetermined. Their spatial falloff therefore cannot supply a uniform rank coefficient here.

## Conclusion

The concentration gate remains open. The nonlinear Ward identity has an uncontrolled weighted-stress sign. Unstabilized unbounded tail sources are unbounded below; natural bounded tail sources saturate on the continuum escape channels. The stabilized susceptibility inequality is valid, and its fixed-rank regulator removal is justified above assuming uniqueness and a finite second moment, but its rank-uniform susceptibility product bound is unproved. None of these observations is a counterexample to the estimate in the actual normalized BFSS zero mode.

The minimum genuinely new input must distinguish that zero mode from the escaping threshold sector and quantitatively control its anisotropic fluctuations. A proved uniform susceptibility estimate with regulator removal, a direct localized weighted-stress certificate, or a verified finite-rank bootstrap dual bound could supply it. Naming any of those requirements is not a solution.
