def fibo(n):
    if n == 0 or n == 1:
        return 1
    
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
    
n = int(input("fibo(n)의 n을 입력하시오 : "))
print(f"fibo({n}) = {fibo(n)}")