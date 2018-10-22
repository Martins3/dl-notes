# 提供对于单一分布的刻画,并不关心link 之间 关系
# 如果提供了前面一个小时的 数据变化，可以利用车流的惯性 来分析
#
# how to predict sequence numbers deep learning
#
#
#
import tensorflow as tf
import fp
import os
import re
import numpy as np
import rehash

def MAPE(true, res):
    """
    考察到缺省的数值使用的为0，需要做一些处理
    """
    assert true.shape == res.shape
    s = np.array(list(zip(true.ravel(),res.ravel())), dtype=('f4,f4')).reshape(true.shape)

    def handle(t):
        true = t[0]
        res = t[1]
        if(true == 0.0):
            return 0.0
        else:
            return abs(true - res) / true
    cnt = np.count_nonzero(true)

    f = np.vectorize(handle)
    m = f(s)
    a = np.sum(m)
    return a / cnt


def general_test_from_file(myfile):
    kvs, _ = rehash.load_kvs()
    if(os.path.exists(fp.rehash_res_2)):
        os.remove(fp.rehash_res_2)
    with open(myfile) as f:
        with open(fp.rehash_res_2, "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)
    res = np.zeros((132, 30,2, 30),dtype=np.float32)
    with open(fp.rehash_res_2) as f:
        for line in f:
            words = line.split("#")
            link = int(words[0])
            day = int(words[1][8:10]) -1
            hour = int(words[2][12:14]) - 6
            time = int(words[2][15:17]) // 2
            res[link][day][hour][time] = float(words[3])
    true = np.load(fp.June)
    return MAPE(true, res)


def test_from_file(myfile):
    kvs, _ = rehash.load_kvs()
    if(os.path.exists(fp.rehash_res_2)):
        os.remove(fp.com_res_2)
        os.remove(fp.time_res_2)
        os.remove(fp.rehash_res_2)
    with open(myfile) as f:
        with open(fp.rehash_res_2, "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)

    with open(fp.rehash_res_2) as f:
        with open(fp.com_res_2, "w+") as g:
            for line in f:
                line = re.sub('[#[\n]', ' ', line)
                line  = re.sub('[(),:-]', ' ', line)
                words = line.split(" ")
                n = words[0]
                n += " "
                n += words[6]
                n += " "
                n += words[7]
                n += " "
                n += words[8]
                n += " "
                n += words[9]
                n += " "
                n += words[18]
                n += "\n"
                g.write(n)

    res = np.zeros((132, 30, 2, 30), dtype=np.float32)

    with open(fp.com_res_2) as f:
        with open(fp.time_res_2, "a+") as g:
            link = 0
            time =0
            hour =0
            day = 0
            for line in sorted(f, key=rehash.natural_keys):
                g.write(line)
                line = re.sub("[\n]", "", line)
                words = line.split(" ")
                res[link][day][hour][time] = float(words[5])
                time = time + 1
                if(time == 30):
                    hour = hour + 1
                    time = 0
                if(hour == 2):
                    hour = 0
                    day = day + 1
                if(day == 30):
                    link = link + 1
                    day = 0

    true = np.load(fp.June)
    return MAPE(true, res)


def pernal_average_test():
    D = np.load(fp.whole)
    D = D[:,:,6:8,:]
    ave = np.mean(D, axis = 1)
    ave_s = list()
    for i in range(30):
        ave_s.append(ave)
    aves = np.stack(ave_s,axis=1)
    assert aves.shape == (132, 30, 2, 30)
    assert aves[0][0][0][0] == aves[0][1][0][0]
    true = np.load(fp.June)
    return MAPE(true, aves)


def average_test_create_file():
    D = np.load(fp.whole)
    D = D[:,:,6:8,:]
    aves = np.mean(D, axis= 1)
    assert aves.shape == (132, 2, 30)
    link = 0
    day = 0
    hour = 0
    time = 0
    with open(fp.res_base_2) as s:
        with open(fp.res_hu, "w+") as f:
            for line in s:
                line = re.sub("[\n]","",line)
                line = line + str(aves[link][hour][time]) + "\n"
                time = time + 1
                if(time == 30):
                    time = 0
                    hour = hour + 1
                if(hour == 2):
                    hour = 0
                    day = day + 1
                if(day == 30):
                    day = 0
                    link = link + 1
                f.write(line)





def create_prediction_test():
    _, vks = rehash.load_kvs()
    with open(fp.res_base_2, "w+") as f:
        for i in range(132):
            for j in range(30):
                for t in range(2):
                    for k in range(30):
                         day = str(j + 1)
                         time = str(k*2)
                         time2 = str(k*2 + 2)
                         if(j < 9):
                             day = "0" + str(j + 1)
                         if(k < 5):
                             time = "0" + str(k*2)
                         if(k < 4):
                             time2 = "0" + str(k*2 + 2)

                         hour = "0"
                         if(t == 0):
                             hour += "6"
                         else:
                             hour += "7"
                         line = vks[str(i)] + "#" + "2016-06-" + day + "#" + \
                         "[2016-06-" + day + " " + hour +":" + time + ":00," + \
                         "2016-06-" + day + " " + hour +":" + time2 + ":00)#\n"
                         f.write(line)

def fix_average():
    D = np.load(fp.fix_data)
    D = D[:,:,8,:]
    assert D.shape == (132, 92, 30)
    aves = np.mean(D,axis = 1)
    assert aves.shape == (132, 30)
    mid_av_write_file(aves)

def mid():
    # make a do a testing
    D = np.load(fp.whole)
    D = D[:,:,8,:]
    mid = np.median(D, axis=1)
    mid_av_write_file(mid)



def average():
    D = np.load(fp.whole)
    D = D[:,:,8,:]
    assert D.shape == (132, 92, 30)
    aves = np.mean(D,axis = 1)
    assert aves.shape == (132, 30)
    mid_av_write_file(aves)

def do_mid_av_difference():
    D = np.load(fp.whole)
    M = D[:,:,8,:]
    mid = np.median(M, axis=1)
    ave = np.mean(M,axis=1)
    print("base mid", MAPE(mid, ave))
    print("base ave",MAPE(ave, mid))



def mid_av_write_file(aves):
    """
    辅助mid 函数和 average()函数，用于写入到文件中间
    """
    link = 0
    day = 0
    time = 0
    if(os.path.exists(fp.res)):
        os.remove(fp.res)
    with open(fp.res_base) as s:
        with open(fp.res, "a+") as f:
            for line in s:
                line = re.sub("[\n]","",line)
                line = line + str(aves[link][time]) + "\n"
                time = time + 1
                if(time == 30):
                    time = 0
                    day = day + 1
                if(day == 30):
                    link = link + 1
                f.write(line)

def create_prediction_material():
    """
    创建一个本底文件来来提交结果
    使用的索引为顺序的结构，也就是说只要和普通的
    9377906285566510514;2016-05-21;[2016-05-21 23:20:00,2016-05-21 23:22:00);\n
    """
    _, vks = rehash.load_kvs()
    with open(fp.res_base, "w+") as f:
        for i in range(132):
            for j in range(30):
                for k in range(30):
                    day = str(j + 1)
                    time = str(k*2)
                    time2 = str(k*2 + 2)
                    if(j < 9):
                        day = "0" + str(j + 1)
                    if(k < 5):
                        time = "0" + str(k*2)
                    if(k < 4):
                        time2 = "0" + str(k*2 + 2)
                    if(time2=="60"):
                        line = vks[str(i)] + "#" + "2017-06-" + day + "#" + \
                        "[2017-06-" + day + " " + "08:" + time + ":00," + \
                        "2017-06-" + day + " " + "09:00" + ":00)#\n"
                        f.write(line)
                    else:
                        line = vks[str(i)] + "#" + "2017-06-" + day + "#" + \
                        "[2017-06-" + day + " " + "08:" + time + ":00," + \
                        "2017-06-" + day + " " + "08:" + time2 + ":00)#\n"
                        f.write(line)






def show_data():
    logdir = fp.to_dir + "/show_data"
    fp.clear(logdir)

    x = tf.placeholder(tf.float32,[30], name = "x")
    tf.summary.histogram("day",x)
    train_writer = tf.summary.FileWriter(logdir)
    merged = tf.summary.merge_all()
    data = np.load(fp.matrix + "/1.npy")
    with tf.Session() as sess:
        for i in range(32*30):
            summary = sess.run(merged, feed_dict={x:data[:,:,i]})
            train_writer.add_summary(summary, i)
    train_writer.close()


def make_matrix_day():
    """
    创建数据之前，首先会清理整个文件夹
    为了创建文件使用一个很智障的操作
    所有6月的数据全部都是被抛弃了，其他的函数用于处理这一个问题
    数值缺失的问题使用的方法是:
    使用0 代替 ，然后使用其他的方法搞定数值的问题，而且同时需要处理的问题不只是这一个，
    错误的数据的处理的方法应该是相同的
    创建数据的使用的方法为：天 小时 2分钟 也就是维度为 92 24 30 的矩阵
    """
    fp.clear(fp.matrix)
    files = [os.path.join(fp.time_dir, f) for f in os.listdir(fp.time_dir)
             if os.path.isfile(os.path.join(fp.time_dir, f))]

    # make matrix for every file and data in june is discared
    for tfile in files:
        M = np.zeros((92,24,30), dtype=np.float32)
        import ntpath
        fname = ntpath.basename(tfile)
        fname = fname.split('.')[0]
        fname += "d"
        fname += ".npy"
        fname = os.path.join(fp.matrix, fname)
        with open(tfile) as f:
            for line in f:
                line = re.sub("[\n]", "", line)
                words = line.split(" ")
                if(words[1]=="06"):
                    continue
                M[map_day(words[1],words[2])][int(words[3])][int(words[4])//2] = float(words[5])
        np.save(fname,M)


def make_matrix_June():
    """
    创建数据的使用的方法为：天 小时 2分钟 也就是维度为132 92 2 30 的矩阵
    """

    files = [os.path.join(fp.time_dir, f) for f in os.listdir(fp.time_dir)
             if os.path.isfile(os.path.join(fp.time_dir, f))]
    files = sorted(files, key = rehash.natural_keys)
    # make matrix for every file and data in june is discared
    fname = fp.June
    M = np.zeros((132, 30, 2, 30), dtype=np.float32)
    link = -1
    for tfile in files:
        link = link + 1
        with open(tfile) as f:
            for line in f:
                line = re.sub("[\n]", "", line)
                words = line.split(" ")
                if(words[1]!="06"):
                    continue
                M[link][map_day(words[1], words[2])][int(words[3]) - 6][int(words[4]) // 2] = float(words[5])
        np.save(fname,M)


def map_day(mon, day):
    """
    支持4个月的数据
    """
    mon = int(mon)
    day = int(day)
    if(mon == 3):
        return day - 1
    elif(mon==4):
        return 31 + day - 1
    elif(mon==5):
        return 61 + day - 1
    else:
        return day -1


def test():
    a = np.load(fp.June)
    cnt = 0
    cn2 = 0
    for i in a:
        for j in i:
            for k in j:
                for m in k:
                    if(m == 1.0):
                        cnt  = cnt + 1
                    cn2 = cn2 + 1
    print(cnt)
    print(cn2)


def test_2():
    a = np.load(fp.June)
    for i in range(30):
        print(a[131][29][1][i])
