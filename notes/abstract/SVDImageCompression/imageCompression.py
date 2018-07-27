"""
compress the MNIST to a smallert image

"""
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import time
from PIL import Image
import pickle, gzip
import numpy as np
from scipy import linalg
from skimage import data 

WORK_DIR = "/home/martin/X-Brain/SVD/"
rowData = WORK_DIR + "mnist.pkl.gz"
storeData = WORK_DIR + "row_mnist.npy"
compress_data = WORK_DIR + "compress.npy"
current_path = WORK_DIR



def toNpy(rowData, storeData):
    """
    transfer the download data to npy data and show it !
    two dimension (index, pic)
    """
    f = gzip.open(rowData, 'rb')
    train_set, valid_set, test_set = pickle.load(f, encoding='iso-8859-1')
    f.close()
    num = np.append(train_set[0], valid_set[0], axis=0)
    num = np.append(num, test_set[0], axis=0)

    ans = np.append(train_set[1], valid_set[1], axis=0)
    ans = np.append(ans, test_set[1], axis=0)

    ans = ans.reshape(ans.shape[0], 1)
    print(num.shape, ans.shape)
    num = np.concatenate((num, ans), axis=1)
    
    np.save(storeData, num)
    

def show_data(npy_data):
    epoch_size = 300
    width = 28
    length = 28
    depth = 1
    input_data = np.load(npy_data)

    num = input_data[0:epoch_size].shape[0] # only 1 ~ 1000 to show
    print(input_data[0:epoch_size, 28 ** 2: 28 ** 2 + 1])
    image = tf.placeholder(tf.float32, [epoch_size, width, length, depth], name = "image")
    tf.summary.image('source_data', image, max_outputs = epoch_size) # 2

    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter(current_path + "showDataRow") # 3
    with tf.Session() as sess:
        for i in range(num // epoch_size):
            data = input_data[i * epoch_size: (i + 1) * epoch_size, 0:width * length]
            data = data.reshape(epoch_size, width, length, depth)
            summary = sess.run(merged, feed_dict = {image:data})
            writer.add_summary(summary, i)
    writer.close()
    



def compress_data(keep_num):
    assert keep_num > 1
    input_data = np.load(storeData)
    pic_num = 10000 # the max is 70000
    
    for i in range(pic_num):
        single_pic = input_data[i][0 : 784].reshape(28 , 28)
        U, s, Vh = linalg.svd(single_pic)
        A = np.dot(U[:, 0:keep_num], np.dot(np.diag(s[0:keep_num]), Vh[0:keep_num, :]))
        input_data[i][0 : 784] = A.reshape(784)

    input_data = input_data[0:pic_num]
    print(input_data.shape)
    np.save(compress_data, input_data)


        


    

def local_toNpy():
    toNpy(rowData, storeData)

def local_show_data():
    show_data(storeData)


if __name__ == "__main__":
    a = np.load(storeData)
    print(a.shape)