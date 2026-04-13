#!/usr/bin/env python3
"""Field recording capture utility."""
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import argparse

def record(device, duration, sample_rate=44100):
    print(f"Recording {duration}s from device {device}...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate,
                   channels=1, device=device, dtype='float32')
    sd.wait()
    out = (audio.flatten() * 32767).astype('int16')
    wavfile.write('output.wav', sample_rate, out)
    print("Saved to output.wav")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--device",   type=int, default=0)
    ap.add_argument("--duration", type=float, default=5.0)
    args = ap.parse_args()
    record(args.device, args.duration)
