"""
处理文件位置的问题
"""
import getpass
FILE_DIR = "/AllWorkStation/Atom/notes/english/lib"


user_name = getpass.getuser()
home_dir = None
if(user_name == "martin"):
    home_dir = "/home/martin"
elif(user_name == "zhangmengxiao"):
    home_dir = "/home/huxueshi"
else:
    home_dir = "/home/ubuntu/hubachelar"

home_dir = home_dir + FILE_DIR