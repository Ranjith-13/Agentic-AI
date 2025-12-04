# 🧪 Test Case Generator Agent (Azure OpenAI)

An autonomous **AI-powered test case generation agent** that reads Python source code, analyzes its functions and behaviors, and produces:

* ✔️ A complete **test plan** (Markdown)
* ✔️ A fully runnable **pytest test file**
* ✔️ Follows strict JSON formatting rules
* ✔️ Uses Azure OpenAI for reasoning

This agent is ideal for:
* Automated QA
* Increasing test coverage
* Code reliability improvements
* Developers who want instant tests for new functions

---

## 🚀 What the Agent Does

For any Python file, the agent:

1. **Reads the file** (`file_tool.py`)
2. **Understands functions, parameters, edge cases**
3. **Generates a complete test plan** (Markdown)
4. **Generates a pytest test file** (unit + boundary + negative cases)
5. **Outputs valid JSON only** (strict validation)
6. **Automatically saves both files**

Output files:

* `sample_code.py_test_plan.md`
* `test_sample_code.py`

---

## 📁 Project Structure

```
test-case-generator/
│
├── test_case_agent.py      # Core agent (LLM-powered test generation)
├── main.py                 # Runner script
├── file_tool.py            # File loading & saving
├── utils.py                # Filename sanitizer
├── sample_code.py          # Input example
├── test_sample_code.py     # (Generated output)
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🧠 How the Agent Works Internally

### 1️⃣ Perception Layer — Reading Code

The agent loads the Python source file using `read_file`.

### 2️⃣ Reasoning Layer — LLM Processing

LLM extracts:

* Function names
* Arguments
* Behaviors
* Conditions
* Failure modes
* Edge cases

### 3️⃣ Planning Layer — Test Strategies

The agent plans:

* Positive tests
* Negative tests
* Boundary tests
* Error handling tests
* Mocking strategy (if applicable)

### 4️⃣ Action Layer — JSON Response

Azure OpenAI must return **strict JSON**:

```
{
  "test_plan": "markdown content",
  "test_file": "pytest content"
}
```

The agent validates it using Python's `json` module.

### 5️⃣ Tool Use — Saving Files

Files are automatically written using `save_text`.

---

## 🔧 Installation & Setup

### 1️⃣ Create and activate the virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Azure OpenAI in `.env`

```
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=your_model_name
```

---

## ▶️ Running the Agent

To process `sample_code.py`:

```bash
python main.py sample_code.py
```

You will see:

```
⏳ Generating test cases...
Saved → sample_code.py_test_plan.md
Saved → test_sample_code.py

✅ Test Case Generation Complete!
```

Both output files will be available.

---

## 📌 Why this use-case:

### ✔️ 1. **Agent Structure**

* LLM wrapper (`TestCaseGeneratorAgent`)
* Tools for reading/saving files
* Execution orchestrator (`main.py`)

### ✔️ 2. **Tool/API Interaction**

* Azure OpenAI (LLM)
* Local file system

### ✔️ 3. **Autonomous Task Completion**

The agent performs:

```
read → analyze → generate plan → generate tests → save → done
```

Zero human intervention.

---

## 🧪 Example Input Functions

From `sample_code.py`:

* `divide(a, b)`
* `is_valid_age(age)`
* `greet(name)`

The agent generates:

* Edge-case coverage
* Exception tests
* Type/validation tests

Example generated tests include:

```python
with pytest.raises(ZeroDivisionError):
    divide(10, 0)
```

---
