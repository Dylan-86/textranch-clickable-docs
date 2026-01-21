import os
from dotenv import load_dotenv

load_dotenv()

# Crea un file .env nella root con: OPENROUTER_API_KEY=sk-or-....
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "openai/gpt-oss-120b:free"  # O un altro modello performante su OpenRouter (es. anthropic/claude-3.5-sonnet)

# Prompt di sistema base
SYSTEM_PROMPT = "Sei un editor esperto e severo. Analizzi testi per blog aziendali."
