import pandas as pd
from tools.ollama_handler import OllamaHandler

ollama = OllamaHandler()

def summarize_job_descriptions(csv_path):
    df = pd.read_csv(csv_path, encoding="ISO-8859-1")

    summaries = []

    for index, row in df.iterrows():
        jd_text = row.get("Job Description") or row.get("Description") or ""
        if not jd_text.strip():
            continue

        prompt = f"Summarize the following job description:\n{jd_text}"
        summary = ollama.query_model(prompt)
        summaries.append({"id": row.get("ID", index), "summary": summary})

    return summaries