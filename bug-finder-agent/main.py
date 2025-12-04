# main.py
import argparse
from file_tool import load_file
from utils import save_output
from bug_analyzer import BugAnalyzerAgent

def run_agent(file_path: str):
    agent = BugAnalyzerAgent()
    code = load_file(file_path)

    print(f"\nAnalyzing {file_path}...\n")
    result = agent.analyze(code)

    print("\n===== ANALYSIS REPORT =====\n")
    print(result)

    save_output(result, f"{file_path}_analysis.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bug Analyzer Agent")
    parser.add_argument("file", help="Python file to analyze")

    args = parser.parse_args()
    run_agent(args.file)
