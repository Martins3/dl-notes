"""
nothing
"""
"""
scp -r -P 43722 zhangmengxiao@115.156.226.252:/home/zhangmengxiao/hubachelar/data/show_data2   /home/martin/X-Brain/abstraction/tian     
"""
import numpy as np
a = np.arange(12).reshape(6, 2)
s = np.copy(a[1],)
print(a)
for i in range(5):
    print(s)
    np.random.shuffle(a)