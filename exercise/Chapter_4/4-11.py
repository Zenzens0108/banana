height = 0
day = 0

while height < 30:
    day += 1
    height = day * 2 + 5
    print("day: ", day, "          달팽이의 위치 : ", height, "미터")
    if height >= 30:
        break

print("우물을 탈출하는 데 걸린 날은 ", day, "일입니다")