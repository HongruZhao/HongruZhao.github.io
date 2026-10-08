# Full KLS in Lean: Cheeger and Poincaré — GPT-6 Astra / Ultra / Fast

<!-- PAGE 1 OF 3 -->

## 1. Fixed theorem and source investigation

Read this entire prompt, then execute the research and formalization. I authorize sustained autonomous work, native Goal creation, and all useful available parallel capacity. Produce unconditional Lean proofs of both full KLS formulations below, using imported definitions of the optimal Poincaré constants, explicit certified bounds, and a technical report; then determine the sharp universal constant. A blueprint alone is an intermediate deliverable.

**Require both the full isotropic Cheeger and Poincaré formulations.** The existing Cheeger statement is pinned below; the Poincaré endpoint matches the variance–gradient inequality in the supplied screenshot. Both cover every integer $n\ge1$ and every Borel probability measure $\mu$ on $\mathbb R^n$ that is log-concave, has finite second moments, has mean zero, and has covariance $I_n$. Include nonsmooth densities, unbounded support, and isotropic uniform measures on convex bodies. Here log-concavity means $\mu(tE+(1-t)F)\ge\mu(E)^t\mu(F)^{1-t}$ for compact sets $E,F$ and $0<t<1$; an equivalent density formulation requires proved bridges. For Poincaré, write

$$
\mathcal E_\mu(f)=\int\|\nabla f\|^2\,d\mu,\qquad
\operatorname{Var}_\mu(f)=\int f^2\,d\mu-\left(\int f\,d\mu\right)^2
$$

with the variance formula used after square integrability is established. Prove **exactly**

$$
\boxed{\begin{gathered}
\exists C\in\mathbb R,\ C>0,\quad \forall n\ge1\ \forall\mu\text{ as above},\\
\forall f:\mathbb R^n\to\mathbb R\text{ locally Lipschitz},\\
\mathcal E_\mu(f)<\infty\ \Longrightarrow
f\in L^2(\mu)\ \text{and}\ \operatorname{Var}_\mu(f)\le C\mathcal E_\mu(f).
\end{gathered}}
$$

Represent energy in Lean by the extended nonnegative integral of the squared almost-everywhere gradient; ordinary real integrals must not default to zero for infinite energy. Choose $C$ before $n$, $\mu$, and $f$. This finite-energy endpoint matches [Song–Zhang, Theorems 1.1 and 9.1](https://arxiv.org/html/2610.01447v2#S1.SS2). Also prove the inequality for all locally Lipschitz $f\in L^2(\mu)$, as in [Bizeul–Klartag–Lehec, Eq. (5) and Theorem 1.1](https://arxiv.org/html/2610.05474v1#S1), allowing infinite energy. Prove the extension between conventions.

**Import the optimal constants into the actual Lean endpoint declarations.** Reuse an audited library definition when available; otherwise create a faithful definition module and import it into the endpoint files. Record its exact import path, declaration names, and revision. Do not invent an existing mathlib import. Define $C_P(\mu)\in[0,\infty]$ as the infimum of all finite nonnegative constants satisfying Poincaré for every locally Lipschitz $L^2(\mu)$ test function; an empty infimum is $+\infty$. Define

$$
C_*=\sup_{n\ge1,\ \mu\ \mathrm{admissible}} C_P(\mu)\in[0,\infty].
$$

The Poincaré endpoint must certify an explicit $C_0>0$, $C_P(\mu)\le C_*\le C_0$, and the full inequality at the finite optimal constant $C_*$. Prove admissibility of the infimum, equivalence of the test-function conventions, and minimality against every smaller finite nonnegative universal constant. Derive $C_P(\mu)\ge1$ from isotropy; handle infinite energy separately. Prove finiteness before real conversion. Importing definitions must not import an assumed KLS theorem. Characterizing $C_*$ does not determine its sharp numerical value.

The Cheeger endpoint is one universal $c>0$ satisfying $h(\mu)\ge c$ for every admissible dimension and measure. Here $h$ is outer Minkowski boundary content divided by $\min\{\mu(A),1-\mu(A)\}$, infimized over measurable $A$ with $0<\mu(A)<1$. Use the exact audited Job 45 definitions below. Track $K=1/c$ separately from $C_P$ and certify conversion losses. Restricted dimensions, measure or function classes, and conditional reductions do not complete either target. “Unconditional verification” excludes unproved mathematical assumptions; it does not restrict measures to the sign-symmetric class also called unconditional.

An October 6, 2026 source scan found no matching KLS declaration in mathlib, Formal Conjectures, or LeanEval at the revisions in `KLS_Lean_Target_Search.md`. Check newer sources for reusable statements and constants. Record repository, commit, file, namespace, full type, and normalization. Label a new Poincaré companion or constants module honestly. Prove density/measure-class equivalence, including the consequence of nonsingular covariance. Freeze both audited targets before proving them; preserve their full scope.

These two files are mandatory semantic-audit references:

- [Job 14](https://github.com/brando90/conjecture-prover/blob/main/proofs/job_14/Job_14.lean) defines `IsIsotropicLogConcave` as `False`; its apparent KLS theorem is vacuous and explicitly disclaimed. It supplies no KLS proof.
- [Job 45 at commit `715c22ee0b55076591f60b76701cc9428e1b55a4`, line 97](https://github.com/brando90/conjecture-prover/blob/715c22ee0b55076591f60b76701cc9428e1b55a4/proofs/job_45/Job_45.lean#L97) defines the exact existing Cheeger proposition **`KLS.KLSConjecture : Prop`**. Its scripts contain unfoldings and conditional checks, not a KLS proof. Audit its measure, boundary, and Cheeger definitions against the full class. Once validated, prove this exact proposition alongside the Poincaré companion. If a definition fails semantic review, preserve the original, document the defect, and use a faithful corrected target without weakening the mathematical scope.

Start the literature search with [Song–Zhang, v2](https://arxiv.org/abs/2610.01447v2) and [Bizeul–Klartag–Lehec, v1](https://arxiv.org/abs/2610.05474v1), which claim full KLS proofs. Include [Letwin's quadratic-form and logarithmic-bound paper](https://arxiv.org/abs/2607.24164v1), [Mikulincer–Zadik's sign-symmetric case](https://arxiv.org/abs/2609.38295v1), and the [UW stochastic-localization formalization project](https://ai.math.uw.edu/projects/fall-2026/). Retrieve complete proofs, newer versions, corrections, and cited prerequisites. Search recent work on stochastic localization, tilt derivatives, cumulants, suspension, quadratic forms, and unconditional measures. Follow primary papers, author repositories, mathlib changes, and Lean community announcements. Separate preprint claims, ordinary proof review, conjecture statements in Lean, and complete kernel-checked proofs. Pin dates and versions. An unsuccessful search is bounded evidence, not proof that an artifact does not exist.

<div style="break-after: page; page-break-after: always;"></div>

<!-- PAGE 2 OF 3 -->

## 2. Parallel proof development and unconditional verification

Adapt the independent search, dynamic delegation, and adversarial scrutiny of the [OpenAI CDC prompt](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf). Search for existing KLS proofs freely. Use the actual runtime capacity; no fixed agent count is assumed.

Maintain a registry of mathematically distinct routes, exact missing lemmas, dependency graphs, and verified outputs. Allocate agents dynamically to source reconstruction, analytic foundations, Lean implementation, constant extraction, and independent semantic review. Initially preserve independent readings of the recent proofs; avoid making every agent inherit the favored argument. Group related ideas, redirect duplicated work, and exchange results when concrete lemmas emerge. A reduction to a KLS-equivalent assertion counts as an unresolved obligation until that assertion is proved. Reopen a stalled route when a new mechanism appears. The primary agent integrates results and launches further useful assignments. Assign separate files or worktrees to prevent conflicting edits.

Every assignment must return a precise theorem with hypotheses, proof or identified gap, source location, constant losses, and a Lean declaration or concrete implementation plan. Keep an independent auditor active when assessing a candidate endpoint. Check quantifiers, normalization, limiting arguments, and circular dependencies.

Construct `blueprint.md` as an executable dependency graph: mathematical statements, exact Lean types, source theorem numbers, existing library coverage, missing infrastructure, and acceptance checks. Select the shortest defensible route supported by the literature and library. You may replace preprint arguments with independently proved lemmas. Formalize every necessary analytic bridge: localization or stochastic calculus if used, derivative exchanges, moment estimates, smoothing, truncation, approximation, and passage to arbitrary admissible measures. A cited theorem is not available to the Lean kernel until proved or found in an audited dependency.

Require both audited endpoints and prove formulation bridges with explicit losses. The Poincaré endpoint file must import the audited constants module and use its $C_P$ and $C_*$ symbols in the theorem types. The Cheeger endpoint must prove the audited `KLS.KLSConjecture` itself and an explicit universal witness $c_0>0$. Establish the almost-everywhere gradient using Rademacher and absolute continuity, or audited library results; prove derivative–gradient identification. Comparison does not identify the sharp reciprocal-Cheeger $K$ with $C_P$. Restricted results require proved extensions to the full measure and function classes.

**Unconditional verification requires all of the following:**

- Pin Lean, mathlib, packages, source versions, and the final theorem type. Permit only the standard logical axioms of the audited pinned foundation, explicitly listed. No added mathematical axioms, `sorryAx`, assumed KLS estimate, assumed conjecture imported as a theorem, or circular hypothesis may occur in the endpoint's transitive dependencies.
- Audit definitions as well as proof terms. Prove the measure class is inhabited in every positive dimension, including a standard Gaussian; verify representative nonsmooth examples. Detect `False` assumptions, empty admissible classes, hidden assumptions of the conclusion, and weakened quantifiers. Check integrability before using integrals, finiteness before real conversions, infimum/supremum side conditions, and all extended-real operations.
- Obtain a successful fresh build from a clean checkout with pinned dependencies, rebuilding project artifacts. Record exact commands, exit status, commit, and logs. Inspect `#print axioms` for every claimed endpoint and audit its dependency closure. Numerical experiments and external solvers may suggest lemmas, but require kernel-checkable proofs or certificates for any mathematical conclusion.
- Have an independent agent compare the compiled theorem with the boxed target and every claimed report endpoint. Compilation without semantic correspondence does not establish KLS. A running build, cached receipt, or README assertion does not establish current verification.

Partial verified lemmas are useful internal progress. Preserve them, but keep the full-proof milestone open until the complete chain passes both kernel and semantic review.

<div style="break-after: page; page-break-after: always;"></div>

<!-- PAGE 3 OF 3 -->

## 3. Constants, reports, runtime, and persistence

Extract certified explicit Poincaré $C_0$ and reciprocal-Cheeger $K_0=1/c_0$ bounds. Replace every unspecified universal factor with a proved bound; track conversions, parameters, approximations, and losses in `constants.md`. Keep $C_P(\mu)$, the optimal universal $C_*$, and the certified upper bound $C_0$ distinct. Prefer exact rational or symbolic expressions with proved inequalities. Floating-point optimization alone is insufficient.

After both full KLS endpoints are verified, continue improving $C_0$ and the separately tracked $K_0$. Prove the equivalent characterization

$$
C_*=\inf\{C>0:\ \forall n\ge1\ \forall\mu\text{ admissible},\ C_P(\mu)\le C\},
$$

with the required nonemptiness and order side conditions. Certify $C_*\ge1$ using isotropy and linear test functions, then explore stronger lower bounds, alternative proofs, exact parameter optimization, and extremal measures. Certify every smaller universal bound in Lean. The numerical sharpness endpoint is an exact value $C_{\mathrm{sharp}}$ with a Lean proof $C_*=C_{\mathrm{sharp}}$, supported by matching universal upper and lower bounds; an extremizer need not exist. Optimizing one argument or merely defining $C_*$ does not prove this endpoint. Preserve a verified interval while sharpness remains unresolved.

Deliver a pinned Lean project, `blueprint.md`, `constants.md`, `report.md`, and `verification.md` with replay instructions and audit evidence. The report must list both full KLS endpoints, the imported constant declarations, the theorem at optimal $C_*$, decisive analytic estimates, necessary bridges, explicit bounds, and certified improvements or sharpness results. Give precise hypotheses, source/version comparison, Lean identifiers, and verification status. Match recent preprints' strongest relevant endpoints when justified; explain changes in the proof route. Put routine infrastructure and logs in the verification appendix. Failed approaches stay internal; disclose any gap affecting a public claim.

Before research, inspect the executing model, reasoning level, speed setting, tools, and effective concurrency limit. Use **GPT-6 Astra, Ultra reasoning, Fast mode** for the primary agent and workers where supported; I authorize supported task-specific controls. Verify the actual settings and label anything unverifiable. Prompt text does not itself switch the model or provision resources. Consult current [Astra prompting guidance](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra#prompting-best-practices), [subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents), and [Fast mode guidance](https://learn.chatgpt.com/docs/agent-configuration/speed). Ultra support is surface-specific; do not assume universal API syntax. Use all useful available concurrency and replenish assignments. If settings are unavailable, report the limitation and use the strongest supported authorized configuration without silently changing the requested model.

**I explicitly request a persistent native Goal.** Inspect the existing Goal; reuse a matching unfinished one or create one when no unfinished Goal conflicts. Use a compact objective referring to this file and including both full KLS endpoints, imported optimal constants, certified explicit bounds, reports, and the exact sharp value of $C_*$. Omit a numeric token budget: I have specified none. Follow the live Goal tool contract and [official Goals guidance](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex).

Send concise updates when the audited blueprint is ready, either endpoint passes unconditional verification, explicit constants are certified, the endpoint report is ready, or a materially better constant is proved. Keep working across failed routes and milestones. Mark the overall Goal complete only after both full proofs, reports, and the certified global Poincaré optimum are achieved. A mathematical gap alone does not justify stopping or native blocked status.

Respect user stops and actual platform, account, and budget limits. At a required interruption, save verified results, exact unresolved obligations, unsuccessful routes, and next actions in a resumable checkpoint. If native Goals or subagents are unavailable, state that limitation and preserve the same work state without claiming unattended continuation. Read applicable runtime instructions and skills; user scope takes precedence over skill preferences within the governing instruction hierarchy. Resolve routine choices autonomously and continue all work that does not depend on missing information. Begin now with runtime inspection, parallel literature/definition audits, and the dependency blueprint.
