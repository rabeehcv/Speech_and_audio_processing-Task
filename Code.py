import soundfile as sf
import numpy as np
import subprocess
import pyaudio
import wave
import librosa
import matplotlib.pyplot as plt


def read_speech_file(filename):
    data, samplerate = sf.read(filename)
    return data, samplerate


# Task 1 Read a speech file
filename = 'harvard.wav'

samples, samplerate = read_speech_file(filename)

print(samples)
print(samplerate)

# Task 2 Play an array of speech samples as an audio file
# Converting stereo audio data to mono by averaging the left and right channels
mono_samples = np.mean(samples, axis=1)

# Save the mono audio data to a temporary WAV file
temp_file = 'temp_audio.wav'
sf.write(temp_file, mono_samples, samplerate)

# Use subprocess to call an external audio player to play the audio file
subprocess.run(['start', temp_file], shell=True, check=True)

# Task 3 Record a speech file
# Set parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream for recording
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record audio in chunks
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording complete.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

# Task 4 Convert the sampling rate associted with a speech file to a different sampling rate
# Specify file paths
input_file = 'harvard.wav'
output_file = 'output4.wav'

# Specify the target sampling rate
target_sampling_rate = 16000  # Example: 16 kHz

# Read the speech file and resample to the target sampling rate
audio_data, current_sampling_rate = librosa.load(
    input_file, sr=target_sampling_rate)

# Save the resampled audio data to a new file using soundfile
sf.write(output_file, audio_data, target_sampling_rate)

# Task 5 Plot a speech file as a waveform.
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
