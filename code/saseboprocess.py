#### SASEBO Process

import numpy as np;
import array
import struct

##USER parameters

#numsamples
numsamples = 6000
#numTrain
numtrain   = 600000
#numTotal
numtotal  = 1000000

##numattack = numtotal-numtrain

#resample = x times of numsamples
# if you dont want resample, set this value to 1
# we do resample because these traces have very large number of sample points
resample = 12

####TODO: range

## folder
folder = "clk3-4steps-wf_gii_2018_12_14_065205"



## PROGRAM Parameters: filenames
INFILE   = "text_in.txt"
OUTFILE  = "text_out.txt"
WAVEFILE = "wave.data"
KEYFILE  = "key.txt"
WRITEFOLDER   = "ML"+folder

## read text in
plaintext = []

plaintext_file = folder+"/"+INFILE
train_plaintext_file = "text_inT.txt"
attack_plaintext_file ="text_inA.txt"

print("reading Plaintext")
with open(plaintext_file, 'r') as f:
  plaintext = f.readlines()

### write to files and folders
with open(train_plaintext_file, 'w') as f:
    for i in range(numtrain):
        f.write(plaintext[i])
           
with open(attack_plaintext_file, 'w') as f:
    for i in range(numtrain, numtotal):
        f.write(plaintext[i])
        
##################################################
## read text out
ciphertext = []

ciphertext_file = folder+"/"+OUTFILE
train_ciphertext_file = "text_outT.txt"
attack_ciphertext_file ="text_outA.txt"

train_ciphertext_file_dacimal = "text_outT_decimal.txt"
attack_ciphertext_file_decimal ="text_outA_decimal.txt"

print("reading Ciphertext")
with open(ciphertext_file, 'r') as f:
  ciphertext = f.readlines()
  
### write to files and folders
with open(train_ciphertext_file, 'w') as f:
    for i in range(numtrain):
        f.write(ciphertext[i])
            
with open(attack_ciphertext_file, 'w') as f:
    for i in range(numtrain, numtotal):
        f.write(ciphertext[i])

## read key file
secretkey = []

secretkey_file = folder+"/"+KEYFILE
train_key_file = "RkeysT.txt"
attack_key_file ="RkeysA.txt"

train_key_file_decimal = "RkeysT_decimal.txt"
attack_key_file_decimal ="RkeysA_decimal.txt"

print("reading Secretkey")
with open(secretkey_file, 'r') as f:
  secretkey = f.readlines()
  
### write to files and folders // to do : detect length and if keys and multiple keys then process
with open(train_key_file, 'w') as f:
    for i in range(numtrain):
        f.write(secretkey[0])
            
with open(attack_key_file, 'w') as f:
    for i in range(numtrain, numtotal):
        f.write(secretkey[0])

###############3333
## wave files

wavedata_file = folder+"/"+WAVEFILE

wavedata = []

## read wave file
print("reading Wavefile")  
f = open(wavedata_file, 'rb')

while(True):
  data = array.array('f')
  try:
    data.fromfile(f, numsamples)
  except EOFError:
    break
  wavedata.append(data)

wavedata = np.array(wavedata)

print(wavedata.shape)


## sample to new array
distance = int(numsamples/resample)

wavesampleddata = [[0 for x in range(distance)] for y in range(numtotal)]

for i in range(numtotal):
    for j in range(distance):
        wavesampleddata[i][j] = wavedata[i][resample*j]

print(distance)

## write train and attack        

output_file = open('wave-normT.data', 'wb')

for j in range(numtrain):
    float_array = wavesampleddata[j] #array('d', [3.14, 2.7, 0.0, -1.0, 1.1])
    for i in range(len(float_array)):
        output_file.write(struct.pack('<f', float_array[i]))

#float_array.tofile(output_file)
output_file.close()


output_file = open('wave-normA.data', 'wb')

for j in range(numtrain, numtotal):
    float_array = wavesampleddata[j] #array('d', [3.14, 2.7, 0.0, -1.0, 1.1])
    for i in range(len(float_array)):
        output_file.write(struct.pack('<f', float_array[i]))

#float_array.tofile(output_file)
output_file.close()


        

