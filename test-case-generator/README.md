# Test Case Generator Agent

An autonomous test generation agent that parses Python source code, derives comprehensive test plans, and synthesizes runnable `pytest` test suites enforcing strict JSON schema constraints via Azure OpenAI.

---

## Capabilities

- **Automated Behavioral Analysis:** Evaluates parameter boundaries, return contracts, exceptions, and failure modes.
- **Structured Test Planning:** Compiles a dedicated Markdown test plan document detailing positive, negative, and edge case coverage.
- **Runnable Pytest Synthesis:** Produces a ready-to-run `pytest` test file matching production testing conventions.
- **Schema Enforcement:** Validates model completions against strict JSON schemas before saving artifacts.

---

## Output Artifacts

Running the agent against `sample_code.py` produces two deliverables:
- `<filename>_test_plan.md`: Comprehensive test strategy, test matrix, and expected assertions.
- `test_<filename>.py`: Python test script containing fully formed `pytest` test functions.

---

## Project Structure

```text
test-case-generator/
├── test_case_agent.py      # Core agent logic and JSON schema validation
├── file_tool.py            # Local filesystem handlers
├── utils.py                # Filename and path sanitizers
├── main.py                 # CLI entrypoint
├── sample_code.py          # Input example
├── test_sample_code.py     # Generated output test suite
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## Architecture Lifecycle

```text
[ Input ]                 [ Reasoning ]              [ Validation ]            [ Tool Action ]
Python Source Code ──► LLM Test Synthesis ──► Strict JSON Schema Check ──► Persist Plan & Test Suite
```

1. **Perception:** Reads and tokenizes the target Python script.
2. **Reasoning & Planning:** The LLM devises test strategies for boundary values, null inputs, type errors, and expected exceptions.
3. **Validation:** Verifies the model returned valid JSON conforming to:
   ```json
   {
     "test_plan": "Markdown string describing test scenarios",
     "test_file": "Executable pytest Python code"
   }
   ```
4. **Tool Execution:** Automatically writes the validated test plan and pytest test file to disk.

---

## Installation & Setup

### 1. Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 2. Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in this directory:

```env
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=your_model_name
```

---

## Usage

Generate tests for a target Python file:

```bash
python main.py sample_code.py
```

Console output:
```text
Generating test cases...
Saved: sample_code.py_test_plan.md
Saved: test_sample_code.py

Test Case Generation Complete.
```

Execute the generated test suite:
```bash
pytest test_sample_code.py -v
```

---

## Example Test Coverage

The included fixture `sample_code.py` tests multiple function behaviors:
- `divide(a, b)`: Valid quotients and `pytest.raises(ZeroDivisionError)` assertions.
- `is_valid_age(age)`: Range boundaries (0, 18, 120), negative ages, and type validation.
- `greet(name)`: String formatting, whitespace stripping, and empty string fallbacks.
