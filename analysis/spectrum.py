#!/usr/bin/env python3
"""Spectrogram viewer."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram
import argparse

def plot(path):
    sr, data = wavfile.read(path)
    if data.ndim > 1:
        data = data[:, 0]
    f, t, Sxx = spectrogram(data.astype(float), sr, nperseg=1024)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx + 1e-10), shading='gouraud')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.colorbar(label='dB')
    plt.ylim(0, 4000)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    plot(args := ap.parse_args(), args.input)
