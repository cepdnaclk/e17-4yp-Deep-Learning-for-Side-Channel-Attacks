import pandas as pd
import h5py

###TODO:Add the path
hdf5_file = h5py.File('path_of_h5_dataset_containing_all_the_traces', 'r')

#Load data in H5 format dataset to dataframes
profiling_df = pd.DataFrame(hdf5_file['Profiling_traces/traces'][:])
attacking_df = pd.DataFrame(hdf5_file['Attack_traces/traces'][:])
profiling_plaintext_df = pd.DataFrame(hdf5_file['Profiling_traces/metadata']['plaintext'])
attacking_plaintext_df = pd.DataFrame(hdf5_file['Attack_traces/metadata']['plaintext'])
profiling_ciphertext_df = pd.DataFrame(hdf5_file['Profiling_traces/metadata']['ciphertext'])
attacking_ciphertext_df = pd.DataFrame(hdf5_file['Attack_traces/metadata']['ciphertext'])
profiling_key_df = pd.DataFrame(hdf5_file['Profiling_traces/metadata']['key'])
attacking_key_df = pd.DataFrame(hdf5_file['Attack_traces/metadata']['key'])
hdf5_file.close()


#Rotate the dataset
profiling_df_transposed = profiling_df.transpose()
attacking_df_transposed = attacking_df.transpose()
profiling_plaintext_df_transposed = profiling_plaintext_df.transpose()
attacking_plaintext_df_transposed = attacking_plaintext_df.transpose()
profiling_ciphertext_df_transposed = profiling_ciphertext_df.transpose()
attacking_ciphertext_df_transposed = attacking_ciphertext_df.transpose()
profiling_key_df_transposed = profiling_key_df.transpose()
attacking_key_df_transposed = attacking_key_df.transpose()


#Choose similar traces from profiling set
import numpy as np
i = 0
profiling_df_set1 = pd.DataFrame()
profiling_plaintext_df_set1 = pd.DataFrame()
profiling_ciphertext_df_set1 = pd.DataFrame()
profiling_key_df_set1 = pd.DataFrame()
for trace in profiling_df_transposed:
  R = np.corrcoef(profiling_df_transposed[0],profiling_df_transposed[i])
  if R[0][1] >= 0.75:
    row_to_append = pd.DataFrame([profiling_df_transposed[i]])
    profiling_df_set1 = profiling_df_set1.append(row_to_append, ignore_index=True)
    row_to_append = pd.DataFrame([profiling_plaintext_df_transposed[i]])
    profiling_plaintext_df_set1 = profiling_plaintext_df_set1.append(row_to_append, ignore_index=True)
    row_to_append = pd.DataFrame([profiling_ciphertext_df_transposed[i]])
    profiling_ciphertext_df_set1 = profiling_ciphertext_df_set1.append(row_to_append, ignore_index=True)
    row_to_append = pd.DataFrame([profiling_key_df_transposed[i]])
    profiling_key_df_set1 = profiling_key_df_set1.append(row_to_append, ignore_index=True)
  i = i+1
print(profiling_df_set1.shape)
print(profiling_plaintext_df_set1.shape)
print(profiling_ciphertext_df_set1.shape)
print(profiling_key_df_set1.shape)


#Choose similar traces from attacking set
i = 0
attacking_df_set1 = pd.DataFrame()
attacking_plaintext_df_set1 = pd.DataFrame()
attacking_ciphertext_df_set1 = pd.DataFrame()
attacking_key_df_set1 = pd.DataFrame()
for trace in attacking_df_transposed:
  R = np.corrcoef(profiling_df_transposed[0],attacking_df_transposed[i])
  if R[0][1] >= 0.75:
    row_to_append = pd.DataFrame([attacking_df_transposed[i][0:100]])
    attacking_df_set1 = attacking_df_set1.append(row_to_append, ignore_index=True)
    row_to_append = pd.DataFrame([attacking_plaintext_df_transposed[i]])
    attacking_plaintext_df_set1 = attacking_plaintext_df_set1.append(row_to_append, ignore_index=True)
    row_to_append = pd.DataFrame([attacking_ciphertext_df_transposed[i]])
    attacking_ciphertext_df_set1 = attacking_ciphertext_df_set1.append(row_to_append, ignore_index=True)
    row_to_append = pd.DataFrame([attacking_key_df_transposed[i]])
    attacking_key_df_set1 = attacking_key_df_set1.append(row_to_append, ignore_index=True)
  i = i+1
print(attacking_df_set1.shape)
print(attacking_plaintext_df_set1.shape)
print(attacking_ciphertext_df_set1.shape)
print(attacking_key_df_set1.shape)


#Convert dataframes to arrays
wavedataT = np.array(profiling_df_set1)
plaintexts_profiling = np.array(profiling_plaintext_df_set1)
ciphertexts_profiling = np.array(profiling_ciphertext_df_set1)
keys_profiling = np.array(profiling_key_df_set1)
wavedataA = np.array(attacking_df_set1)
plaintexts_attack = np.array(attacking_plaintext_df_set1)
ciphertexts_attack = np.array(attacking_ciphertext_df_set1)
keys_attack = np.array(attacking_key_df_set1)


#Creating H5 file
nb_profiling_traces = len(wavedataT)
nb_attack_traces = len(wavedataA)
profiling_index = [i for i in range(nb_profiling_traces)]
attack_index = [i for i in range(nb_attack_traces)]

out_file = h5py.File('new_dataset.h5', 'w')

profiling_traces_group = out_file.create_group("Profiling_traces")
attack_traces_group = out_file.create_group("Attack_traces")

""" create fields for profiling and attack sets """
profiling_traces_group.create_dataset(name="traces", data=wavedataT, dtype=wavedataT.dtype)
attack_traces_group.create_dataset(name="traces", data=wavedataA, dtype=wavedataA.dtype)

""" create metadata fields for profiling and attack sets"""
metadata_type_profiling = np.dtype([("plaintext", plaintexts_profiling.dtype, (16,)),
                                    ("ciphertext", ciphertexts_profiling.dtype, (16,)),
                                    ("key", keys_profiling.dtype, (16,))
                                    ])
profiling_metadata = np.array([(plaintexts_profiling[n], ciphertexts_profiling[n], keys_profiling[n]) for n in
                               profiling_index], dtype=metadata_type_profiling)

metadata_type_attack = np.dtype([("plaintext", plaintexts_attack.dtype, (16,)),
                                 ("ciphertext", ciphertexts_attack.dtype, (16,)),
                                 ("key", keys_attack.dtype, (16,))
                                 ])
profiling_traces_group.create_dataset("metadata", data=profiling_metadata, dtype=metadata_type_profiling)

attack_metadata = np.array([(plaintexts_attack[n], ciphertexts_attack[n], keys_attack[n]) for n in
                            attack_index], dtype=metadata_type_attack)
attack_traces_group.create_dataset("metadata", data=attack_metadata, dtype=metadata_type_attack)

out_file.flush()
out_file.close()