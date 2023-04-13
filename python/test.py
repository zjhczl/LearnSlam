# 矩阵的基本运算
import numpy as np
from scipy import linalg
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
# 矩阵和向量相乘
print(np.dot(M33, np.array([1, 2, 3]).T))
# 特征值

# 方程组求解
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])  # 系数矩阵
b = np.array([2, 4, -1])  # 结果
print(linalg.solve(a, b))

# 求解行列式
print("------------行列式------------")
A = np.array([[1, 2], [3, 4]])
x = linalg.det(A)
print(x)

# 求特征值和特征向量
# https://blog.csdn.net/webor2006/article/details/120909642
print("------------特征值和特征向量------------")
A = np.array([[1, 2], [3, 4]])

# Passing the values to the eig function
l, v = linalg.eig(A)

# printing the result for eigen values
print(l)

# printing the result for eigen vectors
print(v)
# 奇异值分解
# 奇异值分解(SVD)可以被认为是特征值问题扩展到非矩阵的矩阵。
# scipy.linalg.svd将矩阵'a'分解为两个酉矩阵'U'和'Vh'，以及一个奇异值(实数，非负)的一维数组's'，使得a == U * S * Vh，其中'S'是具有主对角线's'的适当形状的零点矩阵。
# 让我们来看看下面的例子。
print("-------------奇异值分解--------------")
# Declaring the numpy array
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)

# Passing the values to the eig function
U, s, Vh = linalg.svd(a)

# printing the result
print(U, Vh, s)
