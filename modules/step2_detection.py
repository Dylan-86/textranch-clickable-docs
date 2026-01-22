from .llm_client import call_llm
from .docx_utils import read_docx_content, highlight_text_in_docx
import json

def detect_ai_content(file_path, output_docx_path):
    text, doc = read_docx_content(file_path)
    
    prompt = f"""
    Analizza il seguente testo cercando pattern di scrittura AI "innaturali" e "meccaniche".
    Cerca specificamente:
    1. Parole Spia, come ad esempio "vibrante", "serendipità", "iconico", "magico", "tappeto di...", "giustapposizione".
    2. Cliché, come ad esempio"catturare l'anima", "tradizione e modernità", "cuore pulsante", "caos ordinato".
    3. Strutture Sintattiche, come ad esempio "Non X, ma Y", moralismi finali sulla sicurezza o etica.
    4. Mancanza di dettagli sensoriali, come ad esempio, ma non solo, dire "odori tipici" invece di "odore di aglio fritto".
    5. Ogni parola o modo di dire che sia tipico di un AI.
    
    TESTO DA ANALIZZARE:
    {text}
    
    OUTPUT JSON:
    Restituisci un JSON puro (senza markdown ```json) con due chiavi:
    1. "snippets": [lista di stringhe esatte prese dal testo che sono "sospette" per essere evidenziate]
    2. "report_md": "Un report in markdown che spiega cosa cambiare e come rendere il testo più umano. Per ogni cosa da cambiare, proponi un cambiamento 'umanizzante'."
    """
    
    response_str = call_llm(prompt, system_message="Sei un rilevatore anti-AI cinico e preciso. Rispondi solo in JSON.")
    
    # Pulizia basilare se l'LLM mette backticks
    clean_json = response_str.replace("```json", "").replace("```", "").strip()
    
    try:
        data = json.loads(clean_json)
        snippets = data.get("snippets", [])
        report = data.get("report_md", "")
        
        # Genera il file evidenziato
        highlight_text_in_docx(doc, snippets, output_docx_path)
        
        return report
    except json.JSONDecodeError:
        return f"Errore nel parsing JSON dell'AI. Raw response: {response_str}"

