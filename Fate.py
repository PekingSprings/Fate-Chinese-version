import sys
import time
import math
import tkinter.messagebox
from  tkinter import *
import random

while True:
    try:
        num1=float(input("Birthday(X.XX)"))
        luck = int(input("luck number"))
        break
    except ValueError:
        print("Number must be a number")

num2=time.localtime()
if luck>10:
    tkinter.messagebox.showerror("Error","Luck must be under 10")
    sys.exit()
##计算公式(顺带一提，这就是我没事瞎捣鼓的公式)
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
messages = {
        4: "恭喜恭喜，今日运气爆棚，上上签！",
        3: "还行还行，运气在线，上签！",
        2: "平平淡淡，普普通通，中签",
        1: "运气不咋地，下签",
        0: "看来运气很差，下下签"
    }
sumlast=sum(d%2==0 for d in [con1,con2,con4,con5])
print("命运计算中********")
time.sleep(3)
print(messages[sumlast])

