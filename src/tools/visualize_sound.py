import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

def visualize_sound_and_coherence(sound_file_path):
    try:
        sample_rate, sound_data = wavfile.read(sound_file_path)
        print(f"Loaded sound file: {sound_file_path}")
        
        # Ensure sound_data is 1D (mono or take one channel if stereo)
        if sound_data.ndim > 1:
            sound_data = sound_data[:, 0]  # Take the first channel if stereo

        # Normalize sound data to float between -1 and 1
        sound_data = sound_data / np.max(np.abs(sound_data))

        # Time domain visualization
        time = np.linspace(0, len(sound_data) / sample_rate, num=len(sound_data))
        plt.figure(figsize=(12, 6))
        plt.plot(time, sound_data)
        plt.title('Sound Waveform (Time Domain)')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.savefig('sound_waveform.png')
        plt.close()
        print('Saved sound_waveform.png')

        # Frequency domain (FFT) visualization
        N = len(sound_data)
        yf = np.fft.fft(sound_data)
        xf = np.fft.fftfreq(N, 1 / sample_rate)

        plt.figure(figsize=(12, 6))
        plt.plot(xf[:N//2], 2.0/N * np.abs(yf[0:N//2]))
        plt.title('Sound Spectrum (Frequency Domain)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.savefig('sound_spectrum.png')
        plt.close()
        print('Saved sound_spectrum.png')

        # Phase coherence visualization (simplified)
        phase_data = np.angle(yf)
        
        plt.figure(figsize=(12, 6))
        plt.plot(xf, phase_data)
        plt.title('Phase Data (Frequency Domain)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Phase (radians)')
        plt.grid(True)
        plt.savefig('sound_phase.png')
        plt.close()
        print('Saved sound_phase.png')

        print("Visualizations generated successfully.")

    except FileNotFoundError:
        print(f"Error: Sound file not found at {sound_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sound_file = "golden_ratio_963hz_harmonics.wav"
    visualize_sound_and_coherence(sound_file)


