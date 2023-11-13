import numpy as np
import matplotlib.pyplot as plt
import struct

# Load the wave.data file using the file path
wavedata_file = 'D:/Com_Eng/Sem7/FYP/AISY/AISY_Framework/attack_power_traces/wave-normT.data'

# Load the entire wavedata from the file
wavedata = np.fromfile(wavedata_file, dtype=np.float32)
print(wavedata.shape)
num_samples_per_trace = 600
num_traces = 600000

# Reshape the wavedata array into a 2D array of shape (num_traces, num_samples_per_trace)
wavedata_reshaped = wavedata.reshape(num_traces, num_samples_per_trace)

# Create an array to store denoised traces
denoised_traces = []

# Create a time array with a step size of 1
time_step = 1
time = np.arange(0, num_samples_per_trace * time_step, time_step)  # Adjusted time array

# Iterate through each power trace
for power_trace in wavedata_reshaped:
    # Perform FFT on the noisy power trace
    fft_result = np.fft.fft(power_trace)
    
    # Calculate frequencies based on the time array
    frequencies = np.fft.fftfreq(num_samples_per_trace, d=time_step)  # Adjusted frequencies array

    # Apply a simple noise reduction by zeroing out high-frequency components
    threshold = 0.3  # Adjust this threshold as needed
    fft_result[np.abs(frequencies) > threshold] = 0

    # Inverse FFT to obtain denoised signal
    denoised_signal = np.fft.ifft(fft_result)

    # Append the denoised trace to the denoised_traces array
    denoised_traces.append(denoised_signal.real)

# Convert the denoised_traces list into a NumPy array
denoised_traces = np.array(denoised_traces)


# breakpoint()
print(denoised_traces)
# Plot all denoised traces
plt.figure(figsize=(12, 6))

plt.plot(time, denoised_traces[-1], label='Denoised Power Trace', color='g')

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Denoised Power Traces')
plt.legend()

plt.tight_layout()
plt.show()


# Specify the file path where you want to save the denoised traces as a .data file
save_file_path = 'wave-normT.data'

# Open the file for binary writing
with open(save_file_path, 'wb') as file:
    # Iterate through each denoised trace and write it to the file
    for trace in denoised_traces:
        # Assuming that each element of the denoised trace is a float
        float_array = trace.tolist()
        for value in float_array:
            # Pack and write each float value as binary data
            file.write(struct.pack('<f', value))

