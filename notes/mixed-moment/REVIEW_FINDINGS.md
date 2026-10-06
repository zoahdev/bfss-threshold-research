# Review findings on the mixed moment branch

Author: Yicheng Pan  
Research checkpoint: 6 October 2026  
Status: provisional exact reductions and conditional BFSS consequences

The planar upper estimate \(M_N=\langle\rho^2q_h^2\rangle=O(N^{-2})\) remains unresolved. The weaker sufficient rate \(O(N^{-4/3})\) is also unproved. The substantive findings are an exact rotational reduction, a two-sided comparison of sixth moments, a conditional radius consequence, a justified direct-primitive reduction, and a coordinate-only obstruction. No human expert review has been supplied. Symbolic and computational checks are not human certification or evidence that the actual BFSS zero mode satisfies the missing upper bound.

## Scope and notation

Let \(\operatorname{tr}=\operatorname{Tr}/N\), \(G_{ij}=\operatorname{tr}(Z_iZ_j)\), \(R=\rho^2=\operatorname{Tr}_9G\), and \(B=G-RI_9/9\). For \(h=h^T\), \(\operatorname{Tr}_9h=0\), \(\operatorname{Tr}_9h^2=1\), define
\[
q_h=\operatorname{Tr}_9(hG),\quad a_h=\operatorname{Tr}_9(h^2G),\quad
S=\langle R\rangle,\quad V_q=\langle q_h^2\rangle,\quad
A_6(h)=\langle a_hq_h^2\rangle.
\]
The rotational findings need only \(G\ge0\) and a conjugation-invariant law. The BFSS consequences additionally require the earlier branch's normalized physical singlet zero mode, zero energy, compatible realization and quadratic forms, finite moments, and justified virial and domain arguments. No exterior theorem or uniform-rank upper control is established by this branch.

## Exact cubic coefficient and comparison

For real traceless symmetric \(m\times m\) matrices, \(m\ge3\), the rotational cubic coefficient is
\[
c_m=\frac{8m}{(m-2)(m-1)(m+2)(m+4)}.
\]
The invariant cubic is proportional to \(\operatorname{Tr}C^3\); calibration on \(C=nn^T-I/m\) gives this coefficient. At \(m=9\), \(c_9=9/1001\), while the quadratic orbit average is \(\mathbb E_Oq_h^2=\operatorname{Tr}B^2/44\). Hence, for finite \(M_N\),
\[
A_6(h)=\frac{M_N}{9}
+\frac9{1001}\left(\operatorname{Tr}h^4-\frac19\right)
\langle\operatorname{Tr}B^3\rangle.
\]
No independence or planar factorization is assumed. The bounds
\[
0\le\operatorname{Tr}h^4-1/9\le7/9,\qquad
-\frac R9\operatorname{Tr}B^2\le\operatorname{Tr}B^3
\le\frac{8R}{9}\operatorname{Tr}B^2,
\]
together with \(\langle R\operatorname{Tr}B^2\rangle=44M_N\), yield
\[
\frac1{13}M_N\le A_6(h)\le\frac5{13}M_N.
\]
These constants are conservative and uniform in \(h\) and \(N\). Replacing the radial weight by \(a_h\) therefore does not bypass the concentration problem.

The integrability distinction is essential. Radial cutoffs establish the comparison in the extended nonnegative reals by monotone convergence. If either nonnegative sixth moment is finite, both are finite and the signed cubic term is absolutely integrable. If both are infinite, the signed decomposition is not asserted: it could contain an undefined difference of infinities. No assumption of finite \(\langle\rho^6\rangle\) is needed for the finite mixed-moment identity.

## Conditional radius consequence and sufficient rates

The earlier BFSS branch supplies, under its stated hypotheses,
\[
V_q\ge\frac{2^{1/4}}{27}S^{5/4}N^{-2},\qquad
S\ge2^{-2/3},\qquad
\mathbb P(\rho\le1/2)\le2^{-2N^2}.
\]
With \(q_h^2\le b\rho^4\), \(b=8/9\), the discarded small-radius variance is at most \((b/16)2^{-2N^2}\), and at most \(V_q/2\) for \(N\ge2\). Consequently
\[
M_N\ge\frac18V_q
\ge\frac{2^{1/4}}{216}S^{5/4}N^{-2}.
\]
A planar certificate \(M_N\le C_MN^{-2}\) would imply the substantial additional conclusion
\[
S\le\left(216\,2^{-1/4}C_M\right)^{4/5}.
\]
This is a conditional implication, not a mixed-moment upper bound or evidence against one.

The same radius split gives
\[
V_q\le4M_N+\frac b{16}2^{-2N^2}.
\]
Finite \(M_N\) implies finite \(V_q\), without requiring a finite fourth radial moment. Under \(S<\infty\) and preservation of charge domains by the stated bounded smooth multipliers, the direct primitive has a complete cutoff justification. For \(F_L=\chi(\rho/L)q_h\),
\[
\|[Q_\alpha,\chi(\rho/L)]q_h\Omega\|^2
\le\frac{\|\chi'\|_\infty^2}{2N^2L^2}V_q\longrightarrow0.
\]
Closedness gives \(q_h\Omega\in D(Q_\alpha)\) and \(Q_\alpha q_h\Omega=-2ib_{\alpha,h}\Omega/N\). The existing variational source certificate therefore yields
\[
K_N(s)\le\frac{sN^2}{4}V_q
\le sN^2M_N+\frac b{64}sN^2\,2^{-2N^2}.
\]
For fixed \(\sigma>0\) and \(s=\sigma N^{-4/3}\), a planar moment upper bound would give \(K_N(s)=O(N^{-4/3})\). The weaker rate \(M_N=O(N^{-4/3})\) already suffices for \(K_N(s)=O(N^{-2/3})\). Both remain conditional because neither moment upper estimate is proved.

## The tested Ward identity supplies only a shear current

With \(D_h=\sum_{Aij}h_{ij}Z_i^AP_j^A\), the charge and Clifford core identities give
\[
\sum_{\alpha=1}^{16}\{Q_\alpha,b_{\alpha,h}\}=16D_h/N,\quad
[Q_\alpha,q_h]=-2ib_{\alpha,h}/N,\quad
b_{\alpha,h}^2=a_h/2,\quad [D_h,q_h]=-2ia_h.
\]
Thus, for scalar \(f\),
\[
\sum_\alpha\{Q_\alpha,f(q_h)b_{\alpha,h}\}
=\frac{16}{N}\left[f(q_h)D_h-if'(q_h)a_h\right]
=\frac8N\{f(q_h),D_h\}.
\]
The choice \(f(q)=q^3\) retains the exact coefficient \(-3ia_hq_h^2\). When its expectation is legitimate, its real part imposes zero shear current; its imaginary part is already fixed by \([D_h,q_h^3]=-6ia_hq_h^2\). No separately positive restoring term bounds \(A_6\).

The norm \(\|q_h^3b_{\alpha,h}\Omega\|^2=\langle a_hq_h^6\rangle/2\) is a degree-fourteen moment. Finite \(M_N\) does not justify this unregularized Ward expectation. The result concerns this elementary Ward family only; quantum identities involving additional fermions, momenta, or commutators remain outside its scope.

## Coordinate positivity cannot force the missing suppression

For every \(N\ge2\), choose traceless diagonal Hermitian \(D_N\) with \(\operatorname{tr}D_N^2=1\) and \(\|D_N\|_{\rm op}\le\sqrt{3/2}\). Let \(n\) be uniform on \(S^8\), \(U\) Haar in \(SU(N)\), and set \(Z_i=n_iUD_NU^\dagger\). This rotationally and gauge-invariant coordinate law obeys all finite-rank coordinate trace identities and coordinate-polynomial positivity, and has uniformly bounded fixed-degree normalized trace moments. Nevertheless,
\[
[Z_i,Z_j]=0,\quad R=1,\quad G=nn^T,\quad
\operatorname{Tr}B^2=8/9,\quad M_N=2/99.
\]
It rules out an upper argument based only on these coordinate properties, even with a hard radius bound and vanishing commutator potential. The law is not a BFSS quantum state: canonical momentum, fermion, zero-energy, and virial constraints have not been imposed. It provides no counterexample to the fixed-coupling estimate and no general no-go theorem for quantum sum-of-squares certificates.

## Unresolved dynamical input and sources

Rotational invariance gives \(\langle q_h\rangle=\langle Rq_h\rangle=0\), hence
\[
M_N=S V_q+\kappa_N(R,q_h,q_h).
\]
Uniform estimates \(S=O(1)\), \(V_q=O(N^{-2})\), and \(|\kappa_N|=O(N^{-2})\) would suffice for the planar target. Symmetry and positivity do not establish them. Finite-rank trace splitting retains connected multi-traces; factorizing them would assume the missing input. A successful alternative could establish a weighted tail/capacity or source-specific low-energy resolvent estimate instead of a sixth-moment bound.

The supplied exact checks cover the cubic coefficient, comparison endpoints, and rank-one spherical calibration. They do not test BFSS concentration. The archived primary-source discussion cites [Lin and Zheng, arXiv:2410.14647v2](https://arxiv.org/html/2410.14647v2), whose closure uses factorization and discusses finite-rank tail and regulator issues; [the bosonic multimatrix study, arXiv:2507.21007](https://arxiv.org/abs/2507.21007); and [Lin's TASI notes, arXiv:2508.20970v3](https://arxiv.org/html/2508.20970v3). These references are not used as proofs of the missing finite-rank mixed-moment upper estimate. The literature check is dated and bounded, with no claim of exhaustive originality.
