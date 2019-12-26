# # print("hello world!")

# # print(5*5)
# # print(10/2)

# # print()

# # 変数と配列
# aquarium = ["guppy","medaka","koi"]
# print(aquarium)
# # print(aquarium[2])
# # print(aquarium[1])
# # print(aquarium[0])

# # for 文
# # for fish in aquarium:
# #     print(fish+"様")
# #     print("よろしく")
#     # for i in range(3):
#     #     print(i)
#     # インデント
# # if 文
# for num in range(100):
#     if num%15 == 0:
#         print(str(num) + ": yeah")
#     elif num%5 == 0:
#         print(str(num) + ": bow")
#     elif num%3 == 0:
#         print(str(num) + ": fool")
#     else:
#         print("??")
#     # 3の倍数のとき、"fool"
#     # 5の倍数のとき、"bow"
#     #15の倍数のとき、"yeah"

# # moji = "3"
# # print(moji+3)
# # print(int(moji)+3)

############# turtleモジュール#############
from turtle import *
# fd(100)
# input()

# ６角形を書きましょう

# def print_name(name):
#     print(name + "様よろしくね")
# for name in ["inoue","sasaki","kawamura"]:
#     print_name(name)
# n角形の関数を定義しましょう
def n_gon(n):
	angle = 360/n
	for i in range(n):
		fd(100)
		rt(angle)

# for i in range(10):
#     n_gon(i+3)
# num = 1
# while num < 10:
#     print("ok")
#     num += 1
# 半径が1 ~ 100 までの円を描くwhile文
shape("turtle")

# 亀の時計をつくります。

input()

