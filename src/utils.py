#!/usr/bin/env python3
"""Shared audio utilities."""
import numpy as np
from scipy.io import wavfile

def load_mono(path):
    sr, data = wavfile.read(path)
    if data.ndim > 1:
        data = data[:, 0]
    return sr, data.astype(np.float32)

def rms(signal):
    return np.sqrt(np.mean(signal ** 2))

def normalize(signal):
    peak = np.max(np.abs(signal))
    return signal / peak if peak > 0 else signal
