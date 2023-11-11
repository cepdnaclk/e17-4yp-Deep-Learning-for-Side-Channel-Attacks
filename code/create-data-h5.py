import numpy as np
import h5py
import array

#numsamples
numsamples = 150
#start_of_rounds = 297
#start_of_first_round = 0
#start_of_second_round = 50
#start_of_third_round = 100
#start_of_forth_round = 150
#end_of_tenth_round = 549

wavedataA_file = "file_path_of_wave-normA.data_file"

wavedataA = []
## read wave file
print("reading Wavefile")  
f = open(wavedataA_file, 'rb')

while(True):
  data = array.array('f')
  try:
    data.fromfile(f, numsamples)
  except EOFError:
    break
  wavedataA.append(data)
wavedataA = np.array(wavedataA)
wavedataA = wavedataA[:, 0 : 12]    #Get the sample set that we need (to get only the part of trace corresponding to several rounds)

print(wavedataA.shape)



wavedataT_file = "file_path_of_wave-normT.data_file"

wavedataT = []
## read wave file
print("reading training Wavefile")  
f = open(wavedataT_file, 'rb')

while(True):
  data = array.array('f')
  try:
    data.fromfile(f, numsamples)
  except EOFError:
    break
  wavedataT.append(data)

wavedataT = np.array(wavedataT)
wavedataT = wavedataT[:, 0 : 12]    #Get the sample set that we need (to get only the part of trace corresponding to several rounds)

print(wavedataT.shape)


plaintexts_profiling_file = "file_path_of_text_inT.txt_file"
plaintexts_profiling = []


print("reading plaintexts_profiling")
with open(plaintexts_profiling_file, 'r') as f:
  lines1 = f.readlines()
  #plaintexts_profiling = np.array(plaintexts_profiling)
plaintexts_profiling_txt = [line.strip().split() for line in lines1]
plaintexts_profiling = [[int(hex_string, 16) for hex_string in row] for row in plaintexts_profiling_txt]
plaintexts_profiling = np.array(plaintexts_profiling)

print(plaintexts_profiling)

plaintexts_attack_file = "path_of_text_inA.txt_file"
plaintexts_attack = []


print("reading plaintexts_attack")
with open(plaintexts_attack_file, 'r') as f:
  lines2 = f.readlines()
  #plaintexts_attack = np.array(plaintexts_attack)
plaintexts_attack_txt = [line.strip().split() for line in lines2]
plaintexts_attack = [[int(hex_string, 16) for hex_string in row] for row in plaintexts_attack_txt]
plaintexts_attack = np.array(plaintexts_attack)


ciphertexts_profiling_file = "path_of_text_outT.txt_file"
ciphertexts_profiling = []


print("reading ciphertexts_profiling")
with open(ciphertexts_profiling_file, 'r') as f:
  lines3 = f.readlines()
  #ciphertexts_profiling = np.array(ciphertexts_profiling)
ciphertexts_profiling_txt = [line.strip().split() for line in lines3]
ciphertexts_profiling = [[int(hex_string, 16) for hex_string in row] for row in ciphertexts_profiling_txt]
ciphertexts_profiling = np.array(ciphertexts_profiling)



ciphertexts_attack_file = "path_of_text_outA.txt_file"
ciphertexts_attack = []


print("reading ciphertexts_attack")
with open(ciphertexts_attack_file, 'r') as f:
  lines4 = f.readlines()
  #ciphertexts_attack = np.array(ciphertexts_attack)
ciphertexts_attack_txt = [line.strip().split() for line in lines4]
ciphertexts_attack = [[int(hex_string, 16) for hex_string in row] for row in ciphertexts_attack_txt]
ciphertexts_attack = np.array(ciphertexts_attack)


keys_attack_file = "path_of_RkeysA.txt_file"
keys_attack = []


print("reading keys_attack")
with open(keys_attack_file, 'r') as f:
  lines5 = f.readlines()
  #keys_attack = np.array(keys_attack)
keys_attack_txt = [line.strip().split() for line in lines5]
keys_attack = [[int(hex_string, 16) for hex_string in row] for row in keys_attack_txt]
keys_attack = np.array(keys_attack)

keys_profiling_file = "path_of_RkeysT.txt_file"
keys_profiling = []


print("reading keys_profiling")
with open(keys_profiling_file, 'r') as f:
  lines6 = f.readlines()
  #keys_profiling = np.array(keys_profiling)
keys_profiling_txt = [line.strip().split() for line in lines6]
keys_profiling = [[int(hex_string, 16) for hex_string in row] for row in keys_profiling_txt]
keys_profiling = np.array(keys_profiling) 


""" create dummy profiling traces array with 10000 traces, each one containing 100 samples """
profiling_traces =wavedataT #np.random.rand(10000, 100)

""" create dummy attack traces array with 1000 traces, each one containing 100 samples """
attack_traces = wavedataA   #np.random.rand(1000, 100)


""" create dummy plaintexts, ciphertexts and keys for profiling set: array with 10000 rows x 16 bytes """
#plaintexts_profiling = np.random.randint(0, 256, (10000, 16))
#ciphertexts_profiling = np.random.randint(0, 256, (10000, 16))
#keys_profiling = np.random.randint(0, 256, (10000, 16))
#print(plaintexts_profiling.shape)
""" create dummy plaintexts, ciphertexts and keys for attack set: array with 1000 rows x 16 bytes """
#plaintexts_attack = np.random.randint(0, 256, (1000, 16))
#ciphertexts_attack = np.random.randint(0, 256, (1000, 16))
#keys_attack = np.random.randint(0, 256, (1000, 16))

nb_profiling_traces = len(wavedataT) #10000 
nb_attack_traces = len(wavedataA) #1000
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
