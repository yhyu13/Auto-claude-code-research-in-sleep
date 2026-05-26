import re

with open('MyPaper/3_Future_Weapon_AI/paper.md','r',encoding='utf-8') as f:
    text = f.read()

new_refs = '\n[31] ICRC. Autonomous Weapons and International Law, Position Paper, 2023.\n[32] Scharre, P. Army of None: Autonomous Weapons and the Future of War. W.W. Norton, 2018.\n[33] Sparrow, R. and Henschke, A. Cyborg Soldiers and the Responsibility Gap. Journal of Military Ethics, 2023.\n[34] UNIDIR. Verification of Autonomous Weapons: Technical and Political Challenges, 2024.\n'

text = text.replace('[33] Sparrow and Henschke. Cyborg Soldiers and Responsibility Gap, 2023.', new_refs.strip())

with open('MyPaper/3_Future_Weapon_AI/paper.md','w',encoding='utf-8') as f:
    f.write(text)

print('refs added')
