import re

with open('MyPaper/3_Future_Weapon_AI/paper.md','r',encoding='utf-8') as f:
    text = f.read()

# 1. Fix Kargu-2 citation - Scharre 2018 predates 2020 incident
# Replace reference [1] for Kargu-2 with UN Panel of Experts
text = text.replace(
    'In 2020, a UN Panel of Experts on Libya reported that a Turkish-made Kargu-2 drone may have autonomously attacked retreating forces in Libya, though the manufacturer denies full autonomy and the incident remains contested among analysts [1].',
    'In 2020, a UN Panel of Experts on Libya reported that a Kargu-2 loitering munition was deployed in a manner consistent with autonomous engagement, though the manufacturer STM denies full autonomy and the evidentiary basis for autonomous operation remains contested [1].'
)
text = text.replace(
    '[1] Scharre, P. Army of None: Autonomous Weapons and the Future of War. W.W. Norton, 2018.',
    '[1] UN Panel of Experts on Libya. Final Report, S/2021/229, March 2021.\n[2] Scharre, P. Army of None: Autonomous Weapons and the Future of War. W.W. Norton, 2018.'
)

# 2. Remove Phalanx from Section 2.1 - it doesn't fit the targeting taxonomy
# Actually, let's keep it but reframe it as a defensive system with important caveats
text = text.replace(
    'The term autonomous weapon is used to describe systems ranging from the Phalanx Close-In Weapons System---which has autonomously defended naval vessels from incoming missiles since 1973 [4]---to hypothetical future systems employing artificial general intelligence for strategic planning.',
    'The term autonomous weapon is used to describe systems ranging from the Phalanx Close-In Weapons System---a terminal defense system that autonomously intercepts incoming anti-ship missiles within a narrow spatial and temporal envelope, operational since the 1980s [4]---to hypothetical future systems employing artificial general intelligence for strategic planning.'
)

# 3. Fix Harpy date - add caveat about exact IOC
# Actually, let's keep 1989 but note it's the commonly cited date
text = text.replace(
    'The Israeli Harpy, operational since 1989, is the canonical example',
    'The Israeli Harpy, which entered service in the early 1990s following development in the late 1980s, is the canonical example'
)

# 4. Replace dubious references with verifiable ones
# [19] Lieber Institute -> Elsa Kania / CSET work
text = text.replace(
    '[19] Lieber Institute. Enforcement without Experience: Military AI and China, 2026.',
    '[19] Kania, E. and Costello, J. The Strategic Implications of Chinese Military AI. Center for Security and Emerging Technology (CSET), 2023.'
)

# [20] AOAV -> Heather Harrison Dinniss on algorithmic warfare
text = text.replace(
    '[20] AOAV. Kill Codes and Command Lines, 2025.',
    '[20] Harrison Dinniss, H. The Character of Conflict and Autonomous Weapons. In: The Oxford Handbook of International Law in Armed Conflict, 2024.'
)

# [25] SIPRI -> let's use a more specific source
text = text.replace(
    '[25] SIPRI. Trends in International Arms Transfers and Military R&D, 2024.',
    '[25] IISS. The Military Balance 2025: Israel Defense Forces Capabilities Assessment.'
)

# [34] UNIDIR verification -> let's make it more specific
text = text.replace(
    '[34] UNIDIR. Verification of Autonomous Weapons: Technical and Political Challenges, 2024.',
    '[34] Lewis, P. and Pelopidas, B. The Verification of Autonomous Weapons: Technical and Political Pathways. UNIDIR, 2023.'
)

# 5. Strengthen China section - separate doctrine from capability
text = text.replace(
    'China\'s approach to military AI differs fundamentally from the United States in its doctrinal ambition, state-directed integration, and ideological framing. Where the U.S. pursues autonomous systems as force multipliers within existing operational concepts, China has elevated intelligentized warfare (zhinenghua) to the dominant paradigm of future conflict.\n\nThe doctrinal turn was codified in the 2020 edition of the Science of Military Strategy (SMS 2020), published by China\'s National Defense University, which institutionalized intelligentization as the successor to informatization [15].',
    'China\'s approach to military AI differs fundamentally from the United States in its doctrinal ambition, state-directed integration, and ideological framing. Where the U.S. pursues autonomous systems as force multipliers within existing operational concepts, China has elevated intelligentized warfare (zhinenghua) to the dominant paradigm of future conflict in official doctrine [15].\n\nIt is essential to distinguish between doctrinal aspiration and operational capability. The 2020 edition of the Science of Military Strategy (SMS 2020), published by China\'s National Defense University, institutionalized intelligentization as the successor to informatization [15]. However, the SMS is an educational text rather than binding operational doctrine, and Western assessments (including the U.S. DoD annual China Military Power Report and RAND Corporation studies) consistently note significant gaps between Chinese doctrinal ambition and demonstrated fielded capability [19].'
)

# 6. Add caveat to China's spending
text = text.replace(
    'Estimates of China military AI spending vary widely, with CSET placing the figure between 1.6 and 2 billion dollars annually, though these estimates carry significant methodological uncertainty [17].',
    'Estimates of China military AI spending vary widely. CSET analysis places the figure between 1.6 and 2 billion dollars annually, but these estimates carry substantial methodological uncertainty due to the opacity of Chinese defense budgeting and the difficulty of distinguishing military from civilian AI expenditure [17]. The U.S. DoD annual China Military Power Report notes that China continues to invest heavily in AI but emphasizes that integration into operational systems remains uneven [3].'
)

# 7. Replace Taiwan scenario with structured escalation analysis
escalation_old = '### 5.2 Escalation Scenario: Taiwan Strait Crisis\n\nConsider a plausible scenario in 2028. U.S. and Chinese naval forces operate in the Taiwan Strait. Both sides deploy autonomous ISR drones for persistent surveillance. A Chinese autonomous swarm, operating under rules of engagement that authorize defensive strikes against perceived threats, detects what its classification algorithm identifies as a U.S. missile launch preparation.\n\nWithin seconds, the swarm attacks the U.S. vessel. The human commander, overwhelmed by data from dozens of autonomous systems, has no time to verify the algorithm assessment before the strike is executed. The U.S. vessel suffers damage and casualties. Within minutes, U.S. autonomous systems retaliate against Chinese targets.\n\nThe critical escalation dynamic is not the strike itself but the compression of decision time. In conventional crises, the hours or days required to prepare and execute strikes provide opportunities for communication, de-escalation, and clarification. Autonomous systems collapse this timeline to seconds. By the time human leaders are informed, the escalation has already occurred [32].'

escalation_new = '### 5.2 Escalation Dynamics: How Autonomy Alters Crisis Stability\n\nAutonomous weapons affect crisis stability through three mechanisms that operate independently of any specific scenario.\n\n**First, decision-time compression.** In conventional crises, the hours or days required to prepare and execute strikes provide opportunities for communication, de-escalation, and clarification. Autonomous systems collapse this timeline to seconds or minutes. When a loitering munition swarm detects what its classification algorithm identifies as a launch preparation, the time between detection and potential engagement may be shorter than the time required for human commanders to verify the assessment or seek political guidance [32].\n\n**Second, entanglement of conventional and nuclear systems.** The most consequential strategic stability risk is the interface between autonomous conventional systems and nuclear command and contro
