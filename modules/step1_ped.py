from .llm_client import call_llm
from .docx_utils import read_docx_content, extract_ped_page

def check_ped_compliance(file_path, ped_file_path=None):
    text, doc = read_docx_content(file_path)
    
    # Se ped_file_path è fornito, estraiamo il PED da lì, 
    # altrimenti lo estraiamo dallo stesso file_path.
    if ped_file_path:
        _, ped_doc = read_docx_content(ped_file_path)
        ped_specs = extract_ped_page(ped_doc)
    else:
        ped_specs = extract_ped_page(doc)
    
    prompt = f"""
    Analizza il seguente ARTICOLO basandoti sulle SPECIFICHE PED fornite.
    
    SPECIFICHE PED (estratte dalla prima pagina):
    {ped_specs}
    
    ARTICOLO COMPLETO:
    {text}
    
    COMPITO:
    Verifica ESATTAMENTE i seguenti punti:
    1. Il 'Title' nell'articolo corrisponde a quello nel PED?
    2. La struttura degli H2/H3 corrisponde all'Outline richiesta?
    3. L'Anchor Text è presente esattamente come richiesto?
    4. L'Anchor URL è corretto?
    5. La Link Position è rispettata (es. intro, specific H2, bottom)?
    
    OUTPUT:
    Se tutto è corretto, rispondi SOLO con la stringa: "OK"
    Se ci sono errori, crea un elenco puntato Markdown dettagliato delle correzioni necessarie.
    """
    
    response = call_llm(prompt)
    return response
