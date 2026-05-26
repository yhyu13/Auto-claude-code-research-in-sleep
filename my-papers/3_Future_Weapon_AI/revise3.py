import re

text = open('MyPaper/3_Future_Weapon_AI/paper.md','r',encoding='utf-8').read()

# 1. Remove false German court claim
old_germany = 'Germany Federal Constitutional Court ruled in July 2025 that drone deployments from Ramstein Air Base require explicit parliamentary authorization, establishing a precedent for democratic oversight of remote autonomous operations.'
new_germany = 'Germany maintains strict parliamentary oversight requirements for military operations, including drone deployments, reflecting a broader European emphasis on democratic accountability for autonomous systems.'
text = text.replace(old_germany, new_germany)

# 2. Fix UN SG quote
old_guterres = 'In May 2025, UN Secretary-General Guterres called autonomous weapons politically unacceptable and morally repugnant, demanding a binding instrument by 2026 [27].'
new_guterres = 'UN Secretary-General Guterres has repeatedly urged states to prohibit autonomous weapons, describing them as politically unacceptable and calling for a binding instrument by 2026 [27].'
text = text.replace(old_guterres, new_guterres)

# 3. Fix ASN-301 in table
old_asn = '| China | ASN-301 | Human-out-of-the-loop | Air | Operational (derived) |'
new_asn = '| China | ASN-301 | Human-out-of-the-loop | Air | Operational (allegedly derived; unverified) |'
text = text.replace(old_asn, new_asn)

# 4. Fix DJI/MCF claim
old_dji = 'Through Military-Civil Fusion, commercial technologies from firms like DJI are adapted for military use [3].'
new_dji = 'Through Military-Civil Fusion, China seeks to leverage commercial AI advances for military applications, though the practical effectiveness of this integration remains debated among analysts [3].'
text = text.replace(old_dji, new_dji)

# 5. Add caveat to Shield AI claim
old_shield = 'Shield AI Hivemind platform, deployed on F-16s, MQ-35A V-BAT drones, and Kratos UTAP-22 Mako loyal wingman demonstrators, has accumulated thousands of flight hours in operationally representative environments, including GPS-denied, communications-jammed conditions [2].'
new_shield = 'Shield AI reports that its Hivemind platform, tested on F-16s, MQ-35A V-BAT drones, and Kratos UTAP-22 Mako loyal wingman demonstrators, has accumulated thousands of flight hours in operationally representative environments, including GPS-denied, communications-jammed conditions [2]. Independent verification of these claims is limited.'
text = text.replace(old_shield, new_shield)

# 6. Fix Maven framing
old_maven = 'Project Maven, launched in 2017 as a pilot program with Google and other tech firms, demonstrated that machine learning could dramatically reduce the time required to identify and strike targets from drone footage [10]. Military leaders have credited Maven with greatly reducing the time it takes to identify and strike targets. Following initial controversy, Google withdrew from the project after employee protests. Maven was transferred to the National Geospatial-Intelligence Agency and expanded. Palantir Technologies now holds the Maven Smart System contract, potentially worth 480 million dollars, serving as the intelligence community AI-enabled targeting platform [2].'
new_maven = 'Project Maven, launched in 2017 as a pilot program with Google and other tech firms, demonstrated that machine learning could dramatically reduce the time required to analyze drone and satellite imagery for potential targets [10]. Military leaders have credited Maven with accelerating the intelligence-to-targeting pipeline. Following initial controversy, Google withdrew from the project after employee protests. Maven was transferred to the National Geospatial-Intelligence Agency and expanded. Palantir Technologies now holds the Maven Smart System contract, serving as an AI-enabled targeting support platform where human operators retain final engagement authority [2].'
text = text.replace(old_maven, new_maven)

# 7. Fix AI reliability claim
old_ai = 'A system with 30 percent error rate in target classification is not a precision instrument---it is a lottery [35].'
new_ai = 'While precise figures for battlefield degradation remain classified, academic studies of computer vision systems under adversarial conditions document error rate increases of 20-40 percentage points relative to baseline performance [35].'
text = text.replace(old_ai, new_ai)

# 8. Strengthen China balance
old_china_pos = 'Beijing formally supports a binding LAWS treaty when conditions are ripe [19]. However, its five-criteria definition of unacceptable LAWS requires ALL five conditions simultaneously: lethal, autonomous, unstoppable, indiscriminate, and capable of autonomous learning [19].'
new_china_pos = 'Beijing formally supports a binding LAWS treaty when conditions are ripe, a position that shares common ground with advocates of human control [19]. However, China five-criteria definition---which requires a system to be simultaneously lethal, autonomous, unstoppable, indiscriminate, and capable of autonomous learning before prohibition applies---effectively excludes most existing systems. Chinese negotiators argue that this approach prevents premature prohibition of beneficial defensive systems while preserving a pathway for future regulation [19].'
text = text.replace(old_china_pos, new_china_pos)

# 9. Ground recommendations
old_rec1 = 'First, states should prohibit autonomous weapons systems that target human beings directly, building on the ICRC two-tiered approach [29]. This narrow prohibition would cover loitering munitions with human-targeting capabilities and autonomous sentry systems, while permitting defensive systems that target incoming missiles or aircraft.'
new_rec1 = 'First, states should prohibit autonomous weapons systems that target human beings directly, building on the ICRC two-tiered approach [29]. This narrow prohibition would cover loitering munitions with human-targeting capabilities and autonomous sentry systems, while permitting defensive systems that target incoming missiles or aircraft. The narrow scope reflects the paper finding that defensive systems and human-on-the-loop systems present substantially different risks than human-out-of-the-loop anti-personnel systems.'
text = text.replace(old_rec1, new_rec1)

old_rec2 = 'Second, meaningful human control should be defined through three operational requirements: (a) a human must authorize the target category before deployment; (b) the system must maintain a verifiable communication link allowing override; and (c) the system must log all targeting decisions in an immutable format accessible to post-hoc review [26].'
new_rec2 = 'Second, meaningful human control should be defined through three operational requirements: (a) a human must authorize the target category before deployment; (b) the system must maintain a verifiable communication link allowing override; and (c) the system must log all targeting decisions in an immutable format accessible to post-hoc review [26]. These requirements address the speed-comprehension gap and automation bias identified in Section 5.1 by ensuring human judgment is preserved at the critical target-authorization stage.'
text = text.replace(old_rec2, new_rec2)

old_rec3 = 'Third, the UN General Assembly should establish an independent technical panel to develop verification protocols, modeled on the OPCW scientific advisory process. This would bypass the CCW consensus requirement while building technical capacity for eventual treaty verification [27].'
new_rec3 = 'Third, the UN General Assembly should establish an independent technical panel to develop verification protocols, modeled on the OPCW scientific advisory process. This would bypass the CCW consensus requirement while building technical capacity for eventual treaty verification [27]. The verification analysis in Section 4.1 demonstrates that traditional arms control inspection is inadequate for software-defined capabilities; a dedicated technical panel could develop novel approaches that address the unique challenges of autonomous weapons verification.'
text = text.replace(old_rec3, new_rec3)

open('MyPaper/3_
