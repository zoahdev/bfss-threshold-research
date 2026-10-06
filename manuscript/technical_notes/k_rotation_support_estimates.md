# Corrected rotation algebra and support estimates {#app:rotation}

This appendix records the algebra, normalization and domain extension
used in Section 9. The rotation anticommutator and
kernel-invariance theorem are due to the cited prior work; the
quantitative use of a bounded internal radius is the estimate needed
here.

## Two charge conventions and two summation scopes

Retain the kinetic-one Hamiltonian $h$. Let $\widetilde q$ denote the
convention
$$\{\widetilde q_\alpha,\widetilde q_\beta\}=\delta_{\alpha\beta}h,
 \qquad\sum_{\alpha=1}^{16}\left\lVert \widetilde q_\alpha g\right\rVert^2=8\mathfrak h[g]$$ on
the physical core. The manuscript's baseline charges are
$q=\sqrt2\widetilde q$ and have stack coefficient $16$. For a fixed
$j=(u,v)$ the primitive of [Hasler and Hoppe, Lemma 2(c)](https://arxiv.org/abs/hep-th/0211226) is
$$\widetilde a_{j,\alpha}=\frac1{16}(X_u\Gamma_v-X_v\Gamma_u)_{\alpha\epsilon}\theta_\epsilon
 +\frac1{56}\sum_{w\notin\{u,v\}}X_w(\Gamma_w\Gamma_{uv})_{\alpha\epsilon}\theta_\epsilon.
 \label{eq:expandedprimitive}$$ The color index is contracted in each
summand. This follows from $(5b+2c)/7$ because
$\Gamma_u\Gamma_{uv}=\Gamma_v$ and $\Gamma_v\Gamma_{uv}=-\Gamma_u$.

All coefficient matrices are real. The first two are symmetric grade-one
matrices, the others antisymmetric grade-three matrices. They are
mutually orthogonal in the Frobenius inner product and each has squared
Frobenius norm $16$. Each $\widetilde a_{j,\alpha}$ is a real linear
combination of Majoranas, so its square is scalar by the CAR.
Consequently $$\begin{aligned}
 \sum_\alpha\widetilde a_{j,\alpha}^2
 &=\frac12\left[\frac{16}{16^2}(|X_u|^2+|X_v|^2)
          +\frac{16}{56^2}\sum_{w\notin\{u,v\}}|X_w|^2\right]I\\
 &=\left[\frac{|X_u|^2+|X_v|^2}{32}
          +\frac{\sum_{w\notin\{u,v\}}|X_w|^2}{392}\right]I.
\end{aligned}$$ For several blocks, concatenate color coordinates; no
color-dimension factor occurs. A fixed coordinate belongs to eight of
the $36$ pairs and is outside the other $28$, giving
$$\sum_{u<v}\sum_\alpha\widetilde a_{(u,v),\alpha}^2
 =\left(\frac8{32}+\frac{28}{392}\right)\alpha^2I
 =\frac9{28}\alpha^2I.\label{eq:allsum}$$ Thus $1/32$ is the bound for
one generator, while $9/28$ is the exact coefficient after summing all
generators. They are not alternative estimates for the same sum.

Rescale reciprocally: $$q_\alpha=\sqrt2\widetilde q_\alpha,\qquad
 a_{j,\alpha}=\widetilde a_{j,\alpha}/\sqrt2,\qquad
 J_j=\sum_\alpha\{q_\alpha,a_{j,\alpha}\}.$$ The fixed-generator bound
becomes $\alpha^2/64$, and
K.5 becomes $9\alpha^2/56$. The products $8(1/32)$
and $16(1/64)$ agree. Rescaling the charge alone would change the
generator identity and is not allowed.

## Direct Clifford verification of the identity

Write $\widetilde a_\alpha=X_w(M_w)_{\alpha\epsilon}\theta_\epsilon$ for
a fixed pair $(u,v)$. In the real gamma convention the coefficient
matrices obey $$\begin{aligned}
 \operatorname{Tr}(\Gamma_t^TM_w)&=\delta_{wu}\delta_{tv}-\delta_{wv}\delta_{tu},\\
 \sum_w\Gamma_w^TM_w&=\tfrac14\Gamma_{uv},\\
 \operatorname{Tr}(M_w^T\Gamma_{st})&=0.
\end{aligned}$$ The first identity yields the orbital rotation, the
second the spin contribution $-i\theta\Gamma_{uv}\theta/4$, and the last
removes the interaction anticommutator. These are exact finite Clifford
identities. The included integer-matrix program checks them for all $36$
pairs and all indicated indices. It uses a self-contained real symmetric
Spin(9) representation constructed from the octonion multiplication
table. This test verifies the finite identities only; integration by
parts and closed-domain statements require the arguments in the text.

## A stronger Casimir variant

The weaker coefficient $1/4$ in
Lemma 9.2 is sufficient for the manuscript. For comparison,
the all-generator identity proves
$$H_I[g]\ge\frac7{9R^2}\left\lVert (1-P_I)g\right\rVert^2
 \qquad\text{when }\operatorname{supp} g\subset\{\alpha\le R\}.\label{eq:casimirball}$$
Use the graded sum of block supercharges, or equivalently a blockwise
charge index, with stack coefficient $8$. Its squares add to the
complete $H_I$. Let $C_I=\sum_j(J_j^I)^2$ and initially take a physical
smooth vector in a Casimir eigenspace $C_Ig=\lambda g$, $\lambda>0$. Put
$E=H_I[g]$ and $K=9/28$. Rotational invariance of the complete form
gives $$\sum_j\left\lVert J_j^Ig\right\rVert^2=\lambda\lVert g\rVert^2,
 \qquad\sum_jH_I[J_j^Ig]=\lambda E.$$ Individual supercharges need not
commute with rotations; only their averaged square is used. Pair the
rotation identity with $J_j^Ig$, sum over $j$, and integrate by parts on
the core. The first resulting term is bounded by
$\sqrt{8\lambda E}\sqrt{KR^2\lVert g\rVert^2}$. For the other, pointwise
Cauchy--Schwarz and the fact that each primitive square is scalar give
$$\sum_\alpha\left\lVert\sum_j\widetilde a_{j,\alpha}(X)(J_j^Ig)(X)\right\rVert^2
 \le K\alpha(X)^2\sum_j\lVert(J_j^Ig)(X)\rVert^2.$$ That term has the
same bound. Therefore
$$\lambda\lVert g\rVert^2\le2\sqrt{8K}\,R\sqrt{\lambda E}\lVert g\rVert,
 \qquad E\ge\frac{7\lambda}{72R^2}\lVert g\rVert^2.$$ In the generator
convention used here, a dominant $B_4$ weight has Casimir
$$\lambda_C=\sum_{i=1}^4\lambda_i(\lambda_i+9-2i),\qquad
 \lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4\ge0,$$ with all
coordinates integral or all half-integral. The smallest positive integer
case $(1,0,0,0)$ has Casimir $8$, and the smallest half-integral case
$(1/2,1/2,1/2,1/2)$ has Casimir $9$. Summing positive Casimir sectors
proves K.10.

The rotation-invariant ball preserves all compact-group projections. At
finite Casimir cutoff the generators are bounded angular operators, and
the projected smooth physical core remains radially compact. Invariant
nonnegative forms split orthogonally over the Casimir decomposition.
Finite cutoff, approximation in the form norm, and a limit therefore
extend the result to the closed form domain. For support in a closed
ball use a slightly larger open radius and decrease it to $R$. Spectator
Hilbert spaces pass through the same argument by finite sums and
closure. Neither $\widetilde a g$ nor $Jg$ is asserted to lie in the
Hamiltonian operator domain for a general form vector.

## Kernel invariance without an assumed positive moment

For completeness, the domain mechanism behind [Hasler and Hoppe, Theorem 1(a)](https://arxiv.org/abs/hep-th/0211226) is as
follows. The physical kernel is invariant under the compact rotation
group. Decompose it into isotypes so that $J_j$ is bounded on each
finite-dimensional representation factor. Choose a smooth radial cutoff
$\chi_R$ that is one in a ball and whose derivative is supported where
$R<\rho<3R$. In the generator identity, test with two kernel vectors of
finite isotypic type and move the charge through $\chi_R$. The surviving
shell terms have bounds of the form $$C\left\lVert \phi\right\rVert_{\{R<\rho<3R\}}
  \left\lVert \Psi\right\rVert_{\{R<\rho<3R\}},$$ since $[\widetilde q,\chi_R]=O(R^{-1})$
and $\widetilde a=O(R)$ on that shell. The compatible
maximal/self-adjoint realization and physical-core approximation are the
ones in the cited theorem. The bound tends to zero by $L^2$
integrability alone. Taking $\phi=J_j\Psi$ within each isotype gives
$J_j\Psi=0$. Completing the compact-group decomposition proves
invariance of the full kernel. This is an explanation of the cited prior
theorem, not a new existence or domain theorem.
