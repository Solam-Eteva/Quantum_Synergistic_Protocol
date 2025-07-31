import numpy as np
import scipy.io.wavfile as wavfile

# Parameters
sample_rate = 44100  # Hz
duration = 60.0  # seconds
base_freq = 963.0  # Hz
golden_ratio = 1.61803398875
mod_freq = base_freq / golden_ratio  # Approx 595 Hz for modulation
harmonic_432 = 432.0
harmonic_528 = 528.0

# Generate time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Create base and modulated sine waves
base_wave = 0.5 * np.sin(2 * np.pi * base_freq * t)
mod_wave = 0.5 * np.sin(2 * np.pi * mod_freq * t)

# Add harmonics
harmonic_432_wave = 0.2 * np.sin(2 * np.pi * harmonic_432 * t)
harmonic_528_wave = 0.2 * np.sin(2 * np.pi * harmonic_528 * t)

# Combine waves (amplitude modulation for base, simple addition for harmonics)
sound = base_wave * (1 + 0.3 * mod_wave) + harmonic_432_wave + harmonic_528_wave

# Normalize to prevent clipping
sound = sound / np.max(np.abs(sound))

# Save as WAV file
wavfile.write("golden_ratio_963hz_harmonics.wav", sample_rate, sound.astype(np.float32))

