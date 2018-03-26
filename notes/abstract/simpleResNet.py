# -*- coding: utf-8 -*-
"""
naive resnet
this is not our main work, and what we desire is inner expression of net

1. check point 的使用
2. 构建一个便于调节参数的模型的出来的
3. 
"""
import tensorflow as tf
import numpy as np
import dataDir as dd
import makeData
import os


def naive_ResNet(): 
    # super parameter
    learning_rate = 0.0001
    batch_size = 50
    train_test_ratio = 0.8
    dev = 0.1
    bias_init = 0.1
    training_iters = 8000
    kernel_size = 3


    image_size = 60 
    n_input = 60 * 60 # 图片的大小
    n_output = 10 # 1


    # prepare the data 
    geometric_data_dir = dd.five_star_noise # 2
    if(not os.path.isfile(geometric_data_dir)):
        makeData.make_data(geometric_data_dir)
        print("generate random data finished !")
    polygon_data = np.load(geometric_data_dir)
    dataset_size = polygon_data.shape[0]
    np.random.shuffle(polygon_data)
    train_data = polygon_data[0:int(train_test_ratio * dataset_size)]
    test_data = polygon_data[int(train_test_ratio * dataset_size):dataset_size]
    dd.clear(dd.show_data2)


   

    def make_one_hot(truth, labels):
        base = np.zeros((truth.shape[0], labels), dtype = np.float32)
        for i in range(truth.shape[0]):
            index = int(truth[i][0])
            base[i][index] = 1
        return base


    #  fundamental functions
    def weight_variable(shape, name = None):
        initial = tf.truncated_normal(shape, stddev=dev)
        return tf.Variable(initial, name=name)
    

    def bais_variable(shape, name = None):
        """
        所有创建的bias_variable都是一维向量, 所以shape 必须是数字
        """
        init = tf.constant(bias_init, shape = [shape])
        return tf.Variable(init, name = name)


    def dense_layer(ipt, shape, keep_prob = None, name = None, is_training = None):
        assert keep_prob != None and  name != None and is_training !=None 
        w = weight_variable(shape)
        b = bais_variable(shape[1])    
        o = tf.matmul(ipt, w) + b
        conv_bn = tf.contrib.layers.batch_norm(o,
                                          decay=0.9,
                                          center=True,
                                          scale=True,
                                          updates_collections=None,
                                          is_training=is_training,
                                          reuse=None,
                                          trainable=True,
                                          scope=name)
        r = tf.nn.relu(conv_bn)
        return tf.nn.dropout(r, keep_prob)

    
    def conv_layer(ipt, filter_shape, conv_name, is_training):
        """
        1. 最后有没有必要添加的一个relu ?
        2. 所有的stride为 1

        注意: name 必须不相同
        """
        assert conv_name != None
        conv_filter = weight_variable(filter_shape)
        conv = tf.nn.conv2d(ipt, conv_filter, strides=[1, 1, 1, 1], padding="SAME")
        
        conv_bn = tf.contrib.layers.batch_norm(conv,
                                          decay=0.9,
                                          center=True,
                                          scale=True,
                                          updates_collections=None,
                                          is_training=is_training,
                                          reuse=None,
                                          trainable=True,
                                          scope=conv_name)
        return tf.nn.relu(conv_bn)
    

    def res_block(ipt, output_channel, name = None, down_sample = False, projection = False, is_training = None):
        """
        由于使用了conv_layer,所以一定需要使用不同name
        默认不是down sample 的

        1. 首先使用 把 输入的数据down sample
        2. 两个conv
        3. 两个数据相加起来
        """
        assert name != None
        input_depth = ipt.get_shape().as_list()[3]
        if down_sample:
            filter_ = [1,2,2,1]
            #  如果使用了 down sample 之后, ipt 被重新赋值, 所以只要深度 down sampeling
            ipt = tf.nn.max_pool(ipt, ksize=filter_, strides=filter_, padding='SAME')

        # 中间有没有可以修改的机会
        conv1 = conv_layer(ipt, [kernel_size, kernel_size, input_depth, output_channel], conv_name = name + "conv1", is_training = is_training)
        conv2 = conv_layer(conv1, [kernel_size, kernel_size, output_channel, output_channel], conv_name = name + "conv2", is_training = is_training)
    
        if input_depth != output_channel:
            if projection:
                # Option B: Projection shortcut
                input_layer = conv_layer(ipt, [1, 1, input_depth, output_channel], 2, name + "convProj")
            else:
                # Option A: Zero-padding
                input_layer = tf.pad(ipt, [[0,0], [0,0], [0,0], [0, output_channel - input_depth]])
        else:
            input_layer = ipt
    
        res = conv2 + input_layer
        return res





    # net 手动搭建, 不需要的什么花里胡哨的东西
    # 需要随着随着 iter step 变化 learning rate 的东西

    channel = {
        "res1": 8,
        "res2": 16,
        "res3": 32,
        "res4": 64
    } 
    
    weights = {
        "dc0": 15 * 15 * channel["res3"],
        "dc1": 600,
        "dc2": 100
    }
    def res_net(input_x, keep_prob, is_training, weights = weights, channel = channel):
        """
        x: 训练的数据, 不包含标签
        dropout: 添加给dense connected
        is_training: bn
        使用 res res_block 的 时候的, 只有input channel 和 out channel 的数目不相同的
        时候才会有问题

        首先使用6组进行简单的测试
        1. 要不要使用 full connected 在中间
        2. 为什么开始的时候需要添加 一个 conv 
        3. projection的影响是什么 ?
        4. 查看对于奇数的 max_pool 的使用的结果是什么 ?
        """
        unique_name = ["res1", "res2", "res3", "res4", "res5", 
        "res6", "conv1", "full1", "full2", "full3"]

        # reshape
        x = tf.reshape(input_x, shape = [-1, 60, 60, 1])
        # conv
        conv1 = conv_layer(x, [kernel_size, kernel_size, 1, channel["res1"]], conv_name = unique_name[6], is_training = is_training)  

        # residual
        res1 = res_block(conv1, channel["res1"], name = unique_name[0], is_training = is_training)
        res2 = res_block(res1, channel["res1"], name = unique_name[1], down_sample = True, is_training = is_training)
        # 针对于现有模型的测试代码, 不具有兼容性
        assert res2.get_shape().as_list()[1:] == [30, 30, 8]

        res3 = res_block(res2, channel["res2"], name = unique_name[2], is_training = is_training)
        res4 = res_block(res3, channel["res2"], name = unique_name[3], is_training = is_training)
        assert res4.get_shape().as_list()[1:] == [30, 30, 16]

        res5 = res_block(res4, channel["res3"], name = unique_name[4], is_training = is_training)
        res6 = res_block(res5, channel["res3"], name = unique_name[5], down_sample = True, is_training = is_training)
        assert res6.get_shape().as_list()[1:] == [15, 15, 32]

        # 转换到达普通的full层
        # full
        dc0 = tf.reshape(res6, shape = [-1, weights["dc0"]])
        dc1 = dense_layer(dc0,[weights["dc0"], weights["dc1"]], keep_prob = keep_prob, name = unique_name[7], is_training = is_training)
        dc2 = dense_layer(dc1,[weights["dc1"], weights["dc2"]], keep_prob = keep_prob, name = unique_name[8], is_training = is_training)
        dc3 = dense_layer(dc2,[weights["dc2"], n_output], keep_prob = keep_prob, name = unique_name[9], is_training = is_training)
        return dc3

    

    
    # place holders
    x = tf.placeholder(tf.float32, [None, n_input])
    ground_truth = tf.placeholder(tf.float32, [None, n_output]) # 意味着开始的时候就是需要转化为 one-hot
    is_training = tf.placeholder(tf.bool)
    keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)

    # finish the graph
    pred = res_net(x, keep_prob, is_training)
    cost = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=ground_truth))
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
    correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(ground_truth, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    tf.summary.scalar("accuracy", accuracy)
    tf.summary.scalar("cost",cost)
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
    init = tf.global_variables_initializer()

    # begin the training

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

            if(i % 200 == 0):
                s_train_sample = train_data[0:1000]
                s_train_x = s_train_sample[:, 0:n_input]
                s_train_y = make_one_hot(s_train_sample[:, n_input: n_input + 1], n_output)
                s_acc, summary = sess.run([accuracy, merged], 
                                             feed_dict = {x:s_train_x,
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
    naive_ResNet()