import soundfile as sf
import numpy as np
import subprocess


def read_speech_file(filename):
    data, samplerate = sf.read(filename)
    return data, samplerate


filename = 'harvard.wav'
samples, samplerate = read_speech_file(filename)

# Converting stereo audio data to mono by averaging the left and right channels
mono_samples = np.mean(samples, axis=1)

# Save the mono audio data to a temporary WAV file
temp_file = 'temp_audio.wav'
sf.write(temp_file, mono_samples, samplerate)

# Use subprocess to call an external audio player to play the audio file
subprocess.run(['start', temp_file], shell=True, check=True)
