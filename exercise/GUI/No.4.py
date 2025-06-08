import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def show_selection(): # 체크박스를 만드는 함수
    selections = [] # 사용자가 체크한 항목을 저장, 이게 없으면 결과값이 안 뜬다.
    if var1.get(): selections.append("Option 1") # "Option 1" 버튼
    if var2.get(): selections.append("Option 2") # "Option 2" 버튼
    label.config(text=", ".join(selections)) # 선택된 option들을 ","와 함께 표시할 수 있도록 하는 코드

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
var1 = tk.BooleanVar() # 체크박스 상태를 저장할 객체 생성
var2 = tk.BooleanVar()
tk.Checkbutton(root, text="Option 1", variable=var1).pack() # "Option 1"이라는 체크박스를 root 창 안에 배치 
tk.Checkbutton(root, text="Option 2", variable=var2).pack() # "Option 2"라는 체크박스를 root 창 안에 배치 
tk.Button(root, text="Show", command=show_selection).pack() # "Show"라는 버튼을 배치
label = tk.Label(root, text="") # 텍스트를 표시할 빈 창을 나타내는 위젯
label.pack()
root.mainloop() # 프로그램을 계속해서 유지