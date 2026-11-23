from pathlib import Path

ROLE_DIR = Path(__file__).parent

def pick_role(role):
    file_path = ROLE_DIR / f"{role}.md"
    with open(file_path,"r",encoding="utf-8") as file:
        role_prompt = file.read()
    return role_prompt
