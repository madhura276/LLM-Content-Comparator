import json
import os
from llm_clients import (
    groq_llama,
    openrouter_mistral,
    generate_content,
    summarize_content
)
from themes import THEMES
from comparator import theme_present

# -------------------------------------------------
# USER QUERY (DO NOT CHANGE AS PER YOUR REQUIREMENT)
# -------------------------------------------------
PROMPT = "rent in koramangala"

# -------------------------------------------------
# LLM MODELS USED FOR COMPARISON
# -------------------------------------------------
models = {
    "Groq_LLaMA": groq_llama,
    "OpenRouter_Mistral": openrouter_mistral
}

# -------------------------------------------------
# STEP 1: GET RESPONSES FROM EACH LLM
# -------------------------------------------------
responses = {}

for name, fn in models.items():
    try:
        responses[name] = fn(PROMPT)
    except Exception as e:
        print(f"⚠️ {name} failed:", e)
        responses[name] = ""

# -------------------------------------------------
# STEP 2: THEME COMPARISON
# -------------------------------------------------
comparison = []

for theme in THEMES.values():
    row = {"pointer_theme": theme["label"]}
    count = 0

    for model_name, text in responses.items():
        present = theme_present(text, theme["keywords"])
        row[model_name] = present
        count += int(present)

    row["count_out_of_2"] = count
    comparison.append(row)

# -------------------------------------------------
# STEP 3: CONTENT GENERATION BASED ON THEMES
# -------------------------------------------------
themes_list = [
    theme["label"] for theme in THEMES.values()
]

theme_prompt = f"""
Write a detailed rental overview for Koramangala covering the following points:
{', '.join(themes_list)}
"""

full_content = generate_content(theme_prompt)

# -------------------------------------------------
# STEP 4: SUMMARY GENERATION
# -------------------------------------------------
summary = summarize_content(full_content)

# -------------------------------------------------
# STEP 5: FINAL JSON OUTPUT
# -------------------------------------------------
final_output = {
    "query": PROMPT,
    "models_used": list(models.keys()),
    "generated_content": full_content,
    "summary": summary,
    "comparison": comparison
}

os.makedirs("output", exist_ok=True)

with open("output/comparison.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=4)

print("✅ Comparison, content, and summary saved to JSON")


