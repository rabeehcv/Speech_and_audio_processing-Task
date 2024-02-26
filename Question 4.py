import librosa
import soundfile as sf

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
