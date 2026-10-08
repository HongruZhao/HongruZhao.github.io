# Existing Lean statements of KLS: source search

Search date: October 6, 2026. This search concerns existing formal **statements** and whether their sources prove them. A conjecture declaration is distinct from a proof.

The concrete existing candidate is **`KLS.KLSConjecture` in Job 45 of `brando90/conjecture-prover`**. No matching KLS declaration was located in the pinned mathlib, Formal Conjectures, or LeanEval snapshots below. No pre-existing Poincaré KLS target was located in those libraries. These are bounded findings, not a claim that no other artifact exists.

## Exact existing target

- Repository: `brando90/conjecture-prover`.
- Revision: `715c22ee0b55076591f60b76701cc9428e1b55a4`.
- File: `proofs/job_45/Job_45.lean`.
- Fully qualified declaration: **`KLS.KLSConjecture`**, a definition of type `Prop`.
- [Pinned declaration, starting at line 97](https://github.com/brando90/conjecture-prover/blob/715c22ee0b55076591f60b76701cc9428e1b55a4/proofs/job_45/Job_45.lean#L97).

Its mathematical content is

$$
\exists c\in\mathbb R,\ c>0,\quad
\forall n\in\mathbb N,\ n\ge1\Longrightarrow
\forall\mu:\operatorname{Measure}(\mathbb R^n),\quad
\operatorname{IsKLSMeasure}(\mu)\Longrightarrow h(\mu)\ge c.
$$

This summarizes the actual declaration; the pinned source contains its exact Lean syntax. The ambient space is `KLS.Space n`, defined using `EuclideanSpace ℝ (Fin n)`, and the lower bound uses `ENNReal.ofReal`.

The statement relies on concrete definitions:

- [`KLS.HasLogConcaveDensity`, line 35](https://github.com/brando90/conjecture-prover/blob/715c22ee0b55076591f60b76701cc9428e1b55a4/proofs/job_45/Job_45.lean#L35): density represented by an exponential of a convex extended-real potential.
- [`KLS.IsIsotropic`, line 55](https://github.com/brando90/conjecture-prover/blob/715c22ee0b55076591f60b76701cc9428e1b55a4/proofs/job_45/Job_45.lean#L55): integrability, mean zero, integrable coordinate products, and identity second-moment matrix.
- [`KLS.boundaryMeasure`, line 70](https://github.com/brando90/conjecture-prover/blob/715c22ee0b55076591f60b76701cc9428e1b55a4/proofs/job_45/Job_45.lean#L70), and [`KLS.cheegerConstant`, line 78](https://github.com/brando90/conjecture-prover/blob/715c22ee0b55076591f60b76701cc9428e1b55a4/proofs/job_45/Job_45.lean#L78): metric enlargements, outer Minkowski content, and boundary-to-mass ratios.
- [`KLS.IsKLSMeasure`, line 86](https://github.com/brando90/conjecture-prover/blob/715c22ee0b55076591f60b76701cc9428e1b55a4/proofs/job_45/Job_45.lean#L86): probability, absolute continuity, log-concave density, and isotropy.

**Status:** source-inspected statement candidate. Its definitional and conditional proof scripts do not prove this proposition unconditionally. This search did not independently compile it or prove its full semantic correspondence. Before freezing it, require a pinned build, a definition audit, nonempty-class examples, and a formal bridge from measure-based log-concavity to its density-based class. Its older literature-status comments should not determine the status of the October preprints.

## Preferred libraries and related proposals

| Source snapshot | Search and result |
|---|---|
| [mathlib4 `4beb549110aa44b87d699166cece6e3642bddf34`](https://github.com/leanprover-community/mathlib4/tree/4beb549110aa44b87d699166cece6e3642bddf34) | Searched all 9,192 Lean files, including Mathlib, Archive, Wanted, and tests. No matching KLS declaration was located. Poincaré and isotropy name matches concerned other subjects. Relevant public issue/PR searches supplied no KLS target. |
| [Formal Conjectures `89294ea02bd7cd678d59984add52cb4baef3dbf4`](https://github.com/google-deepmind/formal-conjectures/tree/89294ea02bd7cd678d59984add52cb4baef3dbf4) | Searched all Lean, Markdown, and TOML sources. No KLS or log-concave-measure statement was located. Public KLS/Kannan issue and PR searches found no candidate. |
| [LeanEval `2e58dff1c3d3aa934614d46205e8f430f9a7ca7e`](https://github.com/leanprover/lean-eval/tree/2e58dff1c3d3aa934614d46205e8f430f9a7ca7e) | Same source scan found no KLS statement. [PR #638](https://github.com/leanprover/lean-eval/pull/638) instead states Bourgain's slicing result, with an unfinished proof. |
| [AIM `c9929805cece044705abaaebe1cebddac1ba11a6`](https://github.com/MColbrook/AIM/tree/c9929805cece044705abaaebe1cebddac1ba11a6) | The catalog mentions KLS, but its Lean workspace contains infrastructure and smoke controls rather than an AIM KLS target. Its [workspace README](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/lean-statements/README.md) explicitly describes the absence of problem targets. |

The closed, unmerged [mathlib PR #40824](https://github.com/leanprover-community/mathlib4/pull/40824) contains a related one-dimensional interval Poincaré inequality. Its declaration is `MeasureTheory.lintegral_pow_le_mul_lintegral_pow_deriv_of_integral_eq_zero`, in [the pinned proposed file](https://github.com/alejandro-soto-franco/mathlib4/blob/397188b8550d90e06a477b80df597baeb8157388/Mathlib/Analysis/FunctionalSpaces/PoincareInequality.lean#L564). It is not the all-dimensional log-concave KLS statement and is absent from the searched mathlib snapshot.

Additional checks covered public GitHub code searches, the evand/open-math-problems catalog, OpenTorus's KLS campaign, and Reservoir package metadata. These catalog descriptions and campaign plans supplied no exact KLS Lean declaration. GitHub indexing is incomplete: even known files can be absent from keyword results. Package metadata searches do not audit every registered repository's sources.

## Recommendation for the prompt

Require **both** full formulations. Use the pinned `KLS.KLSConjecture` as the existing Cheeger candidate, subject to the audits above. Define and review a Poincaré companion if no faithful newer upstream declaration is found. Identify that companion as a new formal statement built on audited definitions and mathlib.

Prove every formulation bridge used, with explicit conversion constants. Keep Poincaré and reciprocal-Cheeger constants in separate ledgers. Producing both verified endpoints does not identify their sharp constants with each other.
