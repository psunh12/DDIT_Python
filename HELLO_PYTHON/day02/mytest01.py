# 첫수를 입력하시오 1
# 끝수를 입력하시오 4
# 1에서 4까지의 합은 10입니다.

a = input("첫수를 입력하시오")
b = input("끝수를 입력하시오")

aa = int(a)
bb = int(b)
arr = range(aa,bb+1)
sum = 0
for i in arr:
    sum += i
print("{}에서 {}까지의 합은 {}입니다.".format(aa,bb,sum))




