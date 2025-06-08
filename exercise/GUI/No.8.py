import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def show_message(msg): # label에 저장된 텍스트를 표시하는 함수
    label.config(text=msg) # label 텍스트를 업데이트한다.

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
menu = tk.Menu(root) # root 창의 최상위 메뉴 바를 생성하고 menu 변수에 저장한다.
file_menu = tk.Menu(menu, tearoff=0) # munu 안의 하위 menu 설정; tearoff=0을 덧붙이지 않으면 하위 menu를 열 때 점선도 같이 보인다.
file_menu.add_command(label="Open", command=lambda: show_message("Open clicked")) # 'open' 라벨을 클릭했을 때야 "Open clicked" 메시지가 뜨도록 설정
menu.add_cascade(label="File", menu=file_menu) # 메뉴 바에 "File"이라는 이름 붙인 하위 메뉴인 file_menu를 붙인다.
help_menu = tk.Menu(menu, tearoff=0) # 윗 코드와 비슷하게 메뉴 바에 "Help"라는 이름 하위 메뉴를 생성한다.
help_menu.add_command(label="About", command=lambda: show_message("About clicked")) # 'About' 라벨을 클릭하면 "About clicked" 메시지가 뜨도록 설정
menu.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu) # root 창에 메뉴바 설정
label = tk.Label(root, text="") # 위의 show_fruit 텍스트를 나타낼 빈 위젯
label.pack()
root.mainloop() # 프로그램을 계속해서 유지