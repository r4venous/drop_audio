#!/usr/bin/env python3
"""50 Hz notch filter to remove power-line hum."""
from scipy.signal import iirnotch, lfilter

def apply(data, fs, freq=50.0, Q=30.0):
    b, a = iirnotch(freq / (fs / 2), Q)
    return lfilter(b, a, data)
