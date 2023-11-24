import numpy as np
import matplotlib.pyplot as plt

# Load the wave.data file using the file path
wavedata_file = 'D:/Com_Eng/Sem7/FYP/AISY/AISY_Framework/wf_gii_2014_05_24_151351/wave-normT.data'

# Load the entire wavedata from the file
wavedata = np.fromfile(wavedata_file, dtype=np.float32)
num_samples_per_trace = 1000
num_traces = 80000

# Reshape the wavedata array into a 2D array of shape (num_traces, num_samples_per_trace)
wavedata_reshaped = wavedata.reshape(num_traces, num_samples_per_trace)
power_trace = wavedata_reshaped[0]  # Used for FFT

# Create a time array with a step size of 10
time_step = 10
time = np.arange(0, num_samples_per_trace, time_step)

# Perform FFT on the noisy power trace
fft_result = np.fft.fft(power_trace)
frequencies = np.fft.fftfreq(len(time), d=time_step)  # Calculate frequencies with correct length

# Apply a simple noise reduction by zeroing out high-frequency components
threshold = 0.1  # Adjust this threshold as needed
fft_result[np.abs(frequencies) > threshold] = 0

# Inverse FFT to obtain denoised signal
denoised_signal = np.fft.ifft(fft_result)

# Plot the input and output graphs
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, power_trace[::time_step], label='Noisy Power Trace', color='b')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Input: Noisy Power Trace')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, denoised_signal.real[::time_step], label='Denoised Power Trace', color='g')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Output: Denoised Power Trace')
plt.legend()

plt.tight_layout()
plt.show()
