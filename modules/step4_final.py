from .step1_ped import check_ped_compliance

def final_ped_check(fixed_file_path):
    # Riutilizziamo la logica robusta dello step 1
    return check_ped_compliance(fixed_file_path)
