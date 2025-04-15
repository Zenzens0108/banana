try:
    f_name = input('읽어들일 파일 이름을 입력하세요 : ')
    in_file = open(f_name, 'r')
    buf = in_file.readline()
except FileNotFoundError:
    print("파일 ㅇㄷ?")

else:
    print(buf)