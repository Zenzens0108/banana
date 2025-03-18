while True:
    n = int(input("정수를 입력하세요 : "))
    result = (0 <= n <= 100 and n % 2 == 0)
    print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", result)
    if result:
        break