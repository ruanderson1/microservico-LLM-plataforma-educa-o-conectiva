import os
import requests
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

# Use variável de ambiente para a chave da API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-3.5-turbo"

class OpenAIClient:
    @staticmethod
    def generate(prompt: str) -> str:
        if not OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY environment variable not set.")
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "Você é um assistente educacional. Responda apenas com JSON válido."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 1024
        }
        response = requests.post(OPENAI_URL, headers=headers, json=payload, timeout=120)
        print("OpenAI API response status:", response)
        response.raise_for_status()
        data = response.json()
        print("AAAAAAAAAAAAAAAAAAAAAA", data)
        return data["choices"][0]["message"]["content"]
