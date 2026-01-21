from openai import OpenAI
from .config import OPENROUTER_API_KEY, MODEL_NAME

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def call_llm(prompt, system_message=None):
    messages = []
    if system_message:
        messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.2 # Bassa temperatura per analisi rigorosa
    )
    return response.choices[0].message.content
