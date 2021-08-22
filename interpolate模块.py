import numpy as np
from  scipy.interpolate import interpld

x = np.array([1,2,3,4,5,8,9,10])   # 创建变量 x
y1 = np.array([2,8,18,32,50,128,162,200])  # 创建变量y1
y2 = np.array([3,5,7,9,11,17,19,21])   # 创建变量 y2

linearinvalue1 = interpld(x,y1,kind = 'linear')   # 线性插值拟合x,y1
linearinvalue2 = interpld(x,y2,kind = 'linear')   # 线性插值拟合x,y2

print(linearinvalue1([6,7]))
print(linearinvalue2([6,7]))

# 拉格朗日插值

from scipy.interpolate import lagrange

lagrangevalue1 = lagrange(x,y1)
lagrangevalue2 = lagrange(x,y2)
print(lagrangevalue1([6,7]))
print(lagrangevalue2([6,7]))

# 养条差值
from scipy.interpolate import splint
splintvalue1 = splint(x,y1,xnew = np.array([6,7]))
splintvalue2 = splint(x,y2,xnew = np.array([6,7]))
print(splintvalue1)
print(splintvalue2)
