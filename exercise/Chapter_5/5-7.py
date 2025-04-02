"""
HELP ME GROK!
"""
def mean3(a, b, c):
    return (a + b + c) / 3

def max3(a, b, c):
    return max(a, b, c)

def min3(a, b, c):
    return min(a, b, c)

a, b, c = map(int, input("세 수를 입력하시오 : ").split())

numbers = [a, b, c]
numbers.sort()
a, b, c = numbers

print(f"{a}, {b}, {c}의 평균값은 {mean3(a, b, c):.1f}")
print(f"{a}, {b}, {c}의 최댓값은 {max3(a, b, c)}")
print(f"{a}, {b}, {c}의 최솟값은 {min3(a, b, c)}")