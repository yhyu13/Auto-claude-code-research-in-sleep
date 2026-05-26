# AI Impact on Economy: China Solution

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
Survey and analyze the impact of AI (especially large language models and agentic systems) on the global economy, with a focused examination of China's strategic response, policy frameworks, and indigenous innovation pathway.

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
2. **Distinguish related but distinct phenomena early.** Do not conflate: (a) AI as GPT affecting GDP, (b) AI's sector-specific disruption, (c) China's geostrategic/industrial policy response.
3. **Frame predictions as projections with explicit caveats.** Any timeline or forecast must be labeled "informed speculation."
4. **Add institutional/philosophy framing.** China's AI governance is not just "regulation" — it involves state-capital coordination, social credit frameworks, and data sovereignty.

### Review & Rebuttal Strategy
5. **Use Python `httpx` for all MiniMax API calls on Windows.** `curl` fails with SSL exit code 49 in Git Bash. See `tools/minimax_chat.py` template.
6. **Strip emoji/checkmark characters before API submission.** Windows console GBK encoding crashes on `✅/✓/→`. Sanitize all prompts.
7. **Catch reviewer factual errors — with evidence.** Document exact quotes and timestamps.
8. **Concede small, defend big.** If a source attribution is slightly off, fix it immediately. If the core argument is challenged, defend with evidence.
9. **Force precision on vague criticisms.** If the reviewer claims "overgeneralization," ask: which specific claim, on which page, with what counter-evidence?
10. **Commit to specific, verifiable revisions.** Score movement comes from exactly enumerated micro-fixes, not vague promises.

### Technical Workarounds (Windows / Git Bash)
11. **No `/tmp/` on Windows.** Use `tempfile.gettempdir()` or local project paths.
12. **No LaTeX compiler in environment.** Produce parallel deliverables: `.tex` for Overleaf, print-ready HTML with `@media print` CSS for browser-to-PDF, reveal.js HTML slides via CDN.
13. **No pandoc / markdown library available.** Convert Markdown → HTML and LaTeX manually.

### Quality Control
14. **Use Chinese sources where appropriate.** For a paper on "China Solution," English-only sources signal bias.
15. **Distinguish announced policy from implemented outcome.** Many China AI policies are announced with fanfare but implementation varies by province and sector.
16. **Cross-family review is essential.** Same-model self-review creates correlated errors. The Kimi → MiniMax executor-critic architecture is itself a methodological safeguard.

---

## Lessons Learned (AI Impact Economy China Solution — 7.6/10 Clear Accept)

### The Adversarial Review Arc
**Round 1:** 5.5/10 (Borderline/Weak Accept) → **Round 2:** 7.0/10 (Accept with Reservations) → **Round 3:** 7.3/10 (Accept with Minor Revisions) → **Round 4:** 7.6/10 (Clear Accept)

**What moved the score:**
- **5.5 → 7.0:** Fixing 8 sourcing gaps, removing a fabricated reference, adding 6 missing sections, adding policy recommendations, adding probability assessments to scenarios.
- **7.0 → 7.3:** Fixing 4 new issues introduced by revisions (missing section number, unsupported comparative claim, probability methodology, table formatting).
- **7.3 → 7.6:** Adding private sector strategic behavior analysis, expanding Japan/South Korea comparison with explicit analytical purpose, connecting regional variation to core claims, populating empty section.

### Key Operational Insights
17. **The first draft will have sourcing gaps you didn't notice.** MiniMax caught 8 unverifiable quantitative claims in Round 1. The lesson: every number needs a citation, and every citation needs to be real.
18. **Revisions can introduce new errors.** The Round 2 review caught a missing Section 3.5, an unsupported "most aggressive" claim, and table formatting issues that were introduced while fixing Round 1 problems. Proofread the revised paper as carefully as the original.
19. **Probability estimates need explicit methodology notes.** Even heuristic probabilities must be labeled as "structured expert assessment" to avoid accusations of spurious precision.
20. **Comparative claims must be substantiated or removed.** "One of the world's most aggressive" became "one of the most systematically orchestrated" once South Korea's K-Chips Act ($19B) was considered.
21. **Section numbering errors are fatal to credibility.** A missing section number (3.5) dropped the paper's professionalism score even though the content was substantive.
22. **Private sector dynamics are central, not peripheral.** For a paper on "the China Solution," understanding how Alibaba, Baidu, ByteDance navigate state coordination is as important as understanding state policy itself.
23. **Regional variation qualifies national claims.** The reviewer insisted that acknowledging Beijing/Shanghai concentration without analyzing its implications for the China Solution framework was insufficient. National aggregates must be caveated with internal heterogeneity.
24. **Use Python scripts (not inline bash) for file manipulation with special characters.** Chinese characters, quotes, and pipes in content break JSON parsing for WriteFile and bash heredocs. Write Python scripts to disk, then execute them.
25. **Review prompts should reference previous rounds explicitly.** Round 2 and Round 3 prompts that asked "Did you fix X, Y, Z from my previous review?" produced more focused and useful critiques than generic review prompts.

---

## Deliverables Produced
- `paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_FINAL.md` — Camera-ready survey (~400 lines)
- `paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_FINAL.tex` — LaTeX source for Overleaf/submission
- `paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_FINAL.html` — Print-ready HTML (Ctrl+P → Save as PDF)
- `slides/slides.html` — 15-slide reveal.js presentation
- `rebuttal/REBUTTAL_TO_MINIMAX_ROUND1.md` — Formal rebuttal (15 specific revisions committed)
- `rebuttal/MINIMAX_ROUND1_REVIEW.md` — 5.5/10 review
- `rebuttal/MINIMAX_ROUND2_REVIEW.md` — 7.0/10 review
- `rebuttal/MINIMAX_ROUND3_REVIEW.md` — 7.3/10 review
- `rebuttal/MINIMAX_ROUND4_REVIEW.md` — 7.6/10 Clear Accept
