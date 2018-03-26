from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

"""
展示图片
"""
def show(f):
    plt.imshow(f, cmap = "gray")
    plt.show()
# 存储pictures
pic_dir = "/home/martin/AllWorkStation/Atom/notes/SciNotes/material/a.jpg"
pic_dir_base =  "/home/martin/AllWorkStation/Atom/notes/SciNotes/material/"
# misc.imsave(pic_dir, f) # uses the Image module (PIL)

f = misc.face()
f.dtype
f.shape

f.tofile(pic_dir)
f =  np.fromfile(pic_dir, dtype = "uint8") # 默认的数值类型为 float64, 必须设置为 unit8, 控制分割byte的方法
f.shape
f.dtype
f.shape = (768, 1024, 3)

# 对大型的文件, 使用文件映射系统
f = np.memmap(pic_dir, dtype = np.uint8, shape = (768, 1024, 3))

# 顺便知道 glob 的使用
for i in range(10):
    im = np.random.randint(0, 100, 10000).reshape((100, 100))
    misc.imsave(pic_dir_base + "random{0}.jpg".format(i), im)

from glob import glob
file_list = glob(pic_dir_base + "random*")

# :star: face函数的参数不是很理解
f = misc.face(gray=True)
plt.imshow(f, cmap=plt.cm.gray)
plt.show()
plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.show()

# :star: 不知道为什么图片是 反 的
plt.contour(f, [100,200])
plt.show()

plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray)
plt.show()
plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='nearest')
plt.show()

"""
操作图片
"""
face = misc.face(gray=True)
type(face)
X, Y = face.shape
x, y = np.ogrid[0:X, 0:Y]
x.shape
y.shape
f[0:400,0:100] = 255



# 任何numpy格式数组都是可以实现的,
# 加载过来的 picture 的类型 numpy.ndarray
a = np.random.randint(0, 100, size = [100])
a.mean()
a.min()

face = misc.face(gray=True)
lx, ly = face.shape
# Cropping
crop_face = face[lx // 4: - lx // 4, ly // 4: - ly // 4]
show(crop_face)
# up <-> down flip
flip_ud_face = np.flipud(face)
show(flip_ud_face)
# rotation
from scipy import ndimage
rotate_face = ndimage.rotate(face, 45)
show(rotate_face)

rotate_face_noreshape = ndimage.rotate(face, 45, reshape=False)
show(rotate_face_noreshape)


# 改变图片的清晰度 使用Gaussian 或者 各种filter 的方法
f = misc.face(gray=True)
blurr_face = ndimage.gaussian_filter(f, sigma = 12) # sigma 越大, 其越模糊
show(blurr_face)

blurr_face = ndimage.uniform_filter(f, size = 11)
show(blurr_face)

blurr_face = ndimage.median_filter(f, 20)
show(blurr_face)

# sharpen 的原理 :star: 除非清除 gaussian_filter 的
im = np.zeros((20, 20))
im[5:-5, 5:-5] = 1
show(im)
im = ndimage.distance_transform_bf(im)
show(im)

im_noise = im + 0.2 * np.random.randn(*im.shape)


im_med = ndimage.median_filter(im_noise, 4)
show(im_med)


a = ndimage.generate_binary_structure(2, 1)
a.shape
a.astype(np.int)
show(a)


np.random.seed(2)
im = np.zeros((64, 64))
x, y = (63*np.random.random((2, 8))).astype(np.int)
im[x, y] = np.arange(8)
show(im)
bigger_points = ndimage.grey_dilation(im, size=(5, 5), structure=np.ones((5, 5)))
square = np.zeros((16, 16))
square[4:-4, 4:-4] = 1
dist = ndimage.distance_transform_bf(square)
dilate_dist = ndimage.grey_dilation(dist, size=(3, 3), \
structure=np.ones((3, 3)))


"""
:star: 含有一些特征提取的函数, 目前用不上, 择日再看
"""
