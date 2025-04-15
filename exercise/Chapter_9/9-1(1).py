try:
    a, b = input("두 수를 입력하시오: ").split()
    result = int(a) * int(b)
except ValueError:
    print('정수를 입력하셨는지 다시 한 번 확인하십시오.')
else:
    print('{} * {} = {}'.format(a, b, result))
    
    