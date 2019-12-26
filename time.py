from turtle import *
import time
import datetime


# ひな形の描画
def on_start():
    reset()
    # 中央が原点になるように円を描画
    penup()
    sety(-150)
    pendown()
    circle(150)
    penup()
    home()
    # ひげの描画
    for i in range(12):
        fd(130)
        pendown()
        fd(15)
        penup()
        bk(145)
        rt(30)

def draw_tick(angle,b_angle,length):
    # まずは前のを消す
    pencolor("white")
    pendown()
    seth(90-b_angle)
    fd(length)
    bk(length)
    # 次のを描画
    pendown()
    pencolor("black")
    seth(90-angle)
    fd(length)
    bk(length)

def all_tick(ticked):
    pendown()
    pencolor("black")
    
    seth(90-ticked["hour"]*30-ticked["min"]*0.5)
    fd(75)
    bk(75)
    seth(90-ticked["min"]*6)
    fd(110)
    bk(110)
    seth(90-ticked["sec"]*6)
    fd(130)
    bk(130)

# １秒ごとに描画
def task():
    # 時間の認識
    ticked = {
        "sec":datetime.datetime.now().second,
        "min":datetime.datetime.now().minute,
        "hour":datetime.datetime.now().hour
    }
    all_tick_flag = [False,False]
    while True:
        # 秒単位
        if all_tick_flag[0]:
            all_tick(ticked)
            all_tick_flag[0] = False
        sec = datetime.datetime.now().second
        if ticked["sec"] != sec:
            draw_tick(sec*6,ticked["sec"]*6,130)
            ticked["sec"] = sec
        #分単位
        if all_tick_flag[1]:
            all_tick(ticked)
            all_tick_flag[1] = False
        min = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour
        if ticked["min"] != min:
            if ticked["hour"] != hour:
                draw_tick(hour*30+min*0.5,ticked["hour"]*30+ticked["min"]*0.5,75)
                ticked["hout"] = hour
            else:
                draw_tick(hour*30+min*0.5,hour*30+ticked["min"]*0.5,75)
            draw_tick(min*6,ticked["min"]*6,110)
            ticked["min"] = min
        ticked_vals = ticked.values()
        if len(ticked_vals) != len(set(ticked_vals)):
            all_tick_flag = [True,True]

def main():
    on_start()
    task()

shape("turtle")
tracer(2, 0)
# delay(0)

main()
