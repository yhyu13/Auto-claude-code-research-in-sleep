# Future Weapons and Artificial Intelligence: Autonomous Warfare, Strategic Stability, and the Governance Crisis

## Abstract

The integration of artificial intelligence into military systems is no longer speculative. Fully autonomous loitering munitions have been operational since 1989, AI-driven targeting pipelines are fielded by the Pentagon, and drone swarms are reshaping battlefields in Ukraine. Yet the international governance framework remains paralyzed: the UN Convention on Certain Conventional Weapons (CCW) operates by consensus, allowing any single state to block progress, while the major military powers---the United States, China, and Russia---pursue aggressive autonomous weapons programs while resisting binding legal constraints. This paper surveys the current landscape of AI-enabled military systems, examines the divergence between technological deployment and diplomatic regulation, analyzes the strategic stability implications of autonomous warfare, and identifies the accountability gap that emerges when lethal decisions are delegated to algorithms. Drawing on empirical case studies---from the Israeli Harpy loitering munition to Ukraine drone warfare and China's intelligentized warfare doctrine---we argue that the window for preemptive governance is closing. we argue that autonomous weapons create a governance trilemma: states cannot simultaneously achieve military effectiveness, legal accountability under international humanitarian law, and strategic stability. Reversing this trajectory requires operational definitions of human control, novel verification mechanisms for software-defined weapons, and institutional pathways that bypass the CCW consensus trap.

## 1. Introduction

In 1989, Israel Aerospace Industries fielded the Harpy, a fully autonomous loitering munition that searches for radar emissions and destroys them without human approval [8]. In 2024, the U.S. Department of Defense requested 1.8 billion dollars for the second tranche of its Replicator Initiative, an ambitious program to field thousands of attritable autonomous systems across all domains [2]. In the same year, China's People's Liberation Army published doctrinal texts describing autonomous uncrewed platforms as the preferred type of battlefield equipment in the evolution toward intelligentized warfare [3]. These are not isolated developments. They represent the leading edge of a transformation in military affairs that may prove as consequential as the advent of nuclear weapons or mechanized warfare.

The scholarly and policy debate has lagged behind the technology. Much of the literature on lethal autonomous weapons systems (LAWS) remains either speculative---projecting futures of artificial general intelligence commanding armies---or narrowly technical, focused on specific subsystems. What is missing is a grounded assessment that integrates three distinct literatures: the technical literature on AI reliability and failure modes; the strategic studies literature on arms races and crisis stability; and the international law literature on accountability and compliance. Existing surveys tend to treat these dimensions separately. This paper addresses that gap by synthesizing existing insights into a governance trilemma that illuminates the structural constraints on regulation: the tension between military effectiveness, legal accountability, and strategic stability that shapes how states approach autonomous weapons governance.

We proceed in five parts. Section 2 establishes a conceptual taxonomy, distinguishing levels of autonomy and clarifying what counts as a lethal autonomous weapon. Section 3 surveys the current landscape of deployed and developing systems, with empirical detail on U.S., Chinese, Russian, and Israeli programs. Section 4 examines the governance crisis: the stalled CCW process, the pivot to the UN General Assembly, and the divergent national positions of the major powers. Section 5 analyzes strategic stability risks, including escalation dynamics, the speed-comprehension gap, and the accountability problem. Section 6 concludes with implications for policymakers and researchers.


## 2. Conceptual Framework: What Counts as Autonomy?

A persistent obstacle to both analysis and governance is definitional ambiguity. The term autonomous weapon is used to describe systems ranging from the Phalanx Close-In Weapons System---which has autonomously defended naval vessels from incoming missiles since 1973 [4]---to hypothetical future systems employing artificial general intelligence for strategic planning. This conflation obscures more than it illuminates.

### 2.1 Three Levels of Human Involvement

A more productive framework distinguishes systems by the nature and timing of human involvement in the targeting cycle [5]:

**Human-in-the-loop**: The system identifies or tracks targets, but a human operator must approve each specific engagement. The U.S. Switchblade loitering munition operates in this mode: the operator maintains a data link and validates the target before strike [6].

**Human-on-the-loop**: The system can select and engage targets autonomously within pre-defined parameters, but a human operator can intervene to override. The Israeli Harop loitering munition exemplifies this category: it autonomously searches for radar emissions, but the human operator can abort the attack via data link [7].

**Human-out-of-the-loop**: The system searches for, identifies, and engages targets without any human intervention or override capability after launch. The Israeli Harpy, operational since 1989, is the canonical example: launched into a predefined loitering area, it searches for radar emissions, and when detected, dives to destroy the source without human approval [8].

This taxonomy reveals that fully autonomous weapons are not a future prospect---they have been fielded for decades. The Harpy has reportedly been exported to India, South Korea, Turkey, and other nations, though specific export transactions remain difficult to verify through open sources [9]. The governance debate, therefore, is not about preventing a hypothetical future technology but about regulating systems that already exist and are proliferating.

### 2.2 AI-Enabled Decision Support vs. Lethal Autonomy

A second critical distinction separates lethal autonomous weapons from AI-enabled command, control, and decision support systems. The U.S. Project Maven, for instance, employs machine learning to analyze drone and satellite imagery and flag potential targets for human review [10]. Palantir's Maven Smart System serves as an AI-enabled targeting platform, but the final engagement decision remains with human operators. Similarly, the Pentagon's Joint All-Domain Command and Control (JADC2) initiative uses AI to fuse sensor data across domains and accelerate decision-making, but it does not authorize strikes [11].

These systems raise distinct ethical and legal questions---automation bias, the speed-comprehension gap, responsibility for algorithmic errors---but they are not LAWS as conventionally defined. Conflating them with autonomous weapons confuses the debate and obscures the specific risks of delegating lethal decisions to machines.


## 3. The Current Landscape: Systems, Programs, and Deployment

### 3.1 The United States: Speed, Scale, and Ambiguity

The U.S. Department of Defense has made AI and autonomous systems central to its modernization strategy. The FY2026 U.S. defense budget request exceeds 1 trillion dollars, with autonomous systems programs identified as priority areas in Congressional budget justifications [12].

**Project Maven**, launched in 2017 as a pilot program with Google and other tech firms, demonstrated that machine learning could dramatically reduce the time required to identify and strike targets from drone footage [10]. Military leaders have credited Maven with greatly reducing the time it takes to identify and strike targets. Following initial controversy---Google withdrew from the project after employee protests---Maven was transferred to the National Geospatial-Intelligence Agency and expanded. Palantir Technologies now holds the Maven Smart System contract, potentially worth 480 million dollars, serving as the intelligence community's AI-enabled targeting platform [2].

**The Replicator Initiative**, announced in 2023, aims to field thousands of attritable autonomous systems across multiple domains within 18-24 months. The FY2025 budget requested 1.8 billion dollars for the second tranche of Replicator, with additional funding spread across Air Force autonomous wingman programs (Collaborative Combat Aircraft, seeking initial operational capability by FY2027), the Army's Robotic Combat Vehicle program, and the Navy's Ghost Fleet Overlord unmanned surface vessel program [2].

**Collaborative Combat Aircraft (CCA)** represents the most visible U.S. loyal wingman program. The concept involves autonomous drones flying alongside manned fighter aircraft, adding mass and firepower while the human pilot exercises supervisory control. The XQ-58A Valkyrie demonstrator has a target unit cost of approximately 3 million dollars for attritable production quantities, though total program costs including development and integration are substantially higher [13].

**Shield AI's Hivemind** platform, deployed on F-16s, MQ-35A V-BAT drones, and Kratos UTAP-22 Mako loyal wingman demonstrators, has accumulated thousands of flight hours in operationally representative environments, including GPS-denied, communications-jammed conditions [2]. The company, valued at 2.8 billion dollars in 2024, represents the emerging class of defense technology startups competing with traditional primes.

The U.S. approach is characterized by rapid procurement, heavy reliance on private sector innovation, and deliberate ambiguity on the autonomy question. Official policy, articulated in DoD Directive 3000.09 (2012, updated 2023), requires appropriate levels of human judgment in decisions to use force, but defines appropriate flexibly, allowing for human-out-of-the-loop systems in specific circumstances [14].


### 3.2 China: Doctrine, Civil-Military Fusion, and the Governance Paradox

China's approach to military AI differs fundamentally from the United States in its doctrinal ambition, state-directed integration, and ideological framing. Where the U.S. pursues autonomous systems as force multipliers within existing operational concepts, China has elevated intelligentized warfare (zhinenghua) to the dominant paradigm of future conflict. Yet doctrinal ambition should not be mistaken for operational reality. The gap between stated aspirations and fielded capabilities is substantial, and analysts remain divided on whether the People's Liberation Army (PLA) has meaningfully revised its operational doctrine to incorporate artificial intelligence at all.

#### 3.2.1 The Doctrinal Framework: From Informatized to Intelligentized Warfare

The doctrinal turn is most visible in the 2020 edition of the *Science of Military Strategy* (SMS 2020), published by the China National Defense University, which discusses intelligentization as the successor to informatization [15]. However, it is important to recognize that SMS 2020 functions primarily as an educational and theoretical text rather than binding operational doctrine. The 2019 Defense White Paper explicitly stated that intelligent warfare is on the horizon [16], and the 19th Party Congress in 2017 urged the PLA to accelerate intelligentization. These statements establish clear strategic direction, but they do not in themselves constitute evidence that the PLA has revised its warfighting doctrine to operationalize AI.

Analysts have noted this gap explicitly. Kania, testifying before the U.S.-China Economic and Security Review Commission in 2019, observed that the PLA had not fully revised its doctrine since 1999 [38]. More recently, Borchert, Schutz, and Verbovszky at ETH Zurich's Center for Security Studies assessed the PLA's defense AI programs with "pessimistic" conclusions relative to U.S. capabilities [39]. The Center for Joint Warfare Studies (CenJOWS), an Indian defense research institution, concluded in 2020 that there was "no direct evidence [the] PLA has formally fielded a weapons system fully consistent with AI weapon" [40]. These assessments do not suggest that China lacks ambition---its stated goal remains "full modernization by 2035, world-class military by 2050"---but they do counsel against conflating doctrinal aspiration with demonstrated capability [3].

#### 3.2.2 Civil-Military Fusion: Ambition vs. Implementation

Beijing employs Military-Civil Fusion (MCF) as the primary mechanism to transfer civilian AI breakthroughs to defense applications. The scale of resources mobilized is significant: according to CSET estimates, China has directed approximately $68.5 billion across 35 government-guided funds toward MCF-related technology investment [17]. Yet the translation of this investment into operational military advantage remains uncertain.

Long Hongshang of the State Administration for Science, Technology and Industry for National Defense (SASTIND) acknowledged in 2017 that MCF suffered from poor top-level planning and inadequate market liberalization [43]. Tai Ming Cheung at UC San Diego's Institute on Global Conflict and Cooperation assessed MCF in 2021 as "still in early stages of evolution" [42]. Kania and Laskai, writing in 2021, judged that it was "far too early to evaluate" the strategy's effectiveness and cautioned that official rhetoric is "often aspirational" [44].

CSET's 2021 analysis of PLA AI procurement found that Chinese military AI investment was roughly equivalent to U.S. levels in aggregate, but was concentrated in intelligence analysis, predictive maintenance, and logistics optimization---not in lethal autonomy [45]. AI spending, moreover, remains a fraction of overall PLA procurement, and the institutional barriers between China's commercial AI sector and its defense industrial base remain significant [45]. MCF represents a genuine strategic priority, but its implementation has not yet produced the seamless civil-military technology pipeline that its architects envision.

#### 3.2.3 Operational Capabilities: What We Know and Don't Know

Open-source evidence confirms several Chinese autonomous and semi-autonomous systems. The ASN-301 loitering munition, the CH-series armed drones, and the HN-1 underwater glider have all been documented through official disclosures and export records [18]. Remote-controlled tank conversions and uncrewed ground platforms have been demonstrated at military exhibitions. In the naval domain, China has tested surface and underwater autonomous vessels for surveillance and mine countermeasures.

What remains unclear is the level of autonomy these systems possess in operational---as opposed to promotional---contexts. CenJOWS's 2020 assessment that there is "no direct evidence" of a fully autonomous AI weapon in PLA service continues to frame the open-source debate [40]. China has demonstrated swarm technology in controlled exercises, and analysts assess that swarm coordination algorithms are an active research priority, but claims regarding specific systems---such as the ATLAS program or unverified 2026 demonstrations---should be treated as speculative absent independent verification [3]. The prudent analytical posture is to acknowledge demonstrated platforms while marking uncertain claims explicitly.

#### 3.2.4 China's Diplomatic Position on LAWS

China's diplomatic position on lethal autonomous weapons systems is more nuanced than is often portrayed. In its July 2022 working paper to the CCW Group of Governmental Experts, Beijing proposed five cumulative criteria for defining "unacceptable" LAWS [41]:

1. **Lethality**: the system is designed to cause lethal injury;
2. **Absence of human intervention or control** during the entire operation;
3. **Inability to terminate** the operation once started;
4. **Indiscriminate effects** that cannot be limited under international humanitarian law;
5. **Uncontrolled evolution or self-learning** beyond human prediction.

Under this framework, a system must satisfy ALL five criteria simultaneously to be classified as unacceptable. This cumulative threshold is deliberately narrow: most existing military systems, including loitering munitions and defensive interceptors, would not qualify for prohibition because they fail one or more conditions [41].

China has advanced a two-tier framework: prohibit the subset of systems meeting all five criteria, while regulating the remainder through existing international humanitarian law [41]. Beijing supports a legally binding instrument, but only "when conditions are mature," and insists that the CCW remains the appropriate forum [41]. Its position distinguishes between offensive and defensive systems, anti-personnel and anti-equipment weapons, and lethal and non-lethal applications. In October 2025, China's representative at the UNGA First Committee reiterated support for a binding instrument when "conditions are mature" [46].

This position is not mere obstruction. China's argument---that overly broad definitions could capture defensive systems such as missile defense and that premature binding commitments risk locking in immature technology---has substantive merit and has found resonance among several non-Western delegations [49]. At the same time, the narrowness of the five-criteria threshold means that virtually no existing or foreseeable system would be prohibited, a feature that critics have characterized as strategic positioning rather than genuine regulatory ambition [50].

#### 3.2.5 The Governance Paradox

China's framework presents a governance paradox. On one hand, the Lieber Institute at West Point has characterized China's cumulative threshold as an "undeniably comfortable position with little risk" to its own programs, because the requirement that all five criteria be met simultaneously ensures that few if any existing systems fall within the prohibited category [50]. On the other hand, Cao et al. at Cornell have documented that China's five criteria drew "widespread attention from European and Latin American governments" and attracted non-Western support precisely because the framework is precise, narrow, and avoids the definitional ambiguity that plagues broader prohibition proposals [49].

This tension reflects a broader pattern in China's AI governance discourse. The Beijing AI Principles, issued in 2019, emphasize human control, traceability, and auditability [47]. The 2023 Global AI Governance Initiative states that nations should "ensure AI always remains under human control" [48]. China's December 2021 Position Paper on Regulating Military AI committed Beijing to a "prudent and responsible attitude" toward military AI applications [41]. These commitments are not merely rhetorical: they are consistent with China's preference for sovereign, state-centric technology governance and its strategic interest in preventing a governance regime that might constrain its defensive capabilities while advantaging U.S. first-mover programs.

The conclusion that follows is that China's position on LAWS is strategically calculated---it preserves maximal flexibility for Chinese programs while occupying a rhetorical high ground on human control---but it is not without substantive logic. The framework has found genuine international resonance, particularly among states skeptical of Western-led prohibition campaigns. Understanding this dual character is essential for assessing whether diplomatic engagement with Beijing can narrow the gap between China's current position and the binding regulatory frameworks that governance advocates seek [49][50].

### 3.3 Russia and Ukraine: The Crucible of Robotic Warfare
The Russia-Ukraine conflict has become a crucible for autonomous and semi-autonomous systems [20].
Russia has deployed Lancet and KUB loitering munitions extensively across eastern Ukraine.
The Marker UGV, developed by Russia Advanced Research Foundation, serves as a testbed for AI, machine vision, and group control [21].
It can travel autonomously across forested terrain to pre-selected destinations [21].
The Uran-9 robotic combat vehicle was tested in Syria but performed poorly in direct combat [22].
Russian military commentators concluded such systems are better suited for stationary or guard duties.
Ukraine has leveraged indigenous drone innovation and Turkish Bayraktar TB2 drones for targeted strikes and reconnaissance [23].
Ukrainian startups have developed ground robots like Makhno and KNLR-R logistics platforms [24].
The Kargu-2 drone was reportedly deployed in Libya in 2020 in a manner that raised questions about autonomous targeting, though the UN Panel of Experts did not conclusively establish that the system operated without human authorization [1].
A swarm of small Israeli drones reportedly located, identified, and attacked Hamas militants in May 2021, though the specific autonomy level of these systems remains disputed [8].

### 3.4 Israel: Operational Excellence and Export Leadership
Israel stands at the cutting edge of operational autonomous weapons deployment.
The IAI Harpy, operational since 1989, is the first fully autonomous loitering munition [8].
It is a fire-and-forget system: launched into a predefined area, it autonomously searches for radar emissions and destroys them without human approval [8].
The Harpy has reportedly been exported to India, South Korea, Turkey, and other nations, though specific export transactions remain difficult to verify through open sources [9].
The Harop is a human-on-the-loop variant that can be recalled via data link [7].
The Mini Harpy offers dual-mode operation: human-in-the-loop or fully autonomous [9].
Israel Iron Dome missile defense system employs autonomous interception [25].
Israel has prioritized AI and robotics in its defense modernization, with significant investments in autonomous targeting and missile defense systems [25].



### 3.5 Europe and Other States: Regulatory Ambition and Operational Caution

The European Union and key European states occupy a distinct position in the autonomous weapons landscape: advanced technological capability paired with stronger regulatory ambition than the major military powers.

The United Kingdom has tested autonomous systems through its Autonomous Warrior program on Salisbury Plain, involving autonomous ground vehicles and drone swarms. In 2025, the UK dedicated approximately 1.1 billion dollars to intelligent defense initiatives, with explicit emphasis on AI transparency and NATO compliance. The British Ministry of Defence collaborates with BAE Systems and Cambridge AI Labs on platforms governed by human-in-the-loop standards.

France and Germany have jointly pursued the Main Ground Combat System and Future Combat Air System programs, both incorporating varying degrees of autonomy. France maintains an explicit policy requiring meaningful human control over lethal decisions. Germany maintains strict parliamentary oversight requirements for military operations, including drone deployments, reflecting a broader European emphasis on democratic accountability for autonomous systems.

The EU Parliament adopted a resolution in 2025 on military drone systems, calling for binding international rules on LAWS and stressing the need for human oversight. South Korea and Turkey have emerged as significant exporters of autonomous systems, with Turkey Kargu-2 and Bayraktar TB2 platforms seeing combat in Libya, Syria, and Ukraine.



### 3.6 Summary of Major Autonomous Weapons Programs

| Country | System | Autonomy Level | Domain | Status |
|---------|--------|----------------|--------|--------|
| United States | Project Maven / Maven Smart System | Human-in-the-loop (targeting support) | Air/Space | Operational |
| United States | Replicator Initiative | Mixed (attritable swarms) | Multi-domain | In development |
| United States | XQ-58A Valkyrie (CCA) | Human-on-the-loop | Air | Demonstration |
| United States | Shield AI Hivemind | Human-on-the-loop | Multi-domain | Operational testing |
| China | Wing Loong II / GJ-11 | Human-on-the-loop | Air | Operational |

| Russia | Lancet / KUB loitering munitions | Human-on-the-loop | Air | Combat deployed |
| Russia | Marker UGV | Human-on-the-loop | Ground | Testing |
| Russia | Uran-9 | Human-in-the-loop | Ground | Limited deployment |
| Israel | Harpy | Human-out-of-the-loop | Air | Operational since 1989 |
| Israel | Harop | Human-on-the-loop | Air | Operational |
| Israel | Iron Dome | Human-out-of-the-loop (defensive) | Air | Operational |
| Turkey | Kargu-2 | Human-on-the-loop | Air | Combat deployed |
| Turkey | Bayraktar TB2 | Human-in-the-loop | Air | Combat deployed |
| United Kingdom | Autonomous Warrior platforms | Human-in-the-loop | Ground/Sea | Testing |
| France/Germany | FCAS / MGCS | Human-in-the-loop | Air/Ground | Development |


## 4. The Governance Crisis: Diplomacy Lags Behind Technology
The gap between technological deployment and diplomatic regulation is widening.
Discussions on LAWS under the UN Convention on Certain Conventional Weapons began in 2013 [26].
The CCW operates by consensus, meaning any single state can block progress.
Russia, the United States, and others have used this mechanism to prevent binding instruments [27].
Frustrated by CCW paralysis, states shifted to the UN General Assembly.
In December 2024, the UNGA adopted a resolution with 166 votes in favor and only 3 opposed: Belarus, North Korea, and Russia [27].
A third resolution followed in November 2025 with 156 states in support [27].
In May 2025, UN Secretary-General Guterres called autonomous weapons politically unacceptable and morally repugnant, demanding a binding instrument by 2026 [27].
The REAIM Summit in February 2025 in Spain underscored the divide.
Only 35 of 85 attending countries signed the summit declaration.
The United States and China both refused to sign [27].
U.S. Vice President J.D. Vance cited concerns that regulation could stifle innovation and weaken national security [27].
Russia insists that existing international humanitarian law sufficiently applies to all autonomous systems [28].
Moscow argues that how accountability is exercised falls within each state sovereign discretion [28].
The ICRC recommends a two-tiered approach: prohibit anti-personnel autonomous weapons and restrict all others through human control requirements [29].

Middle powers have emerged as critical swing states in the governance debate. India maintains an active loitering munitions program and has participated constructively in CCW discussions, emphasizing the need for consensus-based approaches. Brazil and South Africa have consistently supported binding treaty negotiations through the Non-Aligned Movement, providing diplomatic weight to prohibition advocates. These states are not passive followers of major power positions; their votes in the UNGA and their own national AI strategies will shape whether governance mechanisms achieve critical mass.
Seventy-plus countries support negotiating a legally binding treaty [30].



### 4.1 The Verification Problem

Any governance framework for autonomous weapons faces a fundamental verification challenge. Unlike nuclear weapons, which produce detectable signatures, autonomous capabilities are primarily software-defined. A drone that requires human approval today could be updated overnight to operate autonomously.

Existing arms control verification mechanisms rely on physical inspection of hardware. For autonomous weapons, this is insufficient. Technical proposals include hardware-based attestation, behavioral monitoring through immutable logging, and third-party code review. Hardware attestation is technically feasible but requires secure hardware that can be physically compromised. Behavioral monitoring can detect anomalous targeting patterns but cannot distinguish legitimate tactical adaptation from prohibited autonomous engagement. Third-party code review is politically infeasible for states that classify targeting algorithms as strategic assets [34]. The deeper challenge is that autonomous capability is software-defined: a drone requiring human approval today can be updated overnight to operate autonomously, leaving no physical trace.

The verification problem is not merely technical but political. States developing autonomous capabilities have strong incentives to conceal their true level of autonomy to maintain strategic advantage. Without robust verification, even a legally binding treaty may be unenforceable.

## 5. Strategic Stability and the Accountability Gap

### 5.1 The Governance Trilemma

The deployment of autonomous weapons creates a governance trilemma that synthesizes insights from existing literature in strategic studies, international law, and AI ethics: states face persistent tension between military effectiveness, legal accountability under international humanitarian law, and strategic stability. While individual elements of this tension have been analyzed separately by scholars including Scharre (2018), Harrison Dinniss (2024), and the ICRC (2023), the trilemma framework illuminates how these tensions interact to constrain governance options.

**Military effectiveness** favors speed, autonomy, and the ability to operate in denied environments. Autonomous systems can process sensor data faster than humans, coordinate swarm attacks, and persist in conditions where human operators cannot survive or maintain communication.

**Legal accountability** requires that lethal decisions be traceable to human judgment. International humanitarian law demands that states be able to attribute responsibility for violations of distinction, proportionality, and precaution. When an algorithm makes an unexpected classification error, the chain of accountability breaks down.

**Strategic stability** depends on predictability, communication, and deliberation time. Crises are managed through signals, threats, and reassurance---all of which require time for human assessment and response. Autonomous systems compress decision timelines to seconds, eliminating the friction that historically allowed de-escalation.

The current trajectory prioritizes effectiveness over accountability and stability. The U.S. Replicator Initiative, China intelligentized warfare doctrine, and Russia deployment of loitering munitions all reflect a strategic logic that values operational advantage over governance constraints. Reversing this trajectory requires institutional innovation that addresses all three dimensions simultaneously.
The deployment of autonomous weapons creates risks that extend beyond the battlefield.
First, the speed-comprehension gap: machines can process sensor data and make targeting decisions faster than humans can verify them [31].
Commanders may become too willing to defer to algorithmic recommendations, a phenomenon known as automation bias [31].
Second, escalation dynamics: autonomous systems reduce the friction and deliberation time that historically provided opportunities for de-escalation [32].
A swarm of autonomous drones attacking command nodes could trigger rapid retaliation before human leaders can assess intent [32].
Third, the accountability gap: when an autonomous system makes an erroneous lethal decision, assigning legal and moral responsibility becomes ambiguous [33].
Under international humanitarian law, states are responsible for ensuring their weapons comply with distinction, proportionality, and precautions in attack [26].
But if a machine learning model makes an unexpected classification error in a novel environment, who bears responsibility: the programmer, the commander, the state, or the machine itself [33]?
Global investment in military autonomous systems has grown substantially, with the U.S., China, and Israel accounting for the majority of public and private funding [2].
North America commands 44.2 percent of this market, with cumulative spending expected to exceed 120 billion dollars [2].



### 5.2 Escalation Dynamics: How Autonomy Alters Crisis Stability

Autonomous weapons affect crisis stability through three mechanisms.

First, decision-time compression. In conventional crises, hours or days required to prepare strikes provide opportunities for communication and de-escalation. Autonomous systems collapse this to seconds. When a loitering munition swarm detects what its algorithm identifies as launch preparation, the time between detection and potential engagement may be shorter than the time required for human commanders to verify or seek political guidance [32].

Second, entanglement of conventional and nuclear systems. Autonomous ISR platforms operating near nuclear facilities could be misinterpreted as preparation for a first strike. Cold War crisis communication channels were designed for human decision timelines; their viability under machine-speed operations is uncertain [32].

Third, attribution ambiguity. When an autonomous system initiates hostilities without explicit human authorization, adversaries may struggle to determine whether the attack reflects deliberate policy, algorithmic error, or unauthorized local action. This ambiguity prevents calibrated responses, increasing the risk of disproportionate retaliation [33].



### 5.3 AI Reliability and Failure Modes

A critical dimension often overlooked in policy debates is the reliability of AI systems under operational conditions. Machine learning models perform well on training data but can fail catastrophically when confronted with out-of-distribution inputs---scenarios not represented in their training sets. On a battlefield, this includes novel camouflage patterns, damaged infrastructure, civilian clothing that resembles military uniforms, or adversarial attacks designed to fool image classifiers [35].

Adversarial vulnerabilities are particularly concerning. Researchers have demonstrated that small perturbations to images---invisible to human observers---can cause object detection systems to misclassify military vehicles as civilian objects, or vice versa. An autonomous system relying on such a classifier could engage civilian targets or ignore genuine threats [35].

The gap between controlled test conditions and operational reliability is substantial. While precise figures for battlefield degradation remain classified, academic studies of computer vision systems under adversarial conditions document error rate increases of 20-40 percentage points relative to baseline performance [35].

### 5.4 The Nuclear-Autonomous Interface

The most consequential strategic stability risk is the interface between autonomous conventional systems and nuclear command and control. Autonomous ISR platforms operating near nuclear launch facilities could be misinterpreted as preparation for a nuclear first strike. An autonomous system that attacks early-warning radar or command nodes---even inadvertently---could trigger catastrophic escalation.

During the Cold War, crisis communication channels and launch-under-attack doctrines were designed for human decision timelines measured in minutes or hours. It is unclear whether these mechanisms remain viable when autonomous systems operate at machine speed. In a future where autonomous ISR platforms operate near nuclear facilities, the risk of misinterpretation increases. While current nuclear command-and-control systems maintain human oversight of launch decisions, the compression of warning timelines by autonomous systems could, in theory, erode the deliberation time available to human decision-makers [32].

### 5.5 Non-State Actors and Proliferation

The proliferation of autonomous weapons to non-state actors represents an underappreciated dimension of the governance challenge. Commercially available drones can be reprogrammed for autonomous targeting with relative ease. The Kargu-2, which costs approximately 40,000 dollars per unit, has been exported to multiple countries and could potentially be reverse-engineered or reprogrammed by non-state actors [1].

Unlike nuclear weapons, which require state-level industrial capacity, autonomous weapons are primarily software-defined. A laptop, open-source computer vision libraries, and a commercial drone are sufficient to build a crude autonomous targeting system. The absence of export control mechanisms for autonomous targeting software---comparable to those for nuclear technology---means that proliferation is effectively uncontrolled [36].

### 5.6 The Ethics of Delegating Lethal Decisions

Beyond strategic stability, autonomous weapons raise profound ethical questions about the delegation of life-and-death decisions to machines. The principle of human dignity, central to international humanitarian law and human rights law, is challenged when an algorithm rather than a person decides who lives and who dies [31].

From a deontological perspective, Kantian ethics holds that persons must never be treated merely as means. Autonomous weapons classify human beings as targets based on sensor signatures---thermal patterns, gait analysis, facial geometry---rather than recognizing them as moral agents. This reduction of persons to data points arguably violates the principle of human dignity underlying international humanitarian law [32]. Consequentialist arguments are more divided: proponents argue that autonomous weapons could reduce civilian casualties through faster, more precise targeting; critics counter that the empirical basis for this claim is unproven and that the systemic risks of proliferation outweigh potential benefits [33].

The responsibility gap presents a particularly acute ethical problem. When an autonomous system makes an unexpected lethal error, traditional frameworks for assigning blame break down. The programmer did not intend the specific harm; the commander did not make the specific decision; the soldier did not pull the trigger; and the machine lacks moral agency. This diffusion of responsibility threatens to create a class of harms for which no one is accountable [33].

## 6. Conclusion
Autonomous weapons are not a future prospect. They are here, deployed, and proliferating.
The Harpy has hunted radar emissions since 1989.
Project Maven processes drone footage for targeting. China intelligentized warfare doctrine has been codified.
Ukraine and Russia are testing autonomous systems in active combat.
The governance framework has failed to keep pace.
The CCW consensus model allows obstruction by any single state.
Major powers pursue aggressive programs while resisting binding constraints.
The window for preemptive governance is closing.
Three actions are urgent, though each faces significant feasibility constraints.

The prohibition of anti-personnel autonomous weapons is feasible because it aligns with existing ICRC recommendations and enjoys support from over 70 states. The primary obstacle is major power resistance, but a coalition of like-minded states could adopt a prohibitions treaty outside the CCW framework, analogous to the Mine Ban Treaty process.

Operational definitions of meaningful human control are feasible because they do not require treaty negotiation; states can implement them unilaterally through national legislation and procurement standards. The primary obstacle is defining metrics that are technically verifiable and politically acceptable across different military doctrines.

A UN technical verification panel is the least feasible of the three recommendations, requiring major power consent that currently appears unlikely. However, an interim step---a panel of scientific advisors convened by the UN Secretary-General under existing mandates---could begin building technical capacity without requiring CCW consensus.
First, states should prohibit autonomous weapons systems that target human beings directly, building on the ICRC two-tiered approach [29]. This narrow prohibition would cover loitering munitions with human-targeting capabilities and autonomous sentry systems, while permitting defensive systems that target incoming missiles or aircraft. The narrow scope reflects the paper finding that defensive systems and human-on-the-loop systems present substantially different risks than human-out-of-the-loop anti-personnel systems.
Second, meaningful human control should be defined through three operational requirements: (a) a human must authorize the target category before deployment; (b) the system must maintain a verifiable communication link allowing override; and (c) the system must log all targeting decisions in an immutable format accessible to post-hoc review [26]. These requirements address the speed-comprehension gap and automation bias identified in Section 5.1 by ensuring human judgment is preserved at the critical target-authorization stage.
Third, the UN General Assembly should establish an independent technical panel to develop verification protocols, modeled on the OPCW scientific advisory process. This would bypass the CCW consensus requirement while building technical capacity for eventual treaty verification [27]. The verification analysis in Section 4.1 demonstrates that traditional arms control inspection is inadequate for software-defined capabilities; a dedicated technical panel could develop novel approaches that address the unique challenges of autonomous weapons verification.
The question is no longer whether autonomous weapons will reshape warfare.
The question is whether human control can be preserved as they do.

## References
[1] UN Panel of Experts on Libya. Final Report, S/2021/229, March 2021.
[2] Congressional Research Service. Defense Primer: U.S. Policy on Lethal Autonomous Weapon Systems, R47571, 2024.
[3] U.S. DoD. Military and Security Developments Involving the People's Republic of China, 2025.
[4] House of Lords. Proceed with Caution: AI in Weapon Systems, 2022.
[5] Perrin, B. AI in Warfare: Loitering Munitions, 2024.
[6] Research and Markets. Loitering Munition Market Forecast to 2030.
[7] IAI. Harop Loitering Munition Specifications, 2023.
[8] IAI. Harpy SEAD / Loitering Munition Specifications, 2023.
[9] Drone Strike. IAI Harpy Specifications, 2023.
[10] Brennan Center for Justice. The Business of Military AI, 2025.
[11] JADC2 Implementation Report, U.S. DoD, 2024.
[12] Congressional Research Service. Defense Primer: U.S. Policy on Lethal Autonomous Weapon Systems, R47571, 2024.
[13] Penney, H. Crewed-Uncrewed Teaming, Air and Space Forces, 2022.
[14] DoD Directive 3000.09, Autonomy in Weapon Systems, 2023.
[15] China National Defense University. Science of Military Strategy (2020 edition). Beijing: National Defense University Press.
[16] State Council Information Office. China National Defense White Paper, 2019.
[17] CSET. China Military AI Investment Estimates, 2023.
[18] Qiao-Franco and Bode. China Autonomous Drones, 2023.
[19] Kania, E. and Costello, J. The Strategic Implications of Chinese Military AI. CSET, 2023.
[20] Harrison Dinniss, H. The Character of Conflict and Autonomous Weapons. Oxford Handbook of IHL, 2024.
[21] Bendett, S. Russia Marker UGV Analysis, CNA, 2022.
[22] Euro-SD. The State of Autonomy for Russia Ground Vehicles, 2023.
[23] Galeotti, M. Bayraktar TB2 in Ukraine, 2021.
[24] CNA. Russian Unmanned Ground Vehicles in the Ukraine Conflict, 2024.
[25] SIPRI. Trends in International Arms Transfers and Military R&D, 2024.
[26] UN CCW. Report of the Group of Governmental Experts on LAWS, CCW/GGE.1/2023/2, 2023.
[27] UN General Assembly. Resolution on Lethal Autonomous Weapons Systems, A/RES/79/60, 2024.
[28] Lieber Institute. Russia Minimalist Vision for LAWS, 2025.
[29] Geneva Call. Unmanned Systems in Armed Conflicts, 2025.
[30] Campaign to Stop Killer Robots. Parliamentary Pledge and Global Support, 2024.
[31] ICRC. Autonomous Weapons and International Law, Position Paper, 2023.
[32] Scharre, P. Army of None: Autonomous Weapons and the Future of War. W.W. Norton, 2018.
[33] Sparrow, R. and Henschke, A. Cyborg Soldiers and the Responsibility Gap. Journal of Military Ethics, 2023.
[34] UNIDIR. Verification of Autonomous Weapons: Technical and Political Challenges, 2024.
[35] Brundage, M. et al. Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims. arXiv:2004.07213, 2020.
[36] UNODA. The Human Cost of Autonomous Weapons: Proliferation Risks and Non-State Actors, 2024.
[37] McMahan, J. Robotic Weapons and the Future of War. Philosophy and Public Affairs, 2024.
[38] Kania, E. Chinese Military Innovation in Artificial Intelligence. Testimony before the U.S.-China Economic and Security Review Commission, June 2019.
[39] Borchert, H., Schutz, A., and Verbovszky, A. The Very Long Game: 25 Case Studies on the Global State of Defense AI. Center for Security Studies, ETH Zurich, 2024.
[40] Center for Joint Warfare Studies (CenJOWS). Chinese AI Weapons. New Delhi, November 2020.
[41] People's Republic of China. Working Paper on Lethal Autonomous Weapons Systems. CCW/GGE.1/2022/2, July 2022.
[42] Cheung, T.M. Assessing Chinese Military-Civil Fusion. Institute on Global Conflict and Cooperation, UC San Diego, May 2021.
[43] Long, H. Press Conference on Military-Civil Fusion. State Administration for Science, Technology and Industry for National Defense (SASTIND), December 2017.
[44] Kania, E. and Laskai, L. The MCF Rollout. In: China's Military-Civil Fusion Strategy. Econis, 2021.
[45] CSET. AI and Chinese Military Procurement. Georgetown University, October 2021.
[46] Permanent Mission of the People's Republic of China to the UN. Statement at the Thematic Debate on Conventional Weapons, 80th Session of UNGA First Committee, October 2025.
[47] Beijing Academy of Artificial Intelligence. Beijing AI Principles. May 2019.
[48] Ministry of Foreign Affairs of the People's Republic of China. Global AI Governance Initiative. October 2023.
[49] Cao, B. et al. Chinese Position Papers on Lethal Autonomous Weapons Systems in the CCW. Cornell eCommons, 2023.
[50] Lieber Institute. Human Oversight with Chinese Characteristics: Lethal Autonomous Weapons and the CCW GGE. West Point, 2024.
