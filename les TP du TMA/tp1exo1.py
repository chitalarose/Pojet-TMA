import numpy as np
import matplotlib.pyplot as plt

f0 = 10
A = 1
phi = 0
fs = 100
duree = 1

t = np.arange(0, duree, 1/fs)
x = A * np.sin(2 * np.pi * f0 * t + phi)

plt.figure()
plt.plot(t, x)
plt.title("Signal sinusoïdal")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.show()

bruit = np.random.normal(0, 0.3, len(x))
y = x + bruit

plt.figure(figsize=(10, 5))
plt.plot(t, x, label="Signal pur x(t)", linewidth=2, color='blue')
plt.plot(t, y, label="Signal bruité y(t)", alpha=0.7, color='orange')
plt.title("Comparaison : Signal Pur vs Signal Bruité")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()


porte = np.zeros(100)
porte[20:41] = 1
convolution_resultat = np.convolve(porte, porte, mode='same')

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.stem(porte)
plt.title("Signal Porte (Rect)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(convolution_resultat)
plt.title("Résultat de la Convolution (Forme Triangulaire)")
plt.grid(True)

plt.tight_layout()
plt.show()