choice = input("메뉴를 선택하세요(알파벳 b, c, p 입력): ")

while choice not in ["b", "c", "p"]:
    choice = input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력): ")
if choice == "b":
    print("햄버거를 선택하였습니다.")
elif choice == "c":
    print("치킨을 선택하였습니다.")
elif choice == "p":
    print("피자를 선택하였습니다.")