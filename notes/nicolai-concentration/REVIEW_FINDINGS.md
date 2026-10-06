# Findings on Nicolai transport and concentration

Author: Yicheng Pan  
Date: 6 October 2026  
Status: Provisional analysis of a conditional obstruction

The Gaussian-transfer normalization and the fixed-Cartan obstruction are consistent: a pointwise covariance bound for the specified class of transports must grow with Euclidean duration, or diverge when a Gaussian mass is removed. This excludes that particular uniform-bound strategy. It neither proves BFSS concentration nor rules out averaged transport estimates, other maps, or other concentration mechanisms. No human expert review was supplied. Finite algebra checks are not independent human certification.

## Required transport hypothesis

Use \(\operatorname{Tr}(T_AT_B)=\delta_{AB}\), \(\operatorname{tr}=\operatorname{Tr}/N\), and a real symmetric traceless \(h\) with \(\operatorname{Tr}_9h^2=1\). Then

\[
q_h=\frac1N\sum_AZ_i^Ah_{ij}Z_j^A,\qquad
a_h=\frac1N\sum_AZ_i^A(h^2)_{ij}Z_j^A,\qquad
|\nabla q_h|^2=\frac{4a_h}{N}.
\]

The finite-interval Gaussian bridge has zero Dirichlet endpoints and covariance \(C_\beta/N\), with \(C_\beta=(-\partial_t^2)^{-1}\). The proposed transfer assumes a real transport T whose inverse is differentiable, with the Sobolev regularity and integrability needed for Gaussian Poincaré, and with the desired interacting probability law equal to \((T^{-1})_\#\gamma\). This includes the gauge and boundary prescriptions. Differentiability and bijectivity of T alone do not guarantee a differentiable inverse.

These are hypotheses, not consequences of the perturbative Nicolai construction. A finite-discretization argument also needs a justified continuum limit; moments or derivative energies may otherwise be infinite.

With \(J=D(T^{-1})\), Gaussian Poincaré gives

\[
\operatorname{Var}(F)
\le\frac1N\mathbb E\langle J^*dF,C_\beta J^*dF\rangle.
\]

For \(F=q_h(Z(t_0))\), the bound \([JC_\beta J^*](t_0,t_0)\le\kappa I\) would imply

\[
\operatorname{Var}(q_h)\le\frac{4\kappa\langle a_h\rangle}{N^2}.
\]

There is no additional rank multiplicity in this normalization. Spin(9) invariance gives \(\langle a_h\rangle=\langle\rho^2\rangle/9\) and \(\langle q_h\rangle=0\).

## Fixed Cartan directions force a large pointwise constant

The formal temporal-gauge coupling flow fixes paths in a single Cartan subalgebra: its interaction vector field vanishes there. This observation follows from [Lechtenfeld and Nicolai, equation (3.10)](https://arxiv.org/html/2109.00346v3). It does not construct a global positive Dirichlet transport or justify changing the paper's propagator and boundary prescription.

For any extension that retains the fixed-subspace property, differentiation of \(T^{-1}|_V=I\) gives \(Jv=v\) on the Cartan subspace V. Relative to V and its orthogonal complement, J can have the form

\[
J=\begin{pmatrix}I&B\\0&D\end{pmatrix}.
\]

One must not infer \(J^*u=u\) for every Cartan covector u. Instead \(J^*u=(u,B^*u)\). Since the Gaussian covariance is diagonal in Lie-algebra indices,

\[
\langle J^*u,CJ^*u\rangle
=\langle u,Cu\rangle+\langle B^*u,CB^*u\rangle
\ge\langle u,Cu\rangle.
\]

Thus root mixing cannot remove the lower bound. The Dirichlet covariance is

\[
C_\beta(t,s)=\min(t,s)-ts/\beta,\qquad
C_\beta(\beta/2,\beta/2)=\beta/4,
\]

so the pointwise constant necessarily obeys \(\kappa_{N,\beta}\ge\beta/4\). The exact commuting locus may have probability zero. A large integrand on that locus does not establish a large average or a variance lower bound.

For covariance \((-\partial_t^2+\omega^2)^{-1}\), the corresponding midpoint value is

\[
C_{\beta,\omega}(\beta/2,\beta/2)
=\frac{\tanh(\omega\beta/2)}{2\omega}.
\]

If the mass-deformed transport also fixes Cartan paths, then \(\kappa\) is at least this value. It tends to \(1/(2\omega)\) as \(\beta\to\infty\). Replacing the covariance alone does not construct such a transport or prove the fixed-Cartan property. These conditional estimates exclude a pointwise constant uniform in both limits.

## Oscillator and nonconvexity calculations

For the genuine free oscillator, the coordinate variance is \(1/(2N\omega)\). With the free U(1) center omitted, Wick contraction gives

\[
\langle\rho^2\rangle=\frac{9(N^2-1)}{2N^2\omega},\qquad
\operatorname{Var}(q_h)=\frac{N^2-1}{2N^4\omega^2}.
\]

This ground state is gauge invariant. Choosing \(\omega\asymp N^{-1/3}\) yields the proposed power only for the oscillator; it establishes no comparison to the BFSS state. Choosing a rank-dependent finite duration similarly leaves the rate and weighted-observable control in the ground-state limit unproved.

For \(A=\sigma_1/\sqrt2\), \(B=\sigma_2/\sqrt2\), and \(Z_1=(t+s)A\), \(Z_2=(t-s)B\), the bosonic potential and its second variation are

\[
V_b=N(t^2-s^2)^2,\qquad V_b''(0)=-4Nt^2.
\]

A scalar quadratic mass changes the Hessian per unit squared variation to \(N(\omega^2-2t^2)\), which is unbounded below. For zero Dirichlet endpoints and a nonzero smooth endpoint-vanishing profile f, the analogous action variation is

\[
2N\int(f')^2+2N\omega^2\int f^2-4NL^2\int f^4.
\]

It is negative for sufficiently large L on any fixed nontrivial interval. Therefore a standard global strict-convexity argument cannot be applied to this bosonic action. Fermionic integration and positivity cannot be omitted. This calculation does not refute every Poincaré inequality for the true equal-time measure.

## Literature scope and unresolved input

[Lechtenfeld and Nicolai, Sections 2.3 and 4](https://arxiv.org/html/2109.00346v3), give the field-dependent Jacobian convergence condition \(|g|<2/(c_N\|X\|_1)\), with rank-dependent \(c_N\). This does not establish map convergence, Majorana-Pfaffian positivity, a positive global transport, or the required inverse-derivative bound. In canonical kinetic-one coordinates \(X=\sqrt N Z\), the scaling \(g\propto N^{-1/2}\) cancels from \(g\|X\|_1\); a small-looking coupling alone supplies no rank gain.

The accompanying applicability discussion also cites [Guionnet and Maurel-Segala](https://arxiv.org/abs/math/0601040), [Guionnet and Shlyakhtenko](https://arxiv.org/abs/math/0701787), [Komatsu et al.](https://arxiv.org/html/2401.16471), and [High-Precision Bootstrap of Multimatrix Quantum Mechanics](https://journals.aps.org/prl/abstract/10.1103/cyq8-4sd7). Their stated convexity, fixed-rank, or infinite-rank/factorization settings do not supply the missing BFSS estimate. The source material's detailed formula-level assessment centered on the Nicolai paper; the other applicability statements were not separately rederived. No new literature search is represented by this summary, and no exhaustive absence or priority claim is made.

A successful continuation would need a positive ground-state transport together with an averaged, rank-controlled inverse-derivative estimate that handles long commuting paths, or a genuinely different dynamical argument. Neither target, \(\langle q_h^2\rangle=O(N^{-4/3})\) or \(\langle\rho^2q_h^2\rangle=O(N^{-4/3})\), follows from the present calculation.
