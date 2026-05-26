import os
import sys
import json
import httpx

API_KEY = os.environ.get("MINIMAX_API_KEY", "")
BASE_URL = os.environ.get("MINIMAX_BASE_URL", "https://api.minimaxi.com/v1")
MODEL = os.environ.get("MINIMAX_MODEL", "MiniMax-M2.7-highspeed")

def call_minimax(prompt: str, temperature: float = 0.7) -> str:
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": max(0.01, min(temperature, 1.0)),
    }
    resp = None
    try:
        resp = httpx.post(url, headers=headers, json=payload, timeout=300)
        resp.raise_for_status()
        data = resp.json()
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        return json.dumps(data, ensure_ascii=False)
    except Exception as e:
        return f"ERROR: {e}\nResponse text: {getattr(resp, 'text', 'No response') if resp else 'No response'}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python minimax_review_round2.py <paper_file.md> [output_file.md]")
        sys.exit(1)

    paper_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    with open(paper_path, "r", encoding="utf-8") as f:
        paper_text = f.read()

    # Sanitize for Windows console compatibility
    paper_text = paper_text.replace("\u2705", "").replace("\u2713", "").replace("\u2192", "->")

    reviewer_prompt = f"""You are an expert academic reviewer in economics, technology policy, and China studies. You previously reviewed an earlier draft of this paper and gave it a score of 5.5/10 (Borderline/Weak Accept), with structured criticisms across factual accuracy, analytical rigor, balance, clarity, missing perspectives, and policy relevance.

The authors have now submitted a revised version. Your task is to evaluate whether the revisions adequately address your criticisms, and to identify any new issues introduced by the revisions.

Specifically, please assess:
1. Did the authors fix the sourcing gaps you identified? (Huawei subsidies, SMIC subsidies, SMIC yield data, Zhejiang worker replacements, production targets, DeepSeek costs, Frey & Osborne applicability, WEF reference)
2. Did they remove the fabricated/placeholder reference (Shi et al., 2026)?
3. Did they add theoretical grounding for "the China Solution"?
4. Did they add the missing sections you requested? (Taiwan, private sector actors, state capacity constraints, MCFusion, surveillance/political control, international governance, Japan/South Korea comparisons)
5. Did they add policy recommendations?
6. Did they improve scenario caveats with probability assessments and driver variables?
7. Did they maintain or improve analytical rigor?
8. Are there any NEW issues introduced by the revisions?

Assign a new score out of 10. If the score has improved, explain why. If it has not improved sufficiently, explain what remains to be done. Be as demanding as before -- the authors want your toughest critique.

Here is the revised paper:

---
{paper_text}
---

Provide your Round 2 review in structured academic format."""

    print("Sending to MiniMax critic (Round 2)...", file=sys.stderr)
    result = call_minimax(reviewer_prompt, temperature=0.3)
    
    # Strip problematic unicode for Windows console
    clean_result = result.encode('ascii', 'replace').decode('ascii')
    print(clean_result)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"\nSaved review to: {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
