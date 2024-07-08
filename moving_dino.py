import librosa
import numpy as np


def object_based_coefficient(x, y, speaker_loc, d):
    a = np.array([[1 / (x_s**2 + (y_s - d)**2) for (x_s, y_s) in speaker_loc],
                  [1 / ((x_s - d)**2 + y_s**2) for (x_s, y_s) in speaker_loc],
                  [1 / (x_s**2 + (y_s + d)**2) for (x_s, y_s) in speaker_loc],
                  [1 / ((x_s + d)**2 + y_s**2) for (x_s, y_s) in speaker_loc]])
    b = np.array([1 / (x**2 + (y - d)**2),
                  1 / ((x - d)**2 + y**2),
                  1 / (x**2 + (y + d)**2),
                  1 / ((x + d)**2 + y**2)])
    return np.linalg.solve(a, b)


dino_data, dino_sr = librosa.load("dino_combined.wav")

speaker_loc = [[0, 4], [4, 0], [0, -4], [-4, 0]]
d = 0.05
x = (np.array(list(range(len(dino_data)))) / len(dino_data) - 0.5) * 32
y = np.array([4] * len(dino_data))
moving_dino_data_fb = []
moving_dino_data_lr = []
for i in range(len(dino_data)):
    coff_f, coff_r, coff_b, coff_l = object_based_coefficient(x[i], y[i], speaker_loc, d)
    moving_dino_data_fb.append([coff_f * dino_data[i], coff_b * dino_data[i]])
    moving_dino_data_lr.append([coff_r * dino_data[i], coff_l * dino_data[i]])
moving_dino_data_fb = np.array(moving_dino_data_fb)
moving_dino_data_lr = np.array(moving_dino_data_lr)
