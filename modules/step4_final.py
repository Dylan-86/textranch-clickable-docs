from .step1_ped import check_ped_compliance

def final_ped_check(fixed_file_path, original_file_path):
    # Riutilizziamo la logica dello step 1, ma passando il file originale per i PED specs
    return check_ped_compliance(fixed_file_path, ped_file_path=original_file_path)
