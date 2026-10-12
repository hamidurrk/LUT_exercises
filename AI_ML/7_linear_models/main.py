import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def conv2d(img, kernel):
    k = kernel.shape[0]
    p = k // 2
    padded = np.pad(img, p, mode="reflect")
    out = np.zeros_like(img, dtype=np.float64)
    kernel = np.flipud(np.fliplr(kernel))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.sum(padded[i:i+k, j:j+k] * kernel)
    return out

def conv_rgb(img, kernel):
    return np.stack([conv2d(img[..., c], kernel) for c in range(3)], axis=-1)

img = np.array(Image.open("butterfly.png").convert("RGB"), dtype=np.float64)  # 256x256x3

f1 = np.array([[-1, -1, -1], [-1, 4, -1], [-1, -1, -1]])
f2 = np.array([[-1,  0, -1], [ 0, 4,  0], [-1,  0, -1]])

r1 = np.clip(np.abs(conv_rgb(img, f1)), 0, 255).astype(np.uint8)
r2 = np.clip(np.abs(conv_rgb(img, f2)), 0, 255).astype(np.uint8)

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
for a, im, t in zip(ax, [img.astype(np.uint8), r1, r2], ["Original", "Filter 1", "Filter 2"]):
    a.imshow(im); a.set_title(t); a.axis("off")
plt.savefig("result.png", dpi=150, bbox_inches="tight")