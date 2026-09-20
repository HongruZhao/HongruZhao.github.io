---
title: "Lean and the Future of Theoretical Research"
date: 2026-09-14
updated: 2026-09-20
sequence: 3
category: Formal Verification and AI
description: "From chess and AI coding to scientific discovery: why verification matters, what Lean checks, and how I would organize research with AI and formal proofs."
image: assets/vibemathing/lean-proof-explained.png?v=proof-start-20260919
image_width: 1600
image_height: 1000
image_alt: "An annotated Lean proof: the colon means has type. The objects a, b, and c have type Nat, the natural numbers 0, 1, 2, and so on. The identifiers hab and hbc are hypothesis/proof names for proofs of a = b and b = c. The keyword by starts the proof; transitivity proves the goal a = c. The complete example is checked in Lean."
caption: "A complete Lean proof, explaining the colon (“has type”), type annotation, hypothesis/proof names, goal, the keyword by that starts the proof, and the proof step."
draft: true
publish: true
draft_label: "First draft"
---

A chess program must win on the board. Generated code must survive being run. An AI-generated proof should come with evidence that survives a check beyond the model's own confidence.

The more capable AI becomes, the more important that last requirement becomes. We can ask models to explore many approaches, produce long arguments, and work on problems we do not yet understand. But the resulting volume of plausible work can grow much faster than our ability to read it. An invented lemma or an unnoticed change of assumptions can then become the foundation of another argument. **Verification is what lets us turn this growing capacity to generate ideas into knowledge we can build on.**

This post is about that transition across mathematics, statistics, computer science, and theoretical physics. Lean is central to the story, but the story begins with a much older idea: progress accelerates when we have a dependable way to tell whether an attempt has succeeded.

## 1. Verification is a source of progress

In its broadest sense, verification means checking a claim against an explicit standard. A game has rules and a recorded outcome. A program has intended behavior. A theorem has a statement and assumptions. A scientific prediction faces observations. These checks have different strengths, but each gives us something beyond an author's assurance.

The ambition to make such checks precise predates today's AI. In **1969**, C. A. R. Hoare's *An Axiomatic Basis for Computer Programming* developed logical rules for proving properties of programs. The question was already how to connect what a program does with a precise account of what it should do. ([Original publication](https://www.cs.ox.ac.uk/publications/publication8205-abstract.html).)

Modern AI offers many concrete examples of the power of a check:

| Example | What provides the check? | What we learn from it |
| --- | --- | --- |
| **Deep Blue, 1997** | Chess rules, legal moves, and the results of its match against Garry Kasparov. | Its victory established performance against the reigning world champion under tournament conditions. It did not require a proof that every move was optimal. ([IBM's history](https://www.ibm.com/history/deep-blue).) |
| **AlphaGo, 2016; AlphaGo Zero, 2017** | Finished games have outcomes determined by the rules; self-play supplies repeated feedback. | A system can improve its strategy through a vast number of attempts because success can be evaluated. ([AlphaGo](https://research.google/blog/alphago-mastering-the-ancient-game-of-go-with-machine-learning/); [AlphaGo Zero](https://deepmind.google/blog/alphago-zero-starting-from-scratch/).) |
| **AlphaCode, 2022** | Candidate programs are executed and filtered using test cases. | Running code makes many mistakes observable and allows automated selection among candidates. ([Research account](https://deepmind.google/blog/competitive-programming-with-alphacode/).) |
| **Vibe coding and AI coding assistants** | Builds, tests, and inspection of the running application. | Generated software can enter a repeated write–run–repair cycle. The quality of that cycle depends on the quality of its checks. ([A practical verification workflow](https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work).) |
| **AlphaTensor, 2022** | An exact algebraic identity certifies a proposed matrix multiplication algorithm. | The certificate establishes correctness for all matrices in the specified dimensions and arithmetic, beyond a collection of numerical examples. ([Research account](https://deepmind.google/blog/discovering-novel-algorithms-with-alphatensor/).) |
| **FunSearch, 2023** | An evaluator executes proposed programs and checks and scores the constructions they produce. | Search can retain valid, promising constructions and discard failed attempts. A better construction need not settle the entire underlying open problem. ([Method and examples](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/).) |
| **AlphaGeometry, 2024** | A symbolic deduction engine applies geometric rules to constructions suggested by a language model. | Creative suggestions become useful when they support a checkable chain of deductions. ([System description](https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/).) |
| **AlphaProof, 2024** | Proof search takes place in Lean, whose checker evaluates the resulting formal proofs. | Verification can guide the search itself. The IMO problems in this experiment were first translated into formal language by humans. ([Research account](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).) |
| **AlphaFold and CASP** | Blind structure predictions are compared with experimentally determined structures withheld from participants. | Predictive accuracy is measured against external evidence, rather than the model's confidence in its prediction. ([Assessment and confidence](https://deepmind.google/blog/enabling-high-accuracy-protein-structure-prediction-at-the-proteome-scale/).) |
| **The A-Lab, 2023** | Proposed synthesis recipes are carried out by robots, and the products are characterized experimentally. | AI-guided materials research can connect proposals to physical measurements and use the outcomes to revise later experiments. ([Original paper, with corrections](https://www.nature.com/articles/s41586-023-06734-w).) |

These examples explain why verification is productive. It gives a search process feedback, exposes failed attempts, and makes successful results reusable. An imperfect generator can still be useful when we can reliably identify which of its outputs deserve to survive.

We should also keep the standards distinct. Winning a game establishes an outcome. Passing tests gives evidence about the cases tested. A formal proof establishes a deduction for every case covered by its statement. An experiment supplies evidence about the physical world, with measurement uncertainty and limits of applicability. Calling all of these “verification” is useful only if we say what each check establishes.

**Carina Hong**, founder and CEO of Axiom Math, emphasizes the cumulative value of verified knowledge: a checked result can support further discoveries and be reused by other people and systems. That is the aspect of her argument that matters most to me. Verification helps intelligence accumulate its gains. ([Her June 3, 2026 discussion](https://www.latent.space/p/axiom).)

### Scholze's Liquid Tensor Experiment

**Even a Fields medalist can have doubts about his own proof.** Peter Scholze, a [2018 Fields medalist](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018), openly described “some small lingering doubts” about a foundational argument in his work with Dustin Clausen. The result supported their new approach to real functional analysis, and later researchers might use it without revisiting its difficult proof. For something carrying that much weight, he wrote, “being 99.9% sure is not enough.” ([Scholze's original challenge](https://xenaproject.wordpress.com/2020/12/05/liquid-tensor-experiment/).)

He therefore challenged the theorem-proving community to formalize the result. The collaboration used **Lean 3**, whose mathematical library supplied the starting point, and was led by **Johan Commelin**, with major contributions from **Adam Topaz** and many others. Scholze remained involved, answering mathematical questions as the team worked. ([Project repository](https://github.com/leanprover-community/lean-liquid); [contributors and completion announcement](https://leanprover-community.github.io/blog/posts/lte-final/).)

The timeline separates finding the mathematical argument from completing its formal verification:

| Date | Milestone |
| --- | --- |
| **July 2019** | After substantial preparation, Scholze worked out the difficult core during an intensive week. He later emphasized that the larger proof was joint work with Clausen and occupied them for about a year. ([Scholze's clarification](https://leanprover-community.github.io/archive/stream/113488-general/topic/Lean.20in.20the.20wild.html#247609527).) |
| **Late 2019** | The argument was written up, becoming part of Scholze's 2019–20 Bonn lectures on analytic geometry. This was the written mathematical proof that the formalization would follow. ([Scholze's account](https://leanprover-community.github.io/archive/stream/113488-general/topic/Lean.20in.20the.20wild.html#247609527); [Buzzard's retrospective](https://xenaproject.wordpress.com/2022/09/12/beyond-the-liquid-tensor-experiment/).) |
| **December 5, 2020** | Scholze publicly issued the **Liquid Tensor Experiment** challenge, asking for formal verification of the theorem. ([Original post](https://xenaproject.wordpress.com/2020/12/05/liquid-tensor-experiment/).) |
| **January 14, 2021** | Commelin had formalized the **statement of Theorem 9.4**, the technical core. Expressing the target precisely was itself an early milestone. ([Scholze's progress report](https://xenaproject.wordpress.com/2021/06/05/half-a-year-of-the-liquid-tensor-experiment-amazing-developments/).) |
| **May 28, 2021** | The team completed the formal proof of **Theorem 9.4**, just under six months after the public challenge. In his June 5 report, Scholze said that the part he had been unsure about was now verified and that his doubts about the main proof were resolved. The full challenge still required further work. ([Progress report](https://xenaproject.wordpress.com/2021/06/05/half-a-year-of-the-liquid-tensor-experiment-amazing-developments/).) |
| **July 14, 2022** | The **full challenge was completed in Lean 3**, including the deduction of the main theorem on liquid vector spaces. The community announced completion on July 15: about **19 months after the challenge**, and roughly three years after the original 2019 argument. ([Completion announcement](https://leanprover-community.github.io/blog/posts/lte-final/); [repository](https://github.com/leanprover-community/lean-liquid).) |

Why did the last stage take so long? **Kevin Buzzard explains that a five-line deduction in the written proof took roughly another year to formalize**, because the team first had to develop substantial libraries for homological algebra and related mathematics. The six-month and nineteen-month durations describe the collaborative work of constructing formal proofs and their prerequisites. Those reusable foundations were themselves an important result. ([Buzzard's account](https://xenaproject.wordpress.com/2022/09/12/beyond-the-liquid-tensor-experiment/).)

The process also improved the mathematics. Small imprecisions were repaired, Commelin found a more explicit construction that avoided an appeal to stable homotopy theory, and Scholze gained a clearer understanding of why the argument worked. He also stressed that checking the formal statement and discussing the difficult steps with the team were essential to his confidence. **Verification helped people understand the proof as well as trust it.** ([Scholze's reflections and follow-up discussion](https://xenaproject.wordpress.com/2021/06/05/half-a-year-of-the-liquid-tensor-experiment-amazing-developments/).)

**Terence Tao's PFR formalization project** offers another example of this shared research infrastructure: a readable proof, a map of its dependencies, and machine-checked components can organize collaborative research. ([Tao's tour](https://terrytao.wordpress.com/2023/11/18/formalizing-the-proof-of-pfr-in-lean4-using-blueprint-a-short-tour/).)

## 2. What Lean is, in one small example

**Lean is a language for writing precise statements and proofs, together with software that checks them.** Leonardo de Moura started the project in **2013**. Lean 4, developed by de Moura, Sebastian Ullrich, and contributors, combines a proof assistant with a programming language. The community's **mathlib** supplies a growing collection of definitions and proved results, so a new project can build on existing mathematics. ([Lean's history](https://lean-lang.org/theorem_proving_in_lean4/Introduction/); [Lean 4 system paper](https://lean-lang.org/papers/lean4.pdf); [mathlib](https://leanprover-community.github.io/).)

The essential idea is easy to see. If $a=b$ and $b=c$, then $a=c$. Here is a complete Lean proof:

```lean
theorem equality_chain
    (a b c : Nat) (hab : a = b) (hbc : b = c) :
    a = c := by
  exact Eq.trans hab hbc
```

The notation is more familiar than it first appears:

| Piece of Lean | Meaning |
| --- | --- |
| `theorem equality_chain` | Give a proved statement a name so it can be reused. A `lemma` is also a proved statement, usually named as an intermediate result. |
| `:` | Read as **“has type.”** `a : Nat` says that `a` is a natural number. In `hab : a = b`, the proposition `a = b` is the type of the proof named `hab`. |
| `(a b c : Nat)` | The objects are natural numbers: $0,1,2,\ldots$. `Nat` is their **type**. |
| `(hab : a = b)` and `(hbc : b = c)` | `hab` and `hbc` are **hypothesis/proof names**. They name proofs of the propositions `a = b` and `b = c`, respectively. |
| `a = c` | The conclusion, or **goal**, that remains to be established. |
| `by` | **Starts the proof**, introducing a block of proof instructions called **tactics**. |
| `exact` | Supplies a proof of the current goal. |
| `Eq.trans hab hbc` | Apply the existing transitivity theorem for equality to the two hypotheses. |

Lean checks that these ingredients really fit. Replacing the conclusion with an unrelated assertion would leave this proof invalid. The example is deliberately small; the same relationship between a statement, its hypotheses, and a proof applies to a limit theorem or a complexity bound. ([Equality in Lean](https://lean-lang.org/theorem_proving_in_lean4/Quantifiers-and-Equality/); [tactics](https://lean-lang.org/theorem_proving_in_lean4/Tactics/).)

A **definition**, written with `def`, specifies an object. An **import** brings in an existing library. A **tactic** helps construct a proof. The **kernel** is the small core that checks the resulting proof against Lean's logical rules. The AI proposes the proof; the kernel performs this check. ([Propositions and proofs](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/).)

For a precisely stated mathematical claim, I regard a checked formal proof as the ultimate target of verification. Short proofs can receive feedback almost immediately. That can feel revolutionary after waiting for human review. But “instant verification” describes the experience of many small checks, not a guarantee about an entire research project: generating a proof, translating it into Lean, and building a large development may still take substantial time.

Lean's guarantee concerns the encoded statement under its declared assumptions and logical foundations. It also rests on the correctness of the checker and its execution. It does not by itself establish novelty, explain the central idea, or decide whether a physical model describes nature.

## 3. The first hard problem is stating the problem

Before asking Lean to verify an argument, we must decide exactly what argument we want it to verify.

Consider the sample-correlation log-determinant problem from [my first vibemathing experiment](../2026-09-14-my-first-vibemathing-attempt/). A formal statement must specify the observations, the population correlation matrix, how the sample mean is removed, the normalization, and the asymptotic regime. A theorem about an uncentered covariance matrix does not automatically cover the Pearson correlation matrix. A result for population correlation $R=I$ does not establish a claim for every positive definite $R$.

Even the order of quantifiers matters. “For every matrix there exists a suitable constant” can be much weaker than “there exists one constant that works for every matrix.” A computer can check a proof of either statement. Choosing the intended one requires understanding the research question.

This is why I would ask an AI to translate its formal statement **back into ordinary language before proving it**. I would compare that translation with the paper, test the definitions on simple examples, and inspect the exceptional cases. In theoretical physics, I would also separate deductions within a model from claims about the physical system the model represents.

There is a historical example of how substantial this work can be. **Buzzard, Commelin, and Massot's perfectoid-spaces project** developed enough formal mathematics to express sophisticated research-level definitions. The achievement included constructing the language in which later theorems could even be stated. ([Project and paper](https://leanprover-community.github.io/lean-perfectoid-spaces/).)

Sometimes the difficulty is missing library infrastructure. Sometimes it is an ambiguity in the paper. Sometimes formalization exposes a genuine gap. These lead to different next steps: develop the missing definitions, clarify the statement, or repair the argument. A failure to finish a Lean proof is a reason to investigate, not by itself a disproof of the theorem.

## 4. Let AI discover, explain, and formalize—with a blueprint

I want to use systems such as **ChatGPT and Claude** for both discovery and formalization. I would usually start with the strongest reasoning model available for the conceptual work: exploring approaches, finding counterexamples, identifying the decisive lemma, and explaining why the argument should succeed. Once the structure is clear, a less expensive model with good Lean skills may be able to handle many of the smaller formalization tasks.

This is a proposed division of labor, not a fixed ranking of intelligence. Formalization can demand real mathematical invention. A model that is strong at informal reasoning may be poor at finding library lemmas; a specialist may excel at that task. When a local proof attempt uncovers a missing estimate or a bad definition, the difficult question should return to the stronger reasoning process.

The handoff should be a **proof blueprint**: a human-readable plan detailed enough that each step has a clear mathematical purpose and a clear formal target. Patrick Massot's *Lean Blueprint* connects such plans with Lean declarations and dependency graphs. Tao's PFR project illustrates the approach in a substantial collaborative proof. ([Blueprint tool](https://github.com/PatrickMassot/leanblueprint); [worked example](https://terrytao.wordpress.com/2023/11/18/formalizing-the-proof-of-pfr-in-lean4-using-blueprint-a-short-tour/).)

For my own work, I would ask the reasoning model to provide:

1. **The exact target.** State the objects, assumptions, quantifiers, and conclusion; identify which parts are new.
2. **The decisive idea.** Explain what overcomes the main obstacle, with a small example whenever possible.
3. **Named intermediate lemmas.** State each lemma precisely and show which earlier results it uses.
4. **A library map.** Separate results already available in Lean from results that must be formalized, and verify the cited sources.
5. **An honest list of gaps.** Mark every unproved step, missing hypothesis, and conjectural input.

The formalization model can then work on bounded tasks, run Lean, and use its feedback to revise the proof. Independent lemmas can be attempted in parallel once their statements and shared definitions are stable. A blueprint's progress colors are an organizational aid; the actual proof and its dependencies must still be checked.

### Six examples from my own Lean releases

My experience extends beyond the first log-determinant experiment. The following six releases make the blueprint idea concrete. Each requires a different decomposition of the argument, and each archive records the relationship between the paper, the formal statements, and their dependencies.

**1. A quantitative normal approximation for the log determinant.** In my *Sharp Berry–Esseen Bounds* project, the task includes exact covariance and variance identities, distributional transforms, and explicit error bounds. The expanded release maps 243 manuscript entries to a public interface containing 288 proved theorem statements. Its reviewed proofs use only Lean's standard foundations, with the statistical assumptions and domains stated as hypotheses. The lesson for my blueprint is to give the analytic ingredients their own precise statements: a lemma that already assumes the desired approximation would conceal the real work. ([Expanded Lean archive, v1.1.4](https://zenodo.org/records/22739087).)

**2. Asymptotic independence of the log determinant and coherence.** These two statistics come from the same sample correlation matrix. Separate limit laws do not establish their joint asymptotic independence. My release includes pair-block factorizations, conditional overshoot estimates, and factorial Bonferroni inequalities, with formal counterparts or proved finite assemblies for the paper's 12 named results and 50 labeled equations. Here the blueprint must expose how dependence is controlled and how finite estimates feed into the limiting argument. This is a useful example of why “prove the CLT” is too coarse a task description. ([Lean archive](https://zenodo.org/records/21936680).)

**3. Exact moments of Gaussian Gram hafnians.** This project connects second and fourth absolute moments to a normalized moment ratio, special-function identities, finite bounds, and the $n^2/\log n$ threshold for weak anticoncentration. The archive provides proved statements for all 14 numbered equations in the Letter, without project-specific mathematical axioms. For a blueprint, this suggests a sequence of separately checkable goals: derive the exact identities, bound their ratio, and justify the claimed asymptotic regime. The verified scope is the Gaussian surrogate; transferring the result to a finite Haar model requires further mathematics. ([Lean archive](https://zenodo.org/records/21959946).)

**4. Local anticoncentration through conditional Wishart geometry.** My *Local Anticoncentration for Gaussian Boson Sampling* release formalizes the main Theorems 2.1 and 2.3 for the actual complex Gaussian matrix models, without additional scientific axioms. The broader development includes Fourier compression, conditional Wishart identities, and perturbation bounds. A useful blueprint must connect these ingredients to the actual probability law. The archive also identifies unfinished extensions, including an unassembled Gaussian-law step in a revised corollary. Completing the main theorems and completing every later application are distinct milestones that the plan should track. ([Lean archive, v1.1.0](https://zenodo.org/records/22554594).)

**5. Uniform hiding and relative accuracy in Gaussian boson sampling.** This development connects a quantitative comparison of matrix laws to Gaussian anticoncentration and then to probability and sampling bounds. The v1.3.0 release adds photon-sector calculations and optimized asymptotics, while mapping the current paper's equations and results to their formal status. The hiding theorem and assembled Route 1 bounds retain **four explicit literature inputs** concerning COE blocks, Takagi integration, the Gaussian GSVD/Jacobi law, and Wishart moments. Route 2 has a separate outstanding comparison and assembly. My blueprint therefore needs to show both the chain of deductions and precisely where outside results enter it. ([Lean archive, v1.3.0](https://zenodo.org/records/22670050).)

**6. Weak typicality of entanglement entropy.** In this project, the proof passes through a singular-value representation of entropy, endpoint regularization, and concentration estimates. The release tracks 57 labeled equations. Its conclusions retain three explicit mathematical inputs: unitary Haar concentration, Mirsky's singular-value inequality, and Gaussian normal-form evidence. They concern the stated ideal Gaussian boson sampling model and its spectral entropy formulation. This example reminds me that the blueprint must describe the physical model and the mathematical representation before applying a concentration theorem. Those choices determine what the final probability statement actually says. ([Lean archive](https://zenodo.org/records/21969265).)

Across these projects, the most useful handoff is a statement-by-statement map: what is being proved, which earlier facts it uses, where it appears in the paper, and what remains outside the verified result. That gives an AI a concrete task and gives me something meaningful to review. A successful build becomes much more informative when I can follow that map back to the research claim.

### Discovery and formalization at a different scale

There is already a striking reported example of discovery and formalization using different model capabilities. OpenAI's **September 8, 2026 Navier–Stokes announcement** attributes the argument to a newer internal model and the subsequent Lean formalization to **GPT-6 Astra**. It reports about **88 hours** to reach the argument and **17 additional hours** for formalization and verification. The announced Navier–Stokes result involves a **smooth external force**, targeting alternatives C and D of the Millennium formulation. This supports the possibility of such a division of labor; it does not establish that formalization is always the easier stage. ([Announcement](https://openai.com/index/navier-stokes-solution/); [released Lean artifacts](https://github.com/openai/NavierStokesAndEuler).)

**Fermat's Last Theorem reached another historic milestone with Anthropic's September 4, 2026 announcement of a complete Lean formalization.** This was the formalization of an established theorem, following the Darmon–Diamond–Taylor exposition of Wiles's proof. Anthropic reported the following timeline and scale. ([Announcement](https://www.anthropic.com/research/formalizing-fermats-last-theorem).)

| Milestone or measure | Reported result |
| --- | --- |
| **Completion** | August 18, 2026, at **02:00:57 UTC**; the public announcement followed on **September 4**. |
| **Elapsed formalization time** | **11 days**, largely autonomously, using an internal Claude model with occasional high-level human guidance. |
| **Code produced** | Approximately **13 million lines of Lean**. |
| **Intermediate theorems** | About **30,300 produced**, of which **29,500** were used in the final proof. |

The human project had a very different planned timescale. Kevin Buzzard's **five-year EPSRC programme, September 2024–September 2029**, set out to formalize substantial mathematics surrounding a modern proof of FLT and to build the definitions and libraries needed for further number theory. Its goals included enabling later researchers to state and work with modern results in Lean. The five years were a funded programme with these broader aims, rather than a measured time for a team to complete exactly the AI's task. ([Original funding proposal](https://gtr.ukri.org/projects?ref=EP/Y022904/1); [community project](https://lean-lang.org/use-cases/flt/).)

The AI effort built on Lean, mathlib, and existing community FLT work. Its **Prove2Me** framework organized dependencies and let agents work on individual proof obligations. This is the blueprint approach at remarkable scale. ([Anthropic's account](https://www.anthropic.com/research/formalizing-fermats-last-theorem).) The released repository includes a final-statement check and an audit restricting the proof to Lean's three standard foundational axioms; it is presented as a research artifact rather than a maintained mathematical library. ([Proof repository and verification instructions](https://github.com/anthropics/fermats-last-theorem).)

For me, the eleven-day result changes what seems possible. Turning such a large formal proof into an accessible, reusable library remains valuable work. The historical theorem, the machine-checked proof, and the infrastructure that helps people understand and extend it are all achievements worth recognizing.

## 5. Conditional and unconditional formalization

“Formalized in Lean” needs a precise object: **which statement has been proved, and on what does it depend?**

Suppose the desired result is $T$, and one crucial conjecture is $C$. A complete Lean proof of

$$
C\;\Longrightarrow\;T
$$

establishes a valid implication. It does not establish $C$. If $C$ is still open, the conclusion $T$ remains conditional on it. That can be a valuable research contribution, provided the condition is visible.

Three situations should be distinguished:

| Status | What has actually been established? |
| --- | --- |
| **A completed conditional result** | The implication from an explicitly stated additional assumption to the conclusion is fully proved. The assumption itself remains to be established. |
| **A partial formalization** | Some components are proved, but the target still depends on missing proofs or unproved imported claims. This is progress toward a complete result. |
| **A completed result without the extra conjecture** | The final theorem and the lemmas it uses are proved within the declared setting and standard foundations, without the extra conjectural input. This is the relevant sense of “unconditional.” |

Ordinary hypotheses are not defects. A theorem for Gaussian observations, positive definite matrices, or a stated parameter range can be unconditional **within that setting**. Likewise, the equality example above is fully proved even though it takes two equalities as hypotheses. “Unconditional” does not mean that a theorem has no assumptions or no logical foundation.

Lean also allows unfinished work to be expressed. **`sorry`** is a placeholder for a missing proof. **`axiom`** can introduce a claim without proving it. If a final result relies on such a placeholder or a new unproved mathematical axiom, a successful build is not enough to support the claimed unconditional theorem. Some axioms are ordinary foundations of classical mathematics; they must be distinguished from an axiom that simply assumes the project's difficult lemma. Lean's `#print axioms` command helps expose a theorem's axiom dependencies. ([Placeholders in the tutorial](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/); [axioms and foundations](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/).)

For my research, I would want the release to answer a concrete question: can another person start from the stated assumptions, rerun the released development, and reach the same final theorem without supplying an unproved missing step? Checking only a convenient supporting file would not answer that question.

## 6. A practical AI–Lean research workflow

The workflow I would recommend has a loop at its center. Formalization should begin early enough to influence the research, while explanation should continue after the proof has been checked.

<ol class="research-flow" aria-label="An AI and Lean research workflow">
<li>Specify the question and its assumptions</li>
<li>Explore ideas with a reasoning model</li>
<li>Write a blueprint and inspect the formal statement</li>
<li>Formalize small lemmas and run Lean</li>
<li>Return mathematical gaps for further reasoning</li>
<li>Check, explain, and release the complete result</li>
</ol>

**Begin with the statement.** Collect the relevant papers and write down exactly what improvement is sought. Ask the model to identify assumptions, existing results, and potential counterexamples. Record the target before proof attempts make it tempting to settle for a nearby, easier statement.

**Explore with the strongest reasoning available.** Ask ChatGPT or Claude for several routes and for explanations of why they might fail. Use computations and special cases to find errors and develop intuition. Retain a distinction between numerical evidence, an informal proof, and a formal proof.

**Build the blueprint and review the translation.** Agree on definitions and lemma statements. Translate the final Lean statement back into ordinary language and compare it with the intended theorem. Resolve mismatches before investing heavily in the proof.

**Formalize in small pieces.** Let an AI with suitable Lean skills implement individual lemmas and run the checker after each change. Smaller, cheaper models can be tried on routine tasks; difficult steps go to a stronger model or a human collaborator. Shared definitions should be stable enough for the pieces to fit together.

**Treat failures as information.** A syntax error needs a local repair. A missing library theorem may need additional formalization. A false intermediate claim needs new mathematics. Ask the model to explain which kind of obstacle it has encountered, and revise the blueprint when the argument changes.

**Check the complete result.** Rebuild the released development with specified Lean and library versions. Inspect the final statement and its dependencies, including placeholders and extra axioms. Have another reader review the correspondence between the paper and the formal theorem; Lean checks the deduction, while that review checks whether we asked it the intended question.

**Write for the next researcher.** Release the readable argument alongside the formal development. Explain the main idea, credit the people, sources, libraries, and AI systems involved, and link the paper's results to their formal counterparts. A proof becomes more useful when someone else can both rerun it and learn from it.

This is where my [first vibemathing experience](../2026-09-14-my-first-vibemathing-attempt/) matters to me. Receiving an argument and understanding it were separate events. The tool that helped produce the proof could also help teach me its geometry. I want formal verification and that educational conversation to strengthen each other.

## 7. What still matters after the proof is checked

Formalization can make the proof reusable, but **understanding remains a research product**. A dependency graph tells us which lemmas support a conclusion. An explanation can reveal why a change of variables was natural, why a geometric representation removed an obstacle, or how the method might transfer to another problem.

Shared libraries also deserve serious credit. A difficult theorem may become easy to formalize because other researchers have already built the definitions and intermediate results it needs. The history of the Liquid Tensor Experiment makes that accumulated effort visible: the celebrated technical steps depended on a larger development of reusable mathematics. ([Buzzard's account](https://xenaproject.wordpress.com/2022/09/12/beyond-the-liquid-tensor-experiment/).)

For the next generation of theoretical researchers, I would emphasize posing questions, reading formal statements, understanding examples, and explaining ideas. AI can help with syntax and routine proof search. Students still need opportunities to judge a definition, notice a hidden assumption, and connect a theorem to a meaningful problem. These skills determine what we ask our increasingly capable tools to do.

The same lesson extends to **AI for science**. Lean can establish a deduction inside a physical model or a guarantee about a statistical procedure. The model's connection to nature must still be assessed through observations and experiments. AlphaFold's blind assessment and the A-Lab's experimental feedback illustrate that connection. We will need better ways to test predictions, quantify uncertainty, reproduce measurements, and recognize when an apparently successful check is answering the wrong question. ([AlphaFold assessment](https://deepmind.google/blog/enabling-high-accuracy-protein-structure-prediction-at-the-proteome-scale/); [A-Lab](https://www.nature.com/articles/s41586-023-06734-w).)

My expectation is that verification will become an increasingly important constraint on progress. When generating ten thousand plausible ideas becomes affordable, the valuable next step is to determine which deserve further work. In mathematics we can often demand a formal certificate. In science we must build an equally serious relationship between computational proposals and empirical evidence.

## 8. My personal view of the new frontier

GPT-6 Astra and the later internal-model results have changed my view of mathematical problem solving. On **August 1, 2026**, OpenAI reported ten advances across mathematics and theoretical computer science from an internal Astra model, with subsequent Lean formalizations. The later Navier–Stokes announcement sharpened my sense that something fundamental had changed. ([Ten advances and proof releases](https://openai.com/index/ten-advances-in-mathematics/); [Navier–Stokes account](https://openai.com/index/navier-stokes-solution/).)

**To me, mathematical problem solving is already reaching what I would call AGI—and, in some tasks, ASI.** Those words express my personal reaction to the breadth and level of the work. They are not a settled classification of these systems, and success on mathematical problems does not by itself establish general intelligence across every domain.

What changes my expectations is the combination: a system can search for an argument, another can help make it formally checkable, and both can help explain it. I no longer want to organize my research around the assumption that discovering a proof must be the slowest part.

I want to ask better questions, explore more ambitious connections, and insist on evidence that can be checked and knowledge that can be shared. Verification gives us a way to remain intellectually responsible while letting our ambition grow.
