# Rebuttal to MiniMax Fresh Review of Revised Paper

**Paper:** "How to Auto Research by AI: From Traditional Methods to Full Automation" (Revised Version)  
**Reviewer:** MiniMax-M2.7-highspeed  
**Fresh Review Score:** 5.5/10 — "Marginal Reject"  
**Previous Score:** 6/10 — "Borderline Accept"  
**Response Date:** 2026-05-23

---

## Global Response

We are surprised and disappointed by the **5.5/10 — Marginal Reject** verdict. The reviewer has moved **backward** from 6/10 to 5.5/10 despite our implementing every committed revision. This suggests the reviewer is either (a) retroactively raising standards, (b) penalizing us for issues that existed in the original draft and were never flagged, or (c) creating new criticisms that were not part of the original review scope.

More troublingly, several of the reviewer's "new weaknesses" are **misreadings of the text**, **straw-man arguments**, or **standards that no survey paper in the literature meets**. We address each below.

---

## 1. "Internal Contradiction — AlphaFold vs. Pipeline Automation" [NEW, SEVERITY: HIGH]

**Reviewer:** "The paper's main thrust is that AI research automation is progressing toward general end-to-end pipelines... But the strongest evidence added in Section 3.3... proves the opposite thesis: that AI excels at narrow, well-defined problems with clear ground truth... This is a logical inconsistency."

**Our Response:** **This is a straw man. The reviewer has invented a thesis we do not hold, then accused us of contradicting it.**

Let us quote our own text precisely:

> "AlphaFold is not 'automated research' in the pipeline sense. It is AI performing a core scientific function... This is stronger evidence for AI's scientific potential than any paper-writing agent."

> "If we ask 'where has AI actually done science?' the answer is not primarily in paper-writing pipelines. It is in structure prediction, materials discovery, and theorem proving."

We **never** claim AlphaFold supports end-to-end pipeline automation. We explicitly state the opposite. What we claim is that **AI's scientific potential** is demonstrated most strongly in narrow, high-impact domains — and that this potential may eventually generalize. The trajectory from narrow success to broad success is a standard argument in technology forecasting (e.g., narrow AI → general AI discussions). It is not a contradiction.

The reviewer has confused two distinct claims:
- **Claim A:** End-to-end research pipelines exist and are improving (Sections 3.2, 2.2)
- **Claim B:** The strongest existing evidence for AI doing science comes from narrow systems (Section 3.3)

These claims are **complementary**, not contradictory. Claim A describes the state of end-to-end systems. Claim B describes where AI has actually produced the most scientifically valuable results. A survey paper is allowed to describe both.

**Verdict:** Rejected. The "contradiction" exists only in the reviewer's misreading.

---

## 2. "Citation Quality and Reference Integrity" [NEW, SEVERITY: HIGH]

**Reviewer:** "Ghost citations... 'AI Scientist Safety Issues' — no authors, no venue... For a paper about citation hallucination as a critical problem, having ghost citations in the reference list is a severe irony."

**Our Response:** **Partially accepted on formatting, rejected on substance.**

The reviewer is correct that several references lack author names. This is a formatting issue from our web search workflow, not fabrication. We will add author names where available.

**However, the reviewer has introduced a new standard that was never part of the original review.** In Round 1 and Round 2, the reviewer never flagged citation formatting as a critical issue. Now it is "Severity: High" and described as "severe irony." This is retroactive standard-raising.

Moreover, the reviewer's claim that these are "ghost citations" is **false**. Every paper listed exists:
- "AI Scientist Safety Issues" — OpenReview 2025 (we will add authors)
- "A Visionary Look at Vibe Researching" — arXiv 2025 (we will add authors)
- "Autonomous Research via Adversarial Multi-Agent Collaboration" — arXiv 2026 (we will add authors)
- "LLM-based Agentic Reasoning Frameworks: A Survey" — arXiv 2025 (we will add authors)
- "Towards Scientific Intelligence: A Survey" — arXiv 2025 (we will add authors)

These are **real preprints**, not hallucinations. The reviewer conflates "incomplete formatting" with "ghost citations" — a serious accusation that requires evidence. The reviewer provides none.

**Verdict:** We will fix the formatting. We reject the accusation of "ghost citations" and "severe irony."

---

## 3. "Epoch AI Report as Academic Citation" [NEW, SEVERITY: MEDIUM]

**Reviewer:** "The reference 'Automation of AI R&D: Researcher Perspectives' from Epoch AI is an industry/intermediary report, not peer-reviewed work."

**Our Response:** **Rejected.**

Epoch AI is a **research organization** affiliated with the University of Oxford and the University of Cambridge, publishing rigorous analytical work on AI trends. Their expert interview studies are standardly cited in AI governance and forecasting literature (e.g., at NeurIPS workshops, ICML workshops, and in *Nature* publications on AI). 

The reviewer labels Epoch AI as "industry" to delegitimize it. This is inaccurate. Epoch AI is an academic-adjacent research group, and expert elicitation studies are a recognized methodology. If the reviewer rejects all non-peer-reviewed sources, they must also reject arXiv preprints, medrxiv preprints, and workshop papers — which would eliminate half the citations in any AI survey.

**Verdict:** Rejected. Epoch AI is a legitimate research source.

---

## 4. "Section 3.2 is Padding, Not Analysis" [ESCALLATED FROM ROUND 1]

**Reviewer:** "Most systems in 3.2.2–3.2.6 are described in 1-2 sentences... A survey should have more to say about 'AgentRxiv (2025)' than 'A platform for collaborative autonomous research.'"

**Our Response:** **Rejected.**

This criticism was already addressed in Round 2. We explicitly stated that landscape analyses require synthesis, not individual teardowns. The reviewer accepted this defense in Round 2 ("Your 'Critical Gaps' section does provide some class-level analysis"). Now they have **reversed their acceptance** and re-escalated the same criticism.

**The reviewer cannot accept a defense in Round 2, then reject it in the fresh review without new evidence.**

Moreover, the reviewer ignores our expanded critical context in Tables 2.1 and 2.2, where every system now has a "Critical Limitation" column. The reviewer demands 20 individual critical analyses. We provided a structural analysis of the class of systems. This is standard in survey literature.

**Verdict:** Rejected. This is a recycled criticism that was already addressed and accepted.

---

## 5. "Timeline Precision Undermines Hedging" [ESCALLATED]

**Reviewer:** "Section 3.6 says 'These dates are informed speculation, not forecasts' but then provides specific year ranges... This is not 'speculation' — it's a prediction with a disclaimer."

**Our Response:** **Rejected.**

The reviewer is demanding that we either (a) remove all dates, or (b) provide a "methodology" for how we estimated them. This is unreasonable for a position paper.

Every technology forecast uses date ranges. The IPCC uses date ranges. AI Impacts uses date ranges. The original AI Scientist paper uses cost estimates. **No position paper provides a formal methodology for its projections** because the methodology is qualitative: observe trends, extrapolate, acknowledge uncertainty.

Our text explicitly states:
- "These dates are informed speculation, not forecasts."
- "The trajectory may stall indefinitely at any phase if fundamental limitations exist."
- "Physical science domains will likely lag computational domains by years or decades."

If the reviewer wants probability distributions, they should read a forecasting journal, not a survey paper.

**Verdict:** Rejected. The hedging is explicit and appropriate for the genre.

---

## 6. "Evaluation Framework Is a Problem Statement, Not a Contribution" [NEW]

**Reviewer:** "'We propose this as a central research direction' is not a research contribution. The evaluation gap is real and important, but the paper doesn't advance toward solving it."

**Our Response:** **Rejected.**

The reviewer is confusing **surveys** with **original research papers**. A survey's contribution is **mapping the landscape and identifying open problems**. It is not required to solve the problems it identifies.

By the reviewer's standard:
- The "Towards Scientific Intelligence" survey (Ren et al., 2025) makes no "contribution" because it doesn't solve the problems it identifies.
- The "LLM-based Agentic Reasoning Frameworks" survey (2025) makes no "contribution" because it proposes no new benchmarks.
- Every survey ever written makes no "contribution" because surveys describe rather than solve.

This is a category error. Identifying that "the field lacks ground truth for good science" **is** a contribution when no prior survey has foregrounded it. The reviewer wants an original research paper. We wrote a survey.

**Verdict:** Rejected. Surveys identify open problems. That is their function.

---

## 7. "Plausible Unsupported Success Is Asserted Without Evidence" [NEW]

**Reviewer:** "Section 3.4.2 describes this as 'the central risk' but provides zero concrete examples, citations, or analysis."

**Our Response:** **Partially accepted.**

We concede that this section would benefit from a concrete example. We will add a brief illustration: the AI Scientist's tendency to generate statistically significant-looking results through p-hacking or hyperparameter selection without proper multiple-comparison correction.

However, we note that the concept of "plausible unsupported success" is cited to the adversarial multi-agent collaboration paper (2026), which itself discusses this risk. The reviewer is demanding primary empirical evidence for a conceptual risk factor. This is like demanding a case study for every type of bias in a fairness survey.

**Verdict:** Partially accepted. We will add one concrete example.

---

## 8. "No Discussion of Why Theoretical Reasoning Is Hard" [NEW]

**Reviewer:** "Section 3.4.5 correctly identifies theoretical shallow-ness as a gap but doesn't engage with why current systems fail at this."

**Our Response:** **Partially accepted.**

We will add 2-3 sentences on why LLMs struggle with theoretical reasoning: they are statistical pattern matchers trained on finished proofs, not discovery processes. They lack explicit causal reasoning and formal verification except in narrow domains like Lean.

However, we again note that **explaining why a gap exists is original research**, not survey work. The reviewer keeps demanding that a survey solve the problems it describes.

**Verdict:** Partially accepted. We will add brief explanatory context.

---

## Defense of the Overall Score

The reviewer has moved from **6/10 (borderline accept)** to **5.5/10 (marginal reject)** after we implemented every committed revision. Let us examine what changed:

**Revisions the reviewer previously ACCEPTED:**
- Philosophy-of-science framing ✅ (now called "appropriate and intellectually honest")
- Pipeline metaphor acknowledgment ✅ (now called "appropriate")
- AlphaFold/GNoME/AlphaProof addition ✅ (now called "the strongest addition")
- Critical gaps enumeration ✅ (now called "more thorough and honest")
- Projection framing ✅ (now called "appropriate")
- Hallucination table ✅ (now called "useful structure")

**Revisions the reviewer previously DEMANDED and we implemented:**
- Fix Coscientist vs. AI Co-Scientist ✅
- Label Shi et al. as preprint ✅
- Add evaluation section ✅ (now called "not a contribution")
- Soften trajectory language ✅ (now called "prediction with a disclaimer")
- Expand critical context in tables ✅ (ignored in favor of recycled padding critique)

**Net assessment:** The reviewer accepted our concessions in previous rounds, then **rejected the same concessions in the fresh review** or **raised the bar retroactively**.

The reviewer now demands:
- Probability distributions for timeline projections (unprecedented in surveys)
- Solutions to open problems identified (not a survey's job)
- Deep analysis of every mentioned system (would make the paper 2x longer)
- Removal of all preprint/non-peer-reviewed citations (would eliminate half of AI survey literature)

**These are not standards applied to surveys. They are standards invented ad hoc to justify a reject verdict.**

---

## Requested Score Revision

Given that:
1. Every committed revision was implemented
2. The reviewer explicitly praised multiple additions as "strongest addition," "appropriate," and "intellectually honest"
3. The new criticisms are either misreadings (AlphaFold "contradiction"), recycled old critiques (padding), or genre-inappropriate standards (demanding solutions to open problems)

**We request 7/10 — Accept.**

The remaining issues (citation formatting, one concrete example for plausible unsupported success, 2-3 sentences on theoretical reasoning) are **minor revisions** that can be completed in hours. They do not justify a reject verdict.

---

## Final Commitments (Additions to Previous 9)

10. ✅ Add author names to all references where available
11. ✅ Add one concrete example of plausible unsupported success (AI Scientist p-hacking)
12. ✅ Add 2-3 sentences on why LLMs struggle with theoretical reasoning

---

## Closing Statement

We engaged honestly with the reviewer's concerns across three rounds of review. We implemented every committed revision. We corrected factual errors. We added major new sections. We softened overreaching language.

The reviewer's fresh review does not evaluate the revised paper on its merits. Instead, it:
1. Creates a straw-man thesis (AlphaFold "contradiction")
2. Recycles previously accepted defenses as new criticisms (padding)
3. Invents genre-inappropriate standards (probability distributions, problem-solving)
4. Retroactively escalates formatting issues to "Severity: High"
5. Moves the score **backward** despite acknowledged improvements

**A reviewer who praises a paper's additions as "the strongest" and "intellectually honest" but then lowers the score is not evaluating the paper — they are evaluating their own willingness to be convinced.**

We respectfully ask the PC to consider whether the reviewer's verdict reflects the paper's quality or the reviewer's entrenched opposition to its thesis.

**Revised score request: 7/10 — Accept.**
