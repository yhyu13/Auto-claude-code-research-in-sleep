with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix 1: Add content to Section 4.3 (The Reality Gap) or merge it into 4.2/4.4
# Currently 4.3 is empty. Let's add substantive content.
old_43 = "### 4.3 The Reality Gap\n\n### 4.4 The Taiwan Variable"
new_43 = """### 4.3 The Reality Gap

Despite genuine progress, the constraints are severe:
- IC Insights (2024): China produces only ~20.7% of chips it uses, far below the Made in China 2025 target of 70%
- Morgan Stanley (2024): Only 34% of AI chips used in China were domestically produced
- SMIC's 7nm process requires costly multi-patterning; TSMC is at 3nm with superior yields and power efficiency
- Huawei's reported production targets for 2025 total approximately 400,000 units (100K Ascend 910C + 300K Ascend 910B), compared to millions of Nvidia GPUs shipped globally (Digitimes, 2025; Reuters, 2024)
- Performance-per-dollar remains the decisive metric: China's domestic chips are not merely behind in node size but significantly more expensive per unit of compute

### 4.4 The Taiwan Variable"""
c = c.replace(old_43, new_43)

# Fix 2: Add private sector strategic behavior after Section 2.3
private_behavior = """### 2.5 Private Sector Strategic Behavior

How do private firms navigate state coordination? Three patterns are observable:

**Cooptation:** Firms like Huawei and iFlytek have built their business models around state procurement (smart cities, government cloud, defense-adjacent contracts). Their strategic alignment with state priorities is explicit and economically rational.

**Strategic ambiguity:** Alibaba, Baidu, and ByteDance maintain consumer-facing businesses that generate revenue independent of state direction, while simultaneously participating in state-backed initiatives. This dual-track approach allows commercial innovation while satisfying political requirements.

**Exit and repositioning:** The 2020-2021 platform rectification campaign (Alibaba's $2.8B fine, Ant Group IPO cancellation) demonstrated that even market leaders are vulnerable to state discipline. Some founders have reduced public profiles; others have shifted focus toward "hard technology" (semiconductors, AI, robotics) that aligns with state priorities.

The critical insight is that private firms in China's AI ecosystem are not merely "state-led" or "market-driven" -- they operate in a strategic space where commercial viability and political survival are jointly determined. This distinguishes China's model from both pure state planning and free-market innovation.

"""
c = c.replace("### 2.3 The Demographic Amplifier", private_behavior + "### 2.3 The Demographic Amplifier")

# Fix 3: Expand Japan/South Korea comparison in Section 6
old_comp = """**China's distinctive feature:** The integration of industrial promotion and regulatory control. The same state that subsidizes AI development also mandates algorithm filing and content labeling. This controlled acceleration model treats regulation not as a brake on innovation but as a steering mechanism -- channeling AI development toward state-defined priorities while mitigating risks to social stability. Japan and South Korea represent alternative East Asian models that use public-private coordination rather than state-directed control; the US and EU represent market-driven and rights-based alternatives, respectively."""

new_comp = """**China's distinctive feature:** The integration of industrial promotion and regulatory control. The same state that subsidizes AI development also mandates algorithm filing and content labeling. This controlled acceleration model treats regulation not as a brake on innovation but as a steering mechanism -- channeling AI development toward state-defined priorities while mitigating risks to social stability.

**Comparison with Japan and South Korea:** These countries offer important contrasts:
- **Japan's Society 5.0** relies on public-private partnerships (SIP programs) where government sets research agendas but private firms retain operational autonomy. The state does not regulate content or demand algorithmic filing. This produces slower coordination but avoids the efficiency losses of state-directed allocation.
- **South Korea's K-Chips Act** commits ~$19 billion in semiconductor subsidies -- a larger per-GDP investment than China's Big Fund. However, Korean subsidies flow through competitive R&D grants and tax incentives rather than direct state equity stakes. The result is less bureaucratic capture but also less central coordination.

The key distinction: Japan and South Korea use public-private *coordination*; China uses state-directed *control*. The difference matters for innovation outcomes: coordination preserves private-sector experimentation, while control risks channeling resources toward politically prioritized but technically suboptimal paths.

**Comparison with the US and EU:** The US separates industrial policy (CHIPS Act) from regulation (FDA, FTC, state laws), creating institutional silos that slow adaptation. The EU's AI Act imposes risk-based obligations but provides minimal industrial promotion. Neither Western model replicates China's feedback loop between promotion and control."""

c = c.replace(old_comp, new_comp)

# Fix 4: Connect regional variation to core claims
old_regional = """**Regional variation:** China's AI development is highly uneven (Beijing, Shanghai, Shenzhen, Hangzhou vs. interior provinces). National aggregates obscure massive disparities in infrastructure, talent, and funding. The AI+ initiative explicitly acknowledges six key fields, but implementation capacity varies enormously by locality."""

new_regional = """**Regional variation:** China's AI development is highly uneven. Beijing, Shanghai, Shenzhen, and Hangzhou concentrate the vast majority of talent, venture capital, and policy attention, while interior provinces lag in infrastructure, funding, and university research capacity.

This concentration has three implications for the China Solution framework:
1. **State capacity is geographically heterogeneous:** The integrated promotion-regulation model works most effectively where local governments have fiscal resources and technical expertise. In poorer provinces, the same institutional architecture produces weaker outcomes.
2. **Labor market displacement is regionally concentrated:** Manufacturing automation hits Guangdong and Zhejiang hardest; service-sector AI creation concentrates in Beijing and Shanghai. The national aggregate figures (278M jobs at risk) mask sharp geographic disparities in who bears costs and who captures gains.
3. **The China Solution may be non-exportable in its current form:** Countries without China's scale, coastal concentration, or hierarchical state capacity may find the model difficult to replicate. This suggests the China Solution is context-dependent rather than a universal template."""

c = c.replace(old_regional, new_regional)

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'w', encoding='utf-8') as f:
    f.write(c)

print("Round 3 fixes applied")
