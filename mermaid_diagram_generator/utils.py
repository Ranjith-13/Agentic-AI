from pathlib import Path
import re
from graphviz import Source

def save_output(content: str, output_file: str = "diagram.md"):
    Path(output_file).write_text(content)
    print(f"Diagram saved to {output_file}")

def extract_mermaid(diagram_text: str) -> str:
    """
    Extract the Mermaid diagram code block from the LLM output.
    """
    pattern = r"```mermaid(.*?)```"
    match = re.search(pattern, diagram_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return diagram_text.strip()

def mermaid_to_dot(mermaid_code: str) -> str:
    """
    VERY basic flowchart-style Mermaid to Graphviz DOT converter.
    Works for flowchart-like Mermaid diagrams.
    """
    lines = mermaid_code.splitlines()
    dot_lines = ["digraph G {", 'rankdir=LR;', 'node [shape=box];']

    for line in lines:
        line = line.strip()

        # A --> B
        if "-->" in line:
            parts = line.split("-->")
            left = parts[0].strip()
            right = parts[1].strip()
            dot_lines.append(f'"{left}" -> "{right}";')

    dot_lines.append("}")
    return "\n".join(dot_lines)

def save_jpg_from_dot(dot_code: str, output_file: str = "diagram.jpg"):
    graph = Source(dot_code)
    graph.format = "jpg"
    graph.render(output_file, cleanup=True)
    print(f"Image saved to {output_file}.jpg")
