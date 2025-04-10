import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt, model="llama3"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except requests.exceptions.RequestException as e:
        print("[Ollama Error]", e)
        return ""

class OllamaHandler:
    def __init__(self, model_name="llama3"):
        self.model_url = OLLAMA_API_URL
        self.model_name = model_name

    def query_model(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(self.model_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            print("[Ollama Error]", e)
            return ""
