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
        print("Usage: python minimax_review_round3.py <paper_file.md> [output_file.md]")
        sys.exit(1)

    paper_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    with open(paper_path, "r", encoding="utf-8") as f:
        paper_text = f.read()

    # Sanitize for Windows console compatibility
    paper_text = paper_text.replace("\u2705", "").replace("\u2713", "").replace("\u2192", "->")

    reviewer_prompt = f"""You are an expert academic reviewer in economics, technology policy, and China studies. You previously reviewed this paper twice:
- Round 1: 5.5/10 (Borderline/Weak Accept)
- Round 2: 7.0/10 (Accept with Reservations)

In Round 2, you identified four new issues that needed fixing:
1. Missing Section 3.5 (ghost section number)
2. Unsupported comparative claim: "one of the world's most aggressive" national AI strategies
3. Probability estimates without methodology
4. Table formatting inconsistencies

You also identified remaining weaknesses:
- Private sector actors underdeveloped
- Japan/South Korea comparison superficial
- "Institutional innovation" claim unsupported
- Enforcement claim potentially overstated
- Regional variation noted but not analyzed

The authors have now submitted a third revision. Please evaluate whether the four specific new issues have been resolved, and whether the remaining weaknesses have been adequately addressed or acknowledged. 

Assign a final score out of 10. If you believe the paper now merits 7.5+ (Clear Accept), say so explicitly. If you believe it still requires further revision, specify exactly what remains.

Here is the revised paper:

---
{paper_text}
---

Provide your Round 3 review in structured academic format."""

    print("Sending to MiniMax critic (Round 3)...", file=sys.stderr)
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
