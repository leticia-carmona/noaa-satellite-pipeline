import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks

# -------- Load audio --------
sample_rate, data = wavfile.read("data/processed/satnogs_audio.wav")

# If stereo, convert to mono
if data.ndim > 1:
    data = data[:, 0]

# Normalize
data = data / np.max(np.abs(data))

# -------- Compute amplitude envelope --------
amplitude = np.abs(data)
times = np.arange(len(amplitude)) / sample_rate

# Save full amplitude
np.savetxt("decoding/cw_amplitude.csv",
           np.column_stack((times, amplitude)),
           delimiter=",",
           header="time,amplitude",
           comments="")

# -------- Detect CW pulses --------
peaks, _ = find_peaks(amplitude, height=0.5, distance=sample_rate * 0.1)

# Save peak times
np.savetxt("decoding/cw_peak_times.csv",
           times[peaks],
           delimiter=",",
           header="peak_time",
           comments="")

print(f"Detected {len(peaks)} CW pulses")

# -------- Plot --------
plt.figure(figsize=(10, 4))
plt.plot(times, amplitude, label="Amplitude")
plt.plot(times[peaks], amplitude[peaks], "rx", label="Detected pulses")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("CW Signal Detection")
plt.tight_layout()
plt.show()
