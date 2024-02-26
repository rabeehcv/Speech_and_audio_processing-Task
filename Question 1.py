import soundfile as sf


def read_speech_file(filename):
    data, samplerate = sf.read(filename)
    return data, samplerate


filename = 'harvard.wav'

samples, samplerate = read_speech_file(filename)

print(samples)
print(samplerate)
