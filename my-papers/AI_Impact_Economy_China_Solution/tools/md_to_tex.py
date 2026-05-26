import re

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_FINAL.md', 'r', encoding='utf-8') as f:
    md = f.read()

# Simple Markdown-to-LaTeX converter for this specific paper
lines = md.split('\n')
out = []
in_table = False
table_lines = []

# LaTeX preamble
preamble = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage[margin=2.5cm]{geometry}
\usepackage{setspace}
\onehalfspacing
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{enumitem}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue!70!black,citecolor=blue!70!black,urlcolor=blue!70!black}
\usepackage{titlesec}
\titleformat{\section}{\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\large\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}{\normalsize\bfseries}{\thesubsubsection}{1em}{}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small AI Impact on the Global Economy and the China Solution}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\begin{document}
"""

out.append(preamble)

for line in lines:
    # Skip horizontal rules
    if line.strip() == '---':
        continue
    
    # Title
    if line.startswith('# ') and not line.startswith('## '):
        title = line[2:].strip()
        out.append(f"\\begin{{center}}\\LARGE\\bfseries {title}\\end{{center}}\\vspace{{1em}}")
        continue
    
    # Section headers
    if line.startswith('## '):
        heading = line[3:].strip()
        out.append(f"\\section{{{heading}}}")
        continue
    
    if line.startswith('### '):
        heading = line[4:].strip()
        # Escape special chars
        heading = heading.replace('&', '\\&').replace('%', '\\%').replace('$', '\\$')
        out.append(f"\\subsection{{{heading}}}")
        continue
    
    # Bold and italic
    text = line
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'\\textbf{\\textit{\1}}', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
    
    # Tables
    if '|' in text and text.strip().startswith('|'):
        if not in_table:
            in_table = True
            table_lines = []
        table_lines.append(text)
        continue
    else:
        if in_table:
            # Process table
            if len(table_lines) >= 2:
                # Filter out separator lines
                data_rows = [r for r in table_lines if not re.match(r'^\s*\|[\s\-:|]+\|\s*$', r)]
                if data_rows:
                    out.append("\\begin{table}[h]")
                    out.append("\\centering\\small")
                    # Count columns
                    first = data_rows[0]
                    cols = len([c for c in first.split('|') if c.strip()]) 
                    out.append(f"\\begin{{tabular}}{{@{{{'l' * cols}@}}}}")
                    out.append("\\toprule")
                    for i, row in enumerate(data_rows):
                        cells = [c.strip() for c in row.split('|') if c.strip()]
                        cells = [c.replace('&', '\\&').replace('%', '\\%').replace('$', '\\$') for c in cells]
                        out.append(" & ".join(cells) + " \\\\")
                        if i == 0:
                            out.append("\\midrule")
                    out.append("\\bottomrule")
                    out.append("\\end{tabular}")
                    out.append("\\end{table}")
            in_table = False
            table_lines = []
    
    # Lists
    if text.strip().startswith('- ') or text.strip().startswith('* '):
        item = text.strip()[2:]
        item = item.replace('&', '\\&').replace('%', '\\%')
        out.append(f"\\item {item}")
        continue
    
    if text.strip().startswith('1. ') or text.strip().startswith('2. ') or text.strip().startswith('3. '):
        item = text.strip()[3:]
        item = item.replace('&', '\\&').replace('%', '\\%')
        out.append(f"\\item {item}")
        continue
    
    # Empty lines
    if not text.strip():
        out.append("")
        continue
    
    # Regular text
    text = text.replace('&', '\\&').replace('%', '\\%').replace('$', '\\$')
    out.append(text)

# Join and fix list environments
result = "\n".join(out)
result = re.sub(r'\n\\item ', r'\n\\begin{itemize}\n\\item ', result)
result = re.sub(r'(\\item .*\n)(?=(?!\\item))', r'\1\\end{itemize}\n', result)

# Fix consecutive list starts
result = re.sub(r'\\end\{itemize\}\n\\begin\{itemize\}', '', result)

out.append("\\end{document}")

with open('paper/AI_IMPACT_ECONOMY_CHINA_SOLUTION_FINAL.tex', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print("LaTeX generated")
