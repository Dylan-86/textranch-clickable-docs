# Textranch Clickable Docs

Questo progetto automatizza l'analisi e la correzione di documenti `.docx` per garantirne la conformità PED, rilevare contenuti generati da IA e applicare correzioni automatiche.

## Requisiti

- Python 3.8+
- Una chiave API di OpenRouter

## Installazione

1. Clona il repository:
   ```bash
   git clone [repository_url]
   cd textranch-clickable-docs
   ```

2. Crea la cartella di output:
   ```bash
   mkdir output
   ```

3. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

## Configurazione

Crea un file `.env` nella root del progetto partendo dal template:

```bash
cp .env.example .env
```

Modifica il file `.env` e inserisci la tua `OPENROUTER_API_KEY`.

## Utilizzo

Per avviare il processo di analisi e correzione:

```bash
python3 main.py
```

Il file di input predefinito è configurato in `main.py` (variabile `FILE_NAME`). Assicurati che il file sia presente nella cartella `input/`.

## Funzionamento

Il processo si divide in 4 step:
1. **Controllo PED Iniziale**: Verifica se il documento rispetta le linee guida PED.
2. **AI Detection**: Identifica parti del testo potenzialmente generate da IA e produce un file evidenziato.
3. **Applicazione Fix**: Corregge il testo per renderlo più naturale e conforme.
4. **Controllo PED Finale**: Verifica che le correzioni non abbiano compromesso la conformità PED.
