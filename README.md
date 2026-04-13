# drop_audio

Field recording tools and audio signal processing experiments.

## Structure

| Folder | Description |
|--------|-------------|
| `src/` | Core signal processing modules |
| `filters/` | DSP filter implementations |
| `analysis/` | Frequency analysis scripts |
| `samples/` | Raw and processed audio samples |
| `docs/` | Technical notes and references |
| `config/` | Runtime parameters and tuning values |

## Requirements

```
pip install numpy scipy matplotlib
```

## Usage

```bash
python src/record.py --device 0 --duration 10
python analysis/spectrum.py --input samples/raw/field_001.wav
```
