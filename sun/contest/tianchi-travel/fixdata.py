import numpy as np
import fp
import linkPrediction as lp
import tensorflow as tf
import matplotlib.pyplot as plt


def naive_day_average():
    """
    使用原则为：首先计算所有的none_zero 求解平均值，然后使用将平均值来填充
    132 92 24 30
    0.375 为最开始的版本
    0.44
    0.47 li
    """
    # 修复数组
    D = np.load(fp.whole)
    print(np.count_nonzero(D))
    for i in range(132):
        for j in range(24):
            for k in range(30):
                time = D[i,:,j,k]
                nonzero = 0
                sumup = 0
                if(np.count_nonzero(time) != 0):
                    for e in time:
                        if(e!=0):
                            nonzero = nonzero + 1
                            sumup = sumup + e
                    average = sumup / nonzero
                    for s in range(92):
                        if(time[s]==0):
                            D[i,s,j,k] = average
    np.save(fp.fix_data, D)


    # 再一次做一个修复


def navie_time_average():
    D = np.load(fp.whole)
    link = list()
    ss = 0
    for link_mess in D:
        link_mess = link_mess.reshape(92 * 24 * 30)
        a = list()
        prev = 0
        for i in link_mess:
            if(i != 0):
                prev = i
            a.append(prev)

        ke = np.flip(link_mess,0)
        prev = 0
        b = list()
        for i in ke:
            if(i != 0):
                prev = i
            b.insert(0,prev)
        c = [(i + j)/2 for (i, j) in zip(a, b)]
        res = np.array(c)
        res = res.reshape(92, 24, 30)
        link.append(res)
        ss = ss + 1
        print(ss)
    D = np.stack(link, axis = 0)
    np.save(fp.fix_data, D)




def navie_time_average_June():
    D = np.load(fp.June)
    S = None
    all_list = list()
    ss = 0
    for Day in D:
        link = list()
        for link_mess in Day:
            link_mess = link_mess.reshape( 2 * 30)
            a = list()
            prev = 0
            for i in link_mess:
                if(i != 0):
                    prev = i
                a.append(prev)

            ke = np.flip(link_mess,0)
            prev = 0
            b = list()
            for i in ke:
                if(i != 0):
                    prev = i
                b.insert(0,prev)
            c = [(i + j)/2 for (i, j) in zip(a, b)]
            res = np.array(c)
            res = res.reshape(2, 30)
            link.append(res)
            D = np.stack(link, axis = 0)
        all_list.append(D)
        print(ss)
        ss =  ss + 1
    S = np.stack(all_list, axis = 0)
    np.save(fp.fix_June, S)


def check_data():
    whole = np.load(fp.whole)
    fix_data = np.load(fp.fix_data)
    print(whole.shape)
    print(fix_data.shape)
    print("没有修复", np.count_nonzero(whole))
    print("修复之后", np.count_nonzero(fix_data))
    print("总的数目是{0}".format(132 * 92 * 24 * 30))
    e = np.equal(whole, fix_data)
    print("相等的数目",np.sum(e))
    a = whole[0].reshape(92 * 24 * 30)
    b = fix_data[0].reshape(92 * 24 * 30)
    for i in range(1000):
        print(a[i],b[i])

def check_data_june():
    June = np.load(fp.June)
    fix_data = np.load(fp.fix_June)
    print(June.shape)
    print(fix_data.shape)
    print("没有修复", np.count_nonzero(June))
    print("修复之后", np.count_nonzero(fix_data))
    print("总的数目是{0}".format(132 * 30 * 2* 30))
    e = np.equal(June, fix_data)
    print("相等的数目",np.sum(e))
    a = June[0].reshape(30 * 2 * 30)
    b = fix_data[0].reshape(30 * 2 * 30)
    for i in range(1000):
        print(a[i],b[i], i %60)




if __name__ == "__main__":
    check_data()
