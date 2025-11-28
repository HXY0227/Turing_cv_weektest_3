import numpy as np

arr = np.arange(1, 26).reshape(5, 5)


print("原始 5x5 数组：")
print(arr)

row2 = arr[1, :]
print("第 2 行所有元素：")
print(row2)

col3 = arr[:, 2]
print("第 3 列所有元素：")
print(col3)


sub_2x2 = arr[3:5, 3:5]
print("右下角 2x2 子数组：")
print(sub_2x2)


print("整个数组的总和：", arr.sum())
print("每一行的和：", arr.sum(axis=1))
print("每一列的和：", arr.sum(axis=0))
print("数组均值：", arr.mean())
print("数组标准差：", arr.std())

print("转置后的数组：")
print(arr.T)
