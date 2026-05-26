with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'r', encoding='utf-8') as f:
    c = f.read()

# Add surveillance section after 3.4 Regulatory Architecture
surveillance = """\n### 3.5 Political Control and the Dual Purpose of AI Governance

A balanced assessment of the China Solution must acknowledge that controlled acceleration serves political control objectives alongside economic development. China's AI governance framework is not merely about product safety or market integrity; it is explicitly designed to maintain social stability and state control over information flows.

Key manifestations:
- AI-enabled surveillance systems have been deployed for biometric tracking and predictive policing in sensitive regions
- Social credit systems use AI-driven scoring to incentivize compliance with state preferences
- The Cyberspace Administration of China actively uses algorithmic transparency requirements as tools for content control, not merely consumer protection
- Export of surveillance technology (e.g., smart city systems, facial recognition) to other countries creates international reputational costs

We do not analyze these dimensions extensively because this paper focuses on economic and technology policy, but they are essential context. The China Solution's integration of promotion and regulation is inseparable from the Chinese party-state's broader governance objectives. Any country considering elements of this model must weigh efficiency gains against civil liberty costs.

"""

c = c.replace("### 3.5 Industrial Policy: The Big Fund and Its Limitations", surveillance + "### 3.5 Industrial Policy: The Big Fund and Its Limitations")

# Add international governance after Section 7.4 (now we need to find where Section 7 ends)
intgov = """\n### 7.5 International Governance and Diffusion of the China Model

China is not merely developing domestic AI policy; it is actively promoting its governance approach internationally. In July 2025, China announced a proposed Global AI Cooperation Organization, potentially headquartered in Shanghai, designed to foster international collaboration on AI development and regulation.

**Context:** This proposal enters a crowded field:
- The UN AI Advisory Body (established 2023) is developing recommendations for global AI governance
- The G7 Hiroshima AI Process has produced international guiding principles
- The OECD AI Principles (2019) remain the most widely adopted normative framework
- The EU AI Act (2024) is establishing extraterritorial regulatory influence

**China's distinctive pitch:** Unlike the EU's risk-prohibition approach or the US's voluntary guidelines, China offers a model of state-coordinated development with rapid regulatory adaptation. For developing countries with strong states and weaker civil society constraints (e.g., parts of Africa, Central Asia, Southeast Asia), elements of the China Solution may appear attractive.

**Risks of diffusion:** If the China Solution spreads, it could normalize:
- Algorithmic filing as a mechanism for state content control
- Data localization requirements that fragment the global internet
- Industrial policy approaches that distort international trade

"""

c = c.replace("## 8. Trajectory: Structured Projection", intgov + "## 8. Trajectory: Structured Projection")

# Fix comparative table to add Japan and Korea
old_table = """| China | United States | European Union |
|-----------|---------------|----------------|
| Primary approach | State-led industrial policy + sector-specific regulation | Market-driven + emerging federal/state regulation | Comprehensive risk-based legislation (AI Act) |"""

new_table = """| Dimension | China | United States | European Union | Japan | South Korea |
|-----------|-------|---------------|----------------|-------|-------------|
| Primary approach | State-led industrial policy + sector-specific regulation | Market-driven + emerging federal/state regulation | Comprehensive risk-based legislation (AI Act) | Society 5.0 + human-centered AI | K-Chips Act + AI Strategy |
| Speed of regulation | Fast -- specific rules enforced since 2022 | Slow -- no comprehensive federal AI law | Medium -- AI Act passed 2024, phased implementation | Medium -- sectoral guidelines | Fast -- sector-specific adaptation |"""

c = c.replace(old_table, new_table)

# Fix the rest of the table rows
old_row1 = "| Speed of regulation | Fast -- specific rules enforced since 2022 | Slow -- no comprehensive federal AI law | Medium -- AI Act passed 2024, phased implementation |"
new_row1 = "| Speed of regulation | Fast -- specific rules enforced since 2022 | Slow -- no comprehensive federal AI law | Medium -- AI Act passed 2024, phased implementation | Medium -- sectoral guidelines | Fast -- sector-specific adaptation |"
c = c.replace(old_row1, new_row1)

old_row2 = "| Data governance | State sovereignty; strict cross-border controls; PIPL | Fragmented; sectoral privacy laws | GDPR baseline; strong individual rights |"
new_row2 = "| Data governance | State sovereignty; strict cross-border controls; PIPL | Fragmented; sectoral privacy laws | GDPR baseline; strong individual rights | Personal Information Protection Act; sectoral | K-PIPA; data localization for critical sectors |"
c = c.replace(old_row2, new_row2)

old_row3 = "| Industrial policy | Explicit subsidies; Big Fund; local government competition | CHIPS Act (~$52B); limited direct planning | European Chips Act; smaller scale |"
new_row3 = "| Industrial policy | Explicit subsidies; Big Fund; local government competition | CHIPS Act (~$52B); limited direct planning | European Chips Act; smaller scale | SIP (Society 5.0) public-private partnerships | K-Chips Act; massive semiconductor subsidies |"
c = c.replace(old_row3, new_row3)

old_row4 = "| Content/values control | Alignment with core socialist values; CAC filing | First Amendment constraints; platform liability debates | Fundamental rights risk assessment |"
new_row4 = "| Content/values control | Alignment with core socialist values; CAC filing | First Amendment constraints; platform liability debates | Fundamental rights risk assessment | Social harmony principles; moderate constraints | Strong content regulation; real-name requirements |"
c = c.replace(old_row4, new_row4)

old_row5 = "| Antitrust/algorithmic | Active -- algorithm filing, dynamic pricing bans | Emerging DOJ/FTC interest | DMA + AI Act transparency requirements |"
new_row5 = "| Antitrust/algorithmic | Active -- algorithm filing, dynamic pricing bans | Emerging DOJ/FTC interest | DMA + AI Act transparency requirements | Moderate FTC-style enforcement | Active Fair Trade Commission oversight |"
c = c.replace(old_row5, new_row5)

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_REVISED.md', 'w', encoding='utf-8') as f:
    f.write(c)

print("Remaining sections added")
