# -*- coding: utf-8 -*-
import math
import featureDrpout as fd
import tensorflow as tf
import numpy as np
def distance_to_segment_line(target, p1, p2):
    """
    Attributes: target 目标数字 p1 p2 端点
    用于计算 点到线段的距离
    """
    x1 , y1, x2, y2, x, y = float(p1[0]),float(p1[1]), \
    float(p2[0]), float(p2[1]), float(target[0]), float(target[1])

    cross = (x2 - x1) * (x - x1) + (y2 - y1) * (y - y1)
    if (cross <= 0):
        return math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))

    d2 = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
    if (cross >= d2):
        return math.sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2))

    r = cross / d2;
    px = x1 + (x2 - x1) * r
    py = y1 + (y2 - y1) * r
    return math.sqrt((x - px) * (x - px) + (py - y) * (py - y))

def collison_five_circle(target, candidates):
    if(not candidates):
        candidates.append(target)
        return candidates
    else:
        for candi in candidates:
            if(abs(target[0] - candi[0]) + abs(target[1] - candi[1]) <= 3):
                return candidates
        candidates.append(target)
        return candidates


def dataset_validation():
    """
    生产的数据的确是没有问题的
    """
    polygon_data = np.load(dd.five_star)

    image = tf.placeholder(tf.float32, [100, 60, 60, 1], name = "image")
    tf.summary.image('images', image, max_outputs = 100)



    merged = tf.summary.merge_all()
    dd.clear(dd.show_data2)
    writer = tf.summary.FileWriter(dd.show_data2)

    with tf.Session() as sess:
        for i in range(10):
            np.random.shuffle(polygon_data)
            x = polygon_data[0:100]
            a = x[:,0:60 * 60]
            b = x[:, 60 *60: 60 * 60 + 1]
            print(b)

            summary = sess.run(merged, feed_dict = {image:np.reshape(a, [100, 60, 60, 1])})
            writer.add_summary(summary, i)

            b = np.reshape(b, [100])
            a = np.sum(a, axis = 1) / 5 - 1
            make = a - b
            ab = np.absolute(make)
            print(np.sum(ab))

    writer.close()


# for making lines,we make this !
def out_of_boundary(point, image_size):
    if(point[0] < 0 or point[0] >= image_size[0] or point[1] < 0 or point[1] >= image_size[1]):
        return True
    return False

def check_angle(target, valid):
    if(not valid):
        valid.append(target)
        return valid
    for i in valid:
        if(abs(i - target) < math.pi * 2 / 15):
            return valid
    valid.append(target)
    return valid
