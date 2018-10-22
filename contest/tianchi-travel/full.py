"""
有几个问题：
1. 将星期分离出来，然后单独训练
2. lstm
3. 完全不相同的数据如何处理，也就是说如何添加 附属的数据 link width length => 使用gan

1. 需要知道的是： 对于星期的区分的程度是什么
2. 继续调节参数 ，提交一个良好的调参数的结果
3. 添加一个压制数值的 项目
4. 添加一个weight decay的项目
"""
import numpy as np
import tensorflow as tf
import fp
import linkPrediction as lp
import os
import re
import datetime

class Para:
    learningRate = 0.01
    epoch = 4000
    batch_size = 500




def navie_full(full_data = False):
    """
    仅仅使用基本最简单的全连接来得到的
    """
    train_data = np.load(fp.train)
    test_data = np.load(fp.test)
    june = None
    source_data = None

    if(full_data):
        whole = np.load(fp.fix_data)
        whole = whole[:,:,6:9,:]
        train_data = whole.reshape(132 * 92, 90)
        june = np.load(fp.June)
        source_data = june.reshape(132*30,60)

    if(full_data):
        assert train_data.shape == (132*92, 90)
        if(june is not None):
            print("go on!")

    if(june is None):
        print("shoule be false")


    fp.clear(fp.logdir)

    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, 60], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, 30], name='y-input')

    def weight_variable(shape):
        """Create a weight variable with appropriate initialization."""
        initial = tf.truncated_normal(shape, stddev=1)
        return tf.Variable(initial)

    def bias_variable(shape):
        """Create a bias variable with appropriate initialization."""
        initial = tf.constant(1.0, shape=shape)
        return tf.Variable(initial)

    def dense_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
        with tf.name_scope(layer_name):
            weights = weight_variable([input_dim, output_dim])
            biases = bias_variable([output_dim])
            preactivate = tf.matmul(input_tensor, weights) + biases
            activations = act(preactivate, name='activation')
            tf.summary.histogram("activation", activations)
            return activations

    def dense_batch_relu(input_tensor,input_dim, output_dim, layer_name, is_training):
        with tf.variable_scope(layer_name):
            h1 = dense_layer(input_tensor,
                             input_dim,
                             output_dim,
                             layer_name,
                             act=tf.nn.relu)
            h2 = tf.contrib.layers.batch_norm(h1,
                                              decay=0.9,
                                              center=True,
                                              scale=True,
                                              updates_collections=None,
                                              is_training=is_training,
                                              reuse=None,
                                              trainable=True,
                                              scope=layer_name)
            return tf.nn.relu(h2, 'relu')

    keep_prob = tf.placeholder(tf.float32)
    is_training = tf.placeholder(tf.bool)
    hidden1 = dense_batch_relu(x, 60, 100,"layer1",is_training)
    dropped1 = tf.nn.dropout(hidden1, keep_prob)

    hidden2 = dense_batch_relu(dropped1, 100,100, "layer2",is_training)
    dropped2 = tf.nn.dropout(hidden2, keep_prob)

    hidden3 = dense_batch_relu(dropped2, 100, 60, "layer3",is_training)
    dropped3 = tf.nn.dropout(hidden3, keep_prob)

    y = dense_layer(dropped3, 60, 30, 'layer4')





    # 真实数据为： y_ 计算数据为 y
    diff = tf.abs(tf.subtract(y_,y))
    ratio = tf.divide(diff,y_)
    mean = tf.reduce_sum(ratio)



    summary = tf.summary.scalar("mean", mean)

    train_step = tf.train.AdamOptimizer(
        learning_rate=Para.learningRate).minimize(mean)

    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        tf.global_variables_initializer().run()
        train_writer = tf.summary.FileWriter(fp.logdir, sess.graph)

        index = 0
        for i in range(Para.epoch):
            if(i % 50 == 0):
                summary,res = sess.run([merged,mean],
                                       feed_dict={x:test_data[:,0:60],
                                       y_:test_data[:,60:90],keep_prob:1,
                                       is_training: False})
                train_writer.add_summary(summary, i)
                print("{0} : {1}".format(i, res/71280))


            np.random.shuffle(train_data)
            train_sample = train_data[0:Para.batch_size]


            train_x = train_sample[:, 0:60]
            train_y = train_sample[:, 60:90]
            sess.run(train_step, feed_dict={x:train_x,
                                            y_:train_y,
                                            keep_prob:0.6,
                                            is_training:True})
        if(full_data):
            res_june = sess.run(y, feed_dict={x:source_data,
                                              keep_prob:1.0,
                                              is_training:False})
            res_june = res_june.reshape(132, 30, 30)
            write_to_file(res_june)
    train_writer.close()


def write_to_file(res_june):
    assert res_june.shape == (132, 30, 30)
    print(res_june.shape)
    link = 0
    day = 0
    time = 0
    if(os.path.exists(fp.res)):
        os.remove(fp.res)
    with open(fp.res_base) as s:
        with open(fp.res, "a+") as f:
            for line in s:
                line = re.sub("[\n]","",line)
                line = line + str(res_june[link][day][time]) + "\n"
                time = time + 1
                if(time == 30):
                    time = 0
                    day = day + 1
                if(day == 30):
                    day = 0
                    link = link + 1
                f.write(line)

def test_week(ass):
    assert datetime.date(2002, 12, 4).weekday() == 2



def navie_divide_data():
    """
    将数据分成两个部分， 3 4 5.15(包括)的数据作为训练集
    然后使用的 5～16 测试集合
    仅仅使用的
    """
    D = np.load(fp.fix_data)
    train = D[:,0:74,6:9,:]
    test = D[:,74:92,6:9,:]
    train = train.reshape(132*74, 90)
    test = test.reshape(132*18, 90 )
    np.save(fp.train, train)
    np.save(fp.test, test)

def just_divide_data():
    D = np.load(fp.whole)
    test = D[:,74:92,6:9,:]
    test = test.reshape(132*18, 90 )
    np.save(fp.test_no_fix, test)








if __name__ == "__main__":
    navie_full(full_data = False)
    # cat cnn_15000.txt | egrep -v "^[0-9]{19}#2017-06-[0-9]{2}#\[2017-06-[0-9]{2} [0-9]{2}:[0-9]{2}:00,2017-06-[0-9]{2} [0-9]{2}:[0-9]{2}:00)#[0-9]*\.[0-9]*$"
