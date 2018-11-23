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


def upload_navie_full_withfix(week=False):
    # 首先， 创建数据


    # 使用测试的参数训练


    # 写入到文件中间的去

    whole = np.load(fp.fix_data)
    whole = whole[:,:,6:9,:]
    train_data = whole.reshape(132 * 92, 90)

    june = np.load(fp.June)
    source_data = june.reshape(132*30,60)



    assert train_data[132 * 92 - 1][30] == whole[131][91][1][0]
    # test_data = np.load(fp.test) 此处没有test data的搞法

    fp.clear(fp.logdir)

    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, 60], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, 30], name='y-input')

    def weight_variable(shape):
        """Create a weight variable with appropriate initialization."""
        initial = tf.truncated_normal(shape, stddev=1.0)
        return tf.Variable(initial)

    def bias_variable(shape):
        """Create a bias variable with appropriate initialization."""
        initial = tf.constant(0.3, shape=shape)
        return tf.Variable(initial)

    def output_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
        with tf.name_scope(layer_name):
            weights = weight_variable([input_dim, output_dim])
            biases = bias_variable([output_dim])
            preactivate = tf.matmul(input_tensor, weights) + biases
            activations = act(preactivate, name='activation')
            tf.summary.histogram("activation", activations)
            return activations

    def dense_batch_relu(input_tensor, output_dim, scope, is_training):
        with tf.variable_scope(scope):
            h1 = tf.contrib.layers.fully_connected(input_tensor,
                                                   output_dim,
                                                   activation_fn=None,
                                                   scope='dense')
            h2 = tf.contrib.layers.batch_norm(h1,
                                              decay=0.9,
                                              center=True,
                                              scale=True,
                                              updates_collections=None,
                                              is_training=is_training,
                                              reuse=None,
                                              trainable=True,
                                              scope=scope)
            return tf.nn.relu(h2, 'relu')

    keep_prob = tf.placeholder(tf.float32)
    is_training = tf.placeholder(tf.bool)
    hidden1 = dense_batch_relu(x, 100, "layer1",is_training)
    dropped1 = tf.nn.dropout(hidden1, keep_prob)

    hidden2 = dense_batch_relu(dropped1, 100, "layer2",is_training)
    dropped2 = tf.nn.dropout(hidden2, keep_prob)
    #
    # hidden3 = nn_layer(dropped2, 100, 100, "layer2")
    # dropped3 = tf.nn.dropout(hidden3, keep_prob)

    y = output_layer(dropped2, 100, 30, 'layer3', act=tf.identity)



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
                                       feed_dict={x:train_data[:,0:60],
                                       y_:train_data[:,60:90],keep_prob:1.0,
                                       is_training: False})
                train_writer.add_summary(summary, i)
                print("{0} : {1}".format(i, res/(132 * 92 * 30)))

            index = index + 1
            if((index + 1) * Para.batch_size > train_data.shape[1]):
                np.random.shuffle(train_data)
                index = 0
            train_sample = train_data[index*Para.batch_size:
                                 (index + 1)*Para.batch_size]


            train_x = train_sample[:, 0:60]
            train_y = train_sample[:, 60:90]
            sess.run(train_step, feed_dict={x:train_x,
                                            y_:train_y,
                                            keep_prob:0.6,
                                            is_training:True})
        # res_june = sess.run(y, feed_dict={x:source_data,
        #                                   keep_prob:1.0,
        #                                   is_training:False})
        # res_june = res_june.reshape(132, 30, 30)
        # write_to_file(res_june)
    train_writer.close()
