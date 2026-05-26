# Rebuttal to MiniMax — Round 2: The Battle Continues

**Paper:** "How to Auto Research by AI"  
**Reviewer:** MiniMax-M2.7-highspeed  
**Previous Score:** 5/10 → 5.5/10 ("Borderline Weak Reject")  
**Rebuttal Round:** 2

---

## Global Response to the Reviewer's Response

We thank the reviewer for engaging substantively with our first rebuttal. However, we are concerned that the reviewer's Round 2 response **introduces new argumentative standards that are asymmetric and unreasonable**, while mischaracterizing several of our defenses as "rhetorical maneuvers" or "sophistry" without engaging with their actual content.

The reviewer has shifted from evaluating our paper to evaluating our rebuttal style — a meta-level distraction that does not advance the substantive discussion. We address each Round 2 point below, then argue for a revised fair score.

---

## Point-by-Point Round 2 Response

### R1-Round2: "'When, Not If' — The Core Problem Remains"

**Reviewer (Round 2):** "You do not argue for it [being engineering vs. fundamental]. You simply declare it so."

**Our Response:** The reviewer now demands that a **survey paper** provide a **proof** that current limitations of LLMs are engineering rather than fundamental. This is an impossible standard. No paper in the literature — including the reviewer's own hypothetical ideal survey — has proven or disproven whether hallucination, shallow reasoning, or same-model bias are fundamental limitations of statistical learning.

What our paper **does** provide is:
- A structured enumeration of current limitations (6 gaps)
- Evidence that each gap has active research addressing it (citation verification pipelines, cross-model review systems, multi-agent debate)
- The historical pattern that previous "fundamental" AI limitations (context length, reasoning, code generation) have yielded to engineering progress

The reviewer wants us to settle an **open question in AI philosophy and cognitive science** within a survey. This is not intellectual rigor — it is scope creep disguised as rigor. We will add a paragraph acknowledging the *possibility* that these are fundamental, but we will not — and cannot — *prove* they are not.

**Reviewer (Round 2):** "A position paper arguing inevitability must engage with the strongest counterarguments."

**Our Response:** We **do** engage with counterarguments. Our entire "Critical Gaps" section (Part 3) is devoted to limitations. We discuss hallucination, plausible unsupported success, same-model bias, domain restriction, theoretical shallow-ness, and safety gaps. These *are* the counterarguments. The reviewer seems to believe that unless we conclude "full AI research may be impossible," we have not "engaged" with counterarguments. This is nonsense. Engaging with counterarguments means presenting them honestly — which we do — not adopting them as the paper's conclusion.

---

### R2-Round2: "Philosophy of Science — Not Disciplinary Overreach"

**Reviewer (Round 2):** "Your dismissal of philosophy of science as 'disciplinary overreach' is itself overreach."

**Our Response:** The reviewer has now **doubled down** on demanding philosophy of science in a CS survey. Let us be precise about what the reviewer demands:

- Hanson's "patterns of discovery"
- Kuhn's paradigm shifts and incommensurability
- The problem of induction
- "What makes research 'research'?"

These are **genuine and important questions**. They are also questions that **entire philosophy of science departments spend careers on**. A survey paper at NeurIPS/ICML is not the venue to settle them. 

The reviewer claims: "A 500-line survey can include a paragraph acknowledging this simplification." **We agreed to do exactly this in Round 1.** The reviewer is now treating our concession as insufficient and demanding more. This is moving the goalposts.

**We draw a line:** One paragraph acknowledging the pipeline simplification and the role of serendipity/intuition — which we committed to — is appropriate. A literature review of philosophy of science is not.

---

### R3-Round2: "Shi et al. Preprint — Accepted With Concern"

**Reviewer (Round 2):** "Preprints are not peer-reviewed... This should be flagged more prominently."

**Our Response:** The reviewer has **shifted ground**. In Round 1, the reviewer accused us of fabrication ("serious integrity violation"). We proved the paper is real. Now the reviewer says "but preprints aren't peer-reviewed."

This is true. It is also **standard practice** in fast-moving AI/ML literature to cite arXiv and medrxiv preprints. GPT-4, Claude, and virtually every LLM paper in the last three years were initially cited as preprints. If the reviewer wants to disqualify all preprint citations from surveys, they are proposing a standard that does not exist in the field.

**We will flag it as a preprint** — which we already agreed to. We reject the implication that preprint data is inadmissible.

---

### R4-Round2: "System Descriptions — You Agree With Me"

**Reviewer (Round 2):** "Why did this not appear in the original paper?"

**Our Response:** Because **every paper is written under scope and length constraints.** The reviewer seems to believe that any improvement suggested by a reviewer retroactively proves the original paper was flawed. By this standard, **every paper ever written is flawed**, because every paper could be improved by reviewer suggestions.

The relevant question is not "could this be better?" (yes, always) but "is the current version below the acceptance threshold for its genre?" A landscape analysis that maps 15+ systems across 3 levels of autonomy, identifies 6 structural gaps, and proposes a trajectory argument is **not below threshold** for a survey. The reviewer's demand for individual critical analysis of every system would push this past 1,000 lines.

---

### R5-Round2: "Evaluation Section — Accepted"

**Our Response:** We appreciate this acceptance. We will develop the "no ground truth" observation as a central contribution.

---

### R6-Round2: "Pipeline Metaphor — Accepted"

**Our Response:** We appreciate this acceptance.

---

### R7-Round2: "ICLR Withdrawal — 'This Defense Is Misleading' / 'Sophistry'"

**Reviewer (Round 2):** "You are arguing that a paper that was withdrawn demonstrates that AI-generated work can pass peer review. This is sophistry."

**Our Response:** The reviewer has **fundamentally misread the ICLR 2025 experiment**, and their accusation of sophistry is **itself sophistry**.

Let us state the facts precisely, as reported by Sakana AI (Yamada et al., 2025) and independent observers:

1. Three fully AI-generated papers were submitted to an ICLR 2025 workshop.
2. Reviewers were informed **after acceptance decisions** that some submissions could be AI-generated. They were offered the option to opt out.
3. **One paper scored above the human acceptance threshold** based on standard peer review criteria.
4. The paper was **withdrawn by the authors** (Sakana AI) prior to publication, for ethical transparency.

The reviewer claims: "The reviewers, having been told the paper was AI-generated (or having suspected it), scored it highly."

This is **factually incorrect**. The reviewers were informed **after** scoring, not before. The experiment was designed to test **blind review quality**. The high scores were given **without knowledge** that the paper was AI-generated.

The reviewer then says: "This tells us nothing about whether peer review, as currently practiced, would accept AI-generated work without disclosure."

This is **exactly what the experiment tested**. The reviewers practiced standard peer review. They did not know the paper was AI-generated. They scored it highly. The authors withdrew it **after** the fact. The withdrawal was an **ethical choice by the authors**, not a **rejection by the reviewers**.

**What the ICLR experiment demonstrates:** AI-generated work can pass blind peer review quality thresholds at a top-tier ML workshop.

**What it does NOT demonstrate:** That AI-generated work should be published without disclosure. (We never claimed this.)

The reviewer has conflated **publication** with **quality-bar passage**. We explicitly state in our paper that the paper was withdrawn. The reviewer accuses us of implying it was "published." We do not. We claim it passed the quality bar. It did.

**This is not sophistry. This is reading comprehension.**

---

### R8-Round2: "Venue Mismatch Defense — 'Most Rhetorically Skilled and Weakest Argument'"

**Reviewer (Round 2):** "NeurIPS and ICML accept surveys and position papers. Surveys at these venues still require intellectual rigor... Your genre must still meet the venue's standards."

**Our Response:** The reviewer has **straw-manned our defense**. We never claimed surveys are "exempt from intellectual standards." We claimed they are **judged by different standards than empirical contributions** — specifically, they are judged on:
- Coverage and taxonomy quality
- Synthesis and structural insight
- Honest acknowledgment of limitations
- Proportionality of conclusions to evidence

The reviewer has implicitly adopted an **empirical-paper rubric** (novel experiments, theorem proofs, benchmark results) and applied it to a survey. This is the definition of category error.

The reviewer says: "A paper that omits AlphaFold as evidence for AI-driven science has a significant evidentiary gap." **We conceded this.** It will be fixed. A single evidentiary gap in a survey of 15+ systems does not reduce a paper to 5/10 unless the reviewer is applying empirical standards.

**We propose a fairer standard:** Compare our paper to actual accepted surveys at NeurIPS/ICML (e.g., "Towards Scientific Intelligence," Ren et al., 2025; "LLM-based Agentic Reasoning Frameworks: A Survey," 2025). These papers:
- Map landscapes without proving theorems
- Include trajectory arguments without formal forecasts
- Omit some systems (no survey is exhaustive)
- Are accepted because they provide **structure and synthesis**

Our paper provides comparable structure and synthesis, plus a more detailed critical gaps analysis than most. **If our paper is 5.5/10, then most accepted surveys are 6–7/10. The gap is not large.**

---

### R9-Round2: "New Weaknesses Exposed by the Rebuttal"

**Reviewer (Round 2):** "Rhetorical deflection over substance... advocacy orientation..."

**Our Response:** The reviewer has shifted from evaluating the paper to **psychoanalyzing the authors**. Accusing us of "advocacy orientation" and "rhetorical deflection" is **ad hominem** dressed as meta-critique.

Every survey has a thesis. "Towards Scientific Intelligence" (Ren et al., 2025) argues that LLM agents are transforming science. "The AI Scientist" (Lu et al., 2024) argues that end-to-end automation is possible. **Having a thesis is not advocacy; it is the purpose of a position survey.** Our thesis is clearly stated: AI research automation is progressing along a trajectory from tools to full autonomy. We present evidence for and against this thesis. The reviewer disagrees with the thesis and therefore labels the paper "advocacy."

This is not peer review. This is **disagreement with conclusions masquerading as methodological critique.**

---

## New Issues Raised by the Reviewer's Round 2

### NW1: Asymmetric Standards

The reviewer demands:
- **From us:** Proof that limitations are engineering (impossible standard)
- **From themselves:** No burden to prove they are fundamental

The reviewer demands:
- **From us:** Engagement with philosophy of science (outside CS scope)
- **From themselves:** No engagement with CS engineering practice

This is asymmetric. A fair reviewer would say: "The paper should acknowledge uncertainty about whether limitations are fundamental." We have agreed to do this. Instead, the reviewer says: "You must argue they are engineering." This is not review — it is **imposition of the reviewer's own philosophical position**.

### NW2: The "Sophistry" Accusation

Accusing authors of sophistry is a **nuclear option** in peer review. It should be reserved for deliberate deception. Our ICLR description is factually accurate (reviewers scored blind; authors withdrew). The reviewer's accusation is itself based on a **factual error** about when reviewers were informed. We expect a correction.

---

## Requested Score Revision

The reviewer has:
- ✅ Accepted our pipeline metaphor defense
- ✅ Accepted our evaluation section defense  
- ✅ Accepted our AlphaFold/theorem-proving concession
- ✅ Accepted our Coscientist correction
- ✅ Accepted our Shi et al. clarification (with residual concern about preprints, which we reject)
- ❌ Rejected our ICLR defense based on a factual error
- ❌ Rejected our venue/genre defense based on straw-manning
- ❌ Added new ad hominem critiques ("advocacy," "sophistry")

**Net result:** 4 substantive concessions accepted, 2 rejections based on errors or asymmetry, 1 new unfair critique.

A reviewer who accepts 4 of 8 major points and concedes that the revisions are "meaningful" should not hold the score at 5.5/10. **We request 6.5/10 — Borderline Accept.**

The remaining disagreement is philosophical (inevitability vs. uncertainty) and methodological (survey scope). These are legitimate disagreements among reasonable researchers. They should not block acceptance.

---

## Final Commitments (Unchanged from Round 1)

1. ✅ Add AlphaFold / GNoME / AlphaProof coverage
2. ✅ Fix Coscientist vs. AI Co-Scientist attribution
3. ✅ Label Shi et al. as medrxiv preprint with proper ID
4. ✅ Soften trajectory timeline language (projections, not predictions)
5. ✅ Add "How to Measure" evaluation subsection (developed as central contribution)
6. ✅ Add brief philosophy-of-science framing paragraph (one paragraph only)
7. ✅ Expand per-system critical context in tables
8. ✅ Clarify ICLR blind-review quality-bar distinction (we will make this even more explicit)
9. ✅ Add explicit acknowledgment that current limitations *may* be fundamental

---

## Closing Statement

We have engaged honestly with the reviewer's concerns, conceded where they were right, and defended where they were wrong. The reviewer's Round 2 response reveals an underlying discomfort with our thesis — that AI research automation is advancing toward full autonomy — that cannot be resolved by revision.

**A reviewer who fundamentally disagrees with a paper's conclusion should score it on the quality of its argumentation, not on whether they share its worldview.** Our argumentation is structured, evidence-based, and acknowledges limitations. We respectfully ask the PC to evaluate the paper on its merits as a survey, not on the reviewer's philosophical opposition to its conclusion.

**Revised score request: 6.5/10 — Borderline Accept.**
