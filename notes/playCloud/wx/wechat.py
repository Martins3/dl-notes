from wxpy import *

bot = Bot(cache_path=True)
logger = get_wechat_logger(receiver=bot)
bot.enable_puid()

# bot.self 的含义是什么
# https://pythonhosted.org/watchdog/quickstart.html#a-simple-example watchdog 和 讲所有的输出重新定向
#向自己通信，bot.file_helper.send("something")

# http://wxpy.readthedocs.io/zh/latest/bot.html

@bot.register()
def print_messages(msg):
    print(msg)


# @bot.register()
# def auto_reply_xiaobing(msg):
#     return '{}'.format(msg.text)

# 堵塞线程，并进入 Python 命令行
embed()
