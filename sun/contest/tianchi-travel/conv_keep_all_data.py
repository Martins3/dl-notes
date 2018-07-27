"""
需要测试多个max_pool
比较好的
"""
import numpy as np
import tensorflow as tf
import fp
import linkPrediction as lp
import os
import re
import datetime
import full

# super parameter
n_input = 60
n_output = 30
learning_rate = 0.007
training_iters = 7000  # means how many times brush the data set
kernel_size = 3
kernel_size_pool = 3
batch_size = 200
dev = 0.1
bias_init = 0.1



def naive_conv(full_data = False):
    train_data = np.load(fp.train)
    test_data_y = np.load(fp.test_no_fix)[:,60:90]
    test_data_x = np.load(fp.test)[:,0:60]
    source_data = None

    if(full_data):
        whole = np.load(fp.fix_data)
        whole = whole[:,:,6:9,:]
        train_data = whole.reshape(132 * 92, 90)
        june = np.load(fp.fix_June)
        source_data = june.reshape(132 * 30,60)



    fp.clear(fp.logdir)


    x = tf.placeholder(tf.float32, [None, n_input])
    y_ = tf.placeholder(tf.float32, [None, n_output])
    is_training = tf.placeholder(tf.bool)
    keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)


    # Create some wrappers for simplicity
    def conv1d(x, W, b):
        # Conv2D wrapper, with bias and relu activation
        x = tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')
        x = tf.nn.bias_add(x, b)
        return tf.nn.relu(x)


    def maxpool2d(x, k=kernel_size_pool):
        # MaxPool2D wrapper
        return tf.nn.max_pool(x, ksize=[1, k, 1, 1], strides=[1, 2, 1, 1],
                          padding='SAME')


    # Create model
    def conv_net(x, weights, biases, dropout):
        # Reshape input picture
        x = tf.reshape(x, shape=[-1, 60,1, 1])

        # Convolution Layer
        conv1 = conv1d(x, weights['wc1'], biases['bc1'])
        # Max Pooling (down-sampling)
        conv1 = maxpool2d(conv1)

        # Convolution Layer
        conv2 = conv1d(conv1, weights['wc2'], biases['bc2'])
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
                                          scope="bn")
        fc1 = tf.nn.relu(bn)
        # Apply Dropout
        fc1 = tf.nn.dropout(fc1, dropout)

        # Output, class prediction
        out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
        return out

    # Store layers weight & bias
    weights = {
        # 5x5 conv, 1 input, 32 outputs
        'wc1': tf.Variable(tf.truncated_normal([kernel_size, 1, 1, 10], stddev = dev)),
        # 5x5 conv, 32 inputs, 64 outputs
        'wc2': tf.Variable(tf.truncated_normal([kernel_size, 1, 10, 15], stddev = dev)),
        # fully connected, 7*7*64 inputs, 1024 outputs
        'wd1': tf.Variable(tf.truncated_normal([15*15, 200], stddev = dev)),
        # 1024 inputs, 10 outputs (class prediction)
        'out': tf.Variable(tf.truncated_normal([200, n_output], stddev = dev))
    }

    biases = {
        'bc1': tf.Variable(tf.constant(bias_init, shape =[10])),
        'bc2': tf.Variable(tf.constant(bias_init, shape=[15])),
        'bd1': tf.Variable(tf.constant(bias_init, shape=[200])),
        'out': tf.Variable(tf.constant(bias_init, shape=[n_output]))
    }

    # Construct model
    y = conv_net(x, weights, biases, keep_prob)

    # filter the zeros
    zeros = tf.cast(tf.zeros_like(y_),dtype=tf.bool)
    ones = tf.cast(tf.ones_like(y_),dtype=tf.bool)

    loc = tf.where(tf.equal(y_, 0), zeros, ones)
    rel_y =tf.boolean_mask(y_, loc)
    pred_y = tf.boolean_mask(y, loc)

    non_zeros = tf.cast(tf.count_nonzero(y_), tf.float32) # for later usage
    diff = tf.abs(tf.subtract(rel_y,pred_y))
    ratio = tf.divide(diff,rel_y)
    cost = tf.reduce_sum(ratio)
    res = tf.divide(cost, non_zeros)

    tf.summary.scalar("count", cost)
    tf.summary.scalar("MAPE", res)

    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)


    # Initializing the variables
    init = tf.global_variables_initializer()

    # Launch the graph
    with tf.Session() as sess:
        mounts = 1
        for i in train_data.shape:
            mounts = mounts * i
        mounts = mounts // 90
        print("训练的总条数 9768 还是 12114: ",mounts)

        merged = tf.summary.merge_all()
        sess.run(init)
        train_writer = tf.summary.FileWriter(fp.logdir, sess.graph)

        for epoch in range(training_iters):
            train_sample = train_data[0:batch_size]
            train_x = train_sample[:, 0:60]
            train_y = train_sample[:, 60:90]
            sess.run(optimizer, feed_dict={x:train_x,
                                            y_:train_y,
                                            keep_prob:0.6,
                                            is_training:True})
            np.random.shuffle(train_data)
            if(epoch % 50 == 0):
                summary,acc = sess.run([merged, res],feed_dict={x:test_data_x,
                                                            y_:test_data_y,
                                                            keep_prob:1,
                                                            is_training:False})
                train_writer.add_summary(summary, epoch)
                print("{0} : {1} {2}".format(epoch, acc ," "))



        if(full_data):
            res_june = sess.run(y, feed_dict={x:source_data,
                                         keep_prob:1.0,
                                         is_training:False})
            res_june = res_june.reshape(132, 30, 30)
            full.write_to_file(res_june)
        train_writer.close()





if __name__ == "__main__":
    naive_conv(full_data = True)
