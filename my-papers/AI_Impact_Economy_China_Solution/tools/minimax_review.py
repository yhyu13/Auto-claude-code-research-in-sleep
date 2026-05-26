import os
import sys
import json
import tempfile

# Use httpx (available in miniconda)
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
        return f"ERROR: {e}\nResponse text: {getattr(resp, 'text', 'N/A') if resp else 'No response'}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python minimax_review.py <paper_file.md> [output_file.md]")
        sys.exit(1)

    paper_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    with open(paper_path, "r", encoding="utf-8") as f:
        paper_text = f.read()

    # Sanitize for Windows console compatibility
    paper_text = paper_text.replace("\u2705", "").replace("\u2713", "").replace("\u2192", "->")

    reviewer_prompt = f"""You are an expert academic reviewer in economics, technology policy, and China studies. Review the following survey paper draft as if for a top-tier policy journal or interdisciplinary venue (e.g., Nature, Foreign Affairs, or a major think-tank publication).

Your task:
1. Assign an overall score out of 10 with a clear verdict: Reject / Weak Reject / Borderline / Accept / Strong Accept
2. Provide structured criticism across these dimensions:
   - Factual accuracy and source credibility
   - Analytical rigor (are claims supported by evidence?)
   - Balance and fairness (especially regarding China claims -- are we avoiding both Sinophobia and naive acceptance of official narratives?)
   - Clarity of argument structure
   - Missing perspectives or major gaps
   - Policy relevance
3. Highlight any specific factual claims that seem questionable or require stronger sourcing
4. Suggest concrete revisions that would improve the score

Be adversarial and demanding. The authors want your toughest critique so they can improve the paper. Do not hold back. If a claim about China lacks evidence, say so explicitly. If the comparison with US/EU models is superficial, call it out. If the trajectory scenarios are under-caveated, demand more precision.

Here is the paper draft:

---
{paper_text}
---

Provide your review in structured academic format."""

    print("Sending to MiniMax critic...", file=sys.stderr)
    result = call_minimax(reviewer_prompt, temperature=0.3)
    print(result)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"\nSaved review to: {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
