---
title: "My First Vibemathing Attempt"
date: 2026-09-14
updated: 2026-09-19
sequence: 2
category: Mathematics and AI
description: "A PDF, an overnight argument, and two days learning the geometry behind a problem that had resisted me for months."
image: assets/vibemathing/logdet-size-and-power.png
image_width: 2340
image_height: 1440
image_alt: "Size and power of a Gaussian complete-independence test based on the standardized sample-correlation log determinant. The null histogram follows the standard normal approximation; the specified AR(1) alternative shifts the distribution into the left-tail rejection region."
caption: "Monte Carlo illustration with p = 64 and n = 129: at a nominal 5% level, empirical size is 5.3% and empirical power is 73.9% against the specified AR(1) alternative with ρ = 0.15. Normal calibration is asymptotic."
draft: true
publish: true
draft_label: "Draft"
---

On **July 28, 2026**, I uploaded a paper to ChatGPT and asked **GPT-5.6 Sol** to remove the unnecessary assumptions and prove the strongest possible result. The next morning, it had produced an argument that I would spend the following two days learning to understand.

The extraordinary mathematics announcements that led me to try this experiment are the subject of [the first post in this series](../2026-09-11-entering-the-era-of-vibemathing/). Here I want to tell the personal story: what happened when I brought the model a statistical problem whose difficulties I knew well.

## The problem I chose

The problem concerns a familiar statistical object. Suppose we observe independent Gaussian vectors $X_1,\ldots,X_n\in\mathbb R^p$, with a positive definite population covariance matrix $\Sigma$. Write

$$
\bar X=\frac1n\sum_{i=1}^n X_i,\qquad
S=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)(X_i-\bar X)^{\mathsf T}.
$$

If $D$ is the diagonal matrix of sample variances, the Pearson sample correlation matrix and the statistic of interest are

$$
\widehat R=D^{-1/2}SD^{-1/2},
\qquad L_{n,p}=\log\det\widehat R.
$$

The determinant measures the collective redundancy among the standardized variables. Geometrically, it is a squared volume. Taking its logarithm turns products into sums and connects the statistic to Gaussian tests of complete independence.

The high-dimensional question is how $L_{n,p}$ fluctuates when $p$ grows. After subtracting an appropriate center and dividing by an appropriate scale, when does it approach a standard normal distribution? Can one theorem cover very small dimension-to-sample-size ratios, ratios approaching one, and population correlations with increasingly extreme eigenvalues?

There is a basic boundary: after estimating the mean, the residual degrees of freedom are $m=n-1$. The ordinary log determinant requires $p\leq m$ and a nonsingular population correlation matrix. “Remove the conditions” must mean removing unnecessary restrictions beyond these requirements.

This question has a substantial history. **Jiang and Yang (2013)** established high-dimensional central limit theorems for classical Gaussian likelihood-ratio statistics. **Tiefeng Jiang and Yongcheng Qi (2015)** extended those results to much wider relative growth rates of dimension and sample size. Their paper, *Likelihood Ratio Tests for High-Dimensional Normal Distributions*, was first published online on **March 25, 2015**. It was an important starting point for the line of work I wanted to pursue. ([Jiang and Yang](https://arxiv.org/abs/1306.0254); [Jiang and Qi](https://onlinelibrary.wiley.com/doi/10.1111/sjos.12147).)

**Jiang’s 2019 paper**, *Determinant of Sample Correlation Matrix with Application*, addressed nonidentity population correlation matrices. It proved a central limit theorem for a substantial class of alternatives; one sufficient regime required a nonvanishing aspect ratio and a smallest population eigenvalue above $1/2$, together with the paper’s other assumptions. It gave the problem a concrete form, but also left restrictions that I wanted to understand and remove. ([Jiang, 2019, *Annals of Applied Probability* 29, 1356–1397](https://doi.org/10.1214/17-AAP1362).)

Later, **Nestor Parolya, Johannes Heiny, and Dorota Kurowicka** developed a logarithmic law allowing non-Gaussian observations with finite fourth moments under spectral and growth conditions. **Heiny and Parolya** also established a heavy-tailed result with infinite fourth moments. Both papers appeared in journal volumes in **2024**. More recently, **Yanpeng Li, Zhi Liu, Jiahui Xie, and Wang Zhou**, in a preprint posted on **March 20, 2026**, studied the logarithmic law for independent-entry data under weak tail conditions, including near-singular regimes. ([Parolya, Heiny, and Kurowicka](https://doi.org/10.3150/23-BEJ1600); [Heiny and Parolya](https://doi.org/10.1214/23-AIHP1368); [Li, Liu, Xie, and Zhou](https://arxiv.org/abs/2603.19800).)

These advances cover different models and regimes. The question I returned to was specific: **could the empirically centered Gaussian Pearson statistic satisfy a central limit theorem throughout its nonsingular high-dimensional domain, for arbitrary positive definite population correlation matrices?**

I had previously spent roughly six months on this problem without a breakthrough. I knew what it felt like to follow a plausible approach until it stopped working, and how much effort another attempt might cost.

That history made it a meaningful experiment. I would recognize a real advance.

## A PDF, a broad request, and a night’s sleep

I dragged the paper into ChatGPT. My request was basic. Reconstructed in substance, it was:

> Remove the conditions and prove the strongest possible result for this problem.

I supplied no new lemma, no geometric reduction, and no proposed proof strategy. I asked the model to solve the problem, and let it work.

The next morning, the argument was there.

My initial reaction was amazement, followed by the need to check it. The writing was extremely compressed. Identities appeared with little explanation of why they were true, why they were useful, or how anyone would have thought to introduce them. Reading it felt like arriving at the end of a conversation whose crucial middle I had missed.

So I changed the task. I asked GPT to rewrite the proof educationally: explain the motivation, expand the transitions, and show the structure behind the calculations.

For the next two days, I kept asking questions. The model that had produced the proof became my tutor.

## Learning to see the geometry

The explanation began with a simple picture. Center each variable’s observations and regard the resulting column as a vector in the $m$-dimensional residual space. Normalize these vectors to unit length, writing them as $u_1,\ldots,u_p$. Then

$$
\widehat R=(u_i^{\mathsf T}u_j)_{i,j=1}^p,
\qquad
\det\widehat R=
\operatorname{Vol}(u_1,\ldots,u_p)^2.
$$

I had been trying to control a difficult matrix statistic. This representation showed me a random volume built from dependent Gaussian directions.

The next ingredient was a **Wiener chaos expansion**. This organizes square-integrable functions of Gaussian variables into orthogonal polynomial components. For the random coordinatewise normalization, the important first component is quadratic. Isolating it exposes a tractable leading term and leaves a remainder that can be controlled.

Together with an exact Wishart transform comparison, this gives a way to treat the dependence without forcing the population eigenvalues into a fixed bounded interval. The eventual theorem covers every sequence $p\to\infty$ with $m=n-1\geq p$ and positive definite population correlation $R_n$, including the square endpoint. ([My first paper, *On the Log Determinant of Sample Correlation Matrices under Gaussianity*](https://arxiv.org/abs/2608.00565).)

What impressed me was how naturally the pieces fit once someone explained the starting point. The geometry made the normalization intelligible; the chaos decomposition identified the fluctuation that mattered. This combination was far outside the approaches I had been pursuing.

I found the expanded AI exposition much easier to learn from than Jiang’s 2019 proof. My experience of that earlier argument had been one of lengthy technical calculations whose purpose was difficult for me to see. The educational rewrite let me see the destination before asking me to follow the algebra. An argument that first looked impossibly terse began to feel elegant and almost elementary.

That change in my own understanding was as memorable as the original output. The proof had appeared overnight, but appreciating it took two days.

Within those two days, I completed and submitted the first manuscript.

## Ten approaches, and the cost of trying

In its written account of the search, the model organized ten possible approaches. It described the first six as unsuccessful, the seventh and eighth as workable, and the ninth and tenth as untried.

I think about that list almost as much as I think about the final proof. For me, seriously learning and testing even one unfamiliar method could easily consume a month. A failed approach still costs time: one has to understand the machinery, adapt it to the problem, and find the obstruction. Human researchers cannot explore every plausible route with equal attention.

The model’s account made that cost visible. It suggested a kind of research assistance whose value includes the approaches we can abandon sooner, as well as the argument we eventually keep.

These are estimates based on my own experience. After spending six months on this very problem, I had a strong sense of the time it had saved me.

## What I mean by “zero-prompt” research

I call this a successful **zero-prompt research experience**. The term is deliberately informal: there was, of course, a prompt.

The “zero” refers to the amount of expert mathematical direction I supplied to the discovery. I uploaded the problem, made a broad request, and hoped the model would find the proof. I did not have to understand the successful route in advance, or teach it the idea that would unlock the result.

In that sense, zero-prompt research means giving the system a problem and almost praying that it will return the right mathematics.

I distinguish this from what I call **one-prompt research**: an expert may write just one message, yet encode a powerful mathematical insight in it—a reduction, a missing lemma, or a carefully chosen route through the literature. The message count is small, but the human contribution inside the message is large.

These are labels for my experience, not standard terminology. They describe how a proof is found. My subsequent questions, checks, and two days of learning were essential to turning the output into a paper I understood and could stand behind.

## Asking again: how accurate is the normal approximation?

The first success led to a natural next question. A central limit theorem says that an approximation becomes correct in the limit. A **Berry–Esseen theorem** asks how quickly it becomes accurate.

I again gave the model the problem without supplying the decisive method. Another paper emerged.

For the identity-correlation case $R=I_p$, let $Z_{m,p}$ denote the log determinant centered by its exact mean and scaled by its exact standard deviation. The approximation error is the largest difference between its distribution function and the standard normal distribution function $\Phi$:

$$
d_K=\sup_x\left|\Pr(Z_{m,p}\leq x)-\Phi(x)\right|.
$$

The result identifies a sharp asymptotic equivalent,

$$
d_K\sim
\frac{A_{m,p}}{6\sqrt{2\pi}\,V_{m,p}^{3/2}},
\qquad p\to\infty,\quad m\geq p,
$$

where $V_{m,p}$ is the exact variance of the unstandardized log determinant and $A_{m,p}$ is the magnitude of its third cumulant. One expression covers the different ways dimension and sample size can grow. At the square endpoint $m=p$, the error is of order $(\log p)^{-3/2}$.

The symbol $\sim$ matters: this is an exact leading asymptotic description of the error, not an equality for each finite sample. For arbitrary positive definite $R$, the paper also establishes a uniform finite-sample bound. ([*Sharp Berry–Esseen Bounds for the Log Determinant of a Gaussian Sample Correlation Matrix*](https://arxiv.org/abs/2608.12242).)

Again, what struck me was the coherence of the answer. A collection of apparently different regimes became instances of one formula. The second experience made the first feel much harder to dismiss as a lucky accident.

## From a convincing argument to a checked theorem

I subsequently used **Lean** to verify the mathematical results behind both projects. What I wanted was an unconditional derivation of the formalized conclusions from the stated statistical assumptions, with no additional unproved mathematical claims inserted as axioms.

The verification follows the actual Gaussian sample through the probability model and the relevant analytic arguments. The archived Berry–Esseen release includes the theorem statements, their correspondence with the paper, the dependency closure, and the build and axiom reports. Its thirteen public endpoints were checked using only Lean’s standard foundational axioms, with no unfinished proof placeholders in their dependencies. ([Verification archive, August 12, 2026](https://doi.org/10.5281/zenodo.21898548).)

That is the precise basis of my confidence: the encoded theorems have machine-checked proofs. The correspondence between those formal statements and the mathematical claims in the paper must also be established. Bibliographic priority and every sentence of exposition are separate matters.

For me, this completed an extraordinary sequence: the AI found an argument, helped me understand it, and the formal verification supplied a way to check the deductions beyond repeated informal rereading.

## A different timescale for research

Without AI, I believe either of these papers could have taken me at least a year. With GPT-5.6 Sol, the initial research and manuscript work took less than a week in total.

Those are my estimates of the discovery and writing time. The public releases and formalization have their own dates: the first paper appeared on arXiv on **August 1, 2026**, and the Berry–Esseen paper and its archived verification appeared on **August 12**. The overnight breakthrough, learning the proof, preparing a manuscript, and releasing a reproducible formalization are different stages of the story. ([First paper](https://arxiv.org/abs/2608.00565); [Berry–Esseen paper](https://arxiv.org/abs/2608.12242); [verification release](https://doi.org/10.5281/zenodo.21898548).)

I do not know how often this kind of success can be repeated. I do know what changed for me. A problem that had resisted six months of work became something I could revisit with one broad request. The proof came back before I understood the idea; then the same tool helped me acquire that understanding.

That reversal is what makes this feel like the beginning of a new era. I am accustomed to learning mathematics in order to discover a proof. This time, I first received a proof, then spent two days learning the mathematics that made it possible.

The experience has changed what I am willing to try. A new dawn calls to me.
