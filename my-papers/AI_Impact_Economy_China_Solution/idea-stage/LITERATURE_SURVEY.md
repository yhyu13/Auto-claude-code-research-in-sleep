# Literature Survey: AI Impact on Economy — China Solution

**Date:** 2026-05-23
**Method:** Web search on 5 target queries
**Status:** Initial landscape scan

---

## 1. Global AI Economic Impact

### Key Estimates (Range is Enormous)
| Source | Estimate | Timeframe | Key Assumptions |
|--------|----------|-----------|-----------------|
| Goldman Sachs (Briggs & Kodnani, 2023) | +7% global GDP (~$7T) | 10 years | Widespread adoption; labor displacement offset by new job creation |
| McKinsey (2023) | $2.6–4.4T annually from genAI alone | Through 2040 | Labor productivity growth 0.1–0.6pp/year |
| PwC | $15.7T by 2030 | 2030 | Includes consumption-driven effects |
| Acemoglu (MIT, 2024; Nobel laureate) | ~1% US GDP over 10 years | 10 years | Only ~5% of tasks profitably automatable in near term |
| PWBM (Penn Wharton, 2025) | 1.5% higher GDP by 2035; 3.7% by 2075 | Long run | Adoption follows historical digital diffusion curves |

**Critical tension:** Optimistic estimates (Goldman, McKinsey, PwC) assume AI automates large swathes of cognitive work. Acemoglu's conservative estimate argues most tasks are not *profitably* automatable at current cost structures. The truth likely depends on domain and timeline.

**Labor market effects:**
- IMF: ~40% of global jobs exposed to AI
- Goldman Sachs: two-thirds of US/EU jobs exposed; up to one-fourth of work substitutable
- Historical precedent (Autor et al.): 60% of current US workers are in occupations that did not exist in 1940 — suggesting long-run job creation offsets displacement

### Important Caveat
These are projections based on limited early data. PWBM explicitly warns: "Caution is required in interpreting these projections... based on limited data on AI's initial effects." Acemoglu emphasizes that task-level profitability, not just technical feasibility, determines automation.

---

## 2. China's AI Policy & Strategic Framework

### The 2017 Next Generation AI Development Plan
The foundational document. Three-phase roadmap:
- **By 2020:** AI synchronized with global advanced levels; AI industry a new growth driver
- **By 2025:** Major theoretical breakthroughs; AI drives industrial transformation
- **By 2030:** Global leader in AI; key hub for global AI innovation

Four principles: technology-led, system layout (socialist resource concentration), market-dominant (with government planning), open-source and open (military-civilian collaboration).

### The 2025 "AI+" Initiative (State Council Document No. 11)
A major escalation. Key targets:
- By 2027: AI broadly integrated across 6 key fields; smart terminal penetration >70%
- By 2030: Smart terminal penetration >90%; intelligent economy a "major growth pole"
- By 2035: Full entry into "intelligent economy and smart society"

Explicitly frames AI as creating **"new quality productive forces" (新质生产力)** — a term now central to Chinese economic discourse.

### Governance Architecture
China has moved faster than US/EU on sector-specific AI regulation:
- **Algorithm Recommendation Measures (2022):** Algorithm filing with CAC; disclosure obligations
- **Deep Synthesis Measures (2023):** Labeling of AI-generated/synthetic content
- **Generative AI Administrative Measures (2023):** Training data legality, IP protection, accuracy requirements
- **Content Labeling Measures (March 2025):** Explicit and implicit labels on AI-generated content
- **Cybersecurity Law Amendment (effective Jan 2026):** First dedicated AI compliance provision in cybersecurity law

**Enforcement is real:** Shanghai CAC penalized unfiled AI apps; Zhejiang CAC ordered removal of unregistered face-swapping apps.

---

## 3. AI and China's Labor Market

### Scale of Displacement Risk
- Zhou et al. (2020): AI may cut up to **278 million jobs by 2049** in China, hitting low-income and less-educated workers hardest
- Frey & Osborne (2017) applied to China: ~77% of Chinese jobs face high susceptibility to automation
- Giuntella et al. (2025, VoxDev): Since 2013, China is the world's largest market for industrial robots. Robot exposure caused declines in employment and wages. State-owned and politically connected firms disproportionately benefit from automation subsidies.

### Sectoral Patterns
- **Manufacturing:** Substitution effect dominates currently. Foxconn replaced 400,000+ jobs with robots; Zhejiang Province targeted 2 million worker replacements.
- **Services:** Gu et al. (2022) find AI expansion positively affects service sector employment — efficiency gains stimulate demand and create new categories.
- **Skill polarization:** Middle-skilled workers most at risk. Low-skilled workers may see reduced demand or downward mobility; high-skilled AI developers see increased demand.

### China's Demographic Amplifier
China's aging population (declining workforce growth) makes AI adoption economically urgent but socially risky. Automation is viewed as addressing rising labor costs and demographic aging, but the speed of displacement may outpace retraining capacity.

---

## 4. Semiconductor Self-Sufficiency — The Bottleneck

### The US Sanctions Regime
- Since 2020, SMIC (China's top foundry) blocked from ASML EUV lithography
- Export controls on cutting-edge GPUs (Nvidia H100, A100 banned; "nerfed" H800/H200 created for China market, later also restricted)
- Huawei specifically targeted; TSMC halted production for Huawei in 2020

### China's Response
- **SMIC:** Achieved 7nm-equivalent using DUV multi-patterning (no EUV). Fabricating Huawei's Ascend 910C AI chip. Yield improved from 20% (Sept 2024) to ~40% (Feb 2025). Targeting 60%.
- **Huawei Ascend 910C:** ~60% of Nvidia H100 inference performance. Huawei plans 100,000 Ascend 910C + 300,000 Ascend 910B in 2025. Accounts for >75% of China's total AI chip production.
- **DeepSeek R1 (Jan 2025):** Demonstrated competitive reasoning capabilities with reportedly $5–6M training cost — far below US counterparts. Signaled China can innovate within compute constraints.

### The Reality Gap
- IC Insights (2024): China produces only ~20.7% of chips it uses; Made in China 2025 target was 70% by 2025.
- Morgan Stanley: Only 34% of AI chips used in China were domestically produced as of 2024.
- SMIC is "generations behind" TSMC (3nm vs. 7nm). Multi-patterning DUV is costly and inefficient.
- Talent shortfall: ~300,000 semiconductor engineers needed (CSIA, 2019).

**Key insight:** China is making real progress under severe constraints, but the gap to global frontier remains large. DeepSeek showed algorithmic innovation can partially compensate for hardware limitations.

---

## 5. Comparative Governance: China vs. US vs. EU

| Dimension | China | US | EU |
|-----------|-------|-----|-----|
| **Primary approach** | State-led industrial policy + sector-specific regulation | Market-driven + emerging federal regulation (EOs, state laws) | Comprehensive risk-based legislation (AI Act) |
| **Speed of regulation** | Fast — specific rules for algorithms, deepfakes, genAI already enforced | Slow — no comprehensive federal AI law; sectoral (FDA, FTC) | Medium — AI Act passed 2024, phased implementation |
| **Data governance** | State sovereignty; strict cross-border controls; PIPL | Fragmented; sectoral privacy laws | GDPR baseline; strong individual rights |
| **Industrial policy** | Explicit subsidies; "Big Fund" ($billions); local government backing | CHIPS Act (~$52B); limited direct industrial planning | Chips Act; limited compared to US/China |
| **Content control** | Alignment with "core socialist values"; CAC filing/approval | First Amendment constraints; platform liability debates | Fundamental rights risk assessment |
| **Antitrust/algorithmic** | Active — algorithm filing, dynamic pricing prohibitions | Emerging DOJ/FTC interest | DMA + AI Act transparency requirements |

**China's distinctive feature:** The integration of industrial policy and regulation. The same state apparatus that subsidizes AI development also regulates its deployment, creating a "controlled acceleration" model unlike either the US's fragmented market approach or the EU's risk-prohibition framework.

---

## 6. Key Open Questions / Gaps in Evidence

1. **Implementation vs. announcement gap:** Many Chinese policies are announced with ambitious targets (70% chip self-sufficiency by 2025) but implementation lags. How much of the "China Solution" is real institutional innovation vs. aspirational planning?

2. **Labor market transition speed:** Can China's vocational training and education systems adapt fast enough to offset 278M jobs at risk? What is the evidence on retraining effectiveness?

3. **Innovation under constraints:** Is DeepSeek a one-off or a signal of sustainable algorithmic innovation that compensates for hardware bottlenecks? Can this scale?

4. **Regional variation:** China's AI development is highly uneven (Beijing, Shanghai, Shenzhen, Hangzhou vs. interior provinces). National aggregates obscure massive disparities.

5. **Global spillovers:** How does China's AI governance model export? The proposed "Global AI Cooperation Organization" (headquartered in Shanghai, 2025) suggests ambitions to shape international norms.

---

## Source Inventory (Initial)

### Global Economic Impact
- Briggs, J. & Kodnani, D. (2023). "The Potentially Large Effects of Artificial Intelligence on Economic Growth." Goldman Sachs.
- McKinsey Global Institute (2023). "The Economic Potential of Generative AI."
- Acemoglu, D. (2024). "The Simple Macroeconomics of AI." MIT.
- PWBM (2025). "The Projected Impact of Generative AI on Future Productivity Growth." Penn Wharton.
- Autor, D. et al. (2022). "New Frontiers: The Origins and Content of New Work." NBER.

### China Policy & Strategy
- State Council (2017). "Next Generation Artificial Intelligence Development Plan."
- State Council (2025). "Opinions on Deepening the Implementation of the 'Artificial Intelligence+' Initiative." Document No. 11. [CSET translation]
- WEF (2025). "China's Path to AI-Powered Industry Transformation."
- Roberts, H. et al. (2021). "Chinese AI Governance." (referenced in CLAUDE.md; needs verification)

### Labor Market
- Zhou, Y. et al. (2020). "The Impact of Artificial Intelligence on China's Labor Market."
- Giuntella, O. et al. (2025). "Will Robots Replace Workers? Lessons from China." VoxDev.
- Frey, C.B. & Osborne, M.A. (2017). "The Future of Employment."
- Gu, Y. et al. (2022). [Service sector employment effects — citation from search results]

### Semiconductors
- Digitimes (2025). "Huawei Ascend 910C reportedly hits 40% yield."
- BenchGecko. "SMIC: 4 Nodes, 1 AI Chips."
- TechNode (2020). "SMIC listing seeks billions to fund chip autonomy push."
- Law & Economics Center (2025). "US Export Controls on AI and Semiconductors."

### Governance & Regulation
- ICLG (2025). "China's Key Developments in AI Governance in 2025."
- ANSI (2025). "China Announces Action Plan for Global AI Governance."
- Infintel (2025). "China's Road to a Unified AI Regulatory System."
- Securiti.ai (2025). "Navigating China's AI Regulatory Landscape."

---

*Survey generated by ARIS executor agent. Initial scan only — many sources need independent verification and deeper reading.*
