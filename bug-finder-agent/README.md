# 🐞 Bug Analyzer Agent (Azure OpenAI)

A fully autonomous **AI-powered bug detection agent** that reads Python source code, identifies bugs/vulnerabilities, explains them, and produces corrected code — all powered using **Azure OpenAI**.

This agent demonstrates:

* ✔️ Agent structure
* ✔️ Tool/API interaction
* ✔️ Autonomous reasoning & task completion
* ✔️ Secure environment-based LLM configuration

---

## 🚀 What This Agent Does

Given any Python file, the agent:

1. **Loads and reads the file** (via `file_tool.py`)
2. **Sends code to Azure OpenAI** (via `AgentLLM`)
3. **Detects bugs, errors, and vulnerabilities**
4. **Mentions line numbers for each issue**
5. **Provides corrected code suggestions**
6. **Outputs a clean Markdown report**
7. **Saves it to `<filename>_analysis.md`**

It is ideal for:

* Code reviews
* Automated QA
* Developer onboarding
* Demonstrating agentic autonomy

---

## 📁 Project Structure

```
bug-analyzer-agent/
│
├── agent_llm.py        # Azure OpenAI wrapper
├── bug_analyzer.py     # Bug analysis logic (agent)
├── file_tool.py        # Code loader utility
├── utils.py            # Output writer
├── main.py             # CLI runner
├── sample_code.py      # Example buggy code
├── requirements.txt    # Dependencies
└── README.md           # This file
```

---

## 🧠 How the Agent Works Internally

### 1️⃣ Perception — Code Loader

Reads the Python target file:

```python
code = load_file(path)
```

### 2️⃣ Reasoning — Bug Detection

The LLM processes:

* logic bugs
* security issues
* incorrect patterns
* Python anti-patterns
* missing returns
* dangerous functions (`eval`, `exec`, etc.)

### 3️⃣ Action — Markdown Report Generation

LLM produces:

* Bug descriptions
* Impact
* Corrected code blocks
* Line number references

### 4️⃣ Tool Use — Saving Report

```python
save_output(result, "sample_code.py_analysis.md")
```

---

## 🔧 Installation & Setup

### 1️⃣ Create & activate venv

```bash
python -m venv .venv
source .venv/bin/activate  # mac/linux
.venv\Scripts\activate     # windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your Azure OpenAI credentials in `.env`

```
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=your_model_name
```

> ⚠️ Never commit `.env` to Git.

---

## ▶️ Running the Agent

To analyze a file:

```bash
python main.py sample_code.py
```

You will see:

```
===== ANALYSIS REPORT =====
# Code Audit Report
...bugs listed...
Saved output to sample_code.py_analysis.md
```

The full analysis will be saved automatically.

---

## 📌 Why this use-case :

### ✔️ 1. Agent Structure Demonstrated

* LLM wrapper (`AgentLLM`)
* Core task logic (`BugAnalyzerAgent`)
* Tools: file loader + writer
* Execution pipeline in `main.py`

### ✔️ 2. Tool/API Interaction

* Azure OpenAI API
* Local filesystem (read/write)

### ✔️ 3. Autonomous Task Breakdown

The agent completes:

* Read → Analyze → Generate fixes → Save report
  With zero human involvement.

---

## 🧪 Included Example Input

`sample_code.py` contains:

* division-by-zero risk
* mutable default argument
* unsafe `eval`
* missing return

These issues help show the agent’s capabilities.

---
