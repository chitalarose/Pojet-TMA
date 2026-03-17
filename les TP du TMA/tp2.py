import numpy as np
import matplotlib.pyplot as plt

fs = 44100
duree = 0.5
t = np.arange(0, duree, 1/fs)
f1, f2 = 440, 880

signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

n = len(signal)

spectre = np.fft.fft(signal)
module_spectre = np.abs(spectre) * 2 / n
frequences = np.fft.fftfreq(n, 1/fs)
indices_positifs = np.where(frequences >= 0)

f_plot = frequences[indices_positifs]
m_plot = module_spectre[indices_positifs]


plt.figure(figsize=(10, 5))
plt.plot(f_plot, m_plot)
plt.title("Spectre du signal (FFT)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 1200)
plt.grid(True)
plt.show()


f_bruit = 5000
bruit_hf = 0.2 * np.sin(2 * np.pi * f_bruit * t)
signal_bruite = signal + bruit_hf

spectre_bruite = np.fft.fft(signal_bruite)
spectre_filtre = spectre_bruite.copy()

for i, f in enumerate(frequences):
    if 4800 <= abs(f) <= 5200:
        spectre_filtre[i] = 0

signal_nettoye = np.fft.ifft(spectre_filtre).real

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(f_plot, (np.abs(spectre_bruite) * 2 / n)[indices_positifs])
plt.title("Spectre Bruité (Pic visible à 5000 Hz)")
plt.xlim(0, 6000)

plt.subplot(2, 1, 2)
plt.plot(f_plot, (np.abs(spectre_filtre) * 2 / n)[indices_positifs])
plt.title("Spectre Filtré (Pic supprimé)")
plt.xlim(0, 6000)

plt.tight_layout()
plt.show()