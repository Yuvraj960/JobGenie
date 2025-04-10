from tools.ollama_handler import ask_ollama

def generate_invite(jd_summary: str, cv_text: str) -> str:
    prompt = f"""
You are a recruiter. Write a professional and friendly interview invite email for the following candidate.

Job Description Summary:
{jd_summary}

Candidate Resume:
{cv_text}

Include: Position title, date (placeholder), time (placeholder), format (virtual), and a closing note.
"""
    return ask_ollama(prompt)
