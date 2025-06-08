import tkinter as tk # tkinter 모듈을 간단하게 tk로 불러낸다.

def save_file():
    with open("note.txt", "w") as f: # note.txt 파일을 열고 "w"로 쓰기 모드 돌입, 파일 객체 f로 지정
        f.write(text.get("1.0", tk.END)) # 처음(1.0)부터 끝(tk.END)까지 모든 텍스트를 가져와 note.txt 파일에 쓴다.

root = tk.Tk() # 기본 창을 불러오는 코드. 이게 없으면 실행이 안 된다.
text = tk.Text(root) # root 창 안에 여러 줄을 쓸 수 있도록 하는 위젯
text.pack()
button = tk.Button(root, text="Save", command=save_file) # "Save" 버튼 생성
button.pack()
root.mainloop() # 프로그램을 계속해서 유지