import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("image2.jpg")

scaled = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

(h, w) = img.shape[:2]
center = (w // 2, h // 2)

angle = 45
scale = 1.0

M = cv2.getRotationMatrix2D(center, angle, scale)

abs_cos = abs(M[0, 0])
abs_sin = abs(M[0, 1])
new_w = int(h * abs_sin + w * abs_cos)
new_h = int(h * abs_cos + w * abs_sin)

M[0, 2] += (new_w / 2) - center[0]
M[1, 2] += (new_h / 2) - center[1]

rotated = cv2.warpAffine(img, M, (new_w, new_h),
                         borderValue=(255, 255, 255))

flipped = cv2.flip(img, 1)
plt.figure(figsize=(10, 10))

def show(title, image, position):
    plt.subplot(2, 2, position)
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

show("Original", img, 1)
show("Scaled 50%", scaled, 2)
show("Rotated 45°", rotated, 3)
show("Flipped Horizontal", flipped, 4)

plt.tight_layout()
plt.show()

cv2.imwrite("rotated_image.jpg", rotated)
