---
title: "Entering the Era of Vibemathing"
date: 2026-09-11
updated: 2026-09-22
sequence: 1
category: Theoretical Research and AI
description: "From the lowest-hanging Erdős problems to research at machine speed—and the question of what theoretical researchers should value next."
image: assets/vibemathing/low-hanging-fruit.png
image_width: 1536
image_height: 1024
image_alt: "A flying machine labeled AI plucks fruit high in a tree while a person on the ground calls it low hanging fruit."
caption: "“Low hanging” depends on who can reach it."
draft: true
publish: true
draft_label: "Draft"
---

During 2025 and 2026, AI for mathematics moved from helping with calculations, contest problems, and literature searches toward producing candidate solutions to open research problems. Two developments have been coming together: the increasingly capable reasoning models developed by organizations such as **OpenAI**, and systems such as **Axiom Math’s AxiomProver** that produce formal proofs. **Lean** is a tool for expressing mathematical statements precisely and checking their proofs according to explicit logical rules. It gives us a way to test a proposed argument beyond how persuasive its prose sounds. ([OpenAI’s research announcement](https://openai.com/index/model-disproves-discrete-geometry-conjecture/); [AxiomProver’s proof release](https://axiommath.ai/research/from-seeing-why-to-checking-everything/); [Lean’s introduction to propositions and proofs](https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/).)

By September, the question I found myself asking had changed. How should someone doing theoretical research work when an argument may arrive much faster than a person can learn to understand it? I want to ask this across mathematics, statistics, theoretical physics, theoretical computer science, and other disciplines where developing theory is central.

This first post traces the events behind that question. My own experiment, beginning on July 28 with a sample-correlation log-determinant problem, belongs in [Post 2: My First Vibemathing Attempt](../2026-09-14-my-first-vibemathing-attempt/). The details of verification belong in [Post 3: Lean and the Future of Theoretical Research](../2026-09-14-lean-and-the-future-of-mathematics/).

## The lowest-hanging fruit

The early successes need a careful description. An Erdős problem listed as open may be a famous obstacle with decades of serious attention. It may also be a question mentioned once in an old paper, a problem whose solution appeared elsewhere under different terminology, or a statement missing an important hypothesis. Finding a solution to one of these neglected questions can be useful even when it requires no new mathematical machinery.

Terence Tao’s comments give a particularly clear record of this stage.

| Date | What Tao actually described |
| --- | --- |
| **November 30, 2025** | Automated sweeps were beginning to “resolve the lowest hanging fruit.” He discussed overlooked literature, lightly studied questions, and a version of Erdős problem 124 that became easier because a hypothesis had been omitted. ([Original post](https://mathstodon.xyz/@tao/115639984077620023); [conclusion of the thread](https://mathstodon.xyz/@tao/115639985263560286).) |
| **December 26, 2025** | He made the meaning explicit: problems “amenable to simple proofs using fairly standard techniques.” His examples included both apparent new proofs and a case later found in the literature. ([Original post](https://mathstodon.xyz/@tao/115788262274999408).) |
| **March 20, 2026** | In his Dwarkesh interview, he said, “Fifty-odd problems have been solved with AI assistance,” while observing an apparent plateau in purely autonomous successes and continued progress through collaboration. ([Interview, discussion beginning around 30:31](https://www.dwarkesh.com/p/terence-tao).) |

“Low-hanging” described the relationship between the available methods and the neglected problem. It did not mean that every result was trivial, or that every purported discovery was already known. In some cases AI made a better literature search possible. In others it combined familiar techniques into a short argument that had not attracted enough attention to be written down. Tao’s December post explicitly considered—and did not simply equate—the possibilities of rediscovery and new reasoning. ([December 26 discussion](https://mathstodon.xyz/@tao/115788262274999408).)

At the same time, formal proof generation was advancing. On **January 8, 2026**, Axiom released Lean proofs for all twelve problems from the 2025 Putnam competition. Eight had been completed within the exam period; the full twelve were completed with additional time. On **February 5**, Axiom’s *Proof of Concept* described work on open problems as well as proof generation. These developments helped make a new workflow credible: a system could search for mathematics and return an artifact that another program could check. ([Putnam release](https://axiommath.ai/research/from-seeing-why-to-checking-everything/); [Proof of Concept](https://axiommath.ai/research/proof-of-concept/).)

## May 20: a turning point in the plane

For me, the **Erdős Unit Distance Conjecture** marked a different level of significance. Given $n$ points in the plane, let $u(n)$ be the greatest possible number of pairs exactly one unit apart. Erdős conjectured growth of the form $n^{1+o(1)}$. On **May 20, 2026**, OpenAI announced that an internal, unreleased model had constructed infinitely many configurations with at least $n^{1+\delta}$ such pairs for a fixed $\delta>0$. This disproved the conjecture. ([Announcement](https://openai.com/index/model-disproves-discrete-geometry-conjecture/).)

The argument brought algebraic number theory, including Golod–Shafarevich theory, into discrete geometry. A same-day companion paper by **Noga Alon, Thomas Bloom, Tim Gowers, Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, and Melanie Matchett Wood** explained and assessed the construction. Their work supplied human mathematical scrutiny and context. ([Companion paper, May 20](https://arxiv.org/abs/2605.20695).)

**Jacob Tsimerman**, who later received a [**2026 Fields Medal**](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026), offered a striking assessment:

> “This is a really impressive piece of work, and I would accept it for any journal without hesitation.”

His role here was as an expert reviewer and coauthor of the companion discussion. The announcement describes human checking; it does not identify his contribution as a Lean formalization. ([Tsimerman’s statement](https://openai.com/index/model-disproves-discrete-geometry-conjecture/).)

The May announcement left the model unnamed. **GPT-5.6 Sol’s limited preview came on June 26**, followed by the wider **GPT-5.6 release on July 9**. By then, researchers could begin trying the new tools on their own questions. ([June 26 preview](https://openai.com/index/previewing-gpt-5-6-sol/); [July 9 release](https://openai.com/index/gpt-5-6/).)

Tsimerman has also turned toward the safety questions raised by these capabilities. He is scientific director of the **Mathematical AI Safety Institute (MAISI)**, an independent nonprofit working on mathematical foundations for AI safety. The institution illustrates another response available to mathematicians: applying mathematical expertise to the systems changing the profession. ([MAISI](https://www.maisi.org/).)

## The July that changed my expectations

The release of stronger tools was followed by a remarkable concentration of announcements. The dates matter because they show how quickly the public conversation changed.

| Date in 2026 | Result and evidence |
| --- | --- |
| **July 10** | OpenAI announced a proof of the **Cycle Double Cover conjecture**: every bridgeless graph has cycles covering each edge exactly twice. A [Lean development](https://github.com/openai/cdc-lean) accompanied the [announcement](https://x.com/__eknight__/status/2075643450196971805). Independent explanations by [Jim Geelen](https://arxiv.org/abs/2607.15399) and [Sang-il Oum](https://arxiv.org/abs/2607.16356) appeared on July 16 and 17. |
| **July 20** | **Levent Alpöge**, crediting Akhil Mathew and Claude Fable, announced a counterexample to the **Jacobian conjecture in dimension 3**. A polynomial map can have a nonzero constant Jacobian determinant and fail to be injective. The construction extends to higher dimensions; dimension 2 is a separate question. ([Independent Isabelle/HOL verification](https://isa-afp.org/entries/Jacobian_Counterexample.html).) |
| **July 22** | **Frederic Koehler and Pui Kuen Leung** posted *Anticoncentration of the Permanent in Ginibre Ensembles*, resolving the complex-Gaussian case of the **Aaronson–Arkhipov Permanent Anticoncentration Conjecture**. This was especially exciting to me because of quantum sampling. I include it as part of the mathematical context; **I have not verified whether GPT-5.6 contributed to this result.** ([Paper](https://arxiv.org/abs/2607.20329).) |
| **July 27** | Three independent contributions on **Feige’s conjecture** appeared, including two papers explicitly crediting GPT-5.6 systems for finding a proof. The third contribution was explicitly conditional. ([Fu et al.](https://arxiv.org/abs/2607.23980); [Nie and Wei](https://arxiv.org/abs/2607.24528); [Stander](https://doi.org/10.5281/zenodo.21626794).) |
| **July 28** | I began my own GPT-5.6 Sol experiment on the log determinant of a Gaussian sample correlation matrix. That personal account is now [Post 2](../2026-09-14-my-first-vibemathing-attempt/). |

On **July 31**, Samuel Allen Alexander published a video titled *35(!) open math problems solved by AI in the last 9 days (people claim)*. The final qualifier matters. It records the extraordinary pace of announcements without making the video a mathematical certification of each claim. ([July 31 video](https://youtu.be/uuQlW_1J_dE); [VibeMathed](https://vibemathed.com/).)

## Collisions and speedruns

I use **collision** for independent groups reaching the same problem at nearly the same time. A **speedrun** is an attempt to reproduce or finish a result quickly, often after learning that a current model can solve it. These phenomena can overlap, but their implications differ: independence concerns provenance, while speed concerns the cost of reaching an answer.

Feige’s conjecture is a case of a **three-way collision**. The July 27 contributions were by **Weibo Fu, Yanjun Han, Guanyang Wang, Jun Yan, Peng Zhang, and Zhengqing Zhou**; **Zipei Nie and Jiaye Wei**; and **Mark Stander**. Counting the announcements as a collision does not erase the conditional status of Stander’s manuscript. ([First paper](https://arxiv.org/abs/2607.23980); [second paper](https://arxiv.org/abs/2607.24528); [conditional contribution](https://doi.org/10.5281/zenodo.21626794).)

Wang’s July 30 account also describes a reproduction experiment before the proof was public. A prompt asking the model to search broadly across the literature succeeded in three of four runs; a shorter prompt without that direction succeeded in none of four. He stresses that he already knew the proof, making the prompt choice partly retrospective. The route combined the recent Vlassis–Thomas work with classical convex geometry. This is evidence of a rapidly reproducible connection once the right ingredients were available, not a general success-rate estimate for mathematical research. ([Wang’s account](https://guanyangwang.github.io/blog/feige-conjecture.html); [Vlassis and Thomas, July 9](https://arxiv.org/abs/2607.08415).)

Litt’s **August 11** essay describes an OpenAI internal model reproducing the Jacobian counterexample and Anthropic replicating several OpenAI results. These reports show reproducibility; they do not establish independent discovery with identical access to information. ([The End of Mathematics](https://www.daniellitt.com/blog/2026/8/11/the-end-of-mathematics/).)

Alexander’s **August 19** video brought the collision metaphor into its title: different groups reportedly resolving **Gromov’s conjecture** almost simultaneously. It is a contemporary account of the pace of announcements, alongside the source-linked Feige case above. ([AI Math Collisions](https://youtu.be/4zZxqsypzsg).)

<!-- Editorial follow-up: the video's complete list of examples still needs its transcript and primary-source checks. The paragraph above reports its title, not a verified inventory of its contents. -->

### Prime gaps: a speedrun in public

The late-August and early-September rush to improve **bounded gaps between primes** gives a particularly concrete example of the speedrun atmosphere. If $p_n$ is the $n$th prime, the quantity at issue is $H_1=\liminf_{n\to\infty}(p_{n+1}-p_n)$. A bound $H_1\leq B$ means that infinitely many consecutive prime pairs have gap at most $B$; it does not bound every prime gap. The twin-prime conjecture would give $H_1=2$. The recent announcements sit on top of more than a decade of analytic and computational work.

**All clock times below are UTC.** The 2026 entries follow the recorded timestamps, down to the second. Each row identifies the event being timed: a deposit, submission, repository event, public link, or announcement. The sequence ends with OpenAI’s own announcement of **186**, the strongest bound among these results; its earlier repository history appears separately.

| Recorded date/time (UTC) | Bound on $H_1$ | Event, contribution, and source |
|---|---|---|
| May 2013 | **70,000,000** | **Yitang Zhang** established the first finite unconditional bound, opening the bounded-gap problem to quantitative improvement. ([Tao’s account](https://terrytao.wordpress.com/2013/11/19/polymath8b-bounded-intervals-with-many-primes-after-maynard/).) |
| July 2013 | **4,680** | **Polymath8a**, the collaborative project involving Tao and many others, combined analytic improvements with numerical optimization. ([Polymath8b paper’s historical account](https://arxiv.org/abs/1407.4897).) |
| November 2013 | **600** | **James Maynard** introduced a new multidimensional sieve method. Tao independently developed a related approach; the 600 bound here is Maynard’s. ([Tao’s November 19 post](https://terrytao.wordpress.com/2013/11/19/polymath8b-bounded-intervals-with-many-primes-after-maynard/).) |
| April 2014 | **246** | **Polymath8b**, again a collective effort involving Tao, reached the unconditional bound that stood for more than twelve years. ([Tao’s April 14 update](https://terrytao.wordpress.com/2014/04/14/polymath8b-x-writing-the-paper-and-chasing-down-loose-ends/); [paper](https://arxiv.org/abs/1407.4897).) |
| August 28, 2026<br>**02:07:01** | **240** | **Zenodo record created; preprint claim. Hanxin Zhang** credited **GPT-5.6 Sol** with discovering the proof. The platform records this creation time and an August 28 publication date. The companion repository checks the finite numerical certificates, a narrower scope than the full analytic argument. ([Original preprint](https://zenodo.org/records/22135842); [timestamp metadata](https://zenodo.org/api/records/22135842); [certificates](https://github.com/hanxinzhang/prime-bound).) |
| August 31<br>**17:39:30** | **240** | **arXiv v1 submission. Julia Stadlmann** submitted her paper combining Bombieri–Vinogradov with newer equidistribution estimates for smooth moduli. This is arXiv’s submission timestamp, not an independently established first-public-access time. Her analytic framework became a starting point for subsequent improvements. ([Paper and submission history](https://arxiv.org/abs/2608.31126).) |
| September 1<br>**22:27:31** | **236** | **Paper added to the website source. Shiva Kintali’s** Git history records the addition of `Prime-Gaps.pdf` at this time. At **22:45:27**, he publicly announced the result and linked the PDF. He describes a human-directed workflow using **Claude, ChatGPT, and two open-weight models**, building on Stadlmann’s framework. ([PDF-addition commit](https://github.com/shivakintali/shivakintali.github.io/commit/33a6d8c90d8b242e65d3e9657ae25feae32eff89); [announcement with paper link](https://x.com/ShivaKintali/status/2094919595199263232); [paper](https://shivakintali.github.io/papers/Prime-Gaps.pdf).) |
| September 2<br>**20:53:32** | **186** | **OpenAI repository created.** GitHub records creation of `PrimeGaps186` at this time; its initial commit is dated **20:53:24**. These are repository timestamps: they do not, by themselves, establish when the repository first became publicly accessible. ([Repository metadata](https://api.github.com/repos/openai/PrimeGaps186); [initial commit](https://github.com/openai/PrimeGaps186/commit/61340d0b74163003b32756bb16e91d9209a5e330).) |
| September 3<br>**14:56:25** | **212** | **Axiom Math’s public announcement.** The team announced its bound of 212, building on Stadlmann’s ideas and extensive numerical optimization. Its September 3 draft describes **AxiomProver** formalizing a deduction from specified analytic and numerical inputs. The time here belongs to the announcement; I have not verified the PDF’s original upload time. ([Announcement](https://x.com/axiommathai/status/2095526333799633063); [paper and formalization appendix](https://primegaps.axiommath.ai/bgp212.pdf).) |
| September 3<br>**17:05:36** | **186** | **OpenAI’s repository publicly linked.** A post linked directly to the repository and described the 186 result. This is the earliest timestamped public link I located, establishing that the repository was being shared by this time, before OpenAI’s own announcement below. ([Contemporaneous public link](https://x.com/scaling01/status/2095558841509318673).) |
| September 3<br>**17:35:02** | **188** | **Reported but unpublished. Levent Alpöge** credited **Jack Kleeman and Claude** with a bound of 188, saying it had been sent privately to Goldston “some weeks ago” and was also formalized. This time dates his public statement. Neither the private discovery date nor a public paper-posting time is established; I have not located a public manuscript or formalization artifact. ([Alpöge’s statement](https://x.com/__alpoge__/status/2095566251804209545).) |
| September 3<br>**19:49:34** | **186** | **OpenAI / GPT-6 Astra announcement—the strongest bound in this sequence. Weijie Su** announced the result and Lean formalization. The paper is dated **August 30**, but that printed date does not establish its first public posting time. It describes Stadlmann’s result as independent concurrent work. The Lean repository explicitly declares three external inputs. ([Su’s announcement](https://x.com/weijie444/status/2095600108956262911); [paper](https://cdn.openai.com/pdf/51126fac-1b68-4128-9666-c908bcc16033/short_gaps.pdf); [Lean repository](https://github.com/openai/PrimeGaps186).) |

**The announcement order is clear: Axiom’s 212 at 14:56:25 → Alpöge’s report of Claude’s 188 at 17:35:02 → Su’s announcement of OpenAI’s 186 at 19:49:34, all on September 3.** OpenAI’s repository was already being shared at 17:05:36, and its repository records date to the previous evening. This distinction matters: the order of announcements does not establish the order of discovery or the first upload time of every paper. Su later described the OpenAI and Anthropic efforts as concurrent. ([Su’s clarification](https://x.com/weijie444/status/2099610299146051896).)

Tao’s September 5 retrospective asks what we should value in such a race: a smaller numerical bound, the methods that produced it, the understanding those methods create, and the researchers who learn through the work. That is why this example interests me. Speed makes the change visible; the lasting contribution also depends on what others can learn, verify, and reuse. ([Tao’s discussion](https://mathstodon.xyz/@tao/117219548485446992).)

These stories make me think differently about priority. A short interval between announcements may reflect several people discovering that the same new capability has become available. Reproduction is useful evidence, but the value of the second result also depends on whether it independently checks, simplifies, explains, or extends the first. Formal verification using a proof assistant such as **Lean** is another valuable contribution.

## What the growth looks like

The first chart uses actual historical files from the **VibeMathed repository**, supplemented by a dated snapshot of its current public dataset. It does not take today’s list and pretend those entries were all visible on their assigned solution dates.

<figure class="article-diagram">
<div class="diagram-scroll"><a href="../../assets/vibemathing/vibemathed-history.svg"><img src="../../assets/vibemathing/vibemathed-history.svg" alt="Recorded VibeMathed catalog counts grew from 75 on July 27 to 717 on September 14; 492 records were marked resolved in the final snapshot." width="1100" height="650" loading="lazy"></a></div>
<figcaption>Historical catalog snapshots, not an audit of every theorem. Blue includes partial results and candidate claims; green uses the catalog’s “resolved” classification. The first snapshot predates that status field. Sources: <a href="https://github.com/mrconter1/vibemathed/commits/main/src/data/problems.json">repository history</a> and <a href="https://vibemathed.com/api/dataset">dataset API</a>. <a href="../../assets/vibemathing/vibemathed-history.csv">Download counts and source links</a>.</figcaption>
</figure>

The repository explains that later community edits live in a database, while its checked-in JSON serves as a baseline and recovery snapshot. Consequently, these observations are not a complete daily archive of the live website. Backfills, reclassification, and newly reported results all affect the curve. The **717 catalog records** and **492 marked resolved** in the September 14 snapshot are useful measures of reported activity, with those limits. ([Repository documentation](https://github.com/mrconter1/vibemathed); [dataset and methodology](https://vibemathed.com/api/dataset).)

The second chart asks a different question: how much mathematics was being submitted to arXiv? It uses the archive’s article counts, **excluding cross-listings into mathematics**, and compares the same eight months of 2025 and 2026.

<figure class="article-diagram">
<div class="diagram-scroll"><a href="../../assets/vibemathing/arxiv-math-monthly.svg"><img src="../../assets/vibemathing/arxiv-math-monthly.svg" alt="arXiv mathematics article counts in 2026 compared with 2025. July rose to 5,697, 44.3 percent above the previous July; August rose to 6,307, 79.1 percent above the previous August." width="1100" height="650" loading="lazy"></a></div>
<figcaption>January–August article counts from arXiv’s <a href="https://arxiv.org/year/math/2025">2025</a> and <a href="https://arxiv.org/year/math/2026">2026</a> mathematics statistics. September is incomplete and omitted. <a href="../../assets/vibemathing/arxiv-math-monthly.csv">Download the monthly data</a>.</figcaption>
</figure>

July 2026 had **5,697** mathematics articles, compared with **3,948** in July 2025: an increase of **44.3%**. August rose from **3,522** to **6,307**, an increase of **79.1%**. Across January–August, the total increased from **29,385** to **39,232**, or **33.5%**. These are submission counts. They do not measure correctness, importance, or the fraction caused by AI. ([Official 2025 counts](https://arxiv.org/year/math/2025); [official 2026 counts](https://arxiv.org/year/math/2026).)

The growing volume makes one consequence difficult to ignore: researchers must decide what deserves sustained attention. Reading, organizing, and explaining new work can become the limiting resources even when producing a manuscript becomes easier.

## Alpöge’s remarkable summer

Levent Alpöge’s recent work offers a compact view of the range of activity. The table collects the ten recent result records associated with him in the catalog reviewed for this post. Dates refer to public announcements or releases unless otherwise stated. The last column distinguishes completed constructions, partial advances, and claims still being assessed.

| Public date in 2026 | Work and collaborators | What was reported |
| --- | --- | --- |
| **July 20** | **Jacobian conjecture**; Akhil Mathew and Claude Fable credited | A counterexample in dimension 3, with higher-dimensional extensions. ([Independent formal verification](https://isa-afp.org/entries/Jacobian_Counterexample.html).) |
| **August 10** | **Zeros of the Riemann zeta function**; Claude and an Anthropic team | A lower bound of **67.2%** of nontrivial zeros on the critical line, up from 41.6%. This is partial progress, not the Riemann hypothesis. ([Announcement and artifacts](https://www.anthropic.com/research/riemann-zeta).) |
| **August 12** | **Hadamard matrices**; Philippe Voinov, Saul Reynolds-Haertle, and Claude | A construction including order 668, previously the smallest unresolved order. Epoch records the reported solution and its provisional AI attribution; the general Hadamard conjecture remains separate. ([Epoch’s record](https://epoch.ai/frontiermath/open-problems/hadamard); [announcement](https://x.com/__alpoge__/status/2087504785952182273).) |
| **August 19** | **Smooth Carathéodory–Loewner conjecture**; John-Paul Smith and AI tools | An announced smooth counterexample, with a public reconstruction and formal artifact. The smooth and analytic formulations must be distinguished. ([Formalization-oriented account](https://github.com/google-deepmind/formal-conjectures/blob/7aa855bb344450777d9b19fe1cf11f2f5f9fae09/FormalConjectures/Other/CaratheodoryLoewnerCounterexample.md).) |
| **August 20** | **Elliptic-curve rank record**; Ava Howell and Claude | An elliptic curve over the rationals with at least 30 independent rational points. An exact-rank assertion requires attention to the certification’s assumptions. ([ICARM announcement](https://icarm.io/news/new-record-breaking-elliptic-curve-reported/); [curve record](https://elliptic-rank.icarm.cloud/curve/273).) |
| **August 23** | **A further elliptic-curve record**; Ava Howell and Claude | A curve with **rank at least 31**. The record lists 31 independent points; its commentary makes the exact-rank certification conditional on BSD and GRH. ([Curve 302](https://elliptic-rank.icarm.cloud/curve/302).) |
| **August 24** | **A complex structure on the six-sphere**; Claude | A proposed construction using a family of complex tori. This is listed here as a **candidate claim under review**, not as an independently established resolution. ([Manuscript](https://alpo.ge/s6.pdf); [catalog](https://vibemathed.com/).) |
| **September 8** | **Incompressible porous media**; Tristan Buckmaster and Matei Coiculescu | Finite-time blowup with a force smooth in space and time. ([Paper](https://cims.nyu.edu/~tristanb/ipm.pdf).) |
| **September 8** | **Inviscid Boussinesq system**; Tristan Buckmaster | Finite-time blowup with smooth forcing. Buckmaster dates the breakthrough to August 15 and Lean verification to August 22. ([Paper](https://cims.nyu.edu/~tristanb/boussinesq.pdf); [firsthand chronology](https://cims.nyu.edu/~tristanb/statement.pdf).) |
| **September 8** | **Three-dimensional incompressible Euler equations**; Tristan Buckmaster | Finite-time blowup with smooth forcing, released with a formal development. This is a forced Euler result. ([Paper](https://cims.nyu.edu/~tristanb/euler.pdf); [Lean repository](https://github.com/tristanbuckmaster/fluid_lean).) |

The fluid results are particularly revealing about the work behind a headline. Buckmaster credits the earlier program of **Diego Córdoba and Luis Martínez-Zoroa**, describes extensive use of several models, and separates finding an argument from understanding and rewriting it. He reports that producing a readable mathematical account remained substantial work after formal verification. ([Buckmaster’s statement](https://cims.nyu.edu/~tristanb/statement.pdf).)

## Ten research advances, then eleven days for Fermat

On **August 1**, OpenAI released **ten advances in mathematics and theoretical computer science** from an internal Astra model. The subjects included sphere packing, codes, non-sofic groups, operator algebras, circuit complexity, quantum games, lattice problems, and extremal combinatorics. The announcement says each argument was subsequently formalized in a Lean certificate. These were research results resolving or advancing open questions—not simply ten solved items on a contest or FrontierMath test. ([Announcement](https://openai.com/index/ten-advances-in-mathematics/); [proof artifacts](https://github.com/openai/ten-proofs).)

On **September 4**, Anthropic announced an **eleven-day formalization of Fermat’s Last Theorem**. Its reported completion time was August 18 UTC. The result followed a known proof and built on existing mathematical and formal infrastructure. It automated an enormous verification project; it did not newly discover the theorem. ([Announcement and repository](https://www.anthropic.com/research/formalizing-fermats-last-theorem).)

The contrast with earlier expectations is real but needs the right denominator. In 2024, Kevin Buzzard described a **five-year funded project** to formalize the theorem and develop the surrounding infrastructure. That is a project timescale, not a proven lower bound on how long formalization must take. The community effort and the later automated campaign also had different aims and starting points. ([Buzzard’s 2024 account](https://www.imperial.ac.uk/be-inspired/magazine/issue-56/42--professor-kevin-buzzard/); [community project](https://lean-lang.org/use-cases/flt/).)

The change is nonetheless extraordinary. A task organized on the scale of years could now have a checked endpoint reported after days. The longer-term value will also depend on how much of that formal development becomes reusable mathematics.

## Eighty-eight hours, and a joke that fiction supplied first

On **September 8**, OpenAI released a proposed resolution of the Navier–Stokes Millennium problem. Its system reported reaching the argument on **September 5**, about **88 hours** after the first agents began, followed by **17 additional hours** of Lean formalization and verification with GPT-6 Astra. The discovery effort used a newer internal model and, in the successful group, roughly 10,000 concurrent agents. This was a coordinated, large-compute effort. ([OpenAI’s account](https://openai.com/index/navier-stokes-solution/).)

The mathematical scope matters: the announced construction has an initially smooth fluid, finite energy, and a **smooth external force**, and targets alternatives **C and D** in the Clay formulation. It should not be silently retold as an unforced Navier–Stokes theorem. Publication of a claimed solution and Lean artifacts is also distinct from the Clay Institute’s recognition process. ([Result statement](https://openai.com/index/navier-stokes-solution/); [official problem formulation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).)

This reminded me of the Chinese novel **《学霸的黑科技系统》**, often translated as *Scholar’s Advanced Technological System*, by **晨星LL**. In Chapter 417, *“Answering a Millennium Problem!”*, Lu Zhou is already close to the end of his Navier–Stokes work when he sets a **168-hour countdown** for the final push. ([Chapter 417](https://book.shencou.com/novel/74/122188.html).)

There is a joke almost too good to resist: even a novelist giving the hero extraordinary assistance allowed a week, while a real laboratory now reports 88 hours. The comparison is playful—the tasks, prior work, and resources differ—but it captures how quickly the timescale has become difficult to imagine.

## Recent updates

*A running record of new announcements and released results.*

### September 21, 2026 — OpenAI reports solving more than 100 additional open problems

OpenAI says the internal model behind its Navier–Stokes announcement has now resolved **more than 100 additional, long-standing open problems across most areas of mathematics**. The company dates the start of training to **August 28**. The scale of this claim extends the story from a sequence of individual breakthroughs to a broad wave of results across different fields. ([OpenAI’s September 21 announcement](https://openai.com/index/advisory-group-on-mathematics-and-ai/).)

**This is an announcement of results awaiting fuller public presentation.** The announcement does not enumerate the problems or provide the statements and proofs for the full collection. It therefore does not yet let a reader assess the claimed solutions individually, their assumptions, or the extent of their formal verification. Those details will matter as the work is released. ([Announcement](https://openai.com/index/advisory-group-on-mathematics-and-ai/).)

The accompanying institutional development is also significant. An independent **Advisory Group on Mathematics and Artificial Intelligence**, hosted at the Institute for Advanced Study, includes **Timothy Gowers, Camillo De Lellis, Martin Hairer, Edward Witten**, and other mathematicians. The group identifies its immediate task as advising OpenAI on coordinating the release of the many results the company reports. Its members are unpaid for this work, plan to publish their recommendations, and emphasize that they have no decision-making authority at AI companies. ([The group’s statement and membership](https://agmai.org/).)

For me, the striking feature is the combination of **breadth and pace**. If these reported solutions withstand scrutiny, researchers across many fields may face the same questions at once: which new arguments should we study first, which ideas connect different results, and how can this work become useful shared knowledge? The advisory group also gives a concrete setting for the disagreement discussed below: how to welcome discoveries while sustaining understanding, attribution, and the development of future researchers.

## A warning from 25 Fields medalists—and a different picture of participation

On **September 11**, 25 Fields medalists published an opinion piece arguing that the goals of AI companies and the mathematical community are “severely misaligned.” They acknowledged the new capabilities while warning that a race to announce solutions can undermine understanding, attribution, and the development of students. Their concern was about the purpose of mathematics and the institutions supporting it. ([Joint opinion in Le Monde](https://www.lemonde.fr/en/opinion/article/2026/09/11/25-fields-medalists-warn-the-goals-of-the-ai-companies-and-the-goals-of-the-mathematical-community-are-severely-misaligned_6757433_23.html).)

On **September 17, Timothy Gowers explained why he did not sign**. He agreed with much of the letter and believed that mathematics faced a crisis, but questioned its hierarchy of values: for some mathematicians, solving problems is itself a central goal, with conceptual understanding helping them get there. He also argued that a flood of AI results could increase the mathematics we successfully understand, even if much remains unread. His urgent concerns included preserving researchers’ motivation, training future mathematicians, and sustaining funding. He doubted that criticizing AI companies for solving problems quickly offered an effective response to capabilities that would soon be widely available. ([Why I didn’t sign the Fields medallists’ letter](https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/).)

For a fuller philosophical exploration of this disagreement, see **[Post 05: A Dialogue Concerning the Future of Mathematics](../2026-09-20-a-dialogue-concerning-the-future-of-mathematics/)**, subtitled *On Proof, Understanding, and Artificial Intelligence*. It is an AI-generated fictional dialogue that examines both positions and asks what mathematical progress, understanding, and responsibility should mean in this new setting.

Another story circulating in mid-September showed the possibility of broader participation. **Aayush Bathija and Prince Rohatgi**, students at Oak Park High School, worked with **Daniel Soskin**, an assistant adjunct professor at UCLA, on bounded ratios for Lorentzian polynomials: inequalities controlling products and ratios of their coefficients. ([Paper](https://arxiv.org/html/2609.05341v3); [Soskin’s biography](https://danielsoskinhome.wixsite.com/portfolio).)

**This addressed a previously unresolved question in the research program of Fields medalist June Huh.** The development of Lorentzian polynomials is explicitly recognized in Huh’s **2022 Fields Medal citation**. Huh had posed and motivated the bounded-ratio problem; his 2025 joint paper with **Daoji Huang, Daniel Soskin, and Botong Wang** established results for the quadratic case. **That earlier work had not resolved the extension to higher-degree Lorentzian polynomials.** Bathija, Rohatgi, and Soskin’s new paper characterizes the bounded ratios in arbitrary degree and determines their optimal bounds in three variables. ([Fields Medal citation](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022); [2025 paper](https://arxiv.org/abs/2510.25030); [new paper, introduction and acknowledgments](https://arxiv.org/html/2609.05341v3).)

The authors acknowledge AI assistance with calculations, ideas, and editing. They report both helpful and misleading suggestions, say they independently checked the computations, and also acknowledge independent overlapping work by other groups. ([Acknowledgments and concurrent work](https://arxiv.org/html/2609.05341v3).)

Its first arXiv version was posted on **September 4**, a week before the medalists’ letter. The collaboration brings students, experienced mathematicians, and new tools into the same research program—a hopeful example of how participation might widen. ([Submission history](https://arxiv.org/abs/2609.05341).)

## Litt’s two essays: the future to avoid and the future to build

Daniel Litt’s **August 11** essay, *The End of Mathematics*, imagines a bad institutional trajectory rather than predicting one. Its worst outcome is that output keeps growing while researchers lose expertise, stop sharing unfinished ideas, and fail to train successors. Even superior machines might then coexist with stagnating mathematics: the community that understands, develops, and cares about the work has weakened. ([The End of Mathematics](https://www.daniellitt.com/blog/2026/8/11/the-end-of-mathematics/).)

His **September 13** response, *A beginning for mathematics*, offers a constructive direction. He welcomes valuable mathematics regardless of its source, while arguing that human understanding must still be developed and demonstrated. He proposes greater emphasis on rigorous PhD defenses, talks, discussion, and seminars. The aim is to preserve mathematical understanding and cultivate mathematicians, rather than preserve every existing professional convention. His phrase “no one can understand mathematics for us” captures the educational obligation particularly well. ([A beginning for mathematics](https://www.daniellitt.com/blog/2026/9/13/a-beginning-for-mathematics/).)

Together, these essays help me read the history above and ask a broader question about theoretical research. A succession of announcements shows what new systems can produce. It does not, by itself, tell us what kind of research community we are building.

<span id="what-should-mathematical-research-value-now"></span>

## What should theoretical research value now?

My view is that the value of research will increasingly depend on what a result enables people to understand and do. Theorems, models, and theoretical explanations remain valuable. When producing candidate arguments becomes cheap, paper counts and priority timestamps become less reliable measures of a researcher’s contribution.

**We should prepare now.** [Gowers’s response](https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/) makes room for both problem solving and conceptual understanding, while asking how we can sustain the motivation and institutions that support research. We should take those questions seriously as increasingly capable AI becomes widely available.

For me, preparation means choosing worthwhile questions, learning to work critically with AI, and making results understandable and reusable. **Formal verification and machine-checked proofs deserve particular emphasis:** systems such as Lean let others check and build on formalized arguments.

**The next generation needs meaningful opportunities to do research alongside AI.** We should rethink training, recognition, and funding with students involved in that discussion, so they can develop judgment, independence, and reasons to pursue theoretical research.

I do not mean that these activities are permanently beyond AI. Their value does not depend on a machine being unable to perform them. They matter because they are among the reasons we pursue theoretical work at all.

The future I want is one in which a result arriving overnight gives us more time to understand its ideas, ask a better next question, and bring someone else into the subject. That is the standard by which I would like to judge the era of vibemathing.
