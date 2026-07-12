"""Nine-dimensional propagation-intent taxonomy used by IGTF."""

INTENT_NAMES = [
    "public-oriented",
    "emotion-driven",
    "individual-focused",
    "popularize",
    "clout-seeking",
    "conflict-creation",
    "smearing",
    "bias-injection",
    "connection-seeking",
]

INTENT_DESCRIPTIONS = {
    "public-oriented": "Provides valuable public information for public interest",
    "emotion-driven": "Intends to provoke emotions, trigger strong emotional responses",
    "individual-focused": "Focuses on personal stories or specific individuals",
    "popularize": "Uses colloquial language, pursues widespread dissemination",
    "clout-seeking": "Intends to attract attention, gain clicks",
    "conflict-creation": "Creates conflicts, intensifies contradictions",
    "smearing": "Negatively attacks specific targets",
    "bias-injection": "Intentionally guides readers toward specific stances",
    "connection-seeking": "Forcibly connects unrelated events",
}


def build_nine_dim_prompt(text: str, max_chars: int = 500) -> str:
    """Return the offline annotation prompt used to create 9-d intent vectors."""
    clipped = text[:max_chars]
    lines = "\n".join(
        f"{idx + 1}. {name}: {INTENT_DESCRIPTIONS[name]}"
        for idx, name in enumerate(INTENT_NAMES)
    )
    return f"""Text:
{clipped}

---

Task: Evaluate the intent strength for these 9 dimensions (use decimals between 0-1):
{lines}

---

Scoring Guidelines:
- If the text strongly exhibits an intent, give a higher score (0.7-0.9)
- If the text partially exhibits an intent, give a medium score (0.4-0.6)
- If the text barely exhibits an intent, give a lower score (0.1-0.3)
- If completely irrelevant, give 0.0

Note:
- Each text's intent combination is unique; different texts should have different score distributions
- Judge based on actual content; do not mechanically use fixed patterns
- Scores can be any decimal between 0.0 and 1.0, such as 0.15, 0.43, 0.78, 0.92

---

Output JSON format directly:
{{
  "intents": {{
    "public-oriented": <specific value 0-1 based on actual text>,
    "emotion-driven": <specific value 0-1 based on actual text>,
    "individual-focused": <specific value 0-1 based on actual text>,
    "popularize": <specific value 0-1 based on actual text>,
    "clout-seeking": <specific value 0-1 based on actual text>,
    "conflict-creation": <specific value 0-1 based on actual text>,
    "smearing": <specific value 0-1 based on actual text>,
    "bias-injection": <specific value 0-1 based on actual text>,
    "connection-seeking": <specific value 0-1 based on actual text>
  }},
  "reasoning": "Brief explanation of your analysis logic",
  "key_features": ["feature1", "feature2", "feature3"]
}}

Important:
1. All intent scores must be specific decimals between 0.0 and 1.0, not placeholders or text
2. Different texts should have different score combinations; score based on actual content
3. Output JSON directly; do not add extra explanatory text
"""
