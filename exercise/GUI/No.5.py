import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def change_color(): # 배경색을 바꿔주는 함수
    root.configure(bg=color.get()) # root 창의 배경색을 설정하는 명령어

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
color = tk.StringVar() # Radiobutton의 선택값을 저장하는 함수
tk.Radiobutton(root, text="Red", variable=color, value="red", command=change_color).pack() # "Red" 버튼을 선택하면 빨간색으로 바뀐다.
tk.Radiobutton(root, text="Blue", variable=color, value="blue", command=change_color).pack() # "Blue" 버튼을 선택하면 파란색으로 바뀐다.
tk.Radiobutton(root, text="Green", variable=color, value="green", command=change_color).pack() # "Green" 버튼을 선택하면 초록색으로 바뀐다.
root.mainloop() # 프로그램을 계속해서 유지