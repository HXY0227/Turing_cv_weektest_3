import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("traffic.jpg")
if image is None:
    raise FileNotFoundError("未找到 traffic.jpg，请确认图片路径")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imwrite("gray.jpg", gray)
cv2.imwrite("blur.jpg", blur)


edges = cv2.Canny(blur, 50, 150)

kernel = np.ones((5, 5), np.uint8)

edges_close = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

edges_open = cv2.morphologyEx(edges_close, cv2.MORPH_OPEN, kernel)



contours, _ = cv2.findContours(
    edges_open, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

vehicle_contours = []
areas = []

output = image.copy()

vehicle_id = 0


for cnt in contours:
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio = w / h if h > 0 else 0


    if area > 800 and 0.5 < aspect_ratio < 3.0:
        vehicle_contours.append(cnt)
        areas.append(area)

vehicle_count = len(vehicle_contours)

areas_np = np.array(areas)

area_mean = np.mean(areas_np)
area_std = np.std(areas_np)
area_min = np.min(areas_np)
area_max = np.max(areas_np)

small_count = 0
large_count = 0

for cnt in vehicle_contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)

    vehicle_id += 1


    if area < area_mean:
        color = (0, 255, 0)
        label = f"Car {vehicle_id} (S)"
        small_count += 1
    else:
        color = (0, 0, 255)
        label = f"Car {vehicle_id} (L)"
        large_count += 1

    cv2.rectangle(output, (x, y), (x + w, y + h), color, 2)
    cv2.putText(
        output, label, (x, y - 5),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1
    )


h, w, _ = image.shape
image_area = h * w
vehicle_density = vehicle_count / image_area


plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Traffic Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edge Detection")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title(f"Vehicle Detection (Total: {vehicle_count})")
plt.axis("off")


plt.subplot(2, 2, 4)
plt.hist(areas_np, bins=10)
plt.title("Vehicle Area Distribution")
plt.xlabel("Area")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("traffic_analysis_report.png", dpi=300)


cv2.imwrite("traffic_detected.jpg", output)


print("====== 交通流量分析报告 ======")
print(f"车辆总数: {vehicle_count}")
print(f"小型车数量: {small_count} ({small_count / vehicle_count:.2%})")
print(f"大型车数量: {large_count} ({large_count / vehicle_count:.2%})")
print(f"车辆面积 - 最小值: {area_min:.2f}")
print(f"车辆面积 - 最大值: {area_max:.2f}")
print(f"车辆面积 - 平均值: {area_mean:.2f}")
print(f"车辆面积 - 标准差: {area_std:.2f}")
print(f"道路车辆密度: {vehicle_density:.8f}")

if vehicle_density > 0.00002:
    print("拥堵评估: 道路存在明显拥堵")
else:
    print("拥堵评估: 当前道路通行较为顺畅")










