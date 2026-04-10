import requests
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------- GROQ (CORE MODEL) --------------------

def groq_llama(prompt):
    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
    )

    data = r.json()
    if "choices" not in data:
        print("⚠️ Groq skipped:", data)
        return ""

    return data["choices"][0]["message"]["content"]


# -------------------- OPENROUTER (OPTIONAL BACKUP) --------------------

def openrouter_mistral(prompt):
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
    )

    data = r.json()
    if "choices" not in data:
        print("⚠️ OpenRouter skipped:", data)
        return ""

    return data["choices"][0]["message"]["content"]


# -------------------- GENERATE CONTENT --------------------

def generate_content(prompt):
    """
    Generates detailed content based on themes
    """
    return groq_llama(prompt)


# -------------------- SUMMARIZE CONTENT --------------------

def summarize_content(text):
    """
    Summarizes generated content into bullet points
    """
    summary_prompt = f"""
Summarize the following content in 5–6 concise bullet points.
Keep it clear, factual, and short.

Content:
{text}
"""
    return groq_llama(summary_prompt)
