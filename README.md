# LLM Content Comparator

## Project Name

LLM Content Comparator and Report Generator

Alternative names:
- Multi-LLM Content Comparator
- LLM Comparison and Reporting Automation Tool
- Automated LLM Evaluation and Excel Reporting System

## GitHub Short Description

A Python-based project that compares responses from multiple Large Language Models (LLMs) for a fixed query, evaluates theme coverage, and generates automated JSON and Excel reports.

## README

### Overview

This project compares responses from multiple Large Language Models (LLMs) for a fixed user query and evaluates them against predefined themes. It then stores the results in JSON format and automatically converts them into a formatted Excel report.

The project is useful for analyzing how well different LLMs cover important aspects of a topic. It also supports content generation and summarization using LLaMA, making it both an evaluation tool and a lightweight reporting automation project.

### Features

- Compare responses from multiple LLMs for the same prompt
- Evaluate outputs using theme-based keyword matching
- Generate structured JSON comparison reports
- Export results to Excel with `Yes` / `No` values
- Apply green/red conditional formatting for easy interpretation
- Generate detailed content based on selected themes
- Summarize generated content into concise bullet points
- Store API keys securely using a `.env` file

### LLMs Used

- `LLaMA 3.1 8B Instant` via Groq
- `Mistral 7B Instruct` via OpenRouter

### Tech Stack

- Python
- Requests
- Pandas
- OpenPyXL
- Python Dotenv
- JSON

### Project Structure

```text
llm_content_comparator/
├── main.py
├── llm_clients.py
├── comparator.py
├── themes.py
├── json_to_excel.py
├── requirements.txt
├── .env.example
└── output/
    ├── comparison.json
    └── comparison.xlsx
```

### How It Works

1. A fixed user query is sent to multiple LLMs.
2. Each model returns its response.
3. Responses are checked against predefined themes using keyword matching.
4. A comparison report is saved in JSON format.
5. Additional detailed content is generated using LLaMA.
6. A concise summary is generated from the content.
7. The JSON output is converted into a formatted Excel report.

### Evaluation Themes

The project checks for the presence of themes such as:

- Locality description
- BHK types
- Rental price range
- Amenities
- Connectivity
- Central location
- Security deposit
- Maintenance charges
- Negotiable rent
- Power backup
- Water supply
- Parking availability
- Apartment type
- Furnishing details
- Balcony or extra space

### Installation

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_groq_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

### Usage

Run the comparison:

```bash
python main.py
```

Generate the Excel report:

```bash
python json_to_excel.py
```

### Output

The project generates:

- `output/comparison.json`
- `output/comparison.xlsx`

These files demonstrate that the project executes successfully and produces structured comparison results.

### Example Use Case

For the prompt `rent in koramangala`, the project:

- collects responses from multiple LLMs
- evaluates whether important rental-related themes are covered
- generates detailed content
- creates a concise summary
- exports the results into a readable Excel report

### Future Improvements

- Add more LLM providers and models
- Replace keyword matching with semantic similarity evaluation
- Support multiple prompts in batch mode
- Add score summaries and charts in Excel
- Build a simple web interface

### Notes

- API keys are required for Groq and OpenRouter
- The current evaluation is keyword-based
- Output files should be retained as proof of execution

## Naukri Project Entry

### Project Title

LLM Content Comparator and Report Generator

### Project Description

Developed a Python-based application to compare responses from multiple Large Language Models for a fixed user query. Implemented theme-based evaluation using keyword matching, generated structured JSON output, and converted results into a formatted Excel report with conditional formatting. Integrated Groq and OpenRouter APIs to fetch model responses and added content generation and summarization capabilities.

### Role

Developer

### Technologies Used

Python, Requests, Pandas, OpenPyXL, JSON, REST APIs, Groq API, OpenRouter API

## LinkedIn Project Entry

### Title

LLM Content Comparator and Report Generator

### Description

Built a Python project to compare outputs from multiple LLMs, evaluate them against predefined themes, and generate automated JSON and Excel reports. Integrated Groq LLaMA and OpenRouter Mistral APIs, added summarization and content generation workflows, and created color-coded Excel reporting for easier interpretation of model performance.

## Resume / Portfolio Version

Developed a multi-LLM comparison tool in Python that analyzes responses from different language models against predefined thematic criteria and exports the results into structured JSON and formatted Excel reports. Integrated Groq and OpenRouter APIs, automated content generation and summarization, and improved interpretability through conditional formatting and report generation.

## Skills / Keywords

- Python
- API Integration
- REST APIs
- Generative AI
- Large Language Models (LLM)
- Prompt Engineering
- JSON Processing
- Pandas
- OpenPyXL
- Excel Automation
- Data Analysis
- Report Generation
- Keyword-Based Text Evaluation
- Environment Variable Management

## One-Line Description

Python-based automation tool for comparing multiple LLM responses, evaluating theme coverage, and generating JSON and Excel reports.
