import re


def extract_answer(text_response: str, pattern: str = r"Answer:\s*(.*)") -> str:
    match = re.search(pattern, text_response)
    if match:
        return match.group(1).strip()
    else:
        return "Answer not found."
