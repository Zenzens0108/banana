import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.
import time # time 모듈을 불러낸다.

def update_time(): # 실시간 시각을 호출하는 함수
    current = time.strftime("%H:%M:%S") # 현재시각을 XX:XX:XX으로 저장
    label.config(text=current) # 저장한 걸 텍스트로 나타냄
    root.after(1000, update_time) # 1000밀리초, 즉 1초마다 업데이트

root = tk.Tk() # root 창 안에 여러 줄을 쓸 수 있도록 하는 위젯
label = tk.Label(root, font=("Arial", 24)) # 글꼴: Arial, 텍스트 크기: 24
label.pack() #update_time()을 고정시키기 위한 함수
update_time() # 실시간 시각 함수 시행
root.mainloop() # 프로그램을 계속해서 유지