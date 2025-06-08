import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def show_fruit(event): # event: .bind가 실행 될 때 호출되는 함수
    selection = listbox.get(listbox.curselection()) # 선택된 과일 항목을 저장
    label.config(text=f"Selected: {selection}") # 저장된 과일 항목에 따라 "Selected: {과일 이름}"으로 출력

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
listbox = tk.Listbox(root) # 리스트를 만들고 이를 선택할 수 있는 위젯
for fruit in ["Apple", "Banana", "Cherry"]: # fruit 리스트에 ["Apple", "Banana", "Cherry"] 저장
    listbox.insert(tk.END, fruit) # 리스트박스를 순차적으로 채워주는 코드, 이게 없으면 저장할 게 없어 프로그램이 시행되지 않는다.
listbox.pack()
'''
<<ListboxSelect>>: 리스트박스에서 항목이 선택될 때 활성화하는 인자
선택된 show_fruit를 표시한다.
'''
listbox.bind("<<ListboxSelect>>", show_fruit)
label = tk.Label(root, text="") # 위의 show_fruit 텍스트를 나타낼 빈 위젯
label.pack()
root.mainloop() # 프로그램을 계속해서 유지