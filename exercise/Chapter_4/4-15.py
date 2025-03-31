fuel = 500

while fuel >= 50:
    fuel += int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: "))
    print("현재 탱크양은 ", fuel, "입니다.")
    
print("경고 : 연료가 10% 미만이니 충전하세요!")