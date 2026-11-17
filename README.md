# Agentic AI: Autonomous LLM Workflows

A modular collection of autonomous AI agents powered by Azure OpenAI. Each implementation demonstrates core agentic design patterns: goal-directed task decomposition, autonomous tool use, structured output validation, and local filesystem interaction.

---

## Agent Portfolio

| Agent | Focus Area | Core Capabilities | Primary Artifacts |
| :--- | :--- | :--- | :--- |
| **[Bug Finder Agent](bug-finder-agent/)** | Static Code Analysis | Audits Python source code, identifies vulnerabilities and anti-patterns, provides line-referenced fixes. | Markdown audit report (`<file>_analysis.md`) |
| **[CodeSketch Agent](codesketch-agent/)** | Architecture Synthesis | Extracts class hierarchies and execution flows, generates Mermaid markup, and renders structural diagrams. | Mermaid definition (`diagram.md`), JPG diagram (`diagram.jpg`) |
| **[Test Case Generator](test-case-generator/)** | Automated QA & Testing | Synthesizes test plans and generates runnable `pytest` test suites covering boundary and negative edge cases. | Test plan (`<file>_test_plan.md`), executable suite (`test_<file>.py`) |

---

## Architecture & Agentic Design Patterns

Each agent in this repository operates on a four-stage autonomous lifecycle:

```text
Input Source ──► [ Perception ] ──► [ Reasoning & Planning ] ──► [ Tool Action ] ──► Final Artifact
                    File Loader          Azure OpenAI LLM            Tool Execution       Markdown / Code / JPG
```

1. **Perception:** Ingests and normalizes local source files without human prompting.
2. **Reasoning & Planning:** Prompts the Azure OpenAI model to perform deep semantic code inspection, plan verification strategies, and enforce strict JSON schemas.
3. **Tool Execution:** Interfaces directly with local environments (filesystem read/write, Graphviz rendering engines, test runners).
4. **Artifact Generation:** Produces durable, deterministic deliverables directly into the workspace.

---

## Example Architecture Output

The CodeSketch agent parses Python class definitions and autonomously outputs rendered visual architecture diagrams:

![CodeSketch Architecture Output](./codesketch-agent/diagram.jpg)

---

## Repository Structure

```text
Agentic-AI/
├── bug-finder-agent/         # Autonomous vulnerability scanner & code reviewer
│   ├── agent_llm.py          # Azure OpenAI client wrapper
│   ├── bug_analyzer.py       # Core analysis agent logic
│   ├── file_tool.py          # Filesystem loader utility
│   ├── main.py               # CLI entrypoint
│   └── sample_code.py        # Reference test fixture
├── codesketch-agent/         # Code-to-diagram architecture generator
│   ├── code_parser.py        # Code structure extractor
│   ├── diagram_generator.py  # Prompt builder and Mermaid synthesizer
│   ├── utils.py              # Graphviz rendering tool integration
│   └── main.py               # CLI entrypoint
└── test-case-generator/      # Automated pytest generation agent
    ├── test_case_agent.py    # LLM test planning and JSON enforcement
    ├── file_tool.py          # File input/output handlers
    └── main.py               # CLI entrypoint
```

---

## Quickstart & Local Setup

### Prerequisites
- Python 3.10+
- Azure OpenAI resource with an active deployment (e.g., GPT-4o or GPT-4o-mini)
- Graphviz (required for CodeSketch diagram rendering to JPG)

### 1. Environment Configuration
Each agent utilizes a `.env` file for secure credential isolation. Configure the following variables in the agent directory you wish to execute:

```env
AZURE_OPENAI_API_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
```

### 2. Execution

Navigate to any agent directory, install dependencies, and run against a target Python file:

```bash
# Bug Finder Agent
cd bug-finder-agent
pip install -r requirements.txt
python main.py sample_code.py

# CodeSketch Agent
cd ../codesketch-agent
pip install -r requirements.txt
python main.py sample_code.py

# Test Case Generator
cd ../test-case-generator
pip install -r requirements.txt
python main.py sample_code.py
```

---

## License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
