 # 也算是见识了import 的厉害
import numpy as np
import matplotlib.pyplot as plt

material_dir = "/home/martin/AllWorkStation/Atom/notes/SciNotes/material"

"""
1. File input output
"""
# matlab data  image data
import scipy.misc
scipy.misc.imread(material_dir + "/a.jpg")

"""
2. Special functions
"""
# 很尴尬, 这些函数都是没有学过的

"""
3. Linear algebra operations
"""
# 不知道和 numpy 有什么区别

"""
4. Fast Fourier transforms
"""
# 傅里叶变换早就忘记了, 回顾需要时间 :star:

"""
5. Optimization and fit
"""
from scipy import optimize
def d(x):
    return x ** 2 + 10 * np.sin(x)

x = np.arange(-10, 10, 0.1)
plt.plot(x, d(x))
plt.show()
optimize.fmin_bfgs(d, 7)

# 还有等等有意思的事情 :star:

"""
Statistics and random numbers
"""
from scipy import  stats
a = np.random.normal(size = 1000)

bins = np.arange(-4, 5)
histogram = np.histogram(a, bins=bins, density = True)[0]

bins = (bins[1:] + bins[:-1]) / 2
b = stats.norm.pdf(bins)

plt.plot(bins, histogram)
plt.plot(bins, b)
plt.show()

# 拟合曲线
loc, std = stats.norm.fit(a)
loc
std

# 计算中位数 和 一般的位置参数
stats.scoreatpercentile(a, 90)
np.median(a)
stats.scoreatpercentile(a, 50)

# https://en.wikipedia.org/wiki/Student%27s_t-test :star: student t-test
a = np.random.normal(0, 1, size = 100)
b = np.random.normal(0, 1, size = 100)
stats.ttest_ind(a, b)

# 插入数值
from scipy import interpolate
measured_time = np.linspace(0, 1, 10)
noise = (np.random.random(10) * 2 - 1) * 1e-1
measures = np.sin(2 * np.pi * measured_time) + noise

inter_build_funciton = interpolate.interp1d(measured_time, measures)
whole_nums = np.linspace(0, 1, 50)
compeled_data = inter_build_funciton(whole_nums)

inter_build_funciton_cu = interpolate.interp1d(measured_time, measures, kind = "cubic")
compeled_data_cu = inter_build_funciton_cu(whole_nums)

plt.plot(whole_nums, compeled_data)
plt.plot(measured_time, measures)
plt.plot(whole_nums, compeled_data_cu)
plt.show()

"""
积分 :star:
"""
# 应该很有意思的

"""
Signal processing :star: 专业范畴之外, 可以获取灵感
"""
