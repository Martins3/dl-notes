import skimage
import numpy as np
import matplotlib.pyplot as plt
def show(picture):
    plt.imshow(picture, cmap= "gray")
    plt.show()


check = np.zeros((9, 9))
check[::2, 1::2] = 1
check[1::2, ::2] = 1
plt.imshow(check, cmap='gray')
plt.show()
