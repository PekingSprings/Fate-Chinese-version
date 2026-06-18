import sys
import time
import math
import tkinter.messagebox
import random

cyclenum=20
num1=float(input("Birthday(X.XX)"))
luck=int(input("luck number"))
num2=time.localtime()
if luck>10:
    tkinter.messagebox.showerror("Error","Luck must be under 10")
    sys.exit()

##计算公式
result=math.exp(num1)*num2.tm_year*num2.tm_mon*num2.tm_mday*luck
# print(result)
length=len(str(math.floor(result)))
#数字位数确定
con1=math.floor(result)//math.pow(10,length-1)
con2=(math.floor(result)//math.pow(10,length-2))%10
con5=(math.floor(result)//math.pow(10,length-5))%10
con4=(math.floor(result)//math.pow(10,length-4))%10
# print(con1,con2,con4,con5,result)
#位数确定，字典用法
sumlast=sum(d%2==0 for d in [con1,con2,con4,con5])
if sumlast==4:


    print("恭喜恭喜，今日运气爆棚，上上签！")
elif sumlast==3:
    print("还行还行，运气在线，上签！")
elif sumlast==2:
    print("平平淡淡，普普通通，中签")
elif sumlast==1:
    print("运气不咋地，下签")
elif sumlast==0:
    print("看来运气很差，下下签")
input()
