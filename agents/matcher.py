from tools.ollama_handler import ask_ollama

def calculate_match_score(jd_summary: str, cv_text: str) -> dict:
    prompt = f"""
You are a recruitment assistant.

Compare the following candidate CV with the Job Description summary and calculate a match score out of 100.

### Job Description Summary:
{jd_summary}

### Candidate CV:
{cv_text}

Give your response in this format:
Match Score: <score out of 100>
Reason: <1-2 sentence reason>
"""
    response = ask_ollama(prompt)
    return parse_match_response(response)

def parse_match_response(response: str) -> dict:
    lines = response.strip().split('\n')
    score = 0
    reason = ""
    for line in lines:
        if "Match Score" in line:
            try:
                score = int(''.join(filter(str.isdigit, line)))
            except:
                score = 0
        elif "Reason" in line:
            reason = line.split(":", 1)[1].strip() if ":" in line else line
    return {"score": score, "reason": reason}
