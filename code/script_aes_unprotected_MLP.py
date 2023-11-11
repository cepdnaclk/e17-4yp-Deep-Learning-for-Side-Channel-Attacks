import sys
sys.path.append('D:/CA/UOP/4th year/Sem7/CO421/AISY_framework')


import aisy_sca
from app import *
from custom.custom_models.neural_networks import *

new_dataset_dict = {
    "filename": "new_dataset_2rounds.h5",
    "key": "000102030405060708090A0B0C0D0EF0",
    "first_sample": 0,
    "number_of_samples": 100,
    "number_of_profiling_traces": 60000,
    "number_of_attack_traces": 40000
}

aisy = aisy_sca.Aisy()
aisy.set_resources_root_folder(resources_root_folder)
aisy.set_database_root_folder(databases_root_folder)
aisy.set_datasets_root_folder(datasets_root_folder)
aisy.set_database_name("database_ascad.sqlite")
#aisy.set_dataset(datasets_dict["ascad-variable.h5"])
aisy.set_dataset(new_dataset_dict)
aisy.set_aes_leakage_model(leakage_model="ID", byte=4, round=1, 
                           target_state="Sbox", direction="Encryption", cipher="AES128")

aisy.set_batch_size(400)
aisy.set_epochs(22)
aisy.set_neural_network(mlp)
aisy.run(key_rank_attack_traces=15000)
#aisy.run()
