from scipy.io import wavfile
import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundcard as sc

from swept_sine_chirps import SineChirps

speakers = sc.all_speakers()
print(speakers)
default_speaker = sc.default_speaker()
print(default_speaker)
mics = sc.all_microphones()
print(mics)
default_mic = sc.default_microphone()
print(default_mic)

# data = default_mic.record(samplerate=48000, numframes=48000)
# default_speaker.play(data / np.max(data), samplerate=48000)
#
#
# with default_mic.recorder(samplerate=48000) as mic, \
#         default_speaker.player(samplerate=48000) as sp:
#     for _ in range(10):
#         data = mic.record(numframes=10240)
#         sp.play(data)
#
# default_mic = sc.default_microphone()
#
# one_mic = sc.get_microphone('线路输入')
#
# data = one_mic.record(samplerate=48000, numframes=1024)
# plt.plot(data)
# plt.xlabel("Samples")
# plt.ylabel("Values")
# plt.grid(True)
# plt.tight_layout()
# plt.savefig("test.png")
#
#
# data, sr = SineChirps().log_sine_chirps(80, 2000)
# default_speaker.play(data / 2, samplerate=sr)


def rot_fac(t_tot, cycles=1, phase=0, sr=48000):
    t = np.array(list(range(int(t_tot * sr)))) / sr
    fac = 1 + np.sin(2 * np.pi * t * cycles / t_tot + phase)
    return fac


T = 10
n_rot = 2
data, sr = SineChirps().log_sine_chirps(80, 2000, t_total=T // 2)

data_lf = data * rot_fac(T, n_rot, 0.0 * np.pi, sr)
data_lb = data * rot_fac(T, n_rot, 0.5 * np.pi, sr)
data_rb = data * rot_fac(T, n_rot, 1.0 * np.pi, sr)
data_rf = data * rot_fac(T, n_rot, 1.5 * np.pi, sr)
data_combined_2 = np.array([data_lf, data_rb]).T
data_combined_4 = np.array([data_lf, data_lb, data_rb, data_rf]).T
#
# save wav file
wavfile.write("test.wav", sr, data_combined_2)
