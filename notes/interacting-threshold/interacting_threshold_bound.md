# Interacting BFSS threshold: a conditional finite-rank bound and its endpoint obstruction

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


6 October 2026. This note proves implications for the actual interacting BFSS operator **conditional on the candidate exterior inequalities in the current manuscript**. It does not certify those exterior inequalities, prove existence of a zero mode, or establish a large-N estimate. No free-channel substitution is used in Sections 1–6. Section 7 is an explicitly different comparison operator, not a counterexample to BFSS.

## Results

In kinetic-one canonical coordinates, let h=2H, r=|X|, X=√N Z, and ρ²=tr ΣZ_i², so r=Nρ. Let R₀ be an exterior radius for the candidate all-vector coefficient c=12<49/4 and put R=16 max(R₀,1). Then the actual Spin(9)-44 sector obeys the conditional **global** estimate

    h₄₄ ≥ 1/[2(R²+r²)].                                      (A)

The same proof gives h_nonsinglet ≥ 1/[4(R²+r²)]. This is an operator-form estimate on the indicated representation sectors, with no zero-mode-existence assumption. It makes the unknown rank dependence explicit through R_N.

If a normalized zero mode Ω exists, the candidate singlet exterior bound supplies all moments ⟨r^m⟩<∞ for m<9. For f=qΩ, (A) then gives

    χ = 2⟨f,H⁻¹f⟩ ≤ 8 N⁻⁴ [R²⟨r⁴⟩+⟨r⁶⟩] < ∞.             (B)

More strongly, for every 0≤β<5/2,

    ∫_(0,∞) E^(-β) dμ_f,H(E) < ∞,
    F_f,H(E) ≤ K_(N,β) E^β.                                  (C)

The same conclusions hold uniformly in sufficiently small positive isotropic regulators, with constants depending on fixed N. Neither uniqueness of the unregulated zero mode nor a controlled free-channel expansion is needed for this boundedness assertion. Uniqueness is needed if one wants to identify the regulated states with one particular chosen Ω on removal.

These are finite-rank improvements over power counting, conditional on the candidate manuscript. They do not give the endpoint β=5/2, rank-uniform K, or a limiting-absorption theorem at positive energies.

## 1. The relevant Spin(9) sector

The invariant zero-mode theorem implies every actual L² zero mode is a Spin(9) singlet. The traceless quadrupole is a tensor in the 44. Consequently qΩ, the resolvent (H+λ)⁻¹qΩ, and any spectral projection of qΩ are in the 44, unless the source vanishes.

The coefficient 121/4 applies to singlets and cannot be used on these vectors. In the two-block reference channel, orbital l=0 tensor a relative fermionic 44 already has total type 44. It has angular kinetic energy zero and only the nine-dimensional radial Hardy coefficient 49/4. The explicit source decomposition in the previous susceptibility audit shows its l=0 coefficient is nonzero. Thus assigning an l=2 barrier to all of qΩ is incorrect.

The larger coefficient remains useful on radial multiples of Ω, where it supplies source moments. The lower coefficient is used on the source resolvent itself. All estimates below act on the full physical 44 sector, including excited transverse oscillators, internal continua and their coupling. No projection onto a free or fast-vacuum channel is made.

## 2. The support-radius bound uses the interacting supercharges

Use the corrected Hasler–Hoppe rotation primitives and conventions in manuscript Appendix K. In kinetic-one normalization with the alternative charge stack ∑α||Q̃αu||²=8h[u],

    J_j = ∑α {Q̃α, ã_(j,α)},
    ∑_(j,α) ã_(j,α)² = (9/28) r² I.

The interaction anticommutators cancel in this exact identity. It is not a free approximation. On a Casimir eigenspace C₂u=λu, rotational invariance of the full form gives ∑j h[J_ju]=λh[u]. Pair the primitive identity with J_ju and sum. Cauchy–Schwarz gives, for support in r≤R,

    λ||u||² ≤ 2√(8·9/28) R √(λ h[u]) ||u||,
    h[u] ≥ [7λ/(72R²)] ||u||².                              (2.1)

Finite Casimir cutoffs and physical-core approximation give the closed-form statement; no operator-domain preservation by the primitives is asserted. The 44 has λ=18, hence

    h[u] ≥ 7/(4R²)||u||²  on the 44 with r≤R.                 (2.2)

The least nonzero Spin(9) Casimir is 8, giving 7/(9R²) for all nonsinglets. The CAR sum contains no color-dimension factor. The exterior radius will nevertheless carry rank dependence.

The underlying rotation identity and kernel-invariance theorem are prior results: Hasler–Hoppe, Lemma 2(c) and Theorem 1, https://arxiv.org/pdf/hep-th/0211226. Equations (2.1)–(2.2) are the quantitative use already detailed in the manuscript, followed here by a new IMS application.

## 3. Explicit globalization, with its IMS loss paid

Assume the manuscript's all-vector exterior estimate h[v]≥12||r⁻¹v||² for support outside R₀. Increase R₀ to at least 1 and set R=16R₀. Define the Lipschitz radial angle

    θ(r)=0                              r≤R₀,
    θ(r)=(π/2)((r−R₀)/(R−R₀))²          R₀<r<R,
    θ(r)=π/2                            r≥R.

Let χ_in=cosθ and χ_out=sinθ. Radial multiplication preserves each Spin(9) type. By IMS, (2.2), and the exterior estimate,

    h[u] ≥ ∫[ (7/(4R²))cos²θ + (12/r²)sin²θ − |θ′|² ] |u|².

Outside the transition the lower coefficients are 7/(4R²) and 12/r². In the transition put t=(r−R₀)/(R−R₀), s=r/R=(1+15t)/16. Since sin(πt²/2)≥t² and π²<10, the coefficient times R² is at least

    (7/4)(1−t⁴) + 12t⁴/s² − (512/45)t².

It is ≥1/2 for 0≤t≤1. An exact algebraic certificate is that

    P(t) = [(7/4)(1−t⁴) − (512/45)t² − 1/2]s² + 12t⁴

has positive degree-six Bernstein coefficients

    5/1024, 15/512, 42851/345600, 51217/230400,
    44977/115200, 3427/4320, 11/90.

Positivity is an exact polynomial argument, not a sampled numerical test. The accompanying check_ims.py reproduces the rational arithmetic. We have proved h≥1/(2R²) inside r≤R and h≥12/r² outside. This implies (A).

Replacing 7/4 by 7/9 and 1/2 by 1/4 gives positive Bernstein coefficients as well, proving the stated all-nonsinglet bound. This calculation uses the full interacting h only through the exact rotation identities, IMS, and the candidate exterior theorem.

## 4. Weighted inverse at zero; kernel and resonance issues

Write W_R=(R²+r²)^(-1/2). Estimate (A) implies, by the variational inverse formula,

    ||W_R(h₄₄+λ)⁻¹W_R|| ≤ 2,       λ>0.                    (4.1)

For f with W_R⁻¹f∈L²,

    ⟨f,h₄₄⁻¹f⟩ ≤ 2||W_R⁻¹f||².                            (4.2)

This is a negative-real-axis weighted resolvent bound, including its zero-energy form limit. It does not claim boundary values at h−E±i0 or exclude positive embedded eigenvalues.

No projection against a guessed zero mode is being suppressed. The 44 is orthogonal to the entire singlet kernel. In fact (A) directly excludes a nonzero 44 kernel vector. It also excludes a zero-energy distributional solution u in L²(W_R² dx), provided local ellipticity and the compatible form realization hold: apply (A) to χ_Lu and use the weak equation to get h[χ_Lu]=∫|∇χ_L|²|u|². Its right side tends to zero because the shell error is bounded by the weighted tail. Monotone exhaustion gives W_Ru=0.

For reference, even without the quantitative support bound, exterior coercivity with c>1 plus local compactness and absence of non-singlet L² zero modes would give an unspecified global weighted constant. A putative weighted resonance first bootstraps to L² by testing with bounded truncations of r and using c>1. The explicit proof above is stronger: it identifies the constant through R_N and does not need a separate Fredholm nonresonance assumption.

In the normalized-trace conventions q=N⁻² Xᵀh_spatial X, with ||h_spatial||op≤1. Hence |q|≤N⁻²r². Since H=h/2, multiplying (4.2) by 4 proves (B). The use of h both for a Hamiltonian and a spatial tensor is avoided in (B); the spatial tensor appears only in this sentence.

## 5. Near-endpoint source spectral bounds without a scattering expansion

The following standard weighted Poisson estimate is enough. Suppose a nonnegative kinetic-one matrix Schrödinger form has global coercivity h≥dW_R² and an exterior bound h≥c r⁻². For 0≤s with (s+1)²<c, solving (h+λ)uλ=f by its spectral resolvent gives

    ||⟨r⟩^s uλ|| ≤ D_(R,c,d,s) ||⟨r⟩^(s+2) f||,           (5.1)

uniformly for λ>0. Here it suffices to take 0≤s<1/2, far below √12−1.

For completeness: first use global coercivity to bound ||W_Ruλ||. Apply the exterior bound and the multiplier identity to ηg_Muλ, where η is a fixed exterior cutoff and g_M is a bounded truncation of r^(s+1). The identity is

    h[ηg_Muλ]+λ||ηg_Muλ||²
      = Re⟨η²g_M²uλ,f⟩ + ∫|∇(ηg_M)|²|uλ|².

The power derivative costs at most (1+ζ)(s+1)²||r⁻¹ηg_Muλ||². The source is bounded by ||r⁻¹ηg_Muλ||·||rηg_M f||, and the latter factor is at most ||r^(s+2)f||. Cutoff errors lie in a fixed annulus and are bounded by the previously controlled weighted norm. Choose ζ so that the coercive margin is positive, use Young's inequality, and then let M increase. Interior L² norms are controlled by W_R. This proves (5.1); weak compactness or spectral monotonicity as λ↓0 identifies u=h⁻¹f in L²_s.

For f=qΩ, the required source norm is bounded by a constant times N⁻²||⟨r⟩^(s+4)Ω||. It is finite whenever 2s+8<9, by the candidate singlet moment theorem. Therefore u=h⁻¹f lies in L²_s for every 0≤s<1/2.

Löwner–Heinz, applied to h≥dW_R² and regularized before taking inverse powers, gives for 0≤s≤1

    ⟨u,h^(-s)u⟩ ≤ d^(-s)||W_R^(-s)u||².

Consequently ⟨f,h^(-2−s)f⟩<∞ for every 0≤s<1/2. Lower inverse moments are finite by splitting the spectrum at 1. Rescaling h=2H proves (C). In particular K_(N,β) may be taken to be the actual inverse spectral moment; the cumulative bound then holds for all E>0, without an unknown threshold-onset window. All these constants still depend on rank.

The same argument yields a source heat bound

    ⟨f,e^(-tH)f⟩ ≤ Γ(β+1) K_(N,β) t^(-β),       0<β<5/2.

This is source-specific and does not establish full heat-kernel bounds or a positive-energy limiting-absorption principle.

## 6. Uniformity in a small positive regulator at each fixed rank

Assume at least one normalized zero mode Ω exists. The candidate singlet theorem supplies finite M=⟨ρ²⟩_Ω. For Hε=H+ερ², every normalized ground state Ωε satisfies

    0≤Eε≤εM,   ⟨ρ²⟩_ε≤M,   ⟨H⟩_ε≤εM.                    (6.1)

The confining regulator has discrete spectrum. The all-nonsinglet global estimate gives H_nonsinglet≥1/[8(R²+r²)]. With x=r², the elementary bound a/(R²+x)+bx≥2√(ab)−bR² therefore gives

    inf spec Hε,nonsinglet ≥ √ε/(√2 N) − εR²/N².

This is strictly larger than εM, and hence larger than the full ground energy, whenever

    0<ε<1/[2N²(M+R²/N²)²].                                (6.1a)

Every regulated ground vector is consequently a singlet under this explicit condition. This uses existence of a zero mode as a variational trial vector, but not uniqueness. Alternatively, tightness from (6.1), local elliptic compactness, and the vanishing supercharge norm show every ε→0 sequence of ground states has a norm-one strong subsequential limit in ker H; kernel singletness then gives the same qualitative conclusion.

Set kε=2(Hε−Eε)=h+2εr²/N²−2Eε. By (A), on the 44,

    kε ≥ (1/2)W_R² + 2εr²/N² − 2εM.

For r²≥2N²M the last two terms are nonnegative. For r²≤2N²M, taking

    ε ≤ 1/[8M(R²+2N²M)]                                  (6.2)

makes 2εM≤(1/4)W_R² there. Thus kε,44≥(1/4)W_R² for all sufficiently small ε. If M=0 the formula is interpreted separately; a normalized continuum-coordinate state in this setting in fact has M>0.

On r≥N√M, the regulator potential 2ερ²−2Eε is nonnegative. Therefore every exterior Hardy inequality for h, all-vector or singlet, remains valid for kε on that fixed exterior region. For a singlet Ωε, the multiplier identity

    h[gΩε] = 2Eε||gΩε||² − 2ε||ρgΩε||²
               + ∫|∇g|²|Ωε|²

has a nonpositive first pair of terms for g supported there. The manuscript's bounded-power Agmon proof consequently gives **uniform** moments supε⟨r^m⟩_ε<∞ for every m<9. Its exterior radius is enlarged by max(N√M, the relevant singlet radius), not by ε-dependent distances.

Apply Sections 4–5 to kε and fε=qΩε. Define Lε=Hε−Eε and με,N(B)=⟨fε,1_B(Lε)fε⟩. The global weighted constant is now 1/4, exterior c and source moments are uniform, and so

    sup_(0<ε<ε₀(N)) χε,N < ∞,
    sup_(0<ε<ε₀(N)) ∫ E^(-β)dμε,N(E) < ∞,   0≤β<5/2.         (6.3)

These are boundedness statements. They do not assert χε→χ or select a unique Ω without an additional uniqueness hypothesis. If the regulated ground level is nondegenerate, χε also has the ground-energy second-derivative interpretation from the previous audit.

## 7. Why the endpoint does not follow from these Hardy statements

Here is a precise comparison operator. It is **not BFSS**, has no asserted BFSS supercharges, and is used only to test the logical strength of exterior Hardy/moment information.

Work on L²(R⁹;44), with the ordinary diagonal Spin(9) action. Let s(n) be the normalized invariant contraction of the orbital l=2 harmonic with the internal 44, and let P₀ be the orthogonal projection onto the total singlet space. This space consists of radial multiples of s(n). Put

    ψ(r)=C r²(1+r²)^(-11/2) log(e+r²),
    Ω(x)=ψ(r)s(n),
    V(r)=ψ″/ψ + (8/r)ψ′/ψ − 18/r².

Ω is smooth at the origin, normalized for suitable C, and ψ(r)~2C r⁻⁹ log r. V extends smoothly through r=0 and

    V(r)=−11/[r² log r] + o(1/[r² log r])  at infinity.

Define the self-adjoint form direct sum

    A = P₀(−Δ+V)P₀  ⊕  (1−P₀)(−Δ)(1−P₀).

The singlet radial ground-state transform proves nonnegativity on P₀ and AΩ=0. The complementary part is the free Laplacian; hence ker A=span{Ω}, with no non-singlet zero mode or threshold weighted resonance. This example contains a nonlocal angular projection and is explicitly a comparison operator, not a local BFSS Hamiltonian.

On singlets the centrifugal term is 18/r², so radial Hardy gives every exterior coefficient c<49/4+18=121/4. On all vectors, the nonsinglet free part supplies 49/4, and the singlet coefficient is larger sufficiently far out. Every ordinary Ω moment m<9 is finite.

Now use the genuine coordinate quadrupole q=xᵀh_spatial x for a nonzero real symmetric traceless h_spatial. Its source lies entirely in total type 44, where A is exactly free. It has tail

    qΩ ~ const·r⁻⁷ log r · [l=0,2,4 angular components].

Differentiating the homogeneous Fourier-transform identity for r^(-β)Y_l at β=7 shows a nonzero k⁻² log(1/k) term. Removing the small-r singularity changes its Fourier transform by a bounded function. The smooth difference between the exact source and this cut-off leading tail has an L¹ gradient, so its transform is O(|k|⁻¹), smaller than the stated leading singularity. Thus

    F_qΩ,A(E) ~ B E^(5/2) [log(1/E)]²,     B>0.

No finite K can satisfy F(E)≤K E^(5/2) near zero. Nevertheless every nonnegative inverse moment below 5/2 is finite, exactly as in Section 5. This proves that the two candidate exterior coefficients, kernel singletness, a quadratic source, and all subcritical radial moments do not by themselves imply the endpoint.

If locality of the comparison operator is preferred, a second example uses L²(R⁹;1⊕44), a positive radial ψ₀=(1+r²)^(-9/2)log(e+r²), and the local block operator A_loc=(−Δ+Δψ₀/ψ₀)⊕(−Δ⊗I₄₄). The ground-state transform, the same two singlet/all-vector coefficients, and uniqueness of ψ₀ in the kernel all hold. The self-adjoint Spin(9)-44 tensor source Q_h=r²(|h⟩⟨0|+|0⟩⟨h|) gives the same logarithmic spectral excess. Here the source is a quadratic matrix-valued tensor rather than the coordinate quadrupole. These two examples separate the logical point from claims about actual BFSS dynamics.

## 8. What remains for large rank

There are now explicit conditional estimates in the actual Hamiltonian, rather than only a free-tail prediction. Their inputs remain unverified portions of the candidate finite-rank manuscript, and their constants are not rank uniform.

For β in (1,5/2), let K_(N,β) be a regulator-uniform constant supplied by (6.3), and Aε=⟨a⟩ε. The f-sum split from the earlier audit gives

    Aε χε ≤ C_β Aε^[2β/(β+1)] K_(N,β)^[2/(β+1)]
                      N^[−2(β−1)/(β+1)].

A sufficient rank gate is therefore

    Aε^β K_(N,β) = O(N^[(2β−4)/3]).                        (8.1)

For β=5/2−η, the right exponent is 1/3−2η/3. Unlike a merely asymptotic spectral law, the conditional all-energy moment bound has no onset-window issue. It still leaves the central rank problem completely open.

The constants enter through the all-vector radius R_(N,12), the singlet exterior radii needed for moments approaching order 9, the actual normalized zero-mode moments, and the regulator scales in (6.1a)–(6.2). The exterior proof deliberately allows these radii to grow arbitrarily with N. None of the calculations bounds that growth. Even (B) is much too crude to imply the desired susceptibility product rate.

To obtain the exact E^(5/2) endpoint, one needs additional BFSS information controlling critical weighted source tails or the threshold resolvent, excluding logarithmic/slowly varying enhancement in the actual coupled channels. To obtain the requested large-N result one additionally needs quantitative rank control of normalization, radii and weighted resolvent/source constants. A full positive-energy weighted LAP requires further spectral/propagation structure; it is not implied by the negative-axis bound (4.1).

The finite-rank boundedness and sub-endpoint estimates above are conditional progress. They are not a proof of the large-N zero-mode problem.
