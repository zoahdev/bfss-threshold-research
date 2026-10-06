# Review findings on Spin9 interference

Author: Yicheng Pan  
Research checkpoint: 6 October 2026  
Status: provisional algebraic findings with conditional zero-mode consequences

The Spin(9) projections and the full isotropic polarization average considered here do not supply an upper bound on the fixed-coupling BFSS mixed moment
\[
M_N=\langle\rho^2q_h^2\rangle.
\]
The exact reductions retain an uncontrolled shear-current norm and unsigned interference. The sufficient rate \(M_N=O(N^{-4/3})\), as well as the stronger planar rate, remains unproved. No human expert review has been supplied. The symbolic derivations and finite Clifford checks provide algebraic evidence, not human certification or a BFSS ground-state computation.

## Assumptions and notation

Use \(\operatorname{tr}=\operatorname{Tr}/N\), \([Z_i^A,P_j^B]=i\delta_{ij}\delta_{AB}\), \(\{\psi_\alpha^A,\psi_\beta^B\}=\delta_{\alpha\beta}\delta_{AB}\), and real symmetric 16-dimensional gamma matrices. The polarization satisfies \(h=h^T\), \(\operatorname{Tr}_9h=0\), and \(\operatorname{Tr}_9h^2=1\). Write
\[
q=\operatorname{tr}(Z_i h_{ij}Z_j),\quad
a=\operatorname{tr}(Z_i(h^2)_{ij}Z_j),\quad
D=\sum_{Aij}h_{ij}Z_i^AP_j^A,\quad A=\{q,D\}/2=qD-ia.
\]
With the fixed BFSS charge
\[
Q_\alpha=N^{-1/2}\operatorname{Tr}(P_i\Gamma_{i,\alpha\beta}\psi_\beta)
-\frac{i\sqrt N}{2}\operatorname{Tr}([Z_i,Z_j]\Gamma_{ij,\alpha\beta}\psi_\beta),
\]
set \(b_\alpha=N^{-1/2}\operatorname{Tr}((hZ)_i\Gamma_{i,\alpha\beta}\psi_\beta)\) and \(R_{\alpha\beta}=\{Q_\alpha,b_\beta\}\).

Polynomial equalities first hold on a common smooth core. Expectations assume a normalized physical gauge- and Spin(9)-singlet zero mode \(\Omega\), the Gauss constraint, and compatible domains. In particular, the norm reductions require \(q^2\Omega\in D(H)\), the displayed descendants and mixed forms, or justified cutoff limits. Finiteness of \(M_N\) alone does not imply those hypotheses. Existence, uniqueness, and rank-uniform domain control are not established.

## Exact irreducible reductions

The antisymmetric spinor space decomposes as \(\Lambda^2(16)=36\oplus84\). For \(E_I=\Gamma_{ij}\) or \(\Gamma_{ijk}\), respectively, use Frobenius normalization \(\sum_{\alpha\beta}(E_I)_{\alpha\beta}(E_J)_{\alpha\beta}=16\delta_{IJ}\), and define
\[
r_I=\frac1{16}\sum_{\alpha\beta}(E_I)_{\alpha\beta}R_{\alpha\beta},\qquad
F_I=-\frac{i}{16}\sum_{\alpha\beta}(E_I)_{\alpha\beta}b_\alpha b_\beta.
\]
For diagonal \(h=\operatorname{diag}(\lambda_1,\ldots,\lambda_9)\) and \(\Psi_I=\sum_A\psi^A\Gamma_I\psi^A\), the retained coefficients are
\[
r_{ij}=\frac{\lambda_j Z_j\!\cdot P_i-\lambda_i Z_i\!\cdot P_j}{N}
+\frac{i(\lambda_i+\lambda_j)}{8N}\Psi_{ij},
\]
\[
r_{ijk}=-i(\lambda_i+\lambda_j+\lambda_k)
\left[\operatorname{Tr}([Z_i,Z_j]Z_k)+\frac{\Psi_{ijk}}{8N}\right].
\]
Thus the 36 channel retains symmetric shear after the angular-momentum term annihilates a singlet. The 84 channel retains the cubic interaction and its fermionic bilinear. Singletness does not make either channel vanish.

For either sector separately, of dimension \(d=36\) or \(84\), the finite gamma Bianchi identity gives
\[
\sum_I F_I^2=\frac{d}{32}a^2,
\]
with coefficients \(9/8\) and \(21/8\). The projected descendant is \(S_I=qr_I+2F_I/N\). Using \(\chi=q^2\Omega\) and \(H\chi=-4iA\Omega/N^2\), the same identity gives
\[
\sum_I\|S_I\Omega\|^2
=\frac{dN^2}{128}\|H\chi\|^2
=\frac{d}{8N^2}\langle A^2\rangle.
\]
Its expansion is
\[
\left\langle q^2\sum_Ir_I^2\right\rangle
+\frac2N\left\langle q\sum_I\{r_I,F_I\}\right\rangle
=\frac{d}{8N^2}\bigl(\langle A^2\rangle-\langle a^2\rangle\bigr).
\]
The mixed term is real and has no established sign. Dropping it is invalid. A nonzero positive invariant weight \(c_2P_{36}+c_3P_{84}\), \(c_2,c_3\ge0\), retains an uncontrolled positive multiple of \(\langle A^2\rangle\). The signed combination with relative coefficient \(-7/3\) cancels both diagonal terms, but leaves a difference of squares and mixed terms. It is an indefinite balance, not a positive upper certificate.

The same-source Clifford contraction \(\sum_\beta b_\beta b_\alpha b_\beta=-7ab_\alpha\) does not repair the sign. The direct cubic Ward expansion controls commutators with \(R_{\alpha\beta}\), whereas the descendant norm contains anticommutators. These expressions cannot be substituted for one another.

## Polarization averaging does not cancel the interaction

For a uniform unit polarization in the 44-dimensional space \(\operatorname{Sym}_0(9)\), the fourth moment is the Gaussian Wick moment with covariance
\[
P_{ij,kl}=\frac{\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}}2
-\frac{\delta_{ij}\delta_{kl}}9
\]
divided by \(44\cdot46\). This Gaussian is an integration device for polarizations only.

At the embedded-SU(2) coordinate point \(Z_1=T_1,Z_2=T_2,Z_3=T_3\), with other coordinates zero, \(\operatorname{Tr}(T_aT_b)=\delta_{ab}\) and \([T_a,T_b]=i\sqrt2\epsilon_{abc}T_c\), the color-1 fermion kernel has Gaussian coefficient \(8\Gamma_{123}/3\). The \(123\) channel contributes \(-4\Gamma_{123}/3\); each of the six \(23k\) channels contributes \(2\Gamma_{123}/3\). After sphere normalization the coefficient is \(\Gamma_{123}/759\). Therefore
\[
\mathbb E_h\sum_{I\in84}q r_I^V F_I
\quad\text{contains}\quad
-\frac{i\sqrt2}{12144N^2}\psi^1\Gamma_{123}\psi^1,
\]
and the real norm interference contains
\[
-\frac{i\sqrt2}{3036N^3}\psi^1\Gamma_{123}\psi^1.
\]
The coefficient is nonzero. This cubic-interaction contribution scales as \(t^7\) under \(Z\mapsto tZ\), whereas the fermionic multiplication contribution from \(r_I\) scales as \(t^4\); those pieces cannot cancel as a polynomial identity. The 36 channel has no cubic-interaction multiplication term.

The nonzero traceless Hermitian fermion component has both signs on the full Clifford module. The coordinate evaluation is an operator-polynomial test, not a physical state or an evaluation of its expectation in \(\Omega\). It excludes the proposed identical cancellation under the full sphere average. It does not exclude additional dynamical identities, specially weighted constructions, or a vanishing expectation in a particular zero mode.

## Remaining gap and evidence

An upper certificate still needs uniform control of the mixed interference, the shear-current norm, or a different coercive estimate for the actual fixed-coupling zero mode. Higher-degree, localized, rational, or coordinate-dependent weights remain outside the negative result.

The supplied exact checks cover the Clifford relations, gamma orthogonality, the two Bianchi identities, the fermion projection factors, both square sums, and the coefficient \(1/759\). A second finite gamma construction checks the Bianchi identities. These finite algebra checks do not establish unbounded-operator domains or large-rank concentration.

The charge and Gauss conventions are compared with [Lin and Zheng, arXiv:2410.14647v3, Section 1.1 and Appendix C.2](https://arxiv.org/html/2410.14647v3). The irreducible reductions and noncancellation coefficient above are findings of this branch; that primary reference is not cited as proving the desired upper bound.
