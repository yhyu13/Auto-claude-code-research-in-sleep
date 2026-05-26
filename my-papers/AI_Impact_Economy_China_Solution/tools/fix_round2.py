import re

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix 1: Remove/qualify "most aggressive" claim in abstract
old_abstract = "China has pursued one of the world's most aggressive and systematically orchestrated national AI strategies"
new_abstract = "China has pursued one of the most systematically orchestrated national AI strategies, with scale and state coordination that rival any other country's approach"
c = c.replace(old_abstract, new_abstract)

# Fix 2: Fix section numbering in Section 3
# 3.4 should be 3.5, 3.6 should be 3.6 (keep), 3.7 should be 3.7 (keep)
# But we need to insert a 3.5 between 3.4 and 3.6
# Actually the current order is: 3.1, 3.2, 3.3, 3.4, 3.6, 3.7
# We should renumber: 3.1, 3.2, 3.3, 3.4, 3.5 (state capacity), 3.6 (MCFusion)
c = c.replace("### 3.6 State Capacity Constraints", "### 3.5 State Capacity Constraints")
c = c.replace("### 3.7 Military-Civil Fusion", "### 3.6 Military-Civil Fusion")

# Fix 3: Fix Section 4 ordering - 4.4 should be after 4.3, not before
# Current: 4.1, 4.2, 4.4, 4.3
# Need: 4.1, 4.2, 4.3, 4.4
# Find and swap
pattern = r'(### 4\.2 China.*?)(### 4\.4 The Taiwan Variable.*?)(### 4\.3 The Reality Gap.*?)'
match = re.search(pattern, c, re.DOTALL)
if match:
    old_order = match.group(0)
    new_order = match.group(1) + match.group(3) + match.group(2)
    c = c.replace(old_order, new_order)

# Fix 4: Fix Section ordering - 10 should be after 9, not before
# Current: 8, 10, 9
# Need: 8, 9, 10
pattern2 = r'(## 8\. Trajectory: Structured Projection.*?)(## 10\. Policy Implications and Open Questions.*?)(## 9\. Conclusion.*?)'
match2 = re.search(pattern2, c, re.DOTALL)
if match2:
    old_order2 = match2.group(0)
    new_order2 = match2.group(1) + match2.group(3) + match2.group(2)
    c = c.replace(old_order2, new_order2)

# Fix 5: Add methodology note for probabilities
old_caveat = "**Critical caveat:** These GDP impact estimates are speculative. China's official statistics are unreliable, and no credible empirical estimate of AI's contribution to Chinese TFP growth currently exists. The scenarios assume no transformative breakthrough in AI architectures that changes compute requirements."
new_caveat = """**Methodological note on probabilities:** These probability estimates represent the authors' structured expert assessment based on current trajectory analysis, not formal model estimation. They are intended to communicate relative likelihoods rather than precise forecasts, and readers should treat them as heuristic rather than statistical.

**Critical caveat:** These GDP impact estimates are speculative. China's official statistics are unreliable, and no credible empirical estimate of AI's contribution to Chinese TFP growth currently exists. The scenarios assume no transformative breakthrough in AI architectures that changes compute requirements."""
c = c.replace(old_caveat, new_caveat)

# Fix 6: Fix table formatting in Section 6 - remove duplicate EU rows
# The table got corrupted during edits. Let's replace the whole table with a clean version.
old_table_start = "## 6. Comparative Analysis: Three Models"
old_table_end = "## 7. Critical Gaps and Uncertainties"

table_text = """## 6. Comparative Analysis: Five Models

| Dimension | China | United States | European Union | Japan | South Korea |
|-----------|-------|---------------|----------------|-------|-------------|
| **Primary approach** | State-led industrial policy + sector-specific regulation | Market-driven + emerging federal/state regulation | Comprehensive risk-based legislation (AI Act) | Society 5.0 + human-centered AI public-private partnerships | K-Chips Act + national AI strategy with heavy semiconductor subsidies |
| **Speed of regulation** | Fast -- specific rules enforced since 2022 | Slow -- no comprehensive federal AI law | Medium -- AI Act passed 2024, phased implementation | Medium -- sectoral guidelines, ethics frameworks | Fast -- sector-specific adaptation, active FTC-style enforcement |
| **Data governance** | State sovereignty; strict cross-border controls; PIPL | Fragmented; sectoral privacy laws | GDPR baseline; strong individual rights | Personal Information Protection Act; sectoral codes | K-PIPA; data localization for critical sectors |
| **Industrial policy** | Explicit subsidies; Big Fund; local government competition | CHIPS Act (~$52B); limited direct planning | European Chips Act; smaller scale | SIP (Society 5.0) public-private partnerships | K-Chips Act; massive semiconductor subsidies (~$19B) |
| **Content/values control** | Alignment with core socialist values; CAC filing | First Amendment constraints; platform liability debates | Fundamental rights risk assessment | Social harmony principles; moderate constraints | Strong content regulation; real-name requirements |
| **Antitrust/algorithmic** | Active -- algorithm filing, dynamic pricing bans | Emerging DOJ/FTC interest | DMA + AI Act transparency requirements | Moderate FTC-style enforcement | Active Fair Trade Commission oversight |

**China's distinctive feature:** The integration of industrial promotion and regulatory control. The same state that subsidizes AI development also mandates algorithm filing and content labeling. This controlled acceleration model treats regulation not as a brake on innovation but as a steering mechanism -- channeling AI development toward state-defined priorities while mitigating risks to social stability. Japan and South Korea represent alternative East Asian models that use public-private coordination rather than state-directed control; the US and EU represent market-driven and rights-based alternatives, respectively.

"""

# Find and replace the section
start_idx = c.find("## 6. Comparative Analysis")
end_idx = c.find("## 7. Critical Gaps and Uncertainties")
if start_idx != -1 and end_idx != -1:
    c = c[:start_idx] + table_text + c[end_idx:]

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'w', encoding='utf-8') as f:
    f.write(c)

print("Round 2 fixes applied")
