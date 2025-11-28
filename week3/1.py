import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
h, w, c = img.shape
print("图像的高度：", h)
print("图像宽度：", w)
print("通道数：", c)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,4))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Gray Image")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.show()

cv2.imwrite("gray_image.jpg", gray)