from test_case_agent import TestCaseGeneratorAgent
from file_tool import read_file, save_text
from utils import sanitize_filename

def run(file):
    code = read_file(file)
    agent = TestCaseGeneratorAgent()

    print("⏳ Generating test cases...")
    result = agent.generate_test_cases(code)

    test_plan = result["test_plan"]
    test_file = result["test_file"]

    save_text(test_plan, f"{sanitize_filename(file)}_test_plan.md")
    save_text(test_file, f"test_{sanitize_filename(file)}.py")

    print("\n✅ Test Case Generation Complete!")

if __name__ == "__main__":
    run("sample_code.py")
