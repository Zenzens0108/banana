while True:
    n = int(input("세 자리 정수를 입력하시오 : "))
    if 100 <= n <= 999:
        hundreds = n // 100
        tens = (n % 100) // 10
        ones = n % 10
        print("백의 자리 :", hundreds)
        print("십의 자리 :", tens)
        print("일의 자리 :", ones)
        break