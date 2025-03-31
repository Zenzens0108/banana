armstrong = []

for n in range(100, 1000):
    a = n // 100
    b = (n % 100) // 10
    c = n % 10
    
    if a ** 3 + b ** 3 + c ** 3 == n:
        armstrong.append(n)
        
print("세 자리의 암스트롱 수 : ", end = "")
for n in armstrong:
    print(n, end = " ")