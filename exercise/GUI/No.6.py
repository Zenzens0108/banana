import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def resize(val): # 출력되는 폰트 크기를 바꾸게 하는 기능
    label.config(font=("Arial", int(val))) # 글꼴: Arial, int 안의 숫자(val)에 따라 텍스트 크기가 바뀐다.

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
'''
tk.Scale을 통해 슬라이더 위젯 생성, 크기는 10에서 40까지
orient="horizontal"를 통해 슬라이더는 수직 방향
command=resize를 통해 숫자가 바뀔 때마다 크기를 조정
'''
scale = tk.Scale(root, from_=10, to=40, orient="horizontal", command=resize)
scale.pack()
label = tk.Label(root, text="Resizable Text") # "Resizable Text" 텍스트 생성
label.pack()
root.mainloop() # 프로그램을 계속해서 유지
