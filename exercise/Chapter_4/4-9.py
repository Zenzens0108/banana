n = int(input("자연수를 입력하세요 : "))

if n < 1:
    n = int(input("다시 입력하세요. 자연수여야 합니다 : "))
else:
    sum = 0
    for i in range(n+1):
        sum += i ** 2

print("결과는",sum,"입니다.")