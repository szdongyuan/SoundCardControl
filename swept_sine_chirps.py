import numpy as np


class SineChirps(object):

    @staticmethod
    def join_chirps():
        pass

    @staticmethod
    def log_sine_chirps(f_begin=80, f_end=2000, t_total=2, sr=48000,
                        chirp_type="log", mode="reverse_mirror"):
        pi = np.pi
        x_t = np.array(list(range(int(sr * t_total)))) / sr
        if chirp_type == "log":
            ln = np.log(f_end / f_begin)
            y_t = np.sin(2 * pi * f_begin * t_total / ln * (np.exp(ln * x_t / t_total) - 1))
        else:
            delta_f = f_end - f_begin
            y_t = np.sin(2 * pi * (0.5 * delta_f / t_total * x_t ** 2 + f_begin * x_t))
        if mode == "reverse_mirror":
            y_t2 = np.array(list(y_t)[::-1] + list(-y_t))
            return y_t2, sr
        elif mode == "mirror":
            y_t2 = np.array(list(y_t) + list(-y_t)[::-1])
            return y_t2, sr
        elif mode == "reverse":
            return y_t[::-1], sr
        else:
            return y_t, sr
