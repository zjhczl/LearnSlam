# 矩阵的基本运算
import numpy as np

A = np.array([1, 2, 3])
# 参数还可以是一个已有的list类型
list_b = [1, 2, 3]
B = np.array(list_b)
C = np.array([[1, 2, 3], [2, 3, 4]])

M33 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(M33)

# 转置
print(M33.T)
# 各元素和
# 迹

# 数乘
# 逆
# 行列式
# 矩阵和向量相乘
print(np.dot(M33, np.array([1, 2, 3]).T))
# 特征值
