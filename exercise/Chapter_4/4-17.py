#솔직히 이 문제는 AI 99% 의존했습니다. 이해하면서 다시 옮겨쓰긴 했지만요.

amicable_numbers = []

for a in range (1, 20001):
    sum_a = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i
    
    for b in range (a + 1, 20001):
        if sum_a == b:
            sum_b = 0
            for j in range(1, b):
                if b % j == 0:
                    sum_b += j
            if sum_b == a:
                amicable_numbers.append((a, b))
                
for a, b in amicable_numbers:
    print(f"{a}의 친화수 {b}")
    print(f"{b}의 친화수 {a}")