# Findings on BMN branch selection and weighted transfer

Author: Yicheng Pan  
Date: 6 October 2026  
Status: Provisional research summary with conditional analytic conclusions

The branch-selection argument gives fixed-rank unweighted convergence, conditional on the existence of the specified BFSS zero mode and the standard operator realization. A unique BFSS kernel also permits an intrinsic compact-localization selector. The quantitative weighted comparison remains unresolved: the established overlap scale and the earlier finite-mass concentration certificate give incompatible sufficient mass windows under order-one moment bounds. This is a limitation of the estimates, not a no-go theorem for BFSS concentration. No human expert review was supplied. Finite algebra checks are not independent human certification.

## Operator setting and spectral conclusions

Work in the physical SU(N) Hilbert space with the free U(1) center removed. Use \(\operatorname{tr}=\operatorname{Tr}/N\), kinetic term \(-\Delta/(2N)\), and \(\rho^2=\operatorname{tr}\sum_I Z_I^2\). Assume compatible self-adjoint supersymmetric realizations, the usual common compact smooth physical core, and local elliptic regularity. Write \(P_m=\mathbf1_{\{0\}}(H_m)\) for the projection onto the entire BMN kernel; no finite-mass vacuum uniqueness is assumed.

The unitary multiplet conditions and descendant increments give

\[
H_m\ge\frac m{12}(1-P_m),\qquad
H_m\big|_{\text{SO(3)×SO(6) singlets}}
\ge\frac m3(1-P_m)\big|_{\text{singlets}}.
\]

The singlet argument includes descendants: below \(m/3\), only the low-energy atypical branch can occur; SU(2) singlets require an even raising level, and neither the nontrivial lowest component nor the possible level-two component is an SU(4) singlet. Shortening removes components rather than creating a missing singlet. An optional sharpening of the global bound to \(m/6\) uses the physical global-group quotient \((\operatorname{Spin}(6)\times\operatorname{Spin}(3))/\mathbb Z_2\); it is not needed for the singlet estimate.

The protected \((0,2,0|0|0)\) multiplet has a scalar at \(2m/3\) for every \(N\ge2\). Hence

\[
\frac m3\le\operatorname{gap}_{\rm singlet}(N,m)\le\frac{2m}3.
\]

A rank-growing lower bound for the full singlet gap cannot improve the comparison. This does not establish any nonzero overlap of a particular BFSS vector with the protected excitation. An improvement specific to that vector needs spectral-overlap information.

These deductions use [Dasgupta, Sheikh-Jabbari and Van Raamsdonk, Sections 2–3 and 6.1](https://arxiv.org/html/hep-th/0207050v3). The relevant lowest-energy and unitarity formulas are equations (5) and (8) in that HTML version, versus the different numbering in the [PDF](https://arxiv.org/pdf/hep-th/0207050).

## Projection estimate and form-domain qualification

Let \(\Omega\) be a normalized Spin(9)-singlet BFSS zero mode and \(R_2=\langle\rho^2\rangle_\Omega<\infty\). The mass deformation is \(H_m=H_0+mV_1+m^2V_2\), with both the Myers and fermion terms in \(V_1\). The mass-linear supercharges and their sum-of-squares form give

\[
\mathfrak h_m[\Omega]=m^2\langle V_2\rangle_\Omega
=\frac{N^2m^2R_2}{36}.
\]

This is a quadratic-form identity, not an assertion that \(\Omega\) is in the operator domain of \(H_m\). Finite \(R_2\) controls the mass-linear charge multipliers. It does not, by itself, justify a separate uncut cubic Myers expectation. The form argument and radial cutoffs avoid that extra integrability assumption. The factor \(N^2\) follows from the trace and kinetic normalization.

With leakage \(\epsilon_m=\|(1-P_m)\Omega\|^2\), the singlet gap implies

\[
\epsilon_m\le\frac{N^2mR_2}{12}.
\]

When \(P_m\Omega\ne0\), define the normalized projected branch

\[
\Phi_{\rm proj}=\frac{P_m\Omega}{\|P_m\Omega\|},\qquad
\|\Phi_{\rm proj}-\Omega\|^2
=2(1-\sqrt{1-\epsilon_m})
\le\frac{N^2mR_2}{6}.
\]

Thus \(O(N^2mR_2)\) is a squared-norm or leakage bound. The norm bound is \(O(N\sqrt{mR_2})\). No uniqueness of either kernel is needed for this construction, but it uses an already specified BFSS zero mode and does not prove its existence.

The charge formulas are supported by [Matrix Perturbation Theory for M-theory on a PP-Wave, Appendix B](https://arxiv.org/pdf/hep-th/0205185), with another superalgebra convention in [Kim and Park, Section 2](https://arxiv.org/pdf/hep-th/0207061).

## Qualitative convergence and the separate intrinsic selector

At fixed N, a cutoff proof removes the radius-moment hypothesis for qualitative convergence. For \(u_L=\chi(\rho/L)\Omega\), put \(t=N^2m\) and \(L=t^{-1/2}\). The localization and mass terms satisfy

\[
\|(1-P_m)u_L\|^2
\le\frac{3}{2N^2mL^2}\langle[\chi'(\rho/L)]^2\rangle_\Omega
+\frac{N^2m}{12}\langle\rho^2\chi(\rho/L)^2\rangle_\Omega.
\]

The first term vanishes with the escaping shell probability. The second tends to zero by dominated convergence, since \((\rho^2/L^2)\chi(\rho/L)^2\le4\). Together with \(u_L\to\Omega\), this gives \(P_m\Omega\to\Omega\) and \(\Phi_{\rm proj}\to\Omega\) strongly, without a rate or radius moment. The corresponding conclusion for arbitrary BFSS zero modes follows from the global gap and the charge-form inequality. Testing weak limits on the common core then yields \(P_m\to P_0\) strongly on the full Hilbert space.

If additionally \(\ker H_0=\mathbb C\Omega\), local elliptic compactness for a compactly supported smooth radial weight \(0\le\chi\le1\), with \(a=\langle\chi\rangle_\Omega>0\), yields

\[
\|\chi(P_m-P_0)\|\to0,\qquad
\|P_m\chi P_m-aP_0\|\to0.
\]

The unique largest eigenline of \(P_m\chi P_m\) therefore defines an intrinsic localized branch \(\Phi_{\rm loc}\to\Omega\), up to phase. The orthogonal ground-state complement escapes fixed compact regions. This prescription does not require explicit knowledge of \(\Omega\), although its proof assumes the unique BFSS kernel. Its finite-mass vector can depend on \(\chi\).

**The two selectors must remain distinct.** The localized branch has qualitative fixed-N convergence only. The displayed quantitative projection error is established for \(\Phi_{\rm proj}\), not for \(\Phi_{\rm loc}\). An interpolation inequality can use either vector's actual norm error, but the explicit mass/rank rate below uses only \(\Phi_{\rm proj}\).

## Weighted interpolation and incompatible sufficient windows

Set \(A_2=q_h\), \(A_3=\rho q_h\), so that \(|A_k|\le\rho^k\). For \(\Phi=\Phi_{\rm proj}\), \(\delta=\|\Phi-\Omega\|\), and \(M_p(u)=\langle\rho^p\rangle_u\), Hölder gives, for \(p>2k\),

\[
\|A_k(\Phi-\Omega)\|
\le\delta^{1-2k/p}
\bigl(\sqrt{M_p(\Phi)}+\sqrt{M_p(\Omega)}\bigr)^{2k/p}.
\]

Both tails matter. Equivalently, a split at \(\rho=L\) bounds the same norm by

\[
L^k\delta+L^{k-p/2}
\bigl(\sqrt{M_p(\Phi)}+\sqrt{M_p(\Omega)}\bigr).
\]

A BFSS moment alone does not control the BMN tail. At the endpoint \(p=2k\), bounded moments alone do not imply uniform integrability; an explicit tail modulus can replace the stronger moment. In particular, a uniform sixth moment does not suffice for degree-six weighted convergence.

For a fixed \(p>2k\), order-one bounds on \(R_2\) and both p-moments, and \(m=N^{-\alpha}\), the squared-error certificate has order

\[
N^{(2-\alpha)(1-2k/p)}.
\]

To guarantee \(O(N^{-4/3})\) by this estimate requires

\[
\alpha\ge2+\frac{4p}{3(p-2k)}.
\]

The candidate BFSS exterior result in the associated research gives, at most and conditional on its analytical validity, fixed-N moments for \(p<9\). For every **fixed** \(6<p<9\), the threshold for \(k=3\) is strictly greater than 6. For every **fixed** \(4<p<9\), the threshold for \(k=2\) is strictly greater than \(22/5\). Those numbers are limiting infima as \(p\uparrow9\), not attained endpoint claims. The candidate BFSS result supplies neither uniform-in-N moments nor the projected BMN moments.

By contrast, the earlier finite-mass bound is

\[
\langle\rho^2q_h^2\rangle_\Phi
\le\frac{M_4(\Phi)}{N^2m}
+\frac{15\langle\rho_6^2\rangle_\Phi}{2N^4m^2}.
\]

Using only order-one upper bounds on its moments gives powers \(N^{\alpha-2}\) and \(N^{2\alpha-4}\). Together they guarantee the target rate only for \(\alpha\le2/3\), disjoint from the preceding interpolation windows. Moments that decrease with N, a sharper state-specific comparison, or new tail information could change this conclusion. The windows describe these certificates, not necessary mass laws for actual states.

## Why ordinary spectral convergence is insufficient

The abstract \(\ell^2\) example has \(H_0e_k=k^{-2}e_k\) for \(k\ge1\), \(H_0e_0=0\), and \(Re_k=ke_k\), \(Re_0=e_0\). Along \(m=j^{-2}\), start with positive eigenvalues \(k^{-2}+m^2k^2\) and rotate the ground vector to

\[
\phi_m=\sqrt{1-m}\,e_0+\sqrt m\,e_j.
\]

The resulting operators have compact resolvent at positive m, an exact gap \(2m\), strong-resolvent convergence, ground-projection norm error \(\sqrt m\), and Rayleigh error \(2m^2\). Nevertheless

\[
\langle R^p\rangle_{\phi_m}=1-m+m^{1-p/2},\qquad
\|R^k(\phi_m-e_0)\|^2
=(\sqrt{1-m}-1)^2+m^{1-k}.
\]

Even the bounded second moments fail to converge to the limiting second moment, while the sixth moments diverge. With mixing probability \(m^3\) instead, the sixth moment stays bounded at \(2-m^3\), yet the degree-six weighted error tends to one. This is an abstract insufficiency example, not a BFSS counterexample. Norm-resolvent convergence is neither claimed nor present in the first construction.

## Moment justification and remaining scope

At fixed N and \(m>0\), [Boulton, García del Moral and Restuccia, Section 3 and Theorem 3](https://arxiv.org/html/1011.4791#S3), provide quadratic exterior growth of the BMN bosonic potential. The fermion matrix contribution is at most linear, so the full potential obeys \(V\ge c(N,m)\rho^2-C(N,m)\), with \(c(N,m)>0\). Weighted eigenfunction localization then yields finite polynomial moments. This relies on coercivity and the eigenfunction argument, not on compact resolvent alone, and supplies no uniform mass/rank tail bound.

The finite checks support coefficient identities, representation-label exclusions, interpolation exponents, and finite instances of the abstract example. They cannot establish the infinite-dimensional core and compactness assumptions, BFSS existence or uniqueness, or uniform BMN tails. The surviving positive result is conditional fixed-rank unweighted transfer. The weighted convergence and the desired large-rank BFSS upper bound remain open.
