import re

with open('MyPaper/3_Future_Weapon_AI/paper.md','r',encoding='utf-8') as f:
    text = f.read()

table_text = '\n\n### 3.6 Summary of Major Autonomous Weapons Programs\n\n| Country | System | Autonomy Level | Domain | Status |\n|---------|--------|----------------|--------|--------|\n| United States | Project Maven / Maven Smart System | Human-in-the-loop (targeting support) | Air/Space | Operational |\n| United States | Replicator Initiative | Mixed (attritable swarms) | Multi-domain | In development |\n| United States | XQ-58A Valkyrie (CCA) | Human-on-the-loop | Air | Demonstration |\n| United States | Shield AI Hivemind | Human-on-the-loop | Multi-domain | Operational testing |\n| China | Wing Loong II / GJ-11 | Human-on-the-loop | Air | Operational |\n| China | ASN-301 | Human-out-of-the-loop | Air | Operational (derived) |\n| Russia | Lancet / KUB loitering munitions | Human-on-the-loop | Air | Combat deployed |\n| Russia | Marker UGV | Human-on-the-loop | Ground | Testing |\n| Russia | Uran-9 | Human-in-the-loop | Ground | Limited deployment |\n| Israel | Harpy | Human-out-of-the-loop | Air | Operational since 1989 |\n| Israel | Harop | Human-on-the-loop | Air | Operational |\n| Israel | Iron Dome | Human-out-of-the-loop (defensive) | Air | Operational |\n| Turkey | Kargu-2 | Human-on-the-loop | Air | Combat deployed |\n| Turkey | Bayraktar TB2 | Human-in-the-loop | Air | Combat deployed |\n| United Kingdom | Autonomous Warrior platforms | Human-in-the-loop | Ground/Sea | Testing |\n| France/Germany | FCAS / MGCS | Human-in-the-loop | Air/Ground | Development |\n'

text = text.replace('## 4. The Governance Crisis', table_text + '\n\n## 4. The Governance Crisis')

with open('MyPaper/3_Future_Weapon_AI/paper.md','w',encoding='utf-8') as f:
    f.write(text)

print('table added')
