from .llm_client import call_llm
from .docx_utils import read_docx_content, save_text_as_docx

def apply_fixes(original_file_path, detection_report_md, output_file_path):
    text, doc = read_docx_content(original_file_path)
    
    prompt = f"""
    Hai il compito di riscrivere un articolo per rimuovere i "tic" dell'AI, basandoti su un report di correzione.
    
    TESTO ORIGINALE:
    {text}
    
    REPORT CORREZIONI (DA APPLICARE RIGOROSAMENTE):
    {detection_report_md}
    
    ISTRUZIONI:
    1. Riscrivi l'articolo applicando le modifiche.
    2. NON cambiare nient'altro (struttura, informazioni tecniche, PED specs se presenti nel testo).
    3. Rendi il tono più umano, diretto e sensoriale dove richiesto.
    4. Restituisci SOLO il testo completo dell'articolo finale. Nient'altro.
    """
    
    fixed_text = call_llm(prompt)
    save_text_as_docx(fixed_text, output_file_path)
    return "Fix applicati."
