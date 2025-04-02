"""
Arigatto Grok!
"""

birth = input("주민등록번호 첫 6자리 형식 입력: ")

yy = int(birth[0:2])
mm = int(birth[2:4])
dd = int(birth[4:6])

if yy >= 50:
    yy += 1900
else:
    yy += 2000
    
print(f"{yy}년 {mm}월 {dd}일")