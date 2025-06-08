import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def greet(): # greet 이라는 함수 설정
    name = entry.get() # 텍스트를 쓰면 그 텍스트를 반환하는 name 함수 정의
    label.config(text=f"Hello, {name}") # 이제 "Hello, {자기가 쓴 텍스트}"가 보일 것이다

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
entry = tk.Entry(root) # root 창 안에 텍스트 입력창을 뜨게 한다.
entry.pack() # 윗 코드와 한 몸
button = tk.Button(root, text="Greet", command=greet) # "Greet"라는 버튼 생성
button.pack() # 윗 코드와 한 몸
label = tk.Label(root, text="") # 텍스트를 표시할 빈 창을 나타내는 위젯
label.pack() # 윗 코드와 한 몸
root.mainloop() # 프로그램 계속해서 유지