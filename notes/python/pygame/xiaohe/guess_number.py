
def byby():
         print("-- 你叫什么")
         a = input()
         print("-- 我知道了， 你叫" + a)
         print("那我们玩一个猜数字游戏吧,继续(y) 结束(n)")
         a = input()
         if(a =='n'):
             return
         s = 23
         times = 0
         first = True
         while(True):
             if(first):
                 first = False
                 print("输入一个数字, 这一个数字在0 ～ 1000")
             else:
                 print("再试一次吧！")
             times = times + 1
             a = input()
             a = int(a)
             if(a == s):
                 print("你赢了")
                 print("你使用了" + str(times) + "次数")
                 break
             elif(a > 23):
                print("太大了")
             else:
                print("太小了")
byby()
