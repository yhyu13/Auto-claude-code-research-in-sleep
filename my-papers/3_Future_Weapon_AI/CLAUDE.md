# Future Weapon AI: Autonomous Systems, Lethal Autonomy, and the AI Arms Race

<!-- ARIS:BEGIN -->
## ARIS Skill Scope
ARIS skills installed in this project: 76 entries.
Manifest: `.aris/installed-skills.txt` (lists every skill ARIS installed and its upstream target).
For ARIS workflows, prefer the project-local skills under `.claude/skills/` over global skills.
Do not modify or delete files inside any skill that is a symlink (symlinks point into `/c/Git-repo-my/Auto-claude-code-research-in-sleep-main`).
Update with: `bash /c/Git-repo-my/Auto-claude-code-research-in-sleep-main/tools/install_aris.sh`  (re-runnable; reconciles new/removed skills).
<!-- ARIS:END -->

## Project Context

This project uses the ARIS (Auto-claude-code-research-in-sleep) skill-based research harness.

**Research Goal:**
Survey and analyze the emergence of AI-enabled autonomous weapon systems (AWS / LAWS — Lethal Autonomous Weapon Systems), examining: (1) the current state of AI in military applications across domains (air, sea, land, space, cyber); (2) the strategic, ethical, and legal debates surrounding lethal autonomy; (3) the AI arms race dynamics between major powers (US, China, Russia, Israel, Turkey); and (4) the governance gap — why existing international law (Geneva Conventions, CCW) is inadequate for AI weapons and what alternatives are being proposed.

**Scope:** This is a **survey/position paper** (not an empirical study). It synthesizes existing evidence on military AI deployment, strategic stability implications, ethical frameworks, and governance proposals. The paper should be analytically rigorous, avoid both techno-optimism ("AI will revolutionize warfare") and techno-pessimism ("AI will destroy humanity"), and provide a balanced assessment of what is known, what is speculative, and what is dangerously uncertain.

**Distinguishing Features (Lessons from Previous Papers):**
- **Distinguish three phenomena:** (a) narrow AI in military support systems (logistics, intelligence, simulation), (b) autonomous platforms with human oversight (drones, unmanned vehicles), (c) fully lethal autonomous weapons (target selection and engagement without meaningful human control)
- **Explicit caveats on predictions:** All timelines are "informed speculation"
- **Use defense/military sources where appropriate:** DoD reports, RAND studies, IISS Military Balance, SIPRI data
- **Distinguish announced capabilities from verified deployment:** Military procurement is opaque; claims of "AI weapons" often refer to narrow automation
- **Ethical framing:** Reference just war theory, moral philosophy of autonomous killing, and international humanitarian law

**Agent Stack:**
- **Executor:** Kimi (Moonshot API) via Kimi Code CLI
- **Critic/Reviewer:** MiniMax API

**Workflows available:**
- `/idea-discovery` — Find novel research ideas
- `/research-pipeline` — Full pipeline from idea to paper
- `/paper-write` — Structured paper drafting
- `/auto-review-loop-minimax` — Multi-round review with MiniMax critic
- `/experiment-plan` — Design experiments
- `/paper-figure` — Generate figures

**Key directories:**
- `.claude/skills/` — ARIS skills (symlinked/copied from main repo)
- `.aris/` — ARIS manifest and tools
- `paper/` — Drafts and final paper
- `rebuttal/` — Reviewer responses
- `idea-stage/` — Early notes and literature survey
- `slides/` — Presentation materials

---

## Inherited Lessons (from How_To_Auto_Research_By_AI — 8/10 Clear Accept)

### Research Process
1. **Start with web search, not LLM hallucination.** Ground the paper in real sources before synthesis.
2. **Distinguish three related but distinct phenomena early.** The reviewer called this "the paper's strongest intellectual move."
3. **Frame predictions as projections with explicit caveats.** Label dates as "informed speculation."
4. **Add philosophy/institutional framing.** The pipeline metaphor needed a Kuhn/Hanson caveat.

### Review & Rebuttal Strategy
5. **Use Python `httpx` for all MiniMax API calls on Windows.** `curl` fails with SSL exit code 49 in Git Bash.
6. **Strip emoji/checkmark characters before API submission.** Windows console GBK encoding crashes on `✅/✓/→`.
7. **Catch reviewer factual errors — politely.** Round 2 rebuttal caught the reviewer in an ICLR timing error; forced retraction of "sophistry" accusation.
8. **Concede small, defend big.** Conceding the Coscientist attribution error bought goodwill to defend the trajectory argument.
9. **Force precision on vague criticisms.** When MiniMax claimed "internal contradiction" with AlphaFold, the rebuttal demonstrated AlphaFold was explicitly framed as domain-specific scientific AI — reviewer withdrew 5 criticisms.
10. **Commit to specific, verifiable revisions.** Score movement (5.5→6→7→8) came from exactly enumerated micro-fixes.

### Technical Workarounds (Windows / Git Bash)
11. **No `/tmp/` on Windows.** Use `tempfile.gettempdir()` or local project paths.
12. **No LaTeX compiler in environment.** Produce parallel deliverables: `.tex` for Overleaf, print-ready HTML with `@media print` CSS, reveal.js HTML slides via CDN.
13. **No pandoc / markdown library available.** Convert Markdown → HTML and LaTeX manually.

---

## Inherited Lessons (from AI_Impact_Economy_China_Solution — 7.6/10 Clear Accept)

### Key Operational Insights
14. **The first draft will have sourcing gaps you didn't notice.** MiniMax caught 8 unverifiable quantitative claims in Round 1. Every number needs a citation, and every citation needs to be real.
15. **Revisions can introduce new errors.** Round 2 caught a missing Section 3.5, an unsupported comparative claim, and table formatting issues introduced while fixing Round 1 problems.
16. **Probability estimates need explicit methodology notes.** Even heuristic probabilities must be labeled as "structured expert assessment."
17. **Comparative claims must be substantiated or removed.** "One of the world's most aggressive" became "one of the most systematically orchestrated" once evidence was checked.
18. **Section numbering errors are fatal to credibility.** A missing section number dropped the professionalism score.
19. **Private sector / non-state dynamics are central, not peripheral.** Understanding how firms/actors navigate state coordination is as important as understanding state policy.
20. **Regional variation qualifies national claims.** National aggregates must be caveated with internal heterogeneity.
21. **Use Python scripts (not inline bash) for file manipulation with special characters.** Chinese characters, quotes, and pipes break JSON parsing for WriteFile and bash heredocs.
22. **Review prompts should reference previous rounds explicitly.** Asking "Did you fix X, Y, Z from my previous review?" produces more focused critiques.

---

## Suggested Paper Structure (Initial)

1. **Abstract & Introduction** — Define scope: military AI applications, lethal autonomy, arms race dynamics, governance gap
2. **The Spectrum of Military AI** — From logistics/support AI → autonomous platforms → lethal autonomous weapons
3. **Current State: AI in Military Applications** — Air (loyal wingman, swarm drones), Sea (USV, submarine autonomy), Land (ground robots, targeting systems), Space (satellite autonomy), Cyber (AI-driven cyber weapons)
4. **The Lethal Autonomy Debate** — Meaningful human control, accountability gap, speed-of-light warfare, strategic stability
5. **The AI Arms Race: Major Powers** — US (Project Maven, JADC2, Replicator), China (intelligentized warfare, MCF), Russia (Uran-9, AI in Ukraine), Israel (Harpy, LORA), Turkey (Kargu, Bayraktar)
6. **Ethical and Legal Frameworks** — Just war theory, IHL, CCW, GGE, proposed bans vs. regulation
7. **Strategic Stability Implications** — Escalation risks, crisis instability, fog of war, accidental conflict
8. **Critical Gaps and Uncertainties** — Verification problem, definition problem, attribution problem
9. **Governance Pathways** — Prohibitions, regulation, confidence-building measures, strategic stability frameworks
10. **Conclusion** — Synthesis and open questions

---

## Key Sources to Investigate (Initial Web Search Targets)
- "lethal autonomous weapons systems LAWS CCW 2024 2025"
- "Project Maven JADC2 US military AI autonomous systems"
- "China intelligentized warfare military AI strategy"
- "Russia AI weapons Ukraine autonomous tanks drones"
- "Israel Harpy loitering munition autonomous weapon"
- "Turkey Kargu Bayraktar autonomous drone swarm"
- "AI arms race strategic stability nuclear escalation"
- "meaningful human control autonomous weapons ethics"
