import argparse
import rehash
import createMDG
import loadInfo
import time
import linkPrediction
import os
import fp
import fixdata
import full
import gg
# MDG means mutilple directed graph
# 4377906283422600514;2017-05-06;[2017-05-06 11:04:00,2017-05-06 11:06:00);3.0
# 9377906285566510514;2016-05-21;[2016-05-21 23:20:00,2016-05-21 23:22:00);17.6
def cry():
    rehash.rehash_link_top()
    rehash.rehash_link_info()
    rehash.rehash_link_train_data()
    rehash.rehash_link_sample()
    rehash.compress()
    rehash.seperate_links()
    rehash.sort_link_bytime()
    linkPrediction.make_matrix_day()
    rehash.merge_matrixs()
    linkPrediction.make_matrix_June()
    fixdata.navie_time_average() # 修复的数据为whole的数据
    full.navie_divide_data()




def main(FLAG):
    begin = time.time()
    full.just_divide_data()
    print("这一波花费时间为：{time}".format(time = time.time() - begin))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--rehash','-r', default=False, type=bool,
                    help='rehash the incredible long id into short id')
    parser.add_argument('--createGraph','-c', default=False, type=bool,
                    help='create the multi graph from link_top file')
    parser.add_argument('--UnNormal','-u', default=True, type=bool,
                    help='for developer testing functions')

    FLAG = parser.parse_args()
    main(FLAG)
