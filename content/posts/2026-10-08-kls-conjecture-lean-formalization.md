---
title: A Lean Formalization of the KLS Conjecture with Universal Poincaré Constant
  at Most 15
date: '2026-10-08'
updated: '2026-10-09'
sequence: 6
category: Convex Geometry and Formal Mathematics
description: KLS history, recent breakthroughs, and a Lean formalization, from the
  earlier bound 500 to an October 9 release with a universal Poincaré constant at most 15.
image: assets/kls-2026/assets/kls-geometry.png
image_width: 3520
image_height: 2068
image_alt: A convex body and a hyperplane cut illustrate the geometry behind KLS.
caption: ''
draft: false
---

In 1995, [Ravi Kannan, László Lovász, and Miklós Simonovits](https://link.springer.com/article/10.1007/BF02574061) conjectured that the best hyperplane cut approximates the optimal isoperimetric bottleneck in a convex body within a universal factor, independent of dimension. In October 2026, several manuscripts claimed a dimension-free bound. I then started a Lean formalization in Codex. Its first completed checkpoint arrived about 23½ hours later.

**October 9 update.** My latest Lean release, **KLS15**, improves the universal Poincaré bound to **15**, building on Balasubramanian–Kasiviswanathan's deterministic variational and spectral framework. The progression of explicit bounds is:

| Development | Poincaré upper bound | Source and verification code |
|---|---|---|
| My earlier Lean release, KLS500 | $C_P(\mu)\le500$ | [GitHub](https://github.com/HongruZhao/KLS500) · [Zenodo](https://doi.org/10.5281/zenodo.23229034) |
| Balasubramanian–Kasiviswanathan, October 8 paper v2 | $C_P(\mu)\le25$ | [Paper](https://arxiv.org/pdf/2610.07728v2) |
| My latest Lean release, KLS15, October 9 | $C_P(\mu)\le15$ | [GitHub](https://github.com/HongruZhao/KLS15/blob/main/README.md) · [Zenodo](https://zenodo.org/records/23272815) |

The paper supplies the method and bound of 25; the KLS15 release adds quantitative refinements. These are sufficient upper bounds, with no claim of optimality.

## What KLS says

An isotropic law has mean zero and identity covariance. KLS predicts one universal **Poincaré Constant** $C>0$ such that, for every dimension $n\ge1$, every isotropic log-concave probability law $\mu$ on $\mathbb{R}^n$, and every locally Lipschitz function $f$ with finite Dirichlet energy, $f\in L^2(\mu)$ and

$$
\operatorname{Var}_\mu(f)\le C\int\|\nabla f\|^2\,d\mu.
$$

Here $h(\mu)$ is the **Cheeger constant**:

$$
h(\mu)=\inf_{0<\mu(A)<1}\frac{\mu^+(A)}{\min\{\mu(A),1-\mu(A)\}}.
$$

The infimum runs over Borel sets; $\mu^+(A)$ is the lower limiting probability growth per unit outward Euclidean enlargement. [Definition](https://arxiv.org/html/2610.01447v2#S2.SS2)

Equivalently, one universal $c>0$ satisfies $h(\mu)\ge c>0$ for every such law: separating substantial mass requires substantial boundary. The **Poincaré Constant** and $h(\mu)^{-2}$ are comparable by the Cheeger–Buser theory for log-concave laws. [Milman (2009)](https://arxiv.org/abs/0712.4092) · [De Ponti–Mondino](https://cvgmt.sns.it/paper/4217/)

Uniform laws on convex bodies and Gaussian laws are log-concave. KLS links their geometry to concentration, random sampling, and volume computation.



## How the dimension dependence improved

The historical bounds below use $\psi_n=\sup_\mu h(\mu)^{-1}$, with the supremum over all isotropic log-concave probability laws on $\mathbb{R}^n$. Smaller is better. Universal factors are suppressed; the corresponding Poincaré dependence is squared.

| Milestone | Upper bound for $\psi_n$ |
|---|---|
| [KLS, 1995](https://link.springer.com/article/10.1007/BF02574061) | $O(\sqrt n)$ |
| [Eldan, 2013](https://arxiv.org/abs/1203.0893) | $O(n^{1/3}\sqrt{\log n})$ |
| [Lee–Vempala, 2016 preprint](https://arxiv.org/abs/1612.01507) | $O(n^{1/4})$ |
| [Chen, 2020 preprint](https://arxiv.org/abs/2011.13661v2) | $n^{o(1)}$ |
| [Klartag–Lehec, 2022](https://arxiv.org/abs/2203.15551); [Jambulapati–Lee–Vempala, 2022](https://arxiv.org/abs/2208.11644v2) | $O((\log n)^5)$, then $O((\log n)^{3.2226})$ |
| [Klartag, 2023](https://arxiv.org/abs/2303.14938v2) | $O(\sqrt{\log n})$ |
| [Letwin, July 2026](https://arxiv.org/abs/2607.24164v1) | $O((\log n)^{1/4})$ |

[Klartag–Lehec's 2025 preprint](https://arxiv.org/abs/2507.15495v1) proved the thin-shell conjecture. [Chen–Klartag's July 2026 preprint](https://arxiv.org/abs/2607.23307v1) subsequently obtained the sharp inequality $\operatorname{Var}(|X|^2)\le8n$. Letwin's quadratic estimate supplied a broader input: for isotropic log-concave $X$ and symmetric $M$,

$$
\operatorname{Var}(X^\top M X)\le8\operatorname{Tr}(M^2).
$$

In their September 29, 2026 [preprint](https://arxiv.org/pdf/2609.38295v1), Dan Mikulincer and Ilias Zadik proved a dimension-free Poincaré bound for isotropic unconditional log-concave laws: laws invariant under changing any coordinate's sign. This settles an important symmetric case of KLS; the general conjecture also covers laws without that symmetry. Here “unconditional” describes a symmetry assumption, whereas my “unconditional formalization” means a proof without an unproved analytic premise.



## The September–October breakthroughs and their connections

The manuscript versions matter: Song–Zhang's first version retains a log-star dependence, while its second claims a constant bound. Both versions cite Letwin. The Bizeul–Klartag–Lehec and October 6 Balasubramanian–Kasiviswanathan versions explicitly refer to Song–Zhang v1.

- **September 29, 17:41 UTC: Mikulincer–Zadik v1.** A dimension-free Poincaré bound for sign-symmetric log-concave laws, the special case discussed above. [Paper](https://arxiv.org/abs/2609.38295v1)
- **October 1, 10:43 UTC: Song–Zhang v1.** Zhao Song and Xinzhi Zhang obtained $\psi_n=O(4^{\log^*(n+2)})$ and a tilt-derivative criterion. [Version 1](https://arxiv.org/abs/2610.01447v1)
- **October 4, 19:30 UTC: Bizeul–Klartag–Lehec v1.** Pierre Bizeul, Boaz Klartag, and Joseph Lehec claimed a dimension-free bound using cumulants and suspension. They cite **Song–Zhang v1** for its criterion and **Mikulincer–Zadik** for the earlier symmetric case (introduction; reference [30]). [Paper](https://arxiv.org/pdf/2610.05474v1)
- **October 4, 21:21 UTC: Song–Zhang v2.** Iterative refinement of polynomial and curvature bounds upgrades the log-star result to $O(1)$. Its bibliography cites Letwin but does not list the October Bizeul–Klartag–Lehec preprint. [Version 2](https://arxiv.org/pdf/2610.01447v2)
- **October 6, 03:15 UTC: Balasubramanian–Kasiviswanathan snapshot.** Krishnakumar Balasubramanian and Shiva Kasiviswanathan claimed a dimension-free Poincaré bound using compatible integration operators and a rank-uniform Hodge comparison. They cite **Song–Zhang v1** and Letwin; the checked snapshot does not cite Bizeul–Klartag–Lehec. [Pinned manuscript](https://github.com/kriznakumar/paper/blob/4837c33649ba2271f43c9684e9350ecbdd725f95/KLS.pdf)
- **October 8: Balasubramanian–Kasiviswanathan v2.** Their [arXiv revision](https://arxiv.org/pdf/2610.07728v2) reports the explicit bound $C_P(\mu)\le25$ for every isotropic log-concave probability measure (Theorem 1.1), using a deterministic variational and spectral argument. This revision also cites Bizeul–Klartag–Lehec and Song–Zhang v2. My earlier KLS500 formalization certified **500**; the October 9 KLS15 release improves this to **15**.

[![Selected version-specific KLS citations through the October 8 revision reporting a Poincaré bound of 25.](/assets/kls-2026/assets/kls-citation-map.png?v=18991d57cd73)](/assets/kls-2026/assets/kls-citation-map.png?v=18991d57cd73)

*Solid arrows run from cited work to citing work; dashed arrows mark manuscript revisions. A citation need not be a proof dependency. Dates use arXiv histories, except the GitHub file's first commit; they record public chronology, not discovery priority. The September and October manuscripts disclose AI assistance.*



## From a Markdown prompt to Lean

The first complete Lean formalization was accomplished in **about 24 hours**, essentially from **one main Markdown prompt**. Codex kept working through to completion without routinely stopping for new instructions; my follow-ups were brief progress questions and guidance.

On October 6, I prepared the [main prompt](/assets/kls-2026/attachments/KLS_Lean_Astra_Ultra_Prompt.html) and a companion [target-search document](/assets/kls-2026/attachments/KLS_Lean_Target_Search.html). **GPT-6.1 Sol (Ultra)** helped write the brief for GPT-6 Astra (Ultra / Fast). The run began at **12:11 CDT** and used **GPT-6 Astra (Ultra) → GPT-6.1 Sol (Ultra, then Max)**; speed settings varied. [Model and timing records](/assets/kls-2026/evidence/session-timeline.json) · [Preparation record](/assets/kls-2026/evidence/prompt-preparation-history.json)

The prompt fixed the full isotropic Cheeger and Poincaré endpoints, finite-energy integrability, the optimal-constant definitions, explicit sufficient bounds, and audit requirements. I later deferred finding the sharp constant.

At **15:41 CDT on October 6**, I encouraged a literature-informed shortcut. These are exact excerpts from one message:

> “You need to first search the literature extensively to identify potentially useful results, without restricting yourself to the original area. Search mathlib/other source what package might already exists.”

> “Also search the literature, is there any other way to by pass the current blue print, that is easy short cut for lean to formalize this task, but still lead to the proof of the KLS conjecture exactly.”

> “You can adaptively adjust the blue print. Just make the lean formalization task proper in lean. I trust in you. You can do this.”

The system could revise the blueprint while preserving the theorem. The earlier KLS500 chain mainly follows **Bizeul–Klartag–Lehec's cumulant, suspension, and Taylor-criterion route**, with Letwin's quadratic input and Song–Zhang's endpoint comparison. A weak moment-map argument at $C^{1,1}$ regularity supplied the quadratic seed, avoiding an unused classical-regularity branch. It does not formalize all three papers line by line. [Exact follow-ups](/assets/kls-2026/attachments/selected-follow-up-prompts.html) · [Technical report](/assets/kls-2026/attachments/technical-report.html)

Multiple agents worked together on proof development and checking. For the local Lean builds, I authorized up to 17 CPU cores on my **2026 Mac with an M5 Pro chip**, while the final whole-project replay recorded nine concurrent single-threaded Lean compilers. That authorization is not a measurement of continuous CPU utilization.

After learning that Balasubramanian and Kasiviswanathan's [October 8 version 2](https://arxiv.org/pdf/2610.07728v2) obtained a Poincaré bound of **25**, I further improved the bound to **15**, with the result verified in Lean 4. The October 9 KLS15 release adapts their framework and adds quantitative refinements; the [GitHub repository](https://github.com/HongruZhao/KLS15/blob/main/README.md) contains the proof and verification code, and [Zenodo](https://zenodo.org/records/23272815) preserves the release. [Detailed changes](https://github.com/HongruZhao/KLS15/blob/main/DETAILED_CHANGES.md) explain the refinements from the paper.



## What the verified project establishes

### Latest release: Poincaré constant at most 15

KLS15 covers every positive dimension and every isotropic log-concave probability law, with locally Lipschitz $L^2(\mu)$ test functions:

$$
\operatorname{Var}_\mu(f)\le15\int\|\nabla f\|^2\,d\mu.
$$

The public declarations are `KLS15.poincare15` and `KLS15.universalPoincareUpper15`; `KLS15.openaiKLS` retains the unchanged pinned OpenAI statement. The release's verification records report a fresh source rebuild of **1,654 project modules**, with only `propext`, `Classical.choice`, and `Quot.sound` in the final axiom closures. [Theorem source](https://github.com/HongruZhao/KLS15/blob/main/KLS15.lean) · [Verification](https://github.com/HongruZhao/KLS15/blob/main/verification/README.md)

### Earlier constant-500 checkpoint

The earlier KLS500 endpoint covered every positive dimension and the full isotropic log-concave class, including nonsmooth laws and unbounded support. Its recorded bounds were

$$
C_P(\mu)\le C_*\le500,
\qquad h(\mu)\ge\frac{100}{197\sqrt{500}}.
$$

Here $C_*$ is the defined optimal universal Poincaré constant, whose value remains unknown. **500** was the sufficient bound in that release; **1.97** is its Cheeger conversion coefficient. Neither is claimed optimal. Stronger analytic Cheeger–Buser comparisons are known. [Comparison](https://cvgmt.sns.it/paper/4217/)

The earlier combined Lean type was:

```lean
KLS.dimensionFree500_and_cheeger197 :
  (∀ (n : ℕ),
      1 ≤ n →
        ∀ (ρ : OAI.LeanBlast.KLS.Space n → ℝ),
          OAI.LeanBlast.KLS.IsLogConcaveDensity ρ →
            OAI.LeanBlast.KLS.IsIsotropic (OAI.LeanBlast.KLS.densityMeasure ρ) →
              OAI.LeanBlast.KLS.PoincareBound (OAI.LeanBlast.KLS.densityMeasure ρ) 500) ∧
    ∀ (n : ℕ),
      1 ≤ n →
        ∀ (μ : MeasureTheory.Measure (KLS.Space n)),
          KLS.admissibleMeasure μ → ENNReal.ofReal (100 / (197 * √500)) ≤ KLS.cheegerConstant μ
```

Its first component preserves the statement supplied by OpenAI's KLS benchmark, with smooth compactly supported tests inside `PoincareBound`. The project also proves the locally Lipschitz finite-energy version, including square-integrability. [Endpoint source](/assets/kls-2026/attachments/Entropy197500FullVerification.lean) · [Definitions and full theorem types](/assets/kls-2026/attachments/technical-report.html)

The first checkpoint's replay rebuilt 1,744 proof modules against a pinned Lean/Mathlib foundation cache. The improved endpoint was independently replayed against that baseline. Its saved statement review explicitly checks the type above, the original definitions, quantifier order, and integrability obligations. The audits report only `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx` or added mathematical axiom. [Baseline verification](/assets/kls-2026/attachments/checkpoint-verification.html) · [Endpoint receipt](/assets/kls-2026/evidence/cheeger-197-c500-receipt.json) · [Statement review](/assets/kls-2026/evidence/cheeger-197-c500-semantic-review.txt)

These are local checks by the proof system and checking agents, not an external mathematical review. Preparing this blog did not run another Lean build. Earlier bounds remain archived; later optimization is excluded from the first-completion measurements below.



## Code, time, and cost

The measurements below use the first completed source checkpoint; later optimization is excluded.

| Measure | KLS files | All project proof modules |
|---|---:|---:|
| Lean files | 1,258 | 1,744 |
| Physical source lines | 115,782 | 263,884 |
| Nonblank lines after removing comments | 98,886 | 216,652 |
| Written `theorem` / `lemma` commands | 4,995 | 10,000 |

The larger totals include supporting and ported libraries, excluding Mathlib and dependency sources. A full recount confirmed **4,995 + 5,005 = 10,000**, with no search-result limit. These are source commands, not distinct research theorems. The environment audit separately records **16,956 theorem constants**, including private and compiler-generated declarations. [Counting method](/assets/kls-2026/evidence/source-statistics.json) · [Recount](/assets/kls-2026/evidence/source-statistics-recount.json)

The task started **October 6 at 12:11:24 CDT**; the main agent reported completion **October 7 at 11:43:40 CDT**: **23 hours, 32 minutes, 16 seconds**. The final replay took approximately **33 minutes**. Earlier prompt preparation and later constant optimization are excluded; blueprint development inside the run is included. These are elapsed times, not CPU-hours. [Timeline](/assets/kls-2026/evidence/session-timeline.json)

The main chat and its three agents recorded approximately **2.59 billion tokens** before completion: **2.53 billion cached input**, **52.27 million uncached input**, and **9.81 million output**. About **97.6%** was cached input. The headline measures reused context and model traffic, not billions of newly generated proof tokens. [Usage calculation](/assets/kls-2026/evidence/usage-at-completion.json)

During the run, I upgraded from the plan I describe as Pro <span class="tex2jax_ignore">&#36;200</span> to Pro <span class="tex2jax_ignore">&#36;500.</span> I reported consuming one weekly allowance on the former, two on the latter, and additional credits.

My subscription allocation was **<span class="tex2jax_ignore">&#36;100</span> + <span class="tex2jax_ignore">&#36;250</span> = <span class="tex2jax_ignore">&#36;350</span>**. The final credit count was **40,000** at <span class="tex2jax_ignore">&#36;0.04</span> per credit, costing **<span class="tex2jax_ignore">&#36;1,600</span>**. The total cost was **<span class="tex2jax_ignore">&#36;350</span> + <span class="tex2jax_ignore">&#36;1,600</span> = <span class="tex2jax_ignore">&#36;1,950</span>**.

The useful outcome is an inspectable chain connecting a precise theorem to explicit constants, formal proofs, and recorded checks. The initial prompt fixed the destination; the proof route could evolve.
