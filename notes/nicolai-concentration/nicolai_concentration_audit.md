# BFSS dynamical concentration test: Nicolai transport

**Publication status (6 October 2026): conditional/provisional research. Author: Yicheng Pan. No independent human expert review has been supplied. Finite checks do not certify the full BFSS theorem or the large-rank target. See [branch status](README.md) and [review findings](REVIEW_FINDINGS.md).**


6 October 2026. This is a failed attempt at a new dynamical mechanism, not a large-rank upper bound. It does not recycle the previously established conditional inverse-energy moments as new progress. No assumption of planar factorization, holography, or hierarchy convergence is made.

## Result

The proposed mechanism is to transfer Gaussian Poincare concentration through a BFSS Nicolai map. The transfer inequality has the correct normalized-trace factor N^-2. However, the straightforward pointwise transport estimate needed to take the ground-state limit has an unavoidable lower bound proportional to Euclidean duration beta on the Cartan subspace. Adding a Gaussian mass omega replaces this by a quantity tending to 1/(2 omega), which still diverges on removing the mass. The mechanism therefore does not prove either <q_h^2>=O(N^-4/3) or <rho^2 q_h^2>=O(N^-4/3).

This is an obstruction to a specified uniform transport bound. It is not a no-go theorem for average-case transport estimates, all Nicolai maps, weighted Poincare inequalities, or the actual BFSS target.

## 1. Setup and the one mechanism tested

Use generators Tr(T_A T_B)=delta_AB and

    H_N = P^2/(2N) - (N/4) sum_ij Tr[Z_i,Z_j]^2 + F_N,
    q_h = (1/N) sum_A Z_i^A h_ij Z_j^A,
    a_h = (1/N) sum_A Z_i^A (h^2)_ij Z_j^A,
    R = rho^2 = (1/N) sum_iA (Z_i^A)^2.

Here h is real symmetric with Tr_9 h=0 and Tr_9 h^2=1. The elementary Euclidean gradient identity is

    |grad q_h|^2 = 4a_h/N.                                      (1)

In a Spin(9)-invariant configuration law, <a_h>=<R>/9 and <q_h>=0. Gauge reduction is not being replaced by an independence assumption.

Consider a finite time interval [0,beta], initially with zero Dirichlet endpoints so the centered free covariance exists. Let gamma_N,beta be the Gaussian path law with kinetic action

    (N/2) sum_iA integral_0^beta |dot Y_i^A(t)|^2 dt.

Its covariance is C_beta/N, where C_beta=(-d_t^2)^-1 with Dirichlet boundary conditions. Suppose, as a hypothesis for testing the mechanism, that there exists a real transport T with a differentiable inverse and the Sobolev regularity and integrability needed below, for which the desired interacting path probability is (T^-1)_# gamma_N,beta, including its boundary state and gauge prescription. This strong hypothesis is not established for BFSS by the cited perturbative Nicolai construction.

Write J=D(T^-1), evaluated at Y=T(Z), and F(Z)=q_h(Z(t0)). Gaussian Poincare, first in a finite time discretization and then under a legitimate continuum limit, gives

    Var(F) <= (1/N) E[ <J* dF, C_beta J* dF> ].                (2)

The pairing sums matrix-coordinate indices and integrates both time arguments. The derivative dF is grad q_h(Z(t0)) times delta_t0. Define the equal-time transported covariance kernel

    K_Z(t0,t0) = [J C_beta J*](t0,t0).

If K_Z(t0,t0)<=kappa_N,beta I pointwise, then (1)-(2) yield

    Var(q_h) <= 4 kappa_N,beta <a_h>/N^2.                    (3)

Thus a legitimate ground-state limit and kappa_N,beta <a_h>=O(N^(2/3)) would suffice for the weaker requested rate. Neither ingredient is assumed as a result. The point of the next test is that a bound with kappa independent of beta is incompatible with the commuting directions for the standard coupling-flow map.

## 2. Exact Cartan test of the transport bound

Fix one Cartan subalgebra of su(N), and restrict all Z_i(t) to it. Such paths commute at every pair of times. The temporal-gauge coupling-flow Nicolai map has no interaction correction on these paths: its corrections contain Lie brackets, and the coupling-flow vector field vanishes on this commuting subspace. At every formal perturbative order it is therefore the identity on that subspace; see [Lechtenfeld--Nicolai, equation (3.10)](https://arxiv.org/html/2109.00346v3). The finite-interval boundary prescription and positive global transport remain hypotheses. Any differentiable sum/flow extension that preserves this fixed-subspace property satisfies

    T(Z)=Z,   J v=v  for Cartan-valued variations v.           (4)

Equivalently, differentiating T^-1 restricted to the Cartan subspace gives Jv=v. J may mix root input into Cartan output, but this only adds a nonnegative term to the adjoint quadratic form.

The statement below is conditional only on this explicit property of the attempted transport, not on the existence of a global nonperturbative map.

At a Cartan path, grad q_h is also Cartan-valued. Equation (4) implies that the Cartan projection of J* dF is exactly dF. C_beta acts diagonally in Lie-algebra indices; positivity of the remaining components gives

    (1/N)<J*dF,C_beta J*dF>
        >= C_beta(t0,t0)|grad q_h|^2/N
        = 4 C_beta(t0,t0)a_h/N^2.                            (5)

The Dirichlet Green function is

    C_beta(t,s)=min(t,s)-ts/beta,
    C_beta(beta/2,beta/2)=beta/4.

Consequently at a midpoint with a_h>0,

    transport Dirichlet energy >= beta a_h/N^2,              (6)
    kappa_N,beta >= beta/4.                                 (7)

This is already true on a single nonzero diagonal direction, so retaining SU(N), normalized traces, and Gauss invariance does not remove the example. Finite temporal discretizations contain the same lower bound up to their convergent discrete Green function.

The exact commuting locus can have probability zero under a candidate path law. Therefore (7) refutes a pointwise uniform-kappa proof, not an expectation estimate. To use (2) successfully one would have to control how often and how strongly its transported derivative is large under the actual interacting measure. That is genuinely new dynamical information; determinant cancellation does not supply it.

Periodic massless Gaussian paths have an additional constant-mode problem: their proposed covariance is not invertible until the mode is removed or regulated. Removing physical relative Cartan coordinates is not a legitimate solution of the BFSS problem.

## 3. A mass regulates the example but does not give a uniform limit

Replace the free covariance by C_beta,omega=(-d_t^2+omega^2)^-1. This does not itself construct a mass-deformed Nicolai transport or prove that it fixes Cartan paths. The midpoint Green function is exactly

    C_beta,omega(beta/2,beta/2)
      = tanh(omega beta/2)/(2 omega).                        (8)

For a transport that remains identity on Cartan paths, the argument above requires

    kappa_N,beta,omega >= tanh(omega beta/2)/(2 omega).

Taking beta to infinity produces a lower bound 1/(2 omega). No constant uniform in the regulator follows from this global mechanism.

As a normalization check, for the genuine free oscillator with

    H_0 = sum_iA [P_iA^2/(2N)+N omega^2(Z_iA)^2/2],

Wick's rule in its normalized ground state gives

    <R> = 9(N^2-1)/(2N^2 omega),
    Var(q_h) = (N^2-1)/(2N^4 omega^2).                       (9)

The oscillator is a comparison system, not BFSS. Its exact result explains why an explicit N^-2 in a Gaussian variance bound is not enough when a regulator-dependent constant is suppressed. It also illustrates that taking omega proportional to N^-1/3 yields the requested N^-4/3 power for the oscillator, but gives no controlled BFSS comparison.

Choosing beta of order N^(2/3) in (3) similarly does not solve the problem. It leaves a quantitative passage from a finite-time prepared state to the threshold ground state, with the unbounded q_h observable, to be proved. Existence of a zero mode and the spectral theorem alone provide no rank-uniform convergence rate for that passage.

## 4. Why ordinary convex stochastic estimates do not repair this step

An explicit two-matrix slice tests the standard strictly convex drift condition. Embed

    A=sigma_1/sqrt(2), B=sigma_2/sqrt(2)

in su(N), so Tr A^2=Tr B^2=1 and Tr[A,B]^2=-2. Set

    Z_1=(t+s)A, Z_2=(t-s)B, Z_3=...=Z_9=0.

The actual BFSS bosonic interaction is then

    V_b(s)=N(t^2-s^2)^2,
    V_b''(0)=-4Nt^2.                                      (10)

A scalar quadratic regulator N omega^2 Tr(sum Z_i^2)/2 adds 2N omega^2 to this second derivative. Dividing by the squared Hilbert-Schmidt norm 2 of the variation gives the curvature

    N(omega^2-2t^2),                                       (11)

which is unbounded below as t grows. The path kinetic term does not change this test for constant periodic variations. For zero Dirichlet endpoints, choose any nonzero smooth endpoint-vanishing profile f and set Z_1=(L+s)f A, Z_2=(L-s)f B. The second variation of the Euclidean action is

    2N integral (f')^2 + 2N omega^2 integral f^2
      - 4N L^2 integral f^4.

It is negative for sufficiently large L on any fixed nontrivial interval.

Thus the bosonic potential is not a strictly convex perturbation of the Gaussian potential, even after any fixed quadratic mass is added. Fermionic integration cannot be ignored: it changes the effective path weight and need not give a positive, uniformly convex density. Equation (11) is not a proof that the true equal-time density fails every Poincare inequality; it prevents invoking the standard convexity theorem on the displayed bosonic action.

The Pauli normalization and second derivatives were checked symbolically in check_normalizations.py.

## 5. What the primary literature actually provides

Lechtenfeld--Nicolai, https://arxiv.org/html/2109.00346v3, constructs a perturbative BFSS Nicolai map. Its Section 4 gives a Jacobian convergence condition

    |g| < 2/[c_N ||X||_1],
    ||X||_1 = sum_aA integral |X_a^A(t)|dt,

with a rank-dependent c_N. The paper explicitly does not infer convergence of the map itself and does not assert positivity of its Majorana Pfaffian. Therefore it supplies neither the positive transport hypothesis preceding (2), nor the needed inverse-derivative estimate. The published statement is field dependent and on L1 paths, not a ground-state concentration theorem.

In our canonical kinetic-one coordinates X=sqrt(N)Z, the quartic coupling is g proportional to N^-1/2, with only a fixed convention-dependent factor. Hence g||X||_1 is proportional to ||Z||_1: the small-looking coupling does not by itself improve the convergence condition at large N. This last cancellation is a normalization calculation here, not a result attributed to that paper.

Other primary-source checks, used only to test applicability:

- Guionnet--Maurel-Segala, https://arxiv.org/abs/math/0601040, proves matrix-trace fluctuation results for convex, weak perturbations of Gaussian matrix integrals. Equations (10)-(11) fail that hypothesis, and these are not fermionic ground-state path measures.
- Guionnet--Shlyakhtenko, https://arxiv.org/abs/math/0701787, treats free diffusions and matrix models with locally convex interactions. This is not a source of unconditional BFSS rank estimates.
- Komatsu et al., https://arxiv.org/html/2401.16471, studies a strong-coupling BMN expansion at fixed N and uses bound-state input in its spectrum interpretation. This does not establish a uniform joint mass-removal and large-N bound on q_h.
- Lin et al., https://journals.aps.org/prl/abstract/10.1103/cyq8-4sd7, studies bosonic infinite-N quantum mechanics using large-N factorization. Its finite-N connected quadrupole rate is not established by that result.

This was a targeted primary-source search through 6 October 2026, not an exhaustive theorem-absence or priority claim.

## Conclusion

No actual BFSS upper rank bound was obtained. The concrete additional result is the conditional obstruction (7)-(8) to a natural dynamical Gaussian-transport proof, together with the normalization and nonconvexity tests. To reopen this method would require a positive ground-state transport and a rank-controlled averaged inverse-map derivative estimate that handles the long commuting paths. Neither follows from the cited Nicolai Jacobian convergence statement. Presenting those missing estimates as assumptions would merely move the unresolved dynamical problem into new notation.
