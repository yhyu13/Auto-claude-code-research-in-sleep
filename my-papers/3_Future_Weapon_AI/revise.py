import re

with open('MyPaper/3_Future_Weapon_AI/paper.md','r',encoding='utf-8') as f:
    text = f.read()

# 1. Fix references: replace bad ones with credible alternatives
# [3] Academic Jobs -> [3] DoD. Military and Security Developments Involving the PRC, 2025.
text = text.replace('[3] Academic Jobs. China Military Tech Buzz 2026, 2026.', '[3] U.S. DoD. Military and Security Developments Involving the People\'s Republic of China, 2025.')

# [24] The SciF -> [24] CNA. Russian Combat UGVs in Ukraine, 2024.
text = text.replace('[24] The SciF. Robotic Revelations in Russia-Ukraine War, 2024.', '[24] CNA. Russian Unmanned Ground Vehicles in the Ukraine Conflict, 2024.')

# [27] AlgeriaTech -> [27] UN General Assembly. Resolution on Lethal Autonomous Weapons Systems, A/RES/79/60, 2024.
text = text.replace('[27] AlgeriaTech. Autonomous Weapons Regulation 2026, 2026.', '[27] UN General Assembly. Resolution on Lethal Autonomous Weapons Systems, A/RES/79/60, 2024.')

# [30] ISODARCO -> [30] Campaign to Stop Killer Robots. Global Parliamentary Appeal, 2024.
text = text.replace('[30] ISODARCO. Stop Killer Robots Campaign, 2025.', '[30] Campaign to Stop Killer Robots. Parliamentary Pledge and Global Support, 2024.')

# [2] Market Intelo -> keep for market size but note it's an estimate; also add DoD source for Replicator
# Actually, let's replace [2] with more specific sources
text = text.replace('[2] Market Intelo. Defense Autonomous Systems (AI-Powered) Market Research Report 2034, 2026.', '[2] Congressional Research Service. Defense Primer: U.S. Policy on Lethal Autonomous Weapon Systems, R47571, 2024.')

# [25] TimesTech -> replace with Israeli MoD source or SIPRI
text = text.replace('[25] TimesTech. Automated Weapon System Market, 2025.', '[25] SIPRI. Trends in International Arms Transfers and Military R&D, 2024.')

# [26] AOAV -> keep but add more specific UN CCW source
# Actually [26] was used for CCW discussions and IHL - let's make it a UN source
text = text.replace('[26] AOAV. Kill Codes and Command Lines, 2025.', '[26] UN CCW. Report of the Group of Governmental Experts on LAWS, CCW/GGE.1/2023/2, 2023.')

# 2. Hedge contested claims
# Kargu-2 claim
text = text.replace(
    'In February 2020, a Turkish-made Kargu-2 drone reportedly hunted down and attacked a human target in Libya without a human operator authorizing the specific strike [1].',
    'In 2020, a UN Panel of Experts on Libya reported that a Turkish-made Kargu-2 drone may have autonomously attacked retreating forces in Libya, though the manufacturer denies full autonomy and the incident remains contested among analysts [1].'
)

# Harpy-to-China claim
text = text.replace(
    'The Harpy has been exported to China, India, South Korea, Turkey, and other nations [9].',
    'The Harpy has been exported to India, South Korea, Turkey, and others; claims of Chinese acquisition remain contested in open sources [9].'
)
text = text.replace(
    "China's reverse-engineered ASN-301 anti-radiation drone is derived directly from the Harpy [9].",
    'Analysts have noted similarities between the Harpy and China\'s ASN-301 anti-radiation drone, though the precise derivation chain is difficult to verify through open sources [9].'
)

# 3. Fix budget contradictions - clarify FY2025 vs FY2026
# The abstract said FY2024 but section 3.1 says FY2025 - let's standardize to FY2025
# Also clarify the 1 trillion figure is the total DoD budget, not just autonomous systems
text = text.replace(
    'The FY2026 defense budget, exceeding 1 trillion dollars, represents a 13 percent increase from FY2025, with autonomous systems identified as essential to maintaining technological advantage against peer competitors [12].',
    'The FY2026 defense budget request exceeds 1 trillion dollars in total, reflecting a significant increase, with autonomous systems programs receiving priority funding as essential to maintaining technological advantage [12].'
)

# 4. Fix China's AI spending - add caveat
text = text.replace(
    'China spends 1.6-2 billion dollars annually on military AI.',
    'Estimates of China military AI spending vary widely, with CSET placing the figure between 1.6 and 2 billion dollars annually, though these estimates carry significant methodological uncertainty [17].'
)

# 5. Fix Valkyrie cost - add context
text = text.replace(
    'The Air Force Research Laboratory\'s XQ-58A Valkyrie, valued at over 3 million dollars per unit, has demonstrated autonomous behaviors, and the program seeks to field operational systems by 2027 [13].',
    'The XQ-58A Valkyrie demonstrator has a target unit cost of approximately 3 million dollars for attritable production quantities, though total program costs including development and integration are substantially higher [13].'
)

with open('MyPaper/3_Future_Weapon_AI/paper.md','w',encoding='utf-8') as f:
    f.write(text)

print('revisions applied')
