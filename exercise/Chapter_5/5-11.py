"""
Help me Grok!
"""
def area(x1, y1, x2, y2):
    base = x2 - x1
    height = y2 - y1
    return (base * height) / 2

while True:
    x1 = int(input("x1 좌표를 입력하시오 : "))
    y1 = int(input("y1 좌표를 입력하시오 : "))
    x2 = int(input("x2 좌표를 입력하시오 : "))
    y2 = int(input("y2 좌표를 입력하시오 : "))
    
    if x2 > x1 and y2 > y1:
        break
    else:
        print("x2 좌표값이 x1보다 크고 y2 좌표값이 y1보다 커야 합니다.")
        print("처음부터 다시 시작하겠습니다.")

print(f"직각삼각형의 면적은 : {area(x1, y1, x2, y2)}")