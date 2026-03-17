import librosa
import numpy as np
import matplotlib.pyplot as plt

sr = 44100
t = np.linspace(0, 1, sr)
y = 0.5 * np.sin(2 * np.pi * 5000 * t)

y_sub = y[::10]
sr_sub = sr // 10
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
D_orig = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(D_orig, sr=sr, x_axis='time', y_axis='hz')
plt.title("Spectrogramme Original (Haute Fidélité)")
plt.subplot(2, 1, 2)
D_sub = librosa.amplitude_to_db(np.abs(librosa.stft(y_sub)), ref=np.max)
librosa.display.specshow(D_sub, sr=sr_sub, x_axis='time', y_axis='hz')
plt.title("Spectrogramme Sous-échantillonné (Repliement/Aliasing)")

plt.tight_layout()
plt.show()
