try:
    a_list = [200, 300, 400]
    print('a_list :', a_list)
    idx = int(input("구하고자 하는 값의 인덱스를 0, 1, 2 중에서 입력하시오 : "))
    result = a_list[idx]
except ValueError:
    print("정수를 입력하셨나요?")
except IndexError:
    print("구하고자 하는 값의 인덱스를 잘못 입력하셨습니다.")

else:
    print('결과 : ', result)