from random import random
# 나 :홀
# 컴 :홀 짝
# 결과 : 이김 짐

mine = input("나 :")
com = ""
result = ""

rnd = random()
if rnd >0.5 :
    com = "홀"
else:
    com = "짝"
    
if com == mine:
    result = "이김"
else:
    result = "짐"

print("컴 :{}".format(com))
print("결과 :{}".format(result))




