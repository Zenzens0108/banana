import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def add(): # 두 숫자를 더해서 결과를 나타내는 함수
    result = int(entry1.get()) + int(entry2.get()) # result = 입력 받은 숫자 하나 + 입력 받은 숫자 둘
    label.config(text=f"Result: {result}") # "Reult = {입력 받은 두 숫자의 합}" 텍스트 출력

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
entry1 = tk.Entry(root) # root 창 안에 텍스트 입력창을 뜨게 한다.
entry1.pack()
entry2 = tk.Entry(root) # 그리고 하나 더
entry2.pack()
button = tk.Button(root, text="Add", command=add) # "Add" 버튼을 생성, 이걸 누르면 add() 함수 시행
button.pack()
label = tk.Label(root, text="") # 텍스트를 표시할 빈 창을 나타내는 위젯
label.pack()
root.mainloop() # 프로그램을 계속해서 유지