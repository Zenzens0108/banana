import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def say_hello(): # 버튼을 누르면 "Hello World"가 출력되도록 하는 함수
    label.config(text="Hello, World!")

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
button = tk.Button(root, text="Click Me", command=say_hello) # 기본 창(root) 안에 버튼을 불러오는 코드, "Click Me"를 클릭하면 "say_hello"가 출력될 것이다.
button.pack() # button의 하위 클래스. 이게 있어야 button 상자가 생긴다.
label = tk.Label(root, text="") # root 안의 텍스트가 표시 될 빈 공간을 나타내는 위젯
label.pack() # 마찬가지로 이게 있어야 빈 공간에 텍스트가 표시된다.
root.mainloop() # 창을 닫을 때까지 계속해서 창을 뜨게 하는 코드
