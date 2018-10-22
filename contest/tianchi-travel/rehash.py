import os
import re
import glob
import time
import fp
import numpy as np


# 由于没有良好设计的， 所以留下如此代码
to_dir = fp.to_dir
fname = fp.fname
fname_2 = fp.fname_2
fname_3 = fp.fname_3
fname_4 = fp.fname_4
train_file = fp.train_file
links_dir = fp.links_dir
time_dir = fp.time_dir
res = fp.res

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def merge_matrixs():
    files = [os.path.join(fp.matrix, f) for f in os.listdir(fp.matrix)
             if os.path.isfile(os.path.join(fp.matrix, f))]
    files = sorted(files, key=natural_keys)

    ms = list()
    for f in files:
        a = np.load(f)
        assert a.shape == (92, 24, 30)
        ms.append(a)
    res = np.stack(ms)
    assert res.shape == (132, 92, 24, 30)
    np.save(fp.whole, res)


def sort_link_bytime():
    """
    相同的原因，首先会对于该文件夹中间的数据进行全部清除，然后添加
    """
    fp.clear(fp.time_dir)
    files = [os.path.join(links_dir, f) for f in os.listdir(links_dir)
             if os.path.isfile(os.path.join(links_dir, f))]
    for linkf in files:
        with open(linkf) as f:
            for line in sorted(f):
                import ntpath
                fname = ntpath.basename(linkf)
                fname = fname.split('.')[0]
                fname += ".time"
                timef = os.path.join(time_dir, fname)
                with open(timef, "a+") as g:
                    g.write(line)


def seperate_links():
    """
    由于使用的文件的处理的方式为append，所以需要首先将links 中间的文件全部删除
    处理之后文件如果放置在相同的位置，那么绝对不可以使用.txt 结尾
    """
    fp.clear(fp.links_dir)
    with open(fp.compressed_train_data) as f:
        for line in f:
            words = line.split(" ")
            link_file = os.path.join(fp.links_dir, words[0]+".txt")
            with open(link_file, "a+") as g:
                g.write(line)


def view_data(count):
    with open(os.path.join(fp.train_file)) as f:
        with open(fp.temp_file, "w+") as g:
            for line in f:
                g.write(line)
                count = count - 1
                if(count==0):
                    return


def compress():
    skip = True
    with open(fp.train_file) as f:
        with open(fp.compressed_train_data, "w+") as g:
            for line in f:
                if(skip):
                    skip = False
                    continue
                line = re.sub('[;[\n]', ' ', line)
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


def make_kvs():
    print("!!!! do you konw what does this means !!!")
    id_set = set()
    with open(fname) as f:
        for line in f:
            space = re.sub('[;#\n]', ' ', line)
            words = space.split(" ")
            for word in words:
                id_set.add(word)
    id_set.remove('') # 不知道为什么有一个蛇皮操作导致含有 ''的字符
    id_set.remove('in_links')
    id_set.remove('link_ID')
    id_set.remove('out_links')

    kvs = {}
    vks = {}
    count = 0
    for i in id_set:
        kvs[i] = str(count)
        vks[str(count)] = i
        count = count + 1
    fp.clear(fp.kv_dir)
    with open(fp.kvs, "w+") as f:
        for i in kvs:
            line = i + " " + kvs[i] + "\n"
            f.write(line)
    with open(fp.vks, "w+") as f:
        for i in vks:
            line = i + " " + vks[i] + "\n"
            f.write(line)

def load_kvs():
    kvs = dict()
    vks = dict()
    with open(fp.kvs,"r+") as f:
        for line in f:
            line = re.sub("[\n]","",line)
            words = line.split(" ")
            kvs[words[0]] = words[1]
    with open(fp.vks,"r+") as f:
        for line in f:
            line = re.sub("[\n]","",line)
            words = line.split(" ")
            vks[words[0]] = words[1]

    return kvs,vks
# 四个函数相同， 不要在乎代码丑
def rehash_link_top():
    kvs, _ = load_kvs()
    new_file = os.path.join(to_dir, "new_link_top")
    with open(fname) as f:
        with open(new_file, "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)
    print("rehash_link_top finished")

def rehash_link_info():
    kvs, _ = load_kvs()
    new_file = os.path.join(to_dir, "new_link_info")
    with open(fname_2) as f:
        with open(new_file, "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)
    print("rehash_link_info finshed")


def rehash_link_train_data():
    kvs, _ = load_kvs()
    new_file = os.path.join(to_dir, "new_link_train_data")
    with open(fname_3) as f:
        with open(new_file, "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)
    print("rehash_link_train_data finshed")

def rehash_link_sample():
    kvs, _ = load_kvs()
    new_file = os.path.join(to_dir, "new_link_sample")
    with open(fname_4) as f:
        with open(new_file, "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)
    print("rehash_link_sample finished")

def seperate_links_June():
    if(os.path.exists(fp.real_data)):
        os.remove(fp.real_data)
    with open(fp.fname_3) as f:
        with open(fp.real_data, "w+") as g:
            for line in f:
                line = re.sub(";","#",line)
                if(line[26]=='6'):
                    g.write(line)

def fix_a_mistake():
    kvs = dict()
    kvs["2016-06"] = "2017-06"
    with open(fp.to_dir + "/res/full_40000.txt") as f:
        with open(fp.to_dir + "/r_full_40000.txt", "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)

def explore_sub():
    kvs, _ = load_kvs()
    new_file = os.path.join(to_dir, "WTF")
    with open(os.path.join(to_dir, "new_gy_contest_result_template.txt")) as f:
        with open(new_file, "w+") as new_f:
            s = f.read()
            for key in kvs:
                s = s.replace(key, kvs[key])
            new_f.write(s)
    print("rehash_link_sample finished")

if __name__ == "__main__":
    explore_sub()
