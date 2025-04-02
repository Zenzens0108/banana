"""
Thanks Grok!
"""
def sum_range(n1, n2):
    return sum(range(n1, n2 + 1))

start1, end1 = 10, 20
sum1 = sum_range(start1, end1)
start2, end2 = 40, 100
sum2 = sum_range(start2, end2)

print(f"{start1}에서 {end1}까지의 정수의 합 : {sum1}")
print(f"{start2}에서 {end2}까지의 정수의 합 : {sum2}")