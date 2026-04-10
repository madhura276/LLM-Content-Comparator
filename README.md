# LLM Content Comparator

## Overview
This project compares responses from multiple Large Language Models (LLMs)
for a fixed user query and evaluates them against predefined themes.
The results are stored in JSON and automatically converted into a formatted Excel report.

## LLMs Used
- LLaMA-3-8B via Groq (primary model)
- Mistral-7B-Instruct via OpenRouter (comparison model)

## Features
- Multi-LLM response comparison
- Theme-based evaluation using keyword matching
- Automated JSON report generation
- Excel export with Yes/No values and green/red conditional formatting
- Content generation and summarization using LLaMA-3

## Tech Stack
- Python
- Requests
- Pandas
- OpenPyXL

## How to Run
```bash
pip install -r requirements.txt
python main.py
python json_to_excel.py

## Output
- output/comparison.json
- output/comparison.xlsx

## Notes
API keys are required for Groq and OpenRouter.
They should be added in a .env file (see .env.example).

---

## 📊 4️⃣ OUTPUT FILES (KEEP THEM)

Include:
- `comparison.json`
- `comparison.xlsx`

This proves **it actually works**.

