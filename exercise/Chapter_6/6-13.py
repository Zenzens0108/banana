import math

num = int(input("n을 입력하세요 : "))
n_list = list(map(int, input("{}개의 수를 입력하세요: ".format(num)).split()))
sumi = sum(n_list)
avg = sumi / num
SD = math.sqrt(sum((i - avg) ** 2 for i in n_list) / num)

print("합: ", sumi)
print("평균: ", avg)
print("표준편차: ", f"{SD:.2f}")