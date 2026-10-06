# Review findings on the quantum Gram branch

Author: Yicheng Pan  
Research checkpoint: 6 October 2026  
Status: provisional finite-family obstructions and conditional zero-mode identities

This branch identifies two distinct obstructions and concrete missing correlators. It does not prove or disprove the actual fixed-coupling BFSS estimate \(M_N=\langle\rho^2q_h^2\rangle=O(N^{-4/3})\). No human expert review has been supplied. Symbolic checks do not constitute human certification, a solved semidefinite program, or a numerical BFSS ground-state calculation.

## Assumptions and the first finite Gram

Use \(\operatorname{tr}=\operatorname{Tr}/N\), \([Z,P]=i\), and \(\{\psi_\alpha^A,\psi_\beta^B\}=\delta_{\alpha\beta}\delta_{AB}\). For real symmetric traceless \(h\) with \(\operatorname{Tr}_9h^2=1\), put
\[
R=\rho^2,\quad q=\operatorname{tr}(Z_i h_{ij}Z_j),\quad
a=\operatorname{tr}(Z_i(h^2)_{ij}Z_j),\quad
D=\sum_{Aij}h_{ij}Z_i^AP_j^A,\quad A=\{q,D\}/2.
\]
Expectations assume a normalized physical gauge- and Spin(9)-singlet zero mode, a compatible self-adjoint BFSS realization, and the indicated domains or justified cutoff limits. Core identities do not automatically extend to high-degree expectations. Existence of \(M_N\) alone does not justify every Gram entry.

For each fixed charge component,
\[
[Q_\alpha,q]=-2ib_\alpha/N,\quad b_\alpha^2=a/2,\quad
\{Q_\alpha,b_\alpha\}=D/N,\quad [D,q]=-2ia.
\]
The natural odd Gram block of \((b_\alpha,qb_\alpha)\) gives a lower inequality for \(\langle aq^2\rangle\). The five-vector family built from \(q^2\Omega,qb_\alpha\Omega,A\Omega,Q_\alpha q^2\Omega,Q_\alpha(qb_\alpha)\Omega\) satisfies
\[
Q_\alpha q^2\Omega=-4iqb_\alpha\Omega/N,\qquad
Q_\alpha(qb_\alpha)\Omega=A\Omega/N,
\]
\[
Hq^2\Omega=-4iA\Omega/N^2,\qquad
\langle q^2\Omega,A\Omega\rangle=2i\langle aq^2\rangle.
\]
Its determinant consequence is
\[
\langle aq^2\rangle^2\le\frac14\langle q^4\rangle\langle A^2\rangle.
\]
Both positive diagonals remain uncontrolled. The previously derived comparison \(M_N/13\le\langle aq^2\rangle\le5M_N/13\) transfers the concentration problem; it does not solve it. The graph-domain argument for these vectors can avoid inserting \(q^3b\) directly, but still needs more than finite \(M_N\).

## Fixed coupling and the bounded polynomial dual class

Assign \(\mathrm{wt}(Z)=1\), \(\mathrm{wt}(P)=2\), and \(\mathrm{wt}(\psi)=0\). Consider exactly the polynomial identity
\[
\begin{aligned}
C_N I-Rq^2={}&\sum_j S_j^\dagger S_j
+\sum_\alpha(Q_\alpha O_\alpha+O_\alpha^\dagger Q_\alpha)
+HB+B^\dagger H\\
&+\sum_A(G_AC_A+C_A^\dagger G_A)
+\sum_{ij}(L_{ij}E_{ij}+E_{ij}^\dagger L_{ij}),
\end{aligned}
\]
where \(G_A,L_{ij}\) are the full gauge and spatial-rotation generators, and the raw-factor bounds are
\[
\mathrm{wt}(S_j)\le4,\quad \mathrm{wt}(O_\alpha)\le6,\quad
\mathrm{wt}(B)\le4,\quad \mathrm{wt}(C_A),\mathrm{wt}(E_{ij})\le5.
\]
All Clifford words and exact finite-rank identities are allowed, and coefficients may depend arbitrarily on \(N\). The cutoffs concern raw factors before cancellations.

The algebraic conclusion is nonexistence of this identity for every \(N\ge2\) and finite \(C_N\). Normal ordering uses \([P,Z]=-i\), lowering weight by three. At the commuting symbol \(Z_i=t n_iD_N,P=0\), with \(|n|=1\), \(D_N\) traceless Hermitian and \(\operatorname{tr}D_N^2=1\), the principal charge, bosonic Hamiltonian, and orbital constraint symbols vanish. Every remaining null-term contribution has weight at most five. The degree-eight coefficient forces every evaluated quartic square factor to vanish. The degree-six coefficient would then require
\[
-(n^Thn)^2 I=\sum_j s_{j,3}^\dagger s_{j,3},
\]
which is impossible for a direction with \(n^Thn\ne0\). Orbit averaging preserves the contradiction with coefficient \(-2/99\).

This is a fixed-coupling operator-symbol obstruction, including arbitrary fermion degree. It is not a physical state construction, nor a proof of an unbounded primal optimum for every possible SDP truncation. Higher raw weights, localized or rational multipliers, and analytic zero-mode estimates are not excluded. The five-vector shear Gram above exceeds this class because \(A\) and \(Q(qb)\) have weight five.

Raw product weight nine is the first order at which a canonical correction can reach weight six. The natural example satisfies
\[
\{Q_\alpha,q^3b_\alpha\}
=\frac{q^3D-3iaq^2}{N}=\frac{\{q^3,D\}}{2N}.
\]
The sixth-moment term is part of the current's Hermitian ordering correction; no favorable upper sign follows. Higher-weight single-charge routes remain possible.

## The separate dilation obstruction

If only the diagonal-supercharge, shear, and Clifford relations are retained, without the fixed interaction coefficient, their homogeneous scaling is
\[
(q,a,R)\mapsto\lambda^2(q,a,R),\quad b_\alpha\mapsto\lambda b_\alpha,
\quad D\mapsto D,\quad Q_\alpha\mapsto\lambda^{-1}Q_\alpha.
\]
After expansion into homogeneous words, finite Gram matrices transform by diagonal congruence while \(M_N\mapsto\lambda^6M_N\). Conditional on an initial compatible finite-moment zero mode, this has a quantum realization through
\[
(U_\lambda\Psi)(Z)=\lambda^{-d/2}\Psi(Z/\lambda),\qquad d=9(N^2-1),
\]
\[
Q_{\alpha,\lambda}=\lambda^{-1}U_\lambda Q_\alpha U_\lambda^\dagger
=K_\alpha+\lambda^{-3}V_\alpha.
\]
The corresponding Hamiltonian is \(T+\lambda^{-6}V_{\rm bos}+\lambda^{-3}F\), on transported domains. The interaction coefficient changes. Consequently this dilation tests the restricted algebra only and supplies no counterexample to fixed-coupling BFSS.

## Unsigned terms that cannot be discarded

For \(\alpha\ne\beta\), put \(R_{\alpha\beta}=\{Q_\alpha,b_\beta\}\) and \(S_{\alpha\beta}=qR_{\alpha\beta}-2ib_\alpha b_\beta/N\). The exact norm relation is
\[
\langle q^2R_{\alpha\beta}^2\rangle+\frac{\langle a^2\rangle}{N^2}
-\frac{2i}{N}\langle q\{R_{\alpha\beta},b_\alpha b_\beta\}\rangle
=\frac{\langle A^2\rangle}{N^2}.
\]
The interference is real and unsigned. Removing it would invalidate the proposed positive estimate.

The Clifford contractions are \(\sum_\beta b_\beta b_\alpha b_\beta=-7ab_\alpha\), with the other two delta contractions equal to \(8ab_\alpha\). Since \(a\) is not a function of \(q\), its dressing adds a genuine term: for \(c_\alpha=b_{\alpha,h^2}\),
\[
\{Q_\alpha,af(q)b_\alpha\}
=\frac1N\left[\frac{\{af(q),D\}}2-if(q)[c_\alpha,b_\alpha]\right].
\]
The last term is an unsigned Hermitian fermion bivector. Alternating cubic words remain independent, with \((ib_\beta b_\gamma b_\delta)^2=a^3/8\) for distinct indices, and introduce off-diagonal correlators rather than an established positive restoring term.

Exact finite-\(N\) cyclicity also retains joint multi-trace expectations. For \(\Pi=P/N\) and coordinate words \(U,V\),
\[
\langle\operatorname{tr}(Z^IU\Pi^JV)-\operatorname{tr}(U\Pi^JVZ^I)\rangle
=i\delta_{IJ}\bigl[\langle\operatorname{tr}U\operatorname{tr}V\rangle
-N^{-2}\langle\operatorname{tr}(UV)\rangle\bigr].
\]
The explicit \(N^{-2}\) subtraction gives no bound on the connected double trace. Replacing the joint expectation by a product would add a factorization hypothesis.

## Evidence and references

The supplied exact checks address canonical-ordering weights, the cubic Clifford coefficient \(-7\), commuting-orbit normalization \(2/99\), finite-rank fermionic constants, and the restricted dilation. They do not prove domain control or the missing upper estimate. Under the earlier source-certificate assumptions, that estimate would be useful because
\[
K_N(s)\le sN^2M_N+\frac{b}{64}sN^2\,2^{-2N^2},\qquad b=8/9.
\]
At \(s=\sigma N^{-4/3}\), the unresolved rate \(M_N=O(N^{-4/3})\) would imply \(K_N(s)=O(N^{-2/3})\).

The archived primary-source discussion cites [Lin and Zheng, arXiv:2410.14647v3](https://arxiv.org/html/2410.14647v3) for the planar cyclicity setting, and [Lin, arXiv:2302.04416](https://arxiv.org/html/2302.04416) for finite-\(N\) Clifford trace corrections. It also records [arXiv:2511.08560v3](https://arxiv.org/html/2511.08560v3) on continuous-time two-point positivity and [arXiv:2507.21007v3](https://arxiv.org/html/2507.21007v3) on bosonic models. None is used as a proof of this BFSS mixed-moment upper bound. The literature assessment is a dated, bounded check, not an exhaustive priority claim.
