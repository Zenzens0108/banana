"""
Grok SAVE ME!
"""
def area_and_circumstance(r):
    area = 3.14 * r ** 2
    circum = 6.28 * r
    return area, circum

while True:
    r = int(input("반지름을 입력하시오: "))
    if r < 0:
        print("프로그램을 종료합니다.")
        break
    
    area, circum = area_and_circumstance(r)
    print(f"넓이 : {area:7.3f}, 둘레 : {circum:7.3f}")