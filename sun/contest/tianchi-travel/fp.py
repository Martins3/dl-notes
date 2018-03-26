import os
import tensorflow as tf
to_dir = "/home/martin/X-Brain/Tianchi"
fname = os.path.join(to_dir, "gy_contest_link_top(20170715).txt")
fname_2 = os.path.join(to_dir, "gy_contest_link_info.txt")
old_fname_3 = os.path.join(to_dir, "gy_contest_link_traveltime_training_data.txt")
fname_3 = os.path.join(to_dir, "new_gy_contest_traveltime_training_data_second.txt")
fname_4 = os.path.join(to_dir, "sample_data_10.txt")

train_file = os.path.join(to_dir, "new_link_train_data")
compressed_train_data = os.path.join(to_dir, "compressed_train_data.txt")
temp_file = os.path.join(to_dir, "view_train_data.txt")

links_dir = "/home/martin/X-Brain/Tianchi/links"
time_dir = os.path.join(to_dir, "link_time")


# logdir
logdir = to_dir + "/show_data"

# result
res_dir = to_dir + "/res"
res = os.path.join(res_dir, "result.txt")
res_base = os.path.join(res_dir, "base.txt")
res_base_2 = os.path.join(res_dir, "base_2.txt")
res_li = os.path.join(res_dir, "result_li.txt")
res_hu = os.path.join(res_dir, "result_hu.txt")
rehash_res_2 = os.path.join(res_dir, "rehash_result_2.txt")
com_res_2 = os.path.join(res_dir, "com_result_2.txt")
time_res_2 = os.path.join(res_dir, "time_result_2.txt")
real_data = os.path.join(res_dir, "real.txt")

partial_data_full =  os.path.join(res_dir, "partial_full_data.txt")
full_data_full =  os.path.join(res_dir, "full_data_full.txt")
week_full = os.path.join(res_dir,"week_full")



# numpy matrix
matrix = to_dir + "/matrix"

tensor = to_dir + "/tensor"
whole = os.path.join(tensor, "whole.npy")
June = os.path.join(tensor, "Jnue.npy")
fix_data = os.path.join(tensor, "fix_data.npy")
train = os.path.join(tensor, "train.npy")
test = os.path.join(tensor, "test.npy")
fix_June = os.path.join(tensor, "fix_June.npy")
test_no_fix = os.path.join(tensor, "test_no_fix.npy")


def clear(logdir):
    if tf.gfile.Exists(logdir):
        tf.gfile.DeleteRecursively(logdir)
    tf.gfile.MakeDirs(logdir)




# key-value paris
kv_dir = to_dir + "/kv"
kvs = os.path.join(kv_dir, "kvs.txt")
kvs
vks = os.path.join(kv_dir , "vks.txt")
