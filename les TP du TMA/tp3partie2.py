import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color, transform

image = data.camera()
img_2bit = np.round(image / (256/4)) * (256/4)
img_1bit = np.round(image / (256/2)) * (256/2)

h, w = image.shape
img_low_res = transform.resize(image, (h//8, w//8), anti_aliasing=True)
img_pixel = transform.resize(img_low_res, (h, w), order=0)

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1); plt.imshow(image, cmap='gray'); plt.title("Original (8 bits)")
plt.subplot(2, 2, 2); plt.imshow(img_2bit, cmap='gray'); plt.title("Quantifiée (2 bits - 4 niveaux)")
plt.subplot(2, 2, 3); plt.imshow(img_1bit, cmap='gray'); plt.title("Quantifiée (1 bit - Binaire)")
plt.subplot(2, 2, 4); plt.imshow(img_pixel, cmap='gray'); plt.title("Pixelisation (Résolution / 8)")
plt.show()