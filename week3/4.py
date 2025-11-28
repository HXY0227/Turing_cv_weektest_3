import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y1 = x ** 2
y2 = x ** 3
y3 = 2 ** x


plt.figure(figsize=(8, 5))

plt.plot(x, y1, 'r-', label="y = x²")
plt.plot(x, y2, 'b--', label="y = x³")
plt.plot(x, y3, 'g-.', label="y = 2^x")


plt.title("数学函数对比")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.savefig("functions_plot.png", dpi=300)
plt.show()

print("图像已保存为 functions_plot.png")

