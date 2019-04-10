import numpy as np

def fft(img):
    fft = np.fft.fft(img, axis=1)
    fabs = np.real(fft * np.conjugate(fft))
    return np.mean(fabs, axis=0)
