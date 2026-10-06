# BFSS source control by bounded quadrupole clipping

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


Research checkpoint, 6 October 2026. This is a conditional reduction for the actual finite-rank BFSS Hamiltonian, with an independently checked radial-ansatz obstruction. It is not a rank-uniform BFSS estimate, a proof of a soft theorem, or a priority claim.

## Outcome

An additional sufficient criterion, distinct from the previously explored full quadrupole variance and radial-cutoff estimates, comes from a bounded, quadrupole-dependent supercharge primitive:

\[
K_N(s)\leq \frac12\mathbb E_N\!\left[a_h\,\mathbf1_{\{|q_h|>L\}}\right]+sN^2L^2.
\tag{1}
\]

Here \(q_h=\operatorname{tr}(h_{ij}Z_iZ_j)\), \(a_h=\operatorname{tr}(Z_i(h^2)_{ij}Z_j)\), and \(\mathbb E_N\) is the bosonic configuration probability in a normalized singlet zero mode. Consequently, at \(s=N^{-4/3}\), it is sufficient to prove

\[
\mathbb E_N\!\left[a_h\,\mathbf1_{\{|q_h|>\kappa N^{-2/3}\}}\right]
=O(N^{-2/3}).
\tag{2}
\]

This concentration statement is not proved here. Unlike the full-norm quadrupole route, (1) is valid under only a finite second radial moment and need not assume a fourth radial moment. Its target controls the gradient-weighted probability of anisotropic configurations, rather than their full quadratic amplitude. It can therefore tolerate rare large quadrupole excursions whose fourth-moment contribution is uncontrolled.

No result below changes the current/source convention, supplies a nonzero-longitudinal-momentum source, or identifies an off-shell source correlator with an invariant physical discontinuity.

## 1. Actual-Hamiltonian assumptions and normalization

Use the physical gauge-singlet Hilbert space at a fixed rank \(N\), with generators normalized by \(\operatorname{Tr}T_AT_B=\delta_{AB}\), \([Z_i^A,P_j^B]=i\delta_{ij}\delta^{AB}\), and \(\{\psi_\alpha^A,\psi_\beta^B\}=\delta_{\alpha\beta}\delta^{AB}\). Fix a single real spinor component \(\alpha\). The dimensionless charge is

\[
Q_\alpha=\operatorname{Tr}\left[N^{-1/2}P_i\Gamma^i_{\alpha\beta}\psi_\beta
-\frac{i\sqrt N}{2}[Z_i,Z_j]\Gamma^{ij}_{\alpha\beta}\psi_\beta\right],
\qquad Q_\alpha^2=\widehat H_N.
\]

The charge is taken in the standard compatible self-adjoint realization. Let \(\Omega_N\in D(Q_\alpha)\) be a normalized gauge- and Spin(9)-invariant zero mode, \(Q_\alpha\Omega_N=0\). Assume

\[
\mathbb E_N\rho^2<\infty,\qquad \rho^2=\operatorname{tr}\sum_i Z_i^2,\quad \operatorname{tr}=N^{-1}\operatorname{Tr}.
\]

Existence and this moment assumption are not established in this note. In particular, the candidate exterior-Hardy manuscript is not silently promoted to an established theorem. Smooth gauge-invariant bounded multipliers with bounded derivatives are assumed to preserve the charge domain, as follows from the usual first-order differential realization and core approximation.

Take real symmetric traceless \(h\) with \(\operatorname{Tr}_9h^2=1\), and define

\[
b=N^{-1/2}\operatorname{Tr}(h_{ij}Z_i\Gamma^j_{\alpha\beta}\psi_\beta),
\qquad w=b\Omega_N,
\qquad K_N(s)=s\langle w,(\widehat H_N+s)^{-1}w\rangle.
\]

Then \([Q_\alpha,q_h]=-2ib/N\), and the Clifford relations give \(b^2=a_h/2\). In particular \(w\) exists under the second-moment assumption. All constants below are for one component; a sum over all 16 components multiplies the corresponding estimates by 16.

These conventions are obtained by the usual 't Hooft rescaling of [Lin–Zheng, equations (3)–(5)](https://arxiv.org/html/2410.14647v2). The descendant identity itself was already derived in this project's earlier `infrared_descendant_and_cluster_gate` calculation and is not new here.

### Physical scaling and the rank-dependent coupling

Let \(x_i\) be physical transverse matrices, \(R\) the lightlike compactification radius, and \(\ell\) a fixed length convention. The bosonic physical Hamiltonian is

\[
H_{\rm phys,b}=\frac R2\operatorname{Tr}P_x^2-\frac{R}{4\ell^6}\operatorname{Tr}[x_i,x_j]^2.
\]

Set \(Y=(R/\ell^3)x\), \(g^2=R^3/\ell^6\), \(\lambda=g^2N\), and

\[
Z=\lambda^{-1/3}Y=\frac{x}{\ell N^{1/3}},\qquad
\widehat H_N=H_{\rm phys}/\Lambda_N,\qquad
\Lambda_N=\lambda^{1/3}=\frac{R N^{1/3}}{\ell^2}.
\]

In the variables used above, with canonical unrescaled Majoranas,

\[
\widehat H_N=\frac12\operatorname{Tr}\left[N^{-1}P_Z^2-\frac N2[Z_i,Z_j]^2-\psi\Gamma^i[Z_i,\psi]\right].
\]

Decompactification at fixed hard longitudinal momentum \(p^+\) means \(R=N/p^+\). Consequently

\[
g^2(N)=\frac{N^3}{(p^+)^3\ell^6},\quad
\lambda(N)=\frac{N^4}{(p^+)^3\ell^6},\quad
\Lambda_N=\frac{N^{4/3}}{\ell^2p^+},\quad
s=\frac{\delta}{\Lambda_N}=\delta\ell^2p^+N^{-4/3}.
\]

Thus this is not a fixed-physical-coupling large-rank limit. Factoring out \(\Lambda_N\) leaves the displayed dimensionless Hamiltonian, still with explicit \(N\)-dependent coefficients. \(\Omega_N\) is the unitary rescaling of a physical zero mode and remains norm one. \(h\) is fixed, real, symmetric, traceless, and has \(\operatorname{Tr}_9h^2=1\), independent of \(N\). Both \(q_h=N^{-1}\operatorname{Tr}(hZZ)\) and \(a_h=N^{-1}\operatorname{Tr}(Zh^2Z)\) are dimensionless. No normalization was chosen to force the desired rank power.

## 2. Exact supercharge variational certificate

For every self-adjoint \(Q\), every \(w\) in Hilbert space, and \(s>0\),

\[
s\langle w,(Q^2+s)^{-1}w\rangle
=\inf_{v\in D(Q)}\bigl\{\|w-Qv\|^2+s\|v\|^2\bigr\}.
\tag{3}
\]

Proof: the minimizer is \(v_*=Q(Q^2+s)^{-1}w\in D(Q)\). Subtracting its objective leaves \(\|(Q^2+s)^{1/2}(v-v_*)\|^2\). The identity includes any zero-energy component of \(w\); no division by \(Q\) or spectral gap is required.

For any real gauge-invariant smooth scalar \(F(Z)\) such that \(F\Omega_N\in D(Q)\), set \(v=iNF\Omega_N/2\). Since the interaction term of \(Q\) commutes with scalar multiplication,

\[
Qv=\frac{\sqrt N}{2}\,\partial_{iA}F\,\Gamma^i_{\alpha\beta}\psi_\beta^A\Omega_N.
\]

All coefficients in the remaining linear Majorana operator are real and commuting. Its square is one half their Euclidean squared norm. Hence its objective is exactly

\[
J_{N,s}[F]=\frac N8\mathbb E_N|\nabla(q_h-F)|^2
+\frac{sN^2}{4}\mathbb E_NF^2,
\qquad K_N(s)\le J_{N,s}[F].
\tag{4}
\]

There is no fermion-sign assumption, classical replacement of the Hamiltonian, or Born–Oppenheimer approximation in (4). It is an upper certificate obtained by restricting the variational space in (3). Equality after restriction is not claimed.

The precise capacity target tested here is to find \(F_N\) for which

\[
\mathbb E_N|\nabla(q_h-F_N)|^2=O(N^{-5/3}),
\qquad \mathbb E_NF_N^2=O(N^{-4/3}).
\tag{5}
\]

At \(s=N^{-4/3}\), (5) gives \(J=O(N^{-2/3})\). The first exponent uses the raw color-coordinate gradient; in the ground-state energy form \(\mathcal E_N(F)=\mathbb E_N|\nabla F|^2/(2N)\), the first requirement is \(\mathcal E_N(q_h-F_N)=O(N^{-8/3})\).

If \(q_h\) also has finite Hilbert norm, the scalar-multiplier Dirichlet form defines a nonnegative operator \(L_N\) by closure, and the unrestricted scalar infimum is

\[
\inf_F J_{N,s}[F]=\frac{N^2}{4}s\langle q_h,L_N(L_N+s)^{-1}q_h\rangle_{L^2(\mathbb P_N)}.
\]

This optional expression is not needed for (1), and is not a claim that \(L_N\) equals the full BFSS Hamiltonian. The latter generally does not preserve scalar multiples of \(\Omega_N\).

## 3. Bounded quadrupole clipping, with no fourth moment

Choose a smooth real function \(T_L\) with

\[
T_L(x)=x\ \text{for }|x|\le L,\qquad 0\le T'_L\le1,
\qquad |T_L|\le2L.
\]

It can be made constant outside \(|x|\ge2L\). Put \(F=T_L(q_h)\). Then

\[
|\nabla(q_h-F)|^2=(1-T'_L(q_h))^2|\nabla q_h|^2,
\qquad |\nabla q_h|^2=4a_h/N.
\]

Substitution in (4) proves (1). It also gives the slightly sharper exact expression

\[
J_{N,s}[T_L(q_h)]=\tfrac12\mathbb E_N[a_h(1-T'_L(q_h))^2]
+\tfrac{sN^2}{4}\mathbb E_N[T_L(q_h)^2].
\]

Domain justification: approximate \(T_L(q_h)\) by \(\chi(\rho/R)T_L(q_h)\). The multipliers converge in Hilbert norm because they are uniformly bounded. The main charge commutator is dominated by a constant times \(\rho\), which is square integrable by assumption. The cutoff commutator is bounded in norm by a constant times \(L/(NR)\). Closedness of \(Q\) supplies the limit in its graph norm. Thus an unproved fourth-moment assertion is not smuggled into the construction.

Because \(a_h\le\rho^2\), the stronger, simpler condition

\[
\mathbb E_N[\rho^2\mathbf1_{\{|q_h|>\kappa N^{-2/3}\}}]=O(N^{-2/3})
\]

also suffices. Proving such an estimate is a genuine ground-state concentration problem. Neither Spin(9) invariance nor ordinary finite-rank moment finiteness proves it. It is an alternative sufficient target, not asserted to be logically weaker than every full-variance hypothesis.

A bound for each member of a fixed orthonormal 44-polarization basis yields a bound for arbitrary unit real \(h\) by the positivity and finite dimension of the source Gram matrix, with at most a fixed factor 44. No rank-dependent angular net is needed.

### Comparison with the old spin-2 variance condition

The previous sufficient condition was \(V_N:=\mathbb E_Nq_h^2=O(N^{-4/3})\). Where this norm exists, the choice \(F=q_h\), justified by approximation, gives directly \(K_N(s)\le sN^2V_N/4\). The full scalar variational formulation therefore includes the old route.

The particular fixed-threshold tail condition (2), however, is **not established to be weaker than** that variance condition. At the level of finite-moment Spin(9)-invariant configuration measures, neither condition implies the other. This remains true with a uniformly bounded radius:

1. Variance need not imply (2). Take a spatial Gram matrix \(M=mI_9+N^{-2/3}X_N RAR^T\), with fixed nonzero traceless symmetric \(A\), Haar-distributed \(R\in SO(9)\), and \(X_N\) a positive unbounded finite-second-moment variable truncated only to maintain \(M\ge0\). For example, start from an exponential random variable and truncate at a constant times \(N^{2/3}\). Then \(\rho^2=9m\), \(V_N=O(N^{-4/3})\), and \(a_h\) stays order one. For every fixed \(\kappa\), the probability that \(|q_h|>\kappa N^{-2/3}\) tends to a positive number, so its \(a_h\)-weighted tail is not \(O(N^{-2/3})\).
2. Condition (2) need not imply the variance rate. Mix the isotropic Gram matrix \(mI_9\) with probability \(1-N^{-2/3}\) and a fixed anisotropic rotational orbit \(mI_9+\eta RAR^T\) with probability \(N^{-2/3}\), taking \(\eta\) small enough for positivity. The weighted tail is \(O(N^{-2/3})\), but \(V_N\asymp N^{-2/3}\).

These are kinematically admissible Gram-matrix probability laws for \(N\ge4\), not proposed BFSS zero modes or counterexamples to any BFSS theorem. Their only role is to prohibit an unsupported logical comparison based on symmetry and positivity alone. Smoothing the laws does not change the scaling examples.

A stronger familiar concentration hypothesis can imply (2): Markov's inequality gives

\[
\mathbb E_N[a_h\mathbf1_{\{|q_h|>L\}}]\le L^{-2}\mathbb E_N[a_hq_h^2].
\]

Therefore the weighted planar-rate estimate \(\mathbb E_N[a_hq_h^2]=O(N^{-2})\) suffices. This is a sixth-degree mixed moment with an unproved uniform coefficient, not a result supplied by finite-rank moment finiteness. Similarly, an actual uniform bound on \(a_h\) together with the stronger planar variance \(V_N=O(N^{-2})\) would suffice. Neither stronger input is assumed in the clipping lemma.

### Basic virial and rotational plausibility checks

Spin(9) invariance gives \(\mathbb E_N q_h=0\), \(\mathbb E_Na_h=\mathbb E_N\rho^2/9\), and the exact traceless-Gram identity (6). The ground-state virial identities, under their integration-by-parts/domain hypotheses, give \(\langle T\rangle=\langle V\rangle\) and \(\langle F_{\rm ferm}\rangle=-2\langle T\rangle\). They do not fix a spin-2 double trace or the weighted tail in (2).

The known radius lower-bound argument, restored to the finite-\(N\) commutator in the earlier project calculation, gives conditionally

\[
\mathbb E_N\operatorname{tr}Z_1^2\ge\frac3{16}(1-N^{-2})^{4/3}.
\]

It forces an order-one lower bound for \(\mathbb E_Na_h\) and \(\|b\Omega_N\|^2\). It does **not** contradict (2): a large scalar Gram matrix can be nearly isotropic, making all traceless quadrupoles small while \(a_h\) remains order one. This distinction is already present in the full-variance route. The underlying virial/bootstrap source is [Lin, 2302.04416](https://arxiv.org/abs/2302.04416); the finite-\(N\) factor is the previously derived conditional correction, not a newly attributed theorem.

There is a finite-color geometric obstruction at the smallest ranks: \(\operatorname{rank}M\le d_N:=\min(9,N^2-1)\) gives \(\operatorname{Tr}M^2-\rho^4/9\ge\rho^4(1/d_N-1/9)\). For \(N\ge4\), this lower bound is zero, so it does not obstruct the proposed large-rank concentration.

Finally, the shear generator \(D_h=\frac12\sum_{Aij}h_{ij}(Z_i^AP_j^A+P_j^AZ_i^A)\) obeys \([D_h,q_h]=-2ia_h\). When the uncertainty relation is justified, \(\operatorname{Var}(D_h)\operatorname{Var}(q_h)\ge(\mathbb E_Na_h)^2\). Quadrupole concentration consequently needs growing shear fluctuations. A variance rate \(N^{-4/3}\) requires at least order \(N^{4/3}\) shear variance; the planar rate \(N^{-2}\) requires at least order \(N^2\). No conflicting upper bound on that variance is known from the elementary identities being used here. These checks establish neither (2) nor a contradiction.

## 4. Why optimizing radial cutoffs alone does not remove the old bottleneck

Consider the natural restricted family \(F=f(\rho)q_h\) with smooth real radial \(f\), regular at zero and compactly supported. Define

\[
c_N(\rho)=\mathbb E_N[q_h^2\mid\rho].
\]

With \(M_{ij}=\operatorname{tr}(Z_iZ_j)\), rotational invariance gives

\[
c_N(\rho)=\frac1{44}\mathbb E_N\!\left[\operatorname{Tr}_9(M-\rho^2I_9/9)^2\mid\rho\right],
\quad 0\le c_N(\rho)\le\frac{2\rho^4}{99}.
\tag{6}
\]

This uses positivity of the spatial Gram matrix and the dimension 44 of symmetric traceless tensors, not factorization. Also \(\mathbb E_N[a_h\mid\rho]=\rho^2/9\). Direct substitution into (4) gives

\[
J[f]=\mathbb E_N\!\left[
\frac{\rho^2(1-f)^2}{18}
+c_N(\rho)\left(-\frac{(1-f)f'}{2\rho}+\frac{f'^2}{8}+\frac{sN^2f^2}{4}\right)\right].
\tag{7}
\]

The derivative terms complete a square:

\[
\frac{f'^2}{8}-\frac{(1-f)f'}{2\rho}
=\frac18\left(f'-\frac{2(1-f)}\rho\right)^2-\frac{(1-f)^2}{2\rho^2}.
\]

Using (6), then minimizing the remaining quadratic in \(f\) pointwise, proves

\[
J[f]\ge\mathbb E_N\!\left[\frac{\rho^2}{22}(1-f)^2+\frac{sN^2c_N(\rho)}4f^2\right]
\ge\mathbb E_N\!\left[\frac{sN^2\rho^2c_N(\rho)}{4\rho^2+22sN^2c_N(\rho)}\right].
\tag{8}
\]

At \(s=N^{-4/3}\), since \(x/(4+22x)\ge\min(1,x)/26\), every successful radial trial must obey

\[
\mathbb E_N\!\left[\rho^2\min\left(1,\frac{N^{2/3}c_N(\rho)}{\rho^2}\right)\right]
=O(N^{-2/3}).
\tag{9}
\]

This is a lower bound on the restricted trial objective, **not** on the exact \(K_N\). It is not an unconditional impossibility theorem: the BFSS state might satisfy (9). It says that choosing a clever radial cutoff cannot by itself create the missing angular concentration. For \(N\ge4\), the spatial Gram matrix can be isotropic at individual configurations, so this algebra supplies no positive uniform lower bound on \(c_N\).

## 5. Connection to the spectral target, and limits of the result

Positivity gives

\[
\|\mathbf1_{(0,s)}(\widehat H_N)b\Omega_N\|^2\le2K_N(s).
\]

Thus (2) supplies the desired \(O(N^{-2/3})\) source weight on the dimensionless window \(s\asymp N^{-4/3}\). Restoring a fixed coefficient in \(s=\delta_0\ell^2p^+N^{-4/3}\) changes only the constants. This can close the previously stated zero-longitudinal-current infrared gate at a fixed physical window. It does not independently construct scattering states, handle rank-changing soft emission, establish large-rank amplitude regularity, or prove generic eleven-dimensional soft factorization.

The indicator in (2) is bounded, but its weight \(a_h\) is not; their product is integrable under the stated second-moment assumption. Any numerical/bootstrap certificate must control that weighted tail and its rank dependence, not merely histogram the unweighted probability of \(|q_h|>L\). A finite-temperature or BMN-regulated estimate needs a justified limit before being used here.

## 6. Current literature comparison

- [Cho–Gabai–Lin–Yeh–Zheng, 2511.08560v3](https://arxiv.org/html/2511.08560v3), revised 30 June 2026 and [published 19 August 2026 as JHEP08(2026)147](https://link.springer.com/article/10.1007/JHEP08(2026)147), gives continuous-time two-point upper certificates by finite-dimensional dual positivity. Its examples are ungauged bosonic one-matrix quantum mechanics. Fermionic gauge-singlet ground-state source Gram matrices are also positive, so fermions do not prohibit applying the framework here. But section 5 leaves convergence and strong duality open; no rank-uniform BFSS certificate is supplied. Equation 44 is a lower correlator bound and cannot be used as decay control. Equation (4) above is a separate variational certificate, not a result attributed to that paper.
- [Lin–Zheng, 2410.14647v2, sections 3–4](https://arxiv.org/html/2410.14647v2) imposes planar factorization, has no unconditional radius upper bound at its displayed levels, and warns of divergent high-degree finite-rank moments. Those issues motivate a bounded primitive rather than an unbounded all-polynomial hierarchy. [Their 2026 high-precision result](https://arxiv.org/abs/2507.21007) is bosonic; [Lin's August 2026 TASI revision](https://arxiv.org/html/2508.20970v3) still lists BFSS Part II as in preparation. No released finite-rank supersymmetric dynamic-bootstrap solution was located in this check.
- [Herderschee–Maldacena, 2312.15111](https://arxiv.org/html/2312.15111v1) uses amplitude regularity/soft-factorization reasoning and restricts higher-point kinematics. It explicitly assumes that any new large-rank singularities are subleading in the soft limit. It does not give the positive source estimate sufficient for the existing rank gate.
- [Guevara–Lupsasca–Maldacena–Strominger, 2608.25239](https://arxiv.org/html/2608.25239v1), sections 1–2 and 7, concerns supersymmetric single-minus amplitudes supported on half-collinear special kinematics and a BPS-index/wall-crossing construction. This is substantial protected progress, not a proof of (2).
- [Laurenzano–Wheater, 2510.15488v2](https://arxiv.org/html/2510.15488v2) derives factorization in the one-loop large-distance effective theory and explicitly omits higher-order three-body interactions. [2602.11667v2, section 4](https://arxiv.org/html/2602.11667v2) localizes the SU(2) relative sector with special boundary conditions; neither supplies a general finite-rank positive-measure concentration estimate.

## 7. Verification and honest stopping point

The accompanying script checks the square completion and constants symbolically; verifies the 44-dimensional traceless projector; checks the residual formula on 500 random finite-rank coordinate configurations; and checks the abstract resolvent variational identity on a self-adjoint finite matrix including a zero mode. These are algebra checks, not verification of BFSS analytic domains or numerical evidence for the desired concentration. A separate algebra audit confirmed the constants and the restricted direction of (8).

The concrete next proposition is (2), or a certified nonradial scalar primitive satisfying (5), with constants independent of rank and the infrared regulator. Proving it would advance the dynamical rank bridge beyond finite-rank Hardy regularity. This checkpoint establishes an additional sufficient criterion and rules out treating unconstrained radial optimization as a solution; it does not establish that proposition. The unresolved nonperturbative physics has been shifted into a specified weighted-concentration/capacity estimate, not removed. The literature check found no source proving that estimate; it does not establish global originality of this variational or clipping construction.
