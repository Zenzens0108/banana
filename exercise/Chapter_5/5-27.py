"""
Help me Grok!
"""

def unit_fraction(frac):
    n = 2
    closest_n = n
    min_diff = abs(frac - 1/n)
    
    while True:
        n += 1
        current = 1/n
        diff = abs(frac - current)
        
        if diff < min_diff:
            min_diff = diff
            closest_n = n
        if current < frac and 1/(n-1) > frac:
            break
    
    return closest_n, 1/closest_n

frac = float(input("1보다 작고 0보다 큰 소수를 입력하세요 : "))

denominator, decimal = unit_fraction(frac)

print(f"가장 가까운 단위 분수는 1/{denominator}이며, 이 값은 {decimal}입니다.")