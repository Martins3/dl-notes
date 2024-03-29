# -*- coding: utf-8 -*-
"""
1. 修改测试数据集合的频率
2. 修改训练顺序

1. 删除 bn 的使用
"""
import tensorflow as tf
import dataDir as dd
import numpy as np
import time
import os
import makeData



def naive_conv_with_bn():
    n_output = 30 # 1
    learning_rate = 0.0001
    batch_size = 50
    train_test_ratio = 0.8
    image_size = 120 # 3
    n_input = image_size * image_size
    dev = 0.1
    bias_init = 0.01
    training_iters = 12000


    geometric_data_dir = dd.five_star_not_huge # 2
    if(not os.path.isfile(geometric_data_dir)):
        makeData.make_data(geometric_data_dir)
        print("generate random data finished !")
    polygon_data = np.load(geometric_data_dir)
    # 提取出来标准的图片

    THE_IMAGE = np.copy(np.reshape(polygon_data[n_output - 1][0:n_input], newshape = (1, n_input)))
    np.random.shuffle(polygon_data)
    dataset_size = polygon_data.shape[0]
    train_data = polygon_data[0:int(train_test_ratio * dataset_size)]
    test_data = polygon_data[int(train_test_ratio * dataset_size):dataset_size]
    dd.clear(dd.show_data2)

    # Store layers weight & bias
    feature_num1 = 4
    feature_num2 = 16
    feature_num3 = 32
    feature_num4 = 64
    kernel_size = 3
    full_hidden_1 = 800
    full_hidden_2 = 300
    full_hidden_3 = 100
    weights = {
        # 5x5 conv, 1 input, 32 outputs
        'wc1': tf.Variable(tf.truncated_normal([kernel_size, kernel_size, 1,
                                                feature_num1], stddev = dev)),
        # 5x5 conv, 32 inputs, 64 outputs
        'wc2': tf.Variable(tf.truncated_normal([kernel_size, kernel_size,
                                    feature_num1, feature_num2], stddev = dev)),
        'wc3': tf.Variable(tf.truncated_normal([kernel_size, kernel_size,
                                    feature_num2, feature_num3], stddev = dev)),

        'wc4': tf.Variable(tf.truncated_normal([kernel_size, kernel_size,
                                    feature_num3, feature_num4], stddev = dev)),
        # fully connected, 7*7*64 inputs, 1024 outputs
        'wd1': tf.Variable(tf.truncated_normal([8 * 8 * feature_num4, full_hidden_1],stddev = dev)),

        # 第二层 全连接
        'wd2': tf.Variable(tf.truncated_normal([full_hidden_1, full_hidden_2], stddev = dev)),

        'wd3': tf.Variable(tf.truncated_normal([full_hidden_2, full_hidden_3], stddev = dev)),

        # 1024 inputs, 10 outputs (class prediction)
        'out': tf.Variable(tf.truncated_normal([full_hidden_3, n_output], stddev = dev))
    }

    biases = {
        'bc1': tf.Variable(tf.constant(bias_init, shape =[feature_num1])),
        'bc2': tf.Variable(tf.constant(bias_init, shape=[feature_num2])),
        'bc3': tf.Variable(tf.constant(bias_init, shape=[feature_num3])),
        'bc4': tf.Variable(tf.constant(bias_init, shape=[feature_num4])),
        'bd1': tf.Variable(tf.constant(bias_init, shape=[full_hidden_1])),
        'bd2': tf.Variable(tf.constant(bias_init, shape=[full_hidden_2])),
        'bd3': tf.Variable(tf.constant(bias_init, shape=[full_hidden_3])),
        'out': tf.Variable(tf.constant(bias_init, shape=[n_output]))
    }




    def make_one_hot(truth, labels):
        base = np.zeros((truth.shape[0], labels), dtype = np.float32)
        for i in range(truth.shape[0]):
            index = int(truth[i][0])
            base[i][index] = 1
        return base
    # Create some wrappers for simplicity
    def conv2d(x, W, b):
        # Conv2D wrapper, with bias and relu activation
        x = tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
        x = tf.nn.bias_add(x, b)
        return tf.nn.relu(x)


    def maxpool2d(x, k = 2):
        # MaxPool2D wrapper
        return tf.nn.max_pool(x, ksize=[1, k, k, 1], strides=[1, k, k, 1],
                          padding='SAME')

    # Create model
    def conv_net(x, weights, biases, dropout):
        # Reshape input picture
        x = tf.reshape(x, shape=[-1, image_size, image_size, 1])
        tf.summary.image("probe0", tf.transpose(x, perm = [3, 1, 2, 0]), max_outputs= 1, collections=["probe"])

        conv1 = conv2d(x, weights['wc1'], biases['bc1'])
        tf.summary.image("probe1", tf.transpose(conv1, perm = [3, 1, 2, 0]), max_outputs= feature_num1, collections=["probe"])
        conv1 = maxpool2d(conv1)

        conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
        tf.summary.image("probe2", tf.transpose(conv2, perm = [3, 1, 2, 0]), max_outputs= feature_num2, collections=["probe"])
        conv2 = maxpool2d(conv2)

        conv3 = conv2d(conv2, weights['wc3'], biases['bc3'])
        tf.summary.image("probe3", tf.transpose(conv3, perm = [3, 1, 2, 0]), max_outputs= feature_num3, collections=["probe"])
        conv3 = maxpool2d(conv3)


        conv4 = conv2d(conv3, weights['wc4'], biases['bc4'])
        tf.summary.image("probe4", tf.transpose(conv4, perm = [3, 1, 2, 0]), max_outputs= feature_num4, collections=["probe"])
        conv4 = maxpool2d(conv4)

        fc1 = tf.reshape(conv4, [-1, weights['wd1'].get_shape().as_list()[0]])
        fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
        bn = tf.contrib.layers.batch_norm(fc1,
                                          decay=0.9,
                                          center=True,
                                          scale=True,
                                          updates_collections=None,
                                          is_training=is_training,
                                          reuse=None,
                                          trainable=True,
                                          scope="bn1")
        fc1 = tf.nn.relu(bn)
        fc1 = tf.nn.dropout(fc1, dropout) # dorpout 不可以去除

        fc2 = tf.add(tf.matmul(fc1, weights['wd2']), biases['bd2'])
        bn2 = tf.contrib.layers.batch_norm(fc2,
                                          decay=0.9,
                                          center=True,
                                          scale=True,
                                          updates_collections=None,
                                          is_training=is_training,
                                          reuse=None,
                                          trainable=True,
                                          scope="bn2")
        fc2 = tf.nn.relu(bn2)
        fc2 = tf.nn.dropout(fc2, dropout) # dorpout 不可以去除

        fc3 = tf.add(tf.matmul(fc2, weights['wd3']), biases['bd3'])
        bn3 = tf.contrib.layers.batch_norm(fc3,
                                          decay=0.9,
                                          center=True,
                                          scale=True,
                                          updates_collections=None,
                                          is_training=is_training,
                                          reuse=None,
                                          trainable=True,
                                          scope="bn3")
        fc3 = tf.nn.relu(bn3)
        fc3 = tf.nn.dropout(fc3, dropout) # dorpout 不可以去除
        # Output, class prediction
        out = tf.nn.relu(tf.add(tf.matmul(fc3, weights['out']), biases['out']))
        return out


    # Construct model
    # (-1, n_output的个数)
    # Construct model

    x = tf.placeholder(tf.float32, [None, n_input])
    ground_truth = tf.placeholder(tf.float32, [None, n_output]) # 意味着开始的时候就是需要转化为 one-hot
    is_training = tf.placeholder(tf.bool)
    keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)

    pred = conv_net(x, weights, biases, keep_prob)
    # Define loss and optimizer
    cost = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=ground_truth))
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

    # Evaluate model
    correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(ground_truth, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    tf.summary.scalar("accuracy", accuracy, collections=["common"]) # 1
    tf.summary.scalar("cost",cost, collections=["common"]) # 2


    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
    # Initializing the variables
    init = tf.global_variables_initializer()

    # Launch the graph
    with tf.Session() as sess:
        merged = tf.summary.merge_all(key = "common")
        merge_probe = tf.summary.merge_all(key = "probe") # test data
        sess.run(init)
        train_writer = tf.summary.FileWriter(dd.show_data2 + "/train")
        test_writer = tf.summary.FileWriter(dd.show_data2 + "/test")
        probe_writer = tf.summary.FileWriter(dd.show_data2 + "/probe")


        for i in range(training_iters):
            if(i % 100 == 0):
                summary,res,acc = sess.run([merged, cost, accuracy],
                                       feed_dict={x:test_data[:, 0:n_input],
                                       ground_truth:make_one_hot(test_data[:, n_input:n_input + 1], n_output),
                                       keep_prob:1,
                                       is_training:False})
                train_writer.add_summary(summary, i)
                print("{0}  {1}".format(i, acc))

            if(i % 200 == 0):
                s_train_sample = train_data[0:1000]
                s_train_x = s_train_sample[:, 0:n_input]
                s_train_y = make_one_hot(s_train_sample[:, n_input: n_input + 1], n_output)
                s_acc, summary = sess.run([accuracy, merged], feed_dict = {x:s_train_x,
                                             ground_truth:s_train_y,
                                             keep_prob:1,
                                             is_training:False})
                test_writer.add_summary(summary, i)
                print("trian: {0}".format(s_acc, i))

            if(i % 500 == 0): # test data
                the_dict = {
                    x:THE_IMAGE, # test data
                    keep_prob:1,
                    is_training:False
                }
                summary = sess.run(merge_probe, feed_dict = the_dict)
                probe_writer.add_summary(summary, i)



            np.random.shuffle(train_data)
            train_sample = train_data[0:batch_size]
            train_x = train_sample[:, 0:n_input]
            train_y = make_one_hot(train_sample[:, n_input: n_input + 1], n_output)
            sess.run(optimizer, feed_dict={x:train_x,
                                            ground_truth:train_y,
                                            keep_prob:0.6,
                                            is_training:True})


        train_writer.close()

if __name__ == "__main__":
    print("begin !")
    a = time.time()
    # naive_conv_add_dense_layers()
    naive_conv_with_bn()
    print((time.time() - a) / 60, " mins !")
    # naive_conv()
