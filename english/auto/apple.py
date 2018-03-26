"""
just a trial
https://www.programiz.com/python-programming/class
http://blog.csdn.net/jiangxiaoma111/article/details/38461447

1. 文件的格式是锁死的,一定需要是 .md格式
2. 所有的文件所在的位置是唯一的, 目前需要location.py 中间配置

    记忆词汇的过程
    1. 首先查询当前词汇是不是一个单词
    2. 遇到< 的处理的, 直接添加到list 中间去
    3. 遇到# 之后, 后面的直接添加
    4. 任何开头只有# < 两种, 其余全部产生错误的

1. 对于数据库只有读取

1. 没有网络 那就是会一定断开, 设置网络请求为 100
2. 背单词 break 可以保存进度
3. 可以回到上一个单词的位置, 在终端里面修改
4. 可以实现函数
5. 自动查看文件出现变化
6. 使用 google 的 api 或者强化 youdao 的api 需要使用, 进一步替换掉例句,只剩下分隔符
7. 修改文件的表示方法
    1. 去除location 文件, 使用json文件处理
8. json 文件来记录单词含义,放置反复查询
9. 终端里面可以对于文件进行修改的
10. 去掉网络示意
11. 不要使用for i in 循环的结构, 使用下标的结构
12. 修改文件结构, json 提供原始的文件的目录,之后的文件 使用标准的序号 和 string 的描述
13. 不使用 json, 而是使用普通的对象的 pickle 的方法
14. 解释含义的输出应该是一个可以编辑的文本, 将所有的含义都是写入到一个json的文件中间
15. 对于home_dir 实现可以修改
16. 只有在必要的时候才会的申请网络, 没有网络的时候添加的没有网络的提醒, 添加网络延时
17. 结束的时候, 列出新添加的单词, 可成为一个的list, 下一次可以开始之前可以首先添加
18. 需要修复一个bug, 结束的时候没有办法停止
19. 如何处理 被注册的文件越来越多的问题 ? 
    1. list 的 the rigister file
    2. delete the file

20. 算法含有问题: mosaic 这一个单词出现的次数不是一次两次了

todo: 看一下有没有别的接口可以使用
"""
import pickle
import location
import time
import sys
import copy
import os
import youdao
import argparse
import json
from socket import error as SocketError
import errno
import conf


class FileInfo():
    def __init__(self):
        self.sort_by_time = False
        self.ones_words   = True
        self.zero_words   = True
        self.just_show    = False
        self.reverse      = True
        self.from_bottom  = True
        self.index        = -1
        self.file_name    = None
        self.debug        = "origin data"
    
class Word:
    """
    保存单词信息
    """

    def __init__(self, word, time, description=""):
        self.word = word
        self.time = time
        self.description = description

    


def read_to_list(file):
    words = list()
    read_txt = False
    with open(file) as f:
        for line in f:
            line = line.strip("\n")
            pieces = line.split(" ", 1)
            if(len(pieces[0]) == 0):
                continue
            elif(read_txt):
                words.append(Word(line, -1))
            elif(pieces[0][0] == '<'):
                # print(line)
                words.append(Word(line, -1))
            elif(pieces[0][0] == '#'):
                words.append(Word(line, -1))
                read_txt = True
            else:
                # 读取单词的部分, 到底是长度为1, 2 还是 3
                if(len(pieces) == 1):
                    words.append(Word(pieces[0], 0))
                    # print("{0} ---> {1}".format(pieces[0], 0))
                else:
                    before = len(pieces[1])
                    pieces[1] = pieces[1].replace("1","")
                    after = len(pieces[1])
                    times = before - after
                    s = Word(pieces[0], times, pieces[1].strip())
                    words.append(s)
                   # print("{0} ---> {1} ----> {2}".format(pieces[0], times, s.description
    return words




def save_as_file(words, new_file):
    with open(new_file, "w+") as f:
        for i in words:
            w = i.word
            t = i.time
            d = i.description
            if(t == -1):
                f.write(w + "\n")
            else:
                ones = "" if(t == 0) else "1" * t
                space1 = " " * (25 - len(w))
                space2 = " " * (20 - t)
                line = w + space1 + ones + space2 + d + "\n"
                f.write(line)


def make_bck_up(backup, data):
    words = read_to_list(backup);
    save_as_file(words, data)

def show_line(w):
    """
    放弃使用自己的解释, 应该是没有办法直接在terminal 中间编辑
    可以直接addline
    更加复杂的修改, 到达对应的json 文件中间
    """    
    # 查询json 文件, 之后添加json 的补充文件 , 直接使用dict 的方法还是使用,还是使用接口
    JSON_description = None
    # todo    

    if(JSON_description == None):
        # json 没有对应单词 使用网络接口
        Network_Connected = False
        # 如果含有网络的时候, 查询网络, 将结果添加到 json数据库的中间

        word_parser = youdao.WordResultParser()
        word_parser.feed(youdao.get_result(w.word))
        print(word_parser.output, end='\n')


    t = w.time
    ones = "" if(t == 0) else "1" * t
    space1 = " " * (25 - len(w.word))
    space2 = " " * (20 - t)
    line = w.word + space1 + ones + space2 + w.description
    print(line)

def remember(file_object):
    """
    process 是保存进度的, 也是核心
    """
    sort_by_time = file_object.sort_by_time
    ones_words   = file_object.ones_words
    zero_words   = file_object.zero_words
    just_show    = file_object.just_show
    reverse      = file_object.reverse
    from_bottom  = file_object.from_bottom
    index        = file_object.index

    # 保存精度, index ,直接跳过 index 的内容

    # data 是文件所在的位置
    data =  location.home_dir + "/" + file_object.file_name + ".md" # 添加文件的后缀
    primitive = read_to_list(data)
    
    words = primitive[:]
    if(from_bottom):
        words.reverse()

    if(sort_by_time):
        words.sort(key = lambda x:x.time, reverse = reverse)

    # 只有会的单词
    if(ones_words and (not zero_words)):
        words = filter(lambda x: x.time > 0, words)
    
    # 只有不会的单词
    if(zero_words and (not ones_words)):
        words = filter(lambda x: x.time == 0, words)
    
    # 默认全部都是含有的 但是不包括分隔符 和 例句
    words = [i for i in words if i.time >= 0]

    if(not just_show):
        # 处理背单词的过程
        index = remember_core(words, index)
    else:
        for i in words:
            show_line(i)

    # 保存index  写入到 json 文件
    file_object.index = max(index -  1, -1)
    file_object.debug = "this file has been changed !"
    save_as_file(primitive, data)



def remember_core(words, index):
        list_index = 0
        while(list_index < len(words)):
            """
            list_index 是访问的顺序, 而index 是进程顺序
            函数修改的数值, 单词的属性, index
            """

            if(list_index <= index):
                list_index = list_index + 1
                continue
            index = list_index
            i = words[list_index]

            if(i.time != -1):
                print("{0} ---> {1}".format(i.word, i.time))
                print("do you remember ([/])")
            else:
                print(i.word)
                continue
            wrong_input = True
            break_remember = False
            while(wrong_input):
                ipt = input()
                if(ipt == "["): # 认识该单词
                    if(i.time == 1):
                        i.time = 0
                        show_line(i)
                    else:
                        i.time = i.time  - 1
                        show_line(i)
                    wrong_input = False
                elif(ipt == "]"): # 不认识该单词
                    i.time = i.time + 1
                    show_line(i)
                    wrong_input = False
                elif(ipt == "break"):
                    break_remember = True
                    break;
                elif(ipt == "retrace"):
                    list_index = max(-1, list_index - 2)
                    index = max(-1, list_index - 1)
                    wrong_input = False
                else:
                    print("please press [ or ]")
            if(break_remember):
                return index;

            list_index = list_index + 1

        if(index == len(words) - 1):
            return -1
        else:
            return index
        



    

def statics():
    """
    1. 还有多少个单词不会
    2. 还有多少个1
    """
    
def round_statics():
    """
    统计一个周期会的单词和一个周期不会的单词
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                    dest='file_name',
                    default = "0",
                    help='choose which file you should use')
    parser.add_argument('-d',
                       dest = 'use_json',
                       type = int,
                       default = 0,
                       help = "if diy is right, it will load ")
    args = parser.parse_args()


    user_config = location.home_dir + "/diy.json"
    configs = location.home_dir + "/config"

    if(not os.path.exists(configs)):
        os.mknod(configs)
    
    # 放置第一个配置文件手写
    if(not os.path.exists(user_config)):
        os.mknod(user_config)
        ob = FileInfo()
        with open(user_config, "w") as f:
            json.dump(ob.__dict__, f, indent=2, separators=(',', ': '))
        
            
            
            
            

    files = list()
    if(os.stat(configs).st_size == 0):
        with open(configs, "wb") as f:
            pickle.dump(files, f)
        

    with open(configs, "rb") as f:
        files = pickle.load(f)
    
    file = None
    for f in files:
        if(f.file_name == args.file_name):
            file = f

    over = False
    if(file == None):
        print("没有该文件, 需要注册新文件吗? [yes / no]")
        make_new_file = input()
        wrong_input = True
        while(wrong_input):
            if(make_new_file == "yes"):
                file = FileInfo()
                file.file_name = args.file_name
                files.append(file) # 添加到序列中间
                with open(configs, "wb") as f: # 此处存储 还是别处存储, 是一个问题
                    pickle.dump(files, f)

                file.file_name = args.file_name
                wrong_input = False
            elif(make_new_file == "no"):
                over = True
                wrong_input = False
                # 错误的输入, 然后提供全部的文件实现
                if(len(files) != 0):
                    print("files have been register as follow")
                    index = 0
                    for f in files:
                        print("{0} : {1}".format(index, f.file_name))
                        index =  index + 1
                else:
                    print("there is no registered file !")
                    
            else:
                print("please press yes or no !")
                make_new_file = input()

    

    if(not over):
        # 错误的输入文件, 重新开始

        # 如果使用json配置文件, 使用最暴力的方法实现数据的读取
        if(args.use_json == 1):
            object_dict = dict()
            with open(user_config, "r") as f:
                object_dict =  json.load(f)
            file.index          = object_dict["index"] # 以后处理
            file.from_bottom    = object_dict["from_bottom"]  
            file.ones_words     = object_dict["ones_words"]       
            file.zero_words     = object_dict["zero_words"]   
            # file.file_name      = object_dict["file_name"] # 有待分析
            file.just_show      = object_dict["just_show"]
            file.reverse        = object_dict["reverse"]
            file.debug          = object_dict["debug"]
            file.sort_by_time   = object_dict["sort_by_time"]


        # 首先输出所有的参数来
        print("Below is the configs:")
        for i in file.__dict__:
            print("-" * 40)
            print("{0:20s}|   {1:20s}".format(str(i), str(file.__dict__[i])))
        print("-" * 40)
        print()


        remember(file) # file 中间背单词中的过程 以及数据库文件

        # 结束之后将文件写入
        with open(configs, "wb") as f:
            pickle.dump(files, f)

        
    
        
    
                
                
                

    

    # files = location.location()[args.file]
    # backup = files[0]
    # data = files[1]
    # config = files[2]

    
    # dic = dict()
    # if(not os.path.exists(config)):
    #     print("what")
    #     dic["index"] = 0
    #     dic["sort_by_time"] = True
    #     dic["ones_words"]   = True
    #     dic["zero_words"]   = True
    #     dic["just_show"]    = False
    #     dic["reverse"]      = True
    #     dic["from_bottom"]  = True
    #     with open(config, "w") as fp:
    #          json.dump(dic, fp)
    # else:
    #     with open(config, "r") as fp:
    #         dic = json.load(fp)
    #     if(args.change_confi):
    #         # 手动配置的文件
    #         dic["sort_by_time"] = False
    #         dic["ones_words"]   = True
    #         dic["zero_words"]   = True
    #         dic["just_show"]    = False
    #         dic["reverse"]      = True
    #         dic["from_bottom"]  = True
    #         # dic["index"]        = 0

    #     dic["index"] = max(dic["index"] - args.back, 0)

    #     if(args.restart):
    #         print("restart")
    #         dic["index"] = 0

        
    #     with open(config, "w") as fp:
    #         json.dump(dic, fp)

    # remember(files[1], config)

