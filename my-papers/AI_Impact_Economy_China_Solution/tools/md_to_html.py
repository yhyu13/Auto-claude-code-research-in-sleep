import re

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_FINAL.md', 'r', encoding='utf-8') as f:
    md = f.read()

lines = md.split('\n')
body = []
in_table = False
table_rows = []

for line in lines:
    if line.strip() == '---':
        continue
    
    # Title
    if line.startswith('# ') and not line.startswith('## '):
        body.append(f'<h1>{line[2:]}</h1>')
        continue
    
    if line.startswith('## '):
        body.append(f'<h2>{line[3:]}</h2>')
        continue
    
    if line.startswith('### '):
        body.append(f'<h3>{line[4:]}</h3>')
        continue
    
    # Table
    if '|' in line and line.strip().startswith('|'):
        if not in_table:
            in_table = True
            table_rows = []
        table_rows.append(line)
        continue
    else:
        if in_table:
            data_rows = [r for r in table_rows if not re.match(r'^\s*\|[\s\-:|]+\|\s*$', r)]
            if data_rows:
                body.append('<table><thead>')
                for i, row in enumerate(data_rows):
                    cells = [c.strip() for c in row.split('|') if c.strip()]
                    tag = 'th' if i == 0 else 'td'
                    body.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
                    if i == 0:
                        body.append('</thead><tbody>')
                body.append('</tbody></table>')
            in_table = False
            table_rows = []
    
    # Lists
    if line.strip().startswith('- ') or line.strip().startswith('* '):
        if not body or not body[-1].startswith('<ul>'):
            body.append('<ul>')
        body.append(f'<li>{line.strip()[2:]}</li>')
        continue
    else:
        if body and body[-1].startswith('<li>'):
            body.append('</ul>')
    
    if re.match(r'^\d+\.\s', line.strip()):
        if not body or not body[-1].startswith('<ol>'):
            body.append('<ol>')
        body.append(f'<li>{re.sub(r"^\d+\.\\s", "", line.strip())}</li>')
        continue
    else:
        if body and body[-1].startswith('<li>') and body[-2].startswith('<ol>'):
            body.append('</ol>')
    
    # Bold/italic
    text = line
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    if text.strip():
        body.append(f'<p>{text}</p>')
    else:
        body.append('')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Impact on the Global Economy and the China Solution</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,300;1,400&family=Source+Sans+Pro:wght@400;600;700&display=swap');
  body {{ font-family: 'Merriweather', Georgia, serif; font-size: 11pt; line-height: 1.65; color: #1a1a1a; background: #e8e8e8; margin: 0; padding: 0; }}
  .page {{ max-width: 210mm; min-height: 297mm; margin: 2em auto; padding: 25mm 20mm; background: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.15); }}
  @media print {{ body {{ background: #fff; }} .page {{ margin: 0; padding: 0; box-shadow: none; max-width: 100%; }} .no-print {{ display: none; }} }}
  h1 {{ font-family: 'Source Sans Pro', sans-serif; font-size: 1.9em; text-align: center; margin-top: 0; }}
  h2 {{ font-family: 'Source Sans Pro', sans-serif; font-size: 1.4em; border-bottom: 1px solid #bbb; padding-bottom: 0.2em; margin-top: 1.5em; }}
  h3 {{ font-family: 'Source Sans Pro', sans-serif; font-size: 1.15em; }}
  p {{ margin: 0.8em 0; text-align: justify; }}
  table {{ width: 100%; border-collapse: collapse; margin: 1em 0; font-size: 0.92em; }}
  thead {{ border-top: 2px solid #333; border-bottom: 1px solid #333; }}
  tbody {{ border-bottom: 2px solid #333; }}
  th, td {{ padding: 0.45em 0.6em; text-align: left; vertical-align: top; }}
  th {{ font-family: 'Source Sans Pro', sans-serif; font-weight: 600; }}
  tr:nth-child(even) {{ background: #f8f9fa; }}
  ul, ol {{ margin: 0.6em 0; padding-left: 2em; }}
  li {{ margin: 0.3em 0; }}
  .no-print {{ text-align: center; padding: 1em; }}
  .no-print button {{ font-family: 'Source Sans Pro', sans-serif; font-size: 1em; padding: 0.6em 1.4em; cursor: pointer; background: #1a5276; color: #fff; border: none; border-radius: 4px; }}
  .page-break {{ page-break-before: always; }}
</style>
</head>
<body>
<div class="no-print"><button onclick="window.print()">Print to PDF</button></div>
<div class="page">
{chr(10).join(body)}
</div>
</body>
</html>
'''

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_FINAL.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML generated")
