# -*- coding: utf-8 -*-
import tensorflow as tf
import dataDir as dd
import numpy as np
import time
import os
import makeData

# 图片的数值参数
# train_data and test_data 的确定
# shuffle
# iamge_size labels 需要成为超参数



def naive_conv():
    geometric_data_dir = dd.five_star_noise # 2
    if(not os.path.isfile(geometric_data_dir)):
        makeData.make_data(geometric_data_dir)
        print("generate random data finished !")
    n_output = 10 # 1

    polygon_data = np.load(geometric_data_dir)
    learning_rate = 0.0001
    batch_size = 50
    train_test_ratio = 0.8
    dataset_size = polygon_data.shape[0]

    image_size = 60
    n_input = 60 * 60 # 图片的大小
    dev = 0.1
    bias_init = 0.1
    training_iters = 8000

    def make_one_hot(truth, labels):
        base = np.zeros((truth.shape[0], labels), dtype = np.float32)
        for i in range(truth.shape[0]):
            index = int(truth[i][0])
            base[i][index] = 1
        return base


    np.random.shuffle(polygon_data)

    train_data = polygon_data[0:int(train_test_ratio * dataset_size)]
    test_data = polygon_data[int(train_test_ratio * dataset_size):dataset_size]

    dd.clear(dd.show_data2)


    x = tf.placeholder(tf.float32, [None, n_input])
    ground_truth = tf.placeholder(tf.float32, [None, n_output]) # 意味着开始的时候就是需要转化为 one-hot
    is_training = tf.placeholder(tf.bool)
    keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)


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

        # Convolution Layer
        conv1 = conv2d(x, weights['wc1'], biases['bc1'])
        # Max Pooling (down-sampling)
        conv1 = maxpool2d(conv1)

        # Convolution Layer
        conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
        # Max Pooling (down-sampling)
        conv2 = maxpool2d(conv2)

        # Fully connected layer
        # Reshape conv2 output to fit fully connected layer input

        fc1 = tf.reshape(conv2, [-1, weights['wd1'].get_shape().as_list()[0]])

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

    # Store layers weight & bias
    feature_num1 = 6
    feature_num2 = 12
    kernel_size = 5
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
        # fully connected, 7*7*64 inputs, 1024 outputs
        'wd1': tf.Variable(tf.truncated_normal([15*15*feature_num2, full_hidden_1],stddev = dev)),

        # 第二层 全连接
        'wd2': tf.Variable(tf.truncated_normal([full_hidden_1, full_hidden_2], stddev = dev)),

        'wd3': tf.Variable(tf.truncated_normal([full_hidden_2, full_hidden_3], stddev = dev)),

        # 1024 inputs, 10 outputs (class prediction)
        'out': tf.Variable(tf.truncated_normal([full_hidden_3, n_output], stddev = dev))
    }

    biases = {
        'bc1': tf.Variable(tf.constant(bias_init, shape =[feature_num1])),
        'bc2': tf.Variable(tf.constant(bias_init, shape=[feature_num2])),
        'bd1': tf.Variable(tf.constant(bias_init, shape=[full_hidden_1])),
        'bd2': tf.Variable(tf.constant(bias_init, shape=[full_hidden_2])),
        'bd3': tf.Variable(tf.constant(bias_init, shape=[full_hidden_3])),
        'out': tf.Variable(tf.constant(bias_init, shape=[n_output]))
    }

    # Construct model
    # (-1, n_output的个数)
    # Construct model

    pred = conv_net(x, weights, biases, keep_prob)

    # Define loss and optimizer
    cost = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=ground_truth))
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

    # Evaluate model
    correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(ground_truth, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    tf.summary.scalar("accuracy", accuracy)
    tf.summary.scalar("cost",cost)

    # Initializing the variables
    init = tf.global_variables_initializer()





    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)


    # Initializing the variables
    init = tf.global_variables_initializer()

    # Launch the graph
    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        sess.run(init)
        train_writer = tf.summary.FileWriter(dd.show_data2 + "/train", sess.graph)
        test_writer = tf.summary.FileWriter(dd.show_data2 + "/test")


        for i in range(training_iters):
            if(i % 50 == 0):
                summary,res,acc = sess.run([merged,cost, accuracy],
                                       feed_dict={x:test_data[:, 0:n_input],
                                       ground_truth:make_one_hot(test_data[:, n_input:n_input + 1], n_output),
                                       keep_prob:1,
                                       is_training:False})
                train_writer.add_summary(summary, i)
                print(acc)

            if(i % 100 == 0):
                s_train_sample = train_data[0:1000]
                s_train_x = s_train_sample[:, 0:n_input]
                s_train_y = make_one_hot(s_train_sample[:, n_input: n_input + 1], n_output)
                s_acc, summary = sess.run([accuracy, merged], feed_dict = {x:s_train_x,
                                             ground_truth:s_train_y,
                                             keep_prob:1,
                                             is_training:False})
                test_writer.add_summary(summary, i)
                print("{1} trianing: {0}".format(s_acc, i))


            np.random.shuffle(train_data)
            train_sample = train_data[0:batch_size]


            train_x = train_sample[:, 0:n_input]
            train_y = make_one_hot(train_sample[:, n_input: n_input + 1], n_output)
            sess.run(optimizer, feed_dict={x:train_x,
                                            ground_truth:train_y,
                                            keep_prob:0.6,
                                            is_training:True})
        train_writer.close()


def naive_conv_with_bn():
    geometric_data_dir = dd.five_star_noise # 2
    if(not os.path.isfile(geometric_data_dir)):
        makeData.make_data(geometric_data_dir)
        print("generate random data finished !")
    n_output = 10 # 1

    polygon_data = np.load(geometric_data_dir)
    learning_rate = 0.0001
    batch_size = 50
    train_test_ratio = 0.8
    dataset_size = polygon_data.shape[0]

    image_size = 60
    n_input = 60 * 60 # 图片的大小
    dev = 0.1
    bias_init = 0.1
    training_iters = 8000

    def make_one_hot(truth, labels):
        base = np.zeros((truth.shape[0], labels), dtype = np.float32)
        for i in range(truth.shape[0]):
            index = int(truth[i][0])
            base[i][index] = 1
        return base


    np.random.shuffle(polygon_data)

    train_data = polygon_data[0:int(train_test_ratio * dataset_size)]
    test_data = polygon_data[int(train_test_ratio * dataset_size):dataset_size]

    dd.clear(dd.show_data2)


    x = tf.placeholder(tf.float32, [None, n_input])
    ground_truth = tf.placeholder(tf.float32, [None, n_output]) # 意味着开始的时候就是需要转化为 one-hot
    is_training = tf.placeholder(tf.bool)
    keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)


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
        x = tf.reshape(x, shape=[-1, 60,60, 1])

        conv1 = conv2d(x, weights['wc1'], biases['bc1'])

        conv1 = tf.contrib.layers.batch_norm(conv1,
                                          decay=0.9,
                                          center=True,
                                          scale=True,
                                          updates_collections=None,
                                          is_training=is_training,
                                          reuse=None,
                                          trainable=True,
                                          scope="bn_conv1")
        conv1 = maxpool2d(conv1)


        conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
        conv2 = tf.contrib.layers.batch_norm(conv2,
                                          decay=0.9,
                                          center=True,
                                          scale=True,
                                          updates_collections=None,
                                          is_training=is_training,
                                          reuse=None,
                                          trainable=True,
                                          scope="bn_conv2")

        conv2 = maxpool2d(conv2)

        fc1 = tf.reshape(conv2, [-1, weights['wd1'].get_shape().as_list()[0]])

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

    # Store layers weight & bias
    feature_num1 = 6
    feature_num2 = 12
    kernel_size = 5
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
        # fully connected, 7*7*64 inputs, 1024 outputs
        'wd1': tf.Variable(tf.truncated_normal([15 * 15 * feature_num2, full_hidden_1],stddev = dev)),

        # 第二层 全连接
        'wd2': tf.Variable(tf.truncated_normal([full_hidden_1, full_hidden_2], stddev = dev)),

        'wd3': tf.Variable(tf.truncated_normal([full_hidden_2, full_hidden_3], stddev = dev)),

        # 1024 inputs, 10 outputs (class prediction)
        'out': tf.Variable(tf.truncated_normal([full_hidden_3, n_output], stddev = dev))
    }

    biases = {
        'bc1': tf.Variable(tf.constant(bias_init, shape =[feature_num1])),
        'bc2': tf.Variable(tf.constant(bias_init, shape=[feature_num2])),
        'bd1': tf.Variable(tf.constant(bias_init, shape=[full_hidden_1])),
        'bd2': tf.Variable(tf.constant(bias_init, shape=[full_hidden_2])),
        'bd3': tf.Variable(tf.constant(bias_init, shape=[full_hidden_3])),
        'out': tf.Variable(tf.constant(bias_init, shape=[n_output]))
    }

    # Construct model
    # (-1, n_output的个数)
    # Construct model

    pred = conv_net(x, weights, biases, keep_prob)

    # Define loss and optimizer
    cost = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=ground_truth))
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

    # Evaluate model
    correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(ground_truth, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    tf.summary.scalar("accuracy", accuracy)
    tf.summary.scalar("cost",cost)

    # Initializing the variables
    init = tf.global_variables_initializer()
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

    # Initializing the variables
    init = tf.global_variables_initializer()

    # Launch the graph
    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        sess.run(init)
        train_writer = tf.summary.FileWriter(dd.show_data2 + "/train", sess.graph)
        test_writer = tf.summary.FileWriter(dd.show_data2 + "/test")


        for i in range(training_iters):
            if(i % 50 == 0):
                summary,res,acc = sess.run([merged,cost, accuracy],
                                       feed_dict={x:test_data[:, 0:n_input],
                                       ground_truth:make_one_hot(test_data[:, n_input:n_input + 1], n_output),
                                       keep_prob:1,
                                       is_training:False})
                train_writer.add_summary(summary, i)
                print(acc)

            if(i % 100 == 0):
                s_train_sample = train_data[0:1000]
                s_train_x = s_train_sample[:, 0:n_input]
                s_train_y = make_one_hot(s_train_sample[:, n_input: n_input + 1], n_output)
                s_acc, summary = sess.run([accuracy, merged], feed_dict = {x:s_train_x,
                                             ground_truth:s_train_y,
                                             keep_prob:1,
                                             is_training:False})
                test_writer.add_summary(summary, i)
                print("{1} trianing: {0}".format(s_acc, i))


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
    naive_conv()
    print(time.time() - a)
    # naive_conv()
