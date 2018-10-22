import tensorflow as tf
import fp
import numpy as np


# some really important superparameters
epoch  = 3000
batch_size = 50
learning_rate = 0.01


# help functions
def weight_variable(shape):
        """Create a weight variable with appropriate initialization."""
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)


def bias_variable(shape):
        """Create a bias variable with appropriate initialization."""
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)


def dense_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
        with tf.name_scope(layer_name):
            weights = weight_variable([input_dim, output_dim])
            biases = bias_variable([output_dim])
            preactivate = tf.matmul(input_tensor, weights) + biases
            activations = act(preactivate, name='activation')
            return activations, [weights, biases]


def dense_batch_relu(input_tensor,input_dim, output_dim, layer_name, is_training):
    with tf.variable_scope(layer_name):
        h1, para = dense_layer(input_tensor,
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
        return tf.nn.relu(h2, 'relu'), para


# discreminator
def build_discriminator(x_data, x_generated, keep_prob, is_training):
    with tf.name_scope("discriminator"):
       """
       x_data batch_size , 90
       x_data batch_size, 60 + 30
       """
       x_in = tf.concat([x_data, x_generated], 0)
       h1, p1 = dense_batch_relu(x_in,
                             x_in.get_shape().as_list()[1],
                             100,
                             "dd",
                             is_training)
       d1 = tf.nn.dropout(h1, keep_prob)

       h2, p2 = dense_batch_relu(d1, 100, 80, "d", is_training)
       d2 = tf.nn.dropout(h2, keep_prob)

       h3, p3= dense_batch_relu(d2, 80, 40, "ddd", is_training)
       d3 = tf.nn.dropout(h3, keep_prob)

       out, p4 = dense_layer(d3, 40, 1, "Doutput", tf.identity)

       y_data = tf.nn.sigmoid(tf.slice(out, [0, 0], [batch_size, -1], name=None))
       y_generated = tf.nn.sigmoid(tf.slice(out, [batch_size, 0], [-1, -1], name=None))

       return y_data, y_generated, p1 + p2 + p3 + p4


def build_generator(six_seven, is_training):
    h1, p1 = dense_batch_relu(six_seven,
                     six_seven.get_shape().as_list()[1],
                     100,
                     "g_one",
                     is_training)
    h2, p2 = dense_batch_relu(h1, 100, 100, "g_two", is_training)
    out, p3 = dense_layer(h2, 100, 30, "Goutput", act = tf.identity)

    x_generate = tf.concat([six_seven, out],1)
    return x_generate, p1 + p2 + p3



def train(full_data = False):
    train_data = np.load(fp.train)
    test_data = np.load(fp.test)
    june = None
    source_data = None

    if(full_data):
        whole = np.load(fp.fix_data)
        whole = whole[:,:,6:9,:]
        train_data = whole.reshape(132 * 92, 90) # important data
        june = np.load(fp.June)
        source_data = june.reshape(132*30,60) # important data


    x_data = tf.placeholder(tf.float32, [None, 90], name="real_data")
    six_and_seven = tf.placeholder(tf.float32, [None, 60], name="source_data")
    y_ = tf.placeholder(tf.float32, [None, 30], name='y-input')
    keep_prob = tf.placeholder(tf.float32, name="keep_prob")
    is_training = tf.placeholder(tf.bool)


    x_generated, para_g = build_generator(six_and_seven, is_training)
    y_data, y_generated, para_d = build_discriminator(x_data, x_generated, keep_prob, is_training)
    tf.summary.histogram("y_data", y_data)
    tf.summary.histogram("y_generated", y_generated)
    d_loss = - (tf.log(y_data) + tf.log(1 - y_generated))
    g_loss = - tf.log(y_generated)


    # 使用mean 这一条路径的时候, 相当于使用generator为一个普通的回归函数
    y = tf.slice(x_generated, [0, 60], [-1, 30], name=None)
    # 真实数据为： y_ 计算数据为 y
    diff = tf.abs(tf.subtract(y_,y))
    ratio = tf.divide(diff,y_)
    mean = tf.reduce_sum(ratio)



    optimizer = tf.train.AdamOptimizer(learning_rate)
    d_trainer = optimizer.minimize(d_loss, var_list = para_d)
    g_trainer = optimizer.minimize(g_loss, var_list = para_g)
    help_generator = optimizer.minimize(mean, var_list = para_g)

    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        tf.global_variables_initializer().run()
        train_writer = tf.summary.FileWriter(fp.logdir, sess.graph)

        index = 0
        for i in range(epoch):
            if(i % 50 == 0):
                res = sess.run(mean,
                                     feed_dict={
                                     six_and_seven:test_data[:,0:60],
                                     y_:test_data[:,60:90],
                                     keep_prob:1,
                                     is_training: False})
                print("{0} : {1}".format(i, res/71280))



            np.random.shuffle(train_data)
            np.random.shuffle(test_data)
            train_sample = train_data[0:batch_size]
            test_sample = test_data[0:batch_size]

            feed_dict = {x_data:train_sample,
                         six_and_seven:test_sample[:,0:60],
                         is_training:True,
                         keep_prob:0.6
                         }

            summary ,_ = sess.run([merged, g_trainer], feed_dict = feed_dict)
            train_writer.add_summary(summary, i)
            if(i % 20 == 0):
                sess.run(d_trainer, feed_dict = feed_dict)

            # 使用传统算法帮办训练一波
            if(i% 2 == 0):
                train_x = train_sample[:, 0:60]
                train_y = train_sample[:, 60:90]
                sess.run(help_generator, feed_dict={six_and_seven:train_x,
                                                y_:train_y,
                                                keep_prob:0.6,
                                                is_training:True})

        train_writer.close()

if __name__ == "__main__":
    train(full_data = False)
