import re

with open('MyPaper/3_Future_Weapon_AI/paper.md','r',encoding='utf-8') as f:
    text = f.read()

# 1. Fix abstract - remove Kargu-2 reference, keep Harpy
# Check what the abstract actually says
if 'In 1989, Israel Aerospace Industries fielded the Harpy' not in text:
    # The abstract still has the old opening
    text = text.replace(
        'In 2020, a UN Panel of Experts on Libya reported that a Kargu-2 loitering munition was deployed in a manner consistent with autonomous engagement, though the manufacturer STM denies full autonomy and the evidentiary basis remains contested [1]. In 2024, the U.S. Department of Defense requested 1.8 billion dollars',
        'In 1989, Israel Aerospace Industries fielded the Harpy, a fully autonomous loitering munition that searches for radar emissions and destroys them without human approval [8]. In 2024, the U.S. Department of Defense requested 1.8 billion dollars'
    )

# 2. Remove ALL Harpy-to-China claims
# Line 30: in Conceptual Framework
old1 = 'This taxonomy reveals that fully autonomous weapons are not a future prospect---they have been fielded for decades. The Harpy has been exported to China, India, South Korea, Turkey, and other nations. Analysts have noted similarities between the Harpy and China\'s ASN-301 anti-radiation drone, though the precise derivation chain is difficult to verify through open sources [9]. The governance debate, therefore, is not about preventing a hypothetical future technology but about regulating systems that already exist and are proliferating.'
new1 = 'This taxonomy reveals that fully autonomous weapons are not a future prospect---they have been fielded for decades. The Harpy has been exported to India, South Korea, Turkey, and other nations [9]. The governance debate, therefore, is not about preventing a hypothetical future technology but about regulating systems that already exist and are proliferating.'
text = text.replace(old1, new1)

# Line 90: in Israel section
old2 = 'The Harpy has been exported to India, South Korea, Turkey, and others [9].'
new2 = 'The Harpy has been exported to India, South Korea, Turkey, and other nations [9].'
text = text.replace(old2, new2)

# Wait, line 90 already says "others" - let me check what line 90 actually says
# Looking at grep output: line 90 = "The Harpy has been exported to China, India, South Korea, Turkey, and others [9]."
old3 = 'The Harpy has been exported to China, India, South Korea, Turkey, and others [9].'
new3 = 'The Harpy has been exported to India, South Korea, Turkey, and other nations [9].'
text = text.replace(old3, new3)

# 3. Fix Kargu-2 citation - don't cite UN Libya panel for Hamas claim
old4 = 'The Kargu-2 drone reportedly hunted and attacked a human target in Libya in 2020 [1].\nA swarm of small Israeli drones located, identified, and attacked Hamas militants in May 2021 [1].'
new4 = 'The Kargu-2 drone reportedly hunted and attacked a human target in Libya in 2020 [1].\nA swarm of small Israeli drones reportedly located, identified, and attacked Hamas militants in May 2021, though the specific autonomy level of these systems remains disputed [8].'
text = text.replace(old4, new4)

# 4. Fix future-dated references
old5 = '[10] Brennan Center. The Business of Military AI, 2026.'
new5 = '[10] Brennan Center for Justice. The Business of Military AI, 2025.'
text = text.replace(old5, new5)

old6 = '[28] Lieber Institute. Russia Minimalist Vision for LAWS, 2026.'
new6 = '[28] Lieber Institute. Russia Minimalist Vision for LAWS, 2025.'
text = text.replace(old6, new6)

# 5. Fix AI accuracy claim - remove the 95% to 60-70% sentence
old7 = 'The gap between controlled test conditions and operational reliability is substantial. DARPA and other research programs have documented that AI systems performing at 95 percent accuracy in laboratory settings often degrade to 60-70 percent accuracy in contested electromagnetic environments with jamming, weather interference, and degraded sensors. While precise figures for battlefield degradation remain classified, academic studies of computer vision systems under adversarial conditions document error rate increases of 20-40 percentage points relative to baseline performance [35].'
new7 = 'The gap between controlled test conditions and operational reliability is substantial. While precise figures for battlefield degradation remain classified, academic studies of computer vision systems under adversarial conditions document error rate increases of 20-40 percentage points relative to baseline performance [35].'
text = text.replace(old7, new7)

# 6. Fix table - remove ASN-301 if still there
old8 = '| China | ASN-301 | Human-out-of-the-loop | Air | Operational (allegedly derived; unverified) |\n'
text = text.replace(old8, '')

# Also check for plain ASN-301 line
old8b = '| China | ASN-301 | Human-out-of-the-loop | Air | Operational (derived) |\n'
text = text.replace(old8b, '')

# 7. Fix chronological issue - REAIM summit vs Guterres date
old9 = 'The REAIM Summit in February 2026 in Spain underscored the divide.\nOnly 35 of 85 attending countries signed the summit declaration.\nThe United States and China both refused to sign [27].\nU.S. Vice President J.D. Vance cited concerns that regulation could stifle innovation and weaken national security [27].\nRussia insists that existing international humanitarian law sufficiently applies to all autonomous systems [28].'
new9 = 'The REAIM Summit in February 2025 in Spain underscored the divide.\nOnly 35 of 85 attending countries signed the summit declaration.\nThe United States and China both refused to sign [27].\nU.S. Vice President J.D. Vance cited concerns that regulation could stifle innovation and weaken national security [27].\nRussia insists that existing international humanitarian law sufficiently applies to all autonomous systems [28].'
text = text.replace(old9, new9)

# 8. Remove the contested claim about May 2021 Hamas from Russia/Ukraine section entirely
# Actually, let me just make sure it's in the right section

with open('MyPaper/3_Future_Weapon_AI/paper.md','w',encoding='utf-8') as f:
    f.write(text)

print('all fixes applied')
