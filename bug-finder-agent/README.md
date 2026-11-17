# Bug Analyzer Agent

An autonomous AI-powered code auditing agent that reads Python source files, identifies security vulnerabilities and logic bugs, explains their impact, and synthesizes corrected code using Azure OpenAI.

---

## Capabilities

Given a target Python source file, the agent executes an end-to-end audit lifecycle:

1. **Loads and parses source code:** Ingests local files via `file_tool.py`.
2. **Performs static reasoning:** Inspects logic bugs, anti-patterns, missing return values, and dangerous function calls (`eval`, `exec`).
3. **Generates line-referenced diagnostics:** Flags precise line numbers and describes exploit risks or execution failures.
4. **Synthesizes corrected implementations:** Generates drop-in replacement snippets.
5. **Compiles Markdown report:** Writes structured audit documentation directly to `<filename>_analysis.md`.

---

## Project Structure

```text
bug-finder-agent/
├── agent_llm.py        # Azure OpenAI client wrapper
├── bug_analyzer.py     # Core bug analysis agent logic
├── file_tool.py        # Code ingestion utility
├── utils.py            # Report persistence helper
├── main.py             # CLI runner
├── sample_code.py      # Example test fixture with known bugs
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## Agent Architecture & Lifecycle

The agent follows a 4-stage autonomous flow:

```text
[ Perception ]           [ Reasoning ]             [ Action ]               [ Tool Use ]
Source Code Loader ──► LLM Code Analysis ──► Markdown Compilation ──► File Persistence
```

1. **Perception:** Reads and validates the target source file.
2. **Reasoning:** Prompts Azure OpenAI with an analytical rubric covering syntax, logic, security, and edge cases.
3. **Action:** Formats findings into standardized Markdown tables and corrected code blocks.
4. **Tool Use:** Calls local file tools to save the resulting audit report.

---

## Installation & Setup

### 1. Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 2. Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in this directory:

```env
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=your_model_name
```

---

## Usage

Analyze any Python file by passing its path as a CLI argument:

```bash
python main.py sample_code.py
```

Console output:
```text
===== ANALYSIS REPORT =====
# Code Audit Report
[Detailed audit findings with line numbers and remediations]
Saved output to sample_code.py_analysis.md
```

---

## Included Sample Fixture

`sample_code.py` contains deliberate reference bugs for testing:
- Division-by-zero vulnerability
- Mutable default arguments (`def append_to(element, target=[])`)
- Unsafe `eval` invocation
- Incomplete conditional branches with missing returns
