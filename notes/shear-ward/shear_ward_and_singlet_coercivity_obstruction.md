# BFSS shear Ward identity and singlet-sector energy obstruction

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


6 October 2026. This note does not prove or disprove the rank-uniform zero-mode quadrupole estimate. The elementary shear spectral moments were already present in the source-moment route; they are recorded only to fix signs. The additional useful outputs are the nonlinear identity with its unsigned term and actual-Hamiltonian singlet trial packets showing why a sector-wide energy coercivity substitute cannot work.

## 1. Conventions and exact nonlinear identity

Write

\[
H=T+V+F,\quad T={1\over2N}\sum_{i,A}(P_i^A)^2,\quad
V=-{N\over4}\sum_{ij}\operatorname{Tr}[Z_i,Z_j]^2,
\]

with the fermionic multiplication operator \(F=-\frac12\operatorname{Tr}\psi\Gamma^i[Z_i,\psi]\). Fix real symmetric traceless \(h\), \(\operatorname{Tr}_9h^2=1\), and set

\[
q={1\over N}\sum_A Z^A\!\cdot hZ^A,\quad
u=hZ,\quad a={|\nu|^2\over N},\quad
c={1\over N}\sum_A Z^A\!\cdot h^3Z^A,
\quad D={1\over2}\{\nu,P\}.
\]

The summed divergence of \(\nu\) is zero. Thus \(D=\nu\cdot P\) on the usual core. Define the shear derivative \(\delta_h=\nu\cdot\nabla\), and its stress

\[
W=i[D,H]=-2T_h+\delta_h(V+F),\qquad
T_h={1\over2N}P\cdot hP.
\]

The exact commutators are

\[
[D,q]=-2ia,\qquad [D,a]=-2ic,\qquad
[H,q]=-{2i\over N^2}D.
\tag{1}
\]

For real smooth \(f\), let \(A_f=\frac12\{f(q),D\}\). On a normalized zero mode, whenever the commutator expectation is justified by core cutoffs,

\[
\boxed{
\frac12\langle\{f(q),W\}\rangle
={2\over N^2}\left\langle D f'(q)D-c f''(q)-a^2f'''(q)\right\rangle .}
\tag{2}
\]

Proof: \(i[H,f(q)]=N^{-2}\{D,f'(q)\}\) and \(i[H,D]=-W\). Consequently

\[
i[H,A_f]={1\over2N^2}\{\{D,f'\},D\}-{1\over2}\{f,W\}.
\]

Use \(\{\{D,f'\},D\}=4Df'D+[D,[D,f']]\) and
\([D,[D,f']]=-4(cf''+a^2f''')\).

An equivalent differential expression, with \(d_A=N^2-1\), is

\[
0=\left\langle {1\over N}P\cdot f(q)hP
+{2\over N^2}P\cdot f'(q)\nu\nu^TP
-f(q)\delta_h(V+F)
-{1\over N^2}\left[d_Af'+4cf''+2a^2f'''\right]\right\rangle.
\tag{3}
\]

The quantum correction follows from
\(\Delta\operatorname{div}(f(q)\nu)=4d_Af'/N+16cf''/N+8a^2f'''/N\).

### The precise missing sign

For \(f'\ge0\), \(Df'D\) is nonnegative. The left side of (2), however, is a weighted stress expectation, not a positive multiple of a quadrupole moment. The traceless kinetic tensor \(T_h\) is indefinite. In a basis diagonalizing \(h\), \(\delta_hV\) weights positive pair potentials by \(2(\lambda_i+\lambda_j)\), with both signs in general, and \(\delta_hF\) is also indefinite. In (3), the positive rank-one deformation tensor \(2f'\nu\nu^T/N\) is accompanied by the indefinite tensor \(fh\). The derivative terms \(cf''+a^2f'''\) have no uniform favorable sign for a clipping function either.

In particular, \(f=q\) gives only

\[
\frac12\langle\{q,W\}\rangle={2\over N^2}\langle D^2\rangle.
\tag{4}
\]

Choosing a tail-adapted monotone \(f\) changes the weighted stress one must control; it does not eliminate that input. No upper estimate for \(\langle a\mathbf1_{|q|>L}\rangle\) follows from (2) plus positivity alone.

There is also an exact, useful reformulation of the target. For a Lipschitz scalar \(g\) with \(g(q)\Omega\in D(Q)\),

\[
\langle g(q)\Omega,Hg(q)\Omega\rangle
={2\over N^2}\mathbb E[a\,g'(q)^2].
\tag{5}
\]

Taking \(g(x)=\operatorname{sgn}(x)(|x|-L)_+\), with domain limits, identifies the desired weighted tail with the energy of the unclipped remainder. This identification as a Hilbert-space energy additionally needs \(q\Omega\in L^2\); under only the second-radius-moment assumption one must keep bounded truncations. Equation (5) identifies what needs bounding but supplies no upper bound for it.

## 2. Linear shear identities, for comparison only

Diagonalize \(h\), with eigenvalues \(\lambda_i\). Define \(V_{ij}=-(N/2)\operatorname{Tr}[Z_i,Z_j]^2\), \(i<j\). In a Spin(9)-singlet zero mode, the ordinary virial relations are \(\langle V\rangle=\langle T\rangle\), \(\langle F\rangle=-2\langle T\rangle\). Therefore

\[
\langle e^{itD}He^{-itD}\rangle=\langle T\rangle
\left[{1\over9}\sum_i e^{-2t\lambda_i}
+{1\over36}\sum_{i<j}e^{2t(\lambda_i+\lambda_j)}
-{2\over9}\sum_i e^{t\lambda_i}\right].
\tag{6}
\]

The entire unitary-shear energy curve has a universal shape multiplied by one scalar \(\langle T\rangle\). Its second derivative gives

\[
\langle[D,[H,D]]\rangle=\langle T\rangle,
\qquad \langle D\Omega,HD\Omega\rangle=\frac12\langle T\rangle.
\tag{7}
\]

For the spectral measure of \(q\Omega\), write \(m_j=\langle q\Omega,H^jq\Omega\rangle\). Then

\[
m_1={2\langle a\rangle\over N^2},\qquad
m_2={4\langle D^2\rangle\over N^4},\qquad
m_3={2\langle T\rangle\over N^4}.
\tag{8}
\]

Cauchy and Robertson give

\[
\langle D^2\rangle\le {N\over2}\sqrt{\langle a\rangle\langle T\rangle},
\qquad
\operatorname{Var}(q)\ge {2\langle a\rangle^{3/2}\over N\sqrt{\langle T\rangle}}.
\tag{9}
\]

This is a lower variance estimate. If radius and kinetic energy have their expected sizes, it is consistent with planar variance. It cannot be reversed into concentration. All identities here require the relevant finite moments and justified commutator limits; the second-radius-moment assumption alone is not being asserted to justify every displayed unbounded identity.

## 3. Actual SU(2) singlet annular packets

### Claim

For the actual \(N=2\) BFSS Hamiltonian, there are normalized smooth compactly supported gauge- and Spin(9)-singlet test states \(\Psi_R\), escaping to infinity, such that

\[
\langle\Psi_R,H\Psi_R\rangle\le C R^{-2},
\qquad
\mathbb E_{\Psi_R}[a_h\mathbf1_{|q_h|>L}]\ge c_hR^2,
\qquad
\mathbb E_{\Psi_R}q_h^2\asymp_h R^4
\tag{10}
\]

for every fixed finite \(L\) and all sufficiently large \(R\). Constants in this statement concern the fixed rank \(N=2\). These are trial states of BFSS, not zero modes and not an arbitrary replacement probability law.

### Construction and error estimate

Use normalized SU(2) color generators. Near the nonzero commuting cone, exact tubular coordinates have the form

\[
Z_i^A=r e^A n_i+r^{-1/2}y_i^A,
\quad |e|=|n|=1,\quad e_Ay_i^A=0,\quad n_iy_i^A=0.
\tag{11}
\]

There are sixteen transverse real coordinates. The leading supersymmetric transverse oscillator has a Gaussian vacuum \(\phi_0(e,n,y)\) annihilated by each fast supercharge. One can choose it invariant under simultaneous gauge and Spin(9) transformations, and even under \((e,n)\mapsto(-e,-n)\). Its Cartan-fermion angular component is the contraction \(n_i n_j|ij\rangle\) with the symmetric traceless \(44\). The existence, invariance and parity of this fast-vacuum section are standard explicit finite-dimensional facts; see the primary references below.

Pick nonzero \(\chi\in C_c^\infty((1,2))\). Multiply

\[
\chi(r/R)\phi_0(e,n,y)
\]

by a smooth transverse cutoff equal to one for \(|y|\le R^\delta\) and zero for \(|y|\ge2R^\delta\), with any fixed sufficiently small \(\delta>0\), and then normalize. The coordinate volume is

\[
J(r,e,n,y)\,dr\,de\,dn\,dy,
\qquad J=r^2(1+o(1))
\]

on the Gaussian scale. Thus the normalization coefficient is \(\asymp R^{-3/2}\). The cutoff and coordinate double-cover identification preserve both symmetries. Extension by zero gives a smooth compactly supported physical test state because the radial and transverse cutoffs lie strictly inside the tubular chart.

Here is the estimate on the actual operator, rather than an assumption that its effective Hamiltonian is exact. Pull back a supercharge to these coordinates. Its coefficients have a regular Taylor expansion in \(r^{-3/2}y\):

\[
Q_\alpha=r^{1/2}Q_{0,\alpha}
+r^{-1}(B_\alpha r\partial_r+C_\alpha)
+r^{-5/2}\mathcal R_{r,\alpha}.
\tag{12}
\]

The first term kills \(\phi_0\). The radial cutoff has uniformly bounded \(r\partial_r\chi(r/R)\). Angular derivatives act on a smooth finite-dimensional equivariant section over compact spheres; transverse derivatives and coefficients give fixed polynomials times a Gaussian. In the cutoff region, \(r^{-3/2}|y|\to0\), so the denominators of the exact coordinate coefficients stay uniformly away from zero, and the Taylor remainder is bounded by finitely many Gaussian-weighted polynomial Sobolev norms. Those norms are finite and independent of \(R\). Derivatives of the transverse cutoff contribute only a polynomial in \(R\) times \(e^{-cR^{2\delta}}\). Consequently

\[
\|Q_\alpha\Psi_R\|\le C/R.
\]

Since \(Q_\alpha^2=H\) on gauge singlets in the present normalization, this proves the energy estimate in (10). It also supplies a form-Weyl sequence at zero in the invariant sector. No claim about an actual zero-mode asymptotic expansion or its unknown normalization is needed for this test-function construction.

### Quadrupole estimates

Orthogonality in (11) eliminates the cross term exactly:

\[
q_h={r^2\over2}n^Thn+{1\over2r}\sum_A(y^A)^Thy^A,
\qquad
 a_h={r^2\over2}n^Th^2n+{1\over2r}\sum_A(y^A)^Th^2y^A.
\tag{13}
\]

The bosonic probability of a Spin(9)-singlet state is rotationally invariant. For nonzero \(h\), choose a fixed positive-measure angular patch where both \(|n^Thn|\) and \(n^Th^2n\) exceed positive constants. On that patch, restrict the Gaussian variables to a fixed bounded set of positive probability. For \(r\in[R,2R]\), the first term in \(q_h\) exceeds any fixed threshold in absolute value, while \(a_h\ge c_hr^2\). This proves the lower bound in (10). The same argument and Gaussian moments prove \(\mathbb E q_h^2\asymp R^4\). More specifically, after normalization the angular averages obey

\[
\int_{S^8}n^Th^2n\,d\omega=1/9,
\qquad
\int_{S^8}(n^Thn)^2\,d\omega=2/99.
\]

Thus the leading tail coefficient agrees with the leading radius coefficient divided by nine; as \(R\to\infty\), almost all angles leave any fixed quadrupole threshold.

### Precisely what this rules out

No quadratic-form inequality such as

\[
a_h\mathbf1_{|q_h|>L}\le C(H+1)
\quad\text{or}\quad q_h^2\le C(H+1)
\tag{14}
\]

can hold throughout the physical Spin(9)-singlet sector, even at rank two. In particular, energy control and the correct singlet symmetries cannot replace the missing zero-mode concentration argument.

This does not disprove an estimate on the exact normalized zero mode. The packets do not satisfy the exact zero-mode Ward identities. It also does not, on its own, disprove a Poincare inequality restricted to scalar multiples of one specified zero mode; that would require additional information about that wavefunction.

There is a stronger continuity warning if a normalized zero mode \(\Omega\) with finite second radius moment is assumed, under the stated hypothesis. Normalize

\[
\widetilde\Psi_R=\Omega+R^{-1}\Psi_R.
\]

These are still pure physical singlets. They converge in norm to \(\Omega\), their energy is \(O(R^{-4})\), and their second radius moments remain bounded. Nevertheless their weighted quadrupole tail at any fixed \(L\) gains a positive order-one contribution from the annulus. The interference term is bounded by a constant times

\[
\left(\mathbb E_\Omega[\rho^2\mathbf1_{\rho\asymp R}]\right)^{1/2}\to0.
\]

Thus a small BPS residual plus a bounded second moment does not certify this unbounded weighted-tail observable. Exact zero-mode input or uniform integrability is essential.

## 4. Why unregulated anisotropic mass susceptibility is unstable

The same tube construction may be multiplied by an angular cutoff supported where \(t n^Thn<0\). This retains gauge invariance; Spin(9) is deliberately broken by the source. Angular derivatives cost only \(O(R^{-2})\) in energy. Therefore

\[
\inf\sigma(H+tq_h)=-\infty\qquad(t\ne0).
\tag{15}
\]

Indeed, the negative source expectation is of order \(-|t|R^2\), whereas the BFSS energy tends to zero. Every nonzero traceless \(h\) has eigenvalues of both signs.

Consequently ordinary isolated-ground-state analytic perturbation theory cannot be invoked for a two-sided anisotropic quadratic source at zero mass. A positive isotropic regulator

\[
H_{\mu,t}=H+N^2(\mu^2\rho^2/2+tq_h)
\]

restores stability only while \(\mu^2I/2+th\) is positive semidefinite, an interval of \(t\) shrinking like \(\mu^2\). At strictly positive regulator, a nondegenerate isolated ground state has the usual conditional susceptibility formula

\[
E_\mu''(0)=-2N^4\langle q_h\Omega_\mu,(H_{\mu,0}-E_\mu)^{-1}_{\perp}q_h\Omega_\mu\rangle.
\tag{16}
\]

Removing the regulator needs an independently proved uniform susceptibility and ground-state limit. Instability (15) does not itself prove that the formal reduced-resolvent matrix element in (16) diverges; that stronger claim is not made.

## Sources and attribution

- Fröhlich–Graf–Hasler–Hoppe–Yau, *Asymptotic Form of Zero Energy Wave Functions in Supersymmetric Matrix Models*, especially the tubular coordinates, supercharge expansion, fast oscillator and invariant/even section in sections 3–4: https://arxiv.org/html/hep-th/9904182 . The paper's all-order zero-mode theorem is explicitly a formal-series theorem; the packet argument above needs only its explicit local operator and leading finite-dimensional oscillator, together with a cutoff remainder estimate.
- Lin–Yin, *On the Ground State Wave Function of Matrix Theory*, sections 2.2–2.4 and 3.1: https://arxiv.org/html/1402.0055 . In particular, the Cartan fermions decompose into 44+84+128; the invariant angular factor uses the 44 and is Weyl-even.
- de Wit–Lüscher–Nicolai, *The Supermembrane Is Unstable*, Nucl. Phys. B 320 (1989) 135–159: https://doi.org/10.1016/0550-3213(89)90214-9 . This is the underlying rigorous continuous-spectrum mechanism; no new claim of priority is made.
- Lin, *Bootstrap bounds on D0-brane quantum mechanics*, for the ordinary BFSS virial/bootstrap context: https://arxiv.org/abs/2302.04416 .

## Honest conclusion

The nonlinear shear route stops at an unsigned weighted stress, and an energy-only coercivity replacement is excluded by actual singlet BFSS packets. None of this supplies a counterexample to the desired bound for exact normalized zero modes. Closing that bound still needs genuine control of their large-rank probability law or source-specific low-energy spectral weight, beyond the displayed Ward identities.


## 5. What can be recovered for positive-mass removal

There is a useful conditional compactness argument that separates the regulator-removal question from the genuinely rank-uniform estimate. At fixed rank suppose the physical zero mode is unique up to phase and has finite \(\langle\rho^2\rangle_\Omega=M_N\). Put \(H_\varepsilon=H+\varepsilon\rho^2\), and let \(\Omega_\varepsilon\) be any normalized ground state. The confining positive quadratic term makes the spectrum discrete. Variationally,

\[
0\le E_\varepsilon\le\varepsilon M_N,\qquad
\langle\rho^2\rangle_{\Omega_\varepsilon}\le M_N,\qquad
\|Q_\alpha\Omega_\varepsilon\|^2
=\langle H\rangle_{\Omega_\varepsilon}\le\varepsilon M_N.
\tag{17}
\]

The radius bound gives uniform spatial tightness at this fixed rank. Local elliptic estimates for the first-order supercharge give bounded local \(H^1\) norms, since its principal Clifford symbol is elliptic and its lower-order coefficients are bounded on each compact set. Rellich compactness and tightness therefore give strong \(L^2\) subsequential convergence. Closedness of \(Q_\alpha\) makes each normalized limit a zero mode. Uniqueness identifies it with \(\Omega\), up to phase. If arbitrarily small regulators had two orthogonal ground states, the same compactness argument would produce two orthogonal zero modes. Thus the regulated ground state is also simple for all sufficiently small \(\varepsilon\), at each fixed rank. No uniform-in-rank regulator threshold is obtained.

For the convention \(H_{\varepsilon,J}=H+\varepsilon\rho^2-Jq\), write \(\chi_{\varepsilon,N}=-E_\varepsilon''(0)\). Spectral Cauchy and the unchanged kinetic f-sum rule give

\[
\operatorname{Var}_{\varepsilon,N}(q)^2
\le {\langle a\rangle_{\varepsilon,N}\chi_{\varepsilon,N}\over N^2}.
\tag{18}
\]

Consequently a genuine bound

\[
\langle a\rangle_{\varepsilon,N}\chi_{\varepsilon,N}
\le C N^{-2/3}
\tag{19}
\]

for sufficiently small regulators, with \(C\) rank-independent, gives the older variance target \(\langle q^2\rangle_\Omega\le C^{1/2}N^{-4/3}\). Strong \(L^2\) convergence and Fatou suffice to transfer this upper bound; convergence of fourth moments is not necessary. This is a variance-route conclusion, not a claim that variance at this rate implies the particular weighted clipping-tail condition.

Without uniqueness, the regulator selects some normalized zero mode, and this argument does not identify it with an arbitrarily specified one. Without (19), stability and compactness supply no rank-uniform variance rate. A uniform radius bound and \(\chi_{\varepsilon,N}=O(N^{-2/3})\) are sufficient separate hypotheses for (19), but only their product is needed.

## 6. The proposed supercharge/Clifford shortcut

For each spinor index set

\[
b_\alpha={iN\over2}[Q_\alpha,q]
=N^{-1/2}\operatorname{Tr}(h_{ij}Z_i\Gamma^j_{\alpha\beta}\psi_\beta).
\]

On the physical sector,

\[
\{Q_\alpha,b_\alpha\}={D\over N},\qquad
\sum_{\alpha=1}^{16}\{Q_\alpha,b_\alpha\}={16D\over N},\qquad
\{b_\alpha,b_\beta\}=a\delta_{\alpha\beta}.
\tag{20}
\]

The first identity is simply \(\{Q,[Q,q]\}=[Q^2,q]\); the second is its sum, and the last is the Clifford relation. Scalar polynomial or clipped dressings obey the exact identity

\[
\{Q_\alpha,b_\alpha f(q)\}={1\over2N}\{f(q),D\}.
\tag{21}
\]

Thus these dressings generate precisely the shear operator already used in (2). Their Clifford squares carry \(a\), not a new small factor of \(N\).

Including the radial \(b_{0,\alpha}\), obtained by replacing \(h\) with \(I\), gives

\[
b_{0,\alpha}^2=\rho^2/2,\quad
\{b_{0,\alpha},b_\alpha\}=q,\quad
[b_{0,\alpha},b_\alpha]^\dagger[b_{0,\alpha},b_\alpha]
=\rho^2a-q^2\ge0.
\tag{22}
\]

This is just the pointwise Cauchy bound \(q^2\le\rho^2a\). It has no favorable rank power. These calculations settle the suggested diagonal-supercharge and Clifford-square family, not every possible higher-degree fermionic bootstrap identity; no completeness or general no-go theorem for the latter is claimed.
