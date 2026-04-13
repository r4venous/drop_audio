#!/usr/bin/env python3
"""Basic DTMF presence detector (not a decoder)."""
import numpy as np
from scipy.io import wavfile

ROW_FREQS = [697, 770, 852, 941]
COL_FREQS = [1209, 1336, 1477, 1633]

def has_dtmf(frame, sr, threshold=0.15):
    freqs = np.fft.rfftfreq(len(frame), 1 / sr)
    fft   = np.abs(np.fft.rfft(frame))
    fft  /= (fft.max() + 1e-9)
    row_e = max(fft[np.argmin(np.abs(freqs - f))] for f in ROW_FREQS)
    col_e = max(fft[np.argmin(np.abs(freqs - f))] for f in COL_FREQS)
    return row_e > threshold and col_e > threshold

if __name__ == "__main__":
    import sys
    sr, data = wavfile.read(sys.argv[1])
    if data.ndim > 1: data = data[:,0]
    hits = 0
    step = int(0.1 * sr)
    for i in range(0, len(data) - step, step):
        if has_dtmf(data[i:i+step].astype(float), sr):
            hits += 1
    print(f"DTMF activity detected in {hits} frames")
