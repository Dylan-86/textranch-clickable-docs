import os
import sys
from modules.step1_ped import check_ped_compliance
from modules.step2_detection import detect_ai_content
from modules.step3_fix import apply_fixes
from modules.step4_final import final_ped_check

INPUT_DIR = "input"
OUTPUT_DIR = "output"
FILE_NAME = "44.docx" # Cambia col nome dinamico o passalo da riga di comando

def main():
    input_path = os.path.join(INPUT_DIR, FILE_NAME)
    base_name = os.path.splitext(FILE_NAME)
    
    if not os.path.exists(input_path):
        print(f"File {input_path} non trovato!")
        return

    print("--- STEP 1: Controllo PED Iniziale ---")
    step1_result = check_ped_compliance(input_path)
    
    if "OK" in step1_result and len(step1_result) < 10:
        print("✅ PED rispettato.")
    else:
        print("⚠️ Trovate discrepanze nel PED.")
        edits_path = os.path.join(OUTPUT_DIR, f"{base_name} - edits.md")
        with open(edits_path, "w", encoding="utf-8") as f:
            f.write(step1_result)
        print(f"Report salvato in: {edits_path}")
        # Qui potresti decidere se fermarti o continuare. Il prompt dice "si passa al secondo step".
    
    print("\n--- STEP 2: AI Detection ---")
    detection_docx_path = os.path.join(OUTPUT_DIR, f"{base_name} - AI detection.docx")
    detection_md_path = os.path.join(OUTPUT_DIR, f"{base_name} - AI detection.md")
    
    detection_report = detect_ai_content(input_path, detection_docx_path)
    
    with open(detection_md_path, "w", encoding="utf-8") as f:
        f.write(detection_report)
    print(f"Report rilevamento salvato in: {detection_md_path}")
    print(f"File evidenziato salvato in: {detection_docx_path}")
    
    print("\n--- STEP 3: Applicazione Fix ---")
    fixed_docx_path = os.path.join(OUTPUT_DIR, f"{base_name} - fixed.docx")
    apply_fixes(input_path, detection_report, fixed_docx_path)
    print(f"File corretto salvato in: {fixed_docx_path}")
    
    print("\n--- STEP 4: Controllo PED Finale ---")
    final_result = final_ped_check(fixed_docx_path)
    
    if "OK" in final_result and len(final_result) < 10:
        print("✅ PROCESSO COMPLETATO CON SUCCESSO. Il file fixed rispetta il PED.")
    else:
        print("❌ ATTENZIONE: Il file corretto ha perso la conformità PED.")
        final_edits_path = os.path.join(OUTPUT_DIR, f"{base_name} - final-edits.md")
        with open(final_edits_path, "w", encoding="utf-8") as f:
            f.write(final_result)
        print(f"Report errori finali in: {final_edits_path}")

if __name__ == "__main__":
    main()
