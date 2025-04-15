"""
feat. Grok 3
"""

import random as rd

x = rd.randrange(1, 21)

n = 0

while True:
    guess = int(input("1~20까지의 숫자를 입력하세요: "))
    n += 1
    
    if guess == x:
        print("정답입니다!")
        if n <= 3:
            print(f"{n}번만에 맞춘 당신은 천재!")
        elif n <= 6:
            print(f"{n}번만에 맞추셨네요. 잘했어요^^")
        else:
            print(f"{n}번만에 맞추다니 쩝쩝...")
        break
    elif guess < x:
        print(f"{guess}보다 큽니다!")
    else:
        print("{guess}보다 작습니다")