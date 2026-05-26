with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'r', encoding='utf-8') as f:
    c = f.read()

# Update title header
old_header = "**Date:** 2026-05-23\n**Topic:** AI Economic Impact and China's Strategic Response -- Landscape Analysis\n**Revision Note:** Revised following Round 1 external critic review (MiniMax-M2.7-highspeed, 5.5/10 Borderline/Weak Accept). All 15 specific revisions committed in rebuttal have been implemented."
new_header = "**Date:** 2026-05-23\n**Topic:** AI Economic Impact and China's Strategic Response -- Landscape Analysis\n**Revision Note:** Revised following Round 1 external critic review (MiniMax-M2.7-highspeed, 5.5/10 Borderline/Weak Accept). All 15 specific revisions committed in rebuttal have been implemented."
# Header already has revision note from earlier

# Update scenarios with probabilities and tail risks
old_scenarios = """**Scenario A: Constrained Convergence (most likely, 2025--2035)**
China maintains leadership in AI applications and deployment scale but remains 2--3 years behind the US in frontier model training due to semiconductor constraints. Domestic AI chip share rises to 50--60% by 2030, but at higher cost and lower efficiency than US alternatives. GDP impact: +0.5--1.0pp annual productivity growth.

**Scenario B: Breakthrough Autonomy (less likely, conditional on semiconductor success)**
SMIC or another domestic foundry achieves economically viable sub-5nm production, or chiplet/3D-stacking architectures bypass monolithic scaling. China's domestic AI ecosystem becomes fully self-sufficient. GDP impact: +1.0--1.5pp annual productivity growth.

**Scenario C: Stagnation (low probability but non-zero)**
US export controls tighten to block all advanced AI chip access; algorithmic efficiency gains hit diminishing returns; talent outflows accelerate. China's AI progress stalls at current levels. GDP impact: +0.2--0.5pp annual productivity growth.

**Caveats:** These scenarios assume no major geopolitical shock (Taiwan conflict, full economic decoupling) and no transformative breakthrough in AI architectures that changes compute requirements."""

new_scenarios = """**Scenario A: Constrained Convergence (Probability: ~55%, conditional on current policy continuity)**
China maintains leadership in AI applications and deployment scale but remains 2--3 years behind the US in frontier model training due to semiconductor constraints. Domestic AI chip share rises to 50--60% by 2030, but at higher cost and lower efficiency than US alternatives. GDP impact: +0.5--1.0pp annual productivity growth.
- *Key drivers:* Continued US export controls at current scope; SMIC incremental progress; algorithmic efficiency gains partially offsetting hardware gaps
- *Tail risk:* Taiwan Strait escalation triggers full supply chain disruption; even in this scenario, China's existing domestic capacity provides baseline functionality

**Scenario B: Breakthrough Autonomy (Probability: ~20%, conditional on semiconductor success)**
SMIC or another domestic foundry achieves economically viable sub-5nm production, or chiplet/3D-stacking architectures bypass monolithic scaling. China's domestic AI ecosystem becomes fully self-sufficient. GDP impact: +1.0--1.5pp annual productivity growth.
- *Key drivers:* Successful DUV multi-patterning at scale; domestic EUV-equivalent breakthrough; or architectural innovation (chiplet-based systems) that reduces reliance on monolithic advanced nodes
- *Risk factor:* This scenario assumes current engineering limitations are temporary; if EUV-equivalent production requires fundamentally unavailable expertise or equipment, probability drops to <10%

**Scenario C: Stagnation (Probability: ~15%, low but non-zero)**
US export controls tighten to block all advanced AI chip access, including DUV equipment; algorithmic efficiency gains hit diminishing returns; talent outflows accelerate. China's AI progress stalls at current levels. GDP impact: +0.2--0.5pp annual productivity growth.
- *Key drivers:* Expanded US-Japan-Netherlands controls; SMIC yield plateaus; top researchers emigrate permanently

**Scenario D: Conflict Disruption (Probability: ~10%, conditional on geopolitical shock)**
Taiwan Strait military confrontation or full economic decoupling disrupts global semiconductor supply chains. Outcome for China is ambiguous: loss of TSMC access would be catastrophic for global supply, but China's domestic capacity might benefit from forced autarky in the medium term. GDP impact: Highly uncertain; likely negative in short run, potentially positive for domestic share in medium run.
- *Key drivers:* Military action in Taiwan Strait; Western comprehensive technology embargo

**Critical caveat:** These GDP impact estimates are speculative. China's official statistics are unreliable, and no credible empirical estimate of AI's contribution to Chinese TFP growth currently exists. The scenarios assume no transformative breakthrough in AI architectures that changes compute requirements."""

c = c.replace(old_scenarios, new_scenarios)

# Add policy implications section before conclusion
policy_section = """## 10. Policy Implications and Open Questions

### For US and EU Policymakers

**What to learn from the China Solution:**
- The integration of industrial policy and regulatory foresight can accelerate sector-specific AI adaptation faster than separated institutional models
- China's rapid regulatory iteration (algorithm filing, content labeling, generative AI measures within 3 years) demonstrates that proactive governance need not wait for perfect information
- State procurement and national data coordination can accelerate deployment in public-sector applications (healthcare, education, transportation)

**What to avoid:**
- The surveillance and political control dimensions of China's model carry civil liberty costs that democratic societies should not replicate
- State-directed allocation risks corruption, inefficiency, and capture by politically connected firms (evident in Big Fund scandals)
- The announcement-implementation gap suggests that top-down planning alone is insufficient; market mechanisms and private-sector innovation remain essential

**Recommendations for export control policy:**
- Current controls have slowed but not stopped China's AI progress. DeepSeek demonstrated that algorithmic innovation can partially compensate for hardware constraints
- Further tightening risks accelerating China's indigenous innovation while permanently losing market access for Western firms (Nvidia CEO Jensen Huang has repeatedly warned of this)
- A more effective long-term strategy may be maintaining a 1-2 generation technology lead through sustained R&D investment rather than attempting total denial

### For International AI Governance

- China's proposed Global AI Cooperation Organization should be engaged critically, not dismissed. If China offers governance frameworks to developing countries, Western democracies must offer credible alternatives
- The OECD AI Principles and G7 Hiroshima Process remain the most credible multilateral frameworks, but they lack developing-country participation
- Technical standards (e.g., ISO/IEC JTC 1/SC 42) are a key battleground; China's active participation in standards bodies shapes implementation globally

### Open Questions for Researchers

1. What is the actual contribution of AI to Chinese productivity growth? Official data is insufficient; independent measurement is a critical research priority
2. Can China's vocational training system adapt fast enough to offset displacement risk? Rigorous program evaluation is urgently needed
3. Is algorithmic efficiency (DeepSeek path) a scalable substitute for hardware access, or a one-time response to specific constraints?
4. Under what conditions do elements of the China Solution export successfully to other countries?

"""

c = c.replace("## 9. Conclusion", policy_section + "## 9. Conclusion")

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'w', encoding='utf-8') as f:
    f.write(c)

print("Final revisions applied")
