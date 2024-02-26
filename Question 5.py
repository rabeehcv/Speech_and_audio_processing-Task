import librosa
import matplotlib.pyplot as plt

# Load the speech file
file_path = 'harvard.wav'
audio_data, sampling_rate = librosa.load(file_path)

# Calculate the time array for x-axis
time = librosa.times_like(audio_data, sr=sampling_rate)

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time, audio_data, color='b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Speech Waveform')
plt.grid(True)
plt.show()
