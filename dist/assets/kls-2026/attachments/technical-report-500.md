# Full KLS endpoints with constant 500

The independently accepted theorem gives

$$4\le C_*\le500,\qquad h_\mu\ge\frac{100}{223\sqrt{500}}.$$

The same constant applies in every positive dimension, to every original isotropic log-concave law and every admissible test. The improvement over the preceding 600 checkpoint is $6/5$, a reduction of about 16.7% in the upper bound. This is a sufficient constant; neither optimality nor agreement with a numerical constant stated in the papers is claimed.

The full law class includes nonsmooth densities and bounded or unbounded supports. The L2 version covers every locally Lipschitz square-integrable test, including infinite-energy tests. The finite-energy version derives square-integrability and integrability of the squared gradient before asserting the real-integral inequality. Actual membership of 500 in the original faithful Poincaré constant set is proved. Both original full Cheeger law formulations and the closed-neighborhood boundary convention are retained.

These important endpoint types were printed by the independent audit of CoupledRankYoungFullVerification.lean (`CoupledRankYoungFullVerification.lean`):

```lean
KLS.universalPoincareConstant_le_coupledRankYoung : KLS.universalPoincareConstant ≤ ENNReal.ofReal 500

KLS.admissibleMeasure.poincare_mem_coupledRankYoung {n : ℕ} (hn : 1 ≤ n) {μ : MeasureTheory.Measure (KLS.Space n)}
  (hμ : KLS.admissibleMeasure μ) : 500 ∈ KLS.poincareConstants μ

KLS.admissibleMeasure.real_poincare_coupledRankYoung {n : ℕ} (hn : 1 ≤ n) {μ : MeasureTheory.Measure (KLS.Space n)}
  (hμ : KLS.admissibleMeasure μ) {f : KLS.Space n → ℝ} (hf : LocallyLipschitz f) (he : KLS.energy μ f < ⊤) :
  MeasureTheory.MemLp f 2 μ ∧
    MeasureTheory.Integrable (fun x => ‖gradient f x‖ ^ 2) μ ∧
      ∫ (x : KLS.Space n), f x ^ 2 ∂μ - (∫ (x : KLS.Space n), f x ∂μ) ^ 2 ≤
        500 * ∫ (x : KLS.Space n), ‖gradient f x‖ ^ 2 ∂μ

KLS.admissibleMeasure.cheeger_lower_coupledRankYoung {n : ℕ} (hn : 1 ≤ n) {μ : MeasureTheory.Measure (KLS.Space n)}
  (hμ : KLS.admissibleMeasure μ) : ENNReal.ofReal (100 / (223 * √500)) ≤ KLS.cheegerConstant μ

KLS.klsConjecture_coupledRankYoung : KLS.KLSConjecture
```

The endpoint matches the full isotropic conclusion of [Bizeul–Klartag–Lehec v1, Theorem 1.1](https://arxiv.org/html/2610.05474v1), and the finite-energy conclusion of [Song–Zhang v2, Theorem 9.1](https://arxiv.org/html/2610.01447v2#S9.Thmtheorem1). The proof follows the BKL cumulant, suspension and Taylor-criterion route, including the quadratic-variance-eight input corresponding to [Letwin v1, Theorem 1.2](https://arxiv.org/html/2607.24164v1). Song–Zhang's separate logarithmic refinement and repeated height-reduction proof have not been independently reproduced by this chain. The nonisotropic covariance-scaled BKL conclusion is not a named endpoint here.

The formal analytic realization uses weak $C^{1,1}$ moment maps, locally square-integrable weak Hessians, weak integration by parts and Itô identities, cutoff approximation and weighted Hilbert-space spectral theory. These replace classical smooth-diffeomorphism and global derivative-growth assumptions in intermediate paper arguments. The accepted full-law approximation removes the smoothness and positive-curvature restrictions from the endpoint measure. The detailed fidelity report (`technical-report-8900.md`) records these analytic departures. The new numerical improvements below are additional estimates within this route, rather than exact reproductions of either paper's quantitative choices.

The main new ingredient is an unconditional symmetric-cumulant Taylor estimate. A proved one-dimensional variance differential inequality bounds the actual scalar third cumulant by two. A self-contained symmetric trilinear argument transfers that diagonal bound to repeated-slot mixed evaluations. Applied to the actual whitened localization law, it gives the cubic contraction seed four; the actual matrix seed eight remains unchanged. A symmetric-tensor energy argument improves the drift coefficient to

$$A(r,\eta)=(4\eta-2)r^2+(8\eta-5)r-2,$$

with next-rank coercivity $1-1/\eta$. Every compact and time-integrated quantity is the actual localization cumulant energy, and lower-energy integrability is proved in the induction.

Exact rational certificates now give actual rank-dependent Taylor coefficients $\beta_d$ through degree 256, with $\beta_1=1$ and $\beta_2=2$. The scalar criterion uses those finite coefficients and the accepted infinite bound

$$\beta_d=\frac{63}{500}\left(\frac{91}{5}\right)^d\quad(d>256),\qquad
\sum_a\operatorname{Taylor}_d(f)_a^2\le\beta_d\|f\|_2^2.$$

The proof checks every finite coefficient and every induction step. The infinite bound retains the finite integrated-envelope excess estimate at most four and an all-rank convolution inequality. The sharp suspension transfer has loss one. The original matrix seed eight and cubic seed four are discharged in the unconditional finite-rank Taylor endpoint (`OptTaylorRankSymmetric256Unconditional.lean`) and the all-rank endpoint (`OptTaylorEighteenFifth.lean`).

A second new ingredient is a proved sharp permutation comparison. For every actual permutation action by linear isometries on any real inner-product space, the ordered complete-transposition defect is at least $4N\|x-Px\|^2$, where $P$ is the permutation average and $N$ the number of positions. An elementary three-position argument proves the weighted series inequality

$$abD(i,j)\le(a+b)\{aD(i,k)+bD(k,j)\},\qquad a,b\ge0.$$

Its proof expresses the difference as a squared norm plus a nonnegative signed permutation average. Induction along an interval gives $D(i,j)\le(j-i)\sum_{k=i}^{j-1}D(k,k+1)$. Exact ordered-pair summation and the sharp complete gap then give

$$\|x-Px\|^2\le\frac14\sum_{k=0}^{q-1}(k+1)(q-k)D(k,k+1),\qquad N=q+1.$$

Applied to the actual centered-gradient permutation action, the factor one quarter cancels the existing adjacent-gradient factor four. The resulting Taylor recurrence has coefficient one on the interval-weighted defect term. These statements include the zero-length interval case and require no finite-dimensionality or completeness assumption on the ambient inner-product space. The independent moving-particle review (`semantic-review.txt`) checks the actual gradient, before-stopping and finite-sum integration; no abstract comparison is assumed in the numerical criterion.

The new improvement couples the stopping rule to the retained diffusion allowance. Write $E_k$ for the actual iteration energy, $D_k$ for its diffusion energy, $\chi_k$ for its nonnegative defect and $\lambda=E_0$. At the first crossing of

$$Q_k=E_k-\frac{D_k}{M\lambda}<\delta\lambda,
\qquad M=\frac{1007}{1000},\quad\delta=\frac1{100000},$$

the coupled stopping theorem (`semantic-review.txt`) gives one actual index $N>0$ and one real $\rho\in[0,1]$ satisfying

$$\sum_{k<N-1}\chi_k=\rho\lambda^2,\qquad
\sum_{k<N}\operatorname{MeanLoss}_k>
\left(1-\frac1M-\delta+\frac\rho M\right)\lambda.$$

At the same index, the actual scales squared before the relevant windows are at most $M\lambda$. The retained recurrence (`semantic-review.txt`) uses this exact budget. Only the defect-window term receives the factor $\rho$; the early-window contribution retains its full coefficient.

One fixed policy is used for every $\rho$. Its selected ranks are $1,2,7,10,14,20,28,40,59,91,147,253$, followed by rank 471 and doubling. The direct jump from rank two to rank seven uses the proved arbitrary-jump recurrence, whose requirements are a positive jump and an admissible window. Exact finite windows and positive rank-dependent Young parameters give the scalar recurrences. Every selected rank uses the coefficient-one moving-particle estimate. The normalization is $((9063/2000)\lambda)^{d-1}$.

For $d\ge257$, jump $d$, window $10d-1$ and Young parameter one use the accepted larger-window bounds (`MovingParticleLargeWindow.lean`) with recovery base $9/2$. Under $\lambda\le1/500$, the normalized main coefficient is at most two, and the early-plus-defect normalized error is at most

$$\left(\frac13+15\rho\right)d^3\left(\frac{199}{250}\right)^d.$$

Finite backwards descent from actual stopping zeros gives the affine tail $(1+32\rho)d^3(199/250)^d$. Exact propagation through the finite ranks proves $S_1\le43/10000+(981/1000)\rho$. The resulting mean-loss upper bound is at most

$$\left[\frac1{500}+\frac{1007}{1000}
\left(\frac{43}{10000}+\frac{981}{1000}\rho\right)\right]\lambda
\le\left(1-\frac1M-\delta+\frac\rho M\right)\lambda.$$

The last inequality is checked exactly at $\rho=0$ and $\rho=1$ and interpolated for this same fixed policy. It contradicts the strict coupled stopping lower bound. The regular criterion (`SpectralReductionCoupledCriterion.lean`) discharges every Taylor premise from the unconditional estimates above. The unchanged full-law approximation and accepted conversion $100/(223\sqrt C)$ give the displayed full endpoints with $C=500$.

The eight literal theorem types (`actual-eight-endpoint-types.txt`), independent receipt (`receipt.json`) and semantic review (`semantic-review.txt`) retain the evidence. The full integration checks 10896 declarations and 4314 strict declaration-origin gates; every axiom closure is contained in the standard three, and every final endpoint uses exactly those three. The finite256 Taylor packet (`receipt.json`), actual cubic seed (`receipt.json`), and symmetric energy core (`receipt.json`) are separately independently accepted.

The separate paired-tail estimate, all-rank base 18.19 improvement and finer Cheeger conversion are outside this frozen numerical checkpoint.
