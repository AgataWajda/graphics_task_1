from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = "plane.jpg"

try:
    im = Image.open(FILE_NAME)
except FileNotFoundError:
    print(f"BŁĄD: Nie znaleziono pliku '{FILE_NAME}'.")
    exit()

new_width = im.width // 2
new_height = im.height // 2
new_im = im.resize((new_width, new_height))
new_im = new_im.convert("L")
new_im = new_im.transpose(Image.Transpose.ROTATE_90)

matrix_origin = np.array(im)
matrix_new = np.array(new_im)

dpi = 100  
fig = plt.figure(figsize=(
    (im.width + new_im.width) / dpi,
    max(im.height, new_im.height) / dpi
))

ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(im, interpolation="nearest")
ax1.set_title("Oryginał")
ax1.axis("on")

ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(new_im, cmap="gray", interpolation="nearest")
ax2.set_title("Po przetwarzaniu")
ax2.axis("on")

plt.tight_layout()
plt.show()

print("\nMacierz oryginalna:")
print(matrix_origin)
print("Wymiary:", matrix_origin.shape)

print("\nMacierz po przetwarzaniu:")
print(matrix_new)
print("Wymiary:", matrix_new.shape)

