from agent_llm import AgentLLM
from code_parser import load_code
from diagram_generator import DiagramGenerator
from utils import save_output, extract_mermaid, mermaid_to_dot, save_jpg_from_dot

def run_agent(file_path):
    llm = AgentLLM()
    code = load_code(file_path)

    dg = DiagramGenerator()
    prompt = dg.build_prompt(code)

    result = llm.generate(
        system_prompt=DiagramGenerator.BASE_PROMPT,
        user_prompt=prompt
    )

    print("\n===== GENERATED DIAGRAM =====\n")
    print(result)
    print("\n=============================\n")

    # 1️⃣ Save Mermaid diagram as MD
    save_output(result, "diagram.md")

    # 2️⃣ Extract Mermaid code
    mermaid_code = extract_mermaid(result)

    # 3️⃣ Convert Mermaid → DOT
    dot = mermaid_to_dot(mermaid_code)

    # 4️⃣ Export DOT → JPG
    save_jpg_from_dot(dot, "diagram")

if __name__ == "__main__":
    run_agent("sample_code.py")
