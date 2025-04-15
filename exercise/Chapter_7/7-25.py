"""
순도 100% AI가 썼습니다.
저는 망했습니다
"""
# 영한사전 딕셔너리 초기화
dictionary = {}

print("사전 프로그램 시작... 종료는 q를 입력")

while True:
    # 사용자 입력 받기
    command = input("$ ")
    
    # 종료 조건
    if command == "q":
        print("사전 프로그램을 종료합니다.")
        break
    
    # 입력 명령 처리
    if command.startswith("< "):
        try:
            # "< " 이후의 문자열 추출
            entry = command[2:].strip()
            # 영어:우리말 분리
            eng, kor = entry.split(":", 1)
            # 공백 제거
            eng = eng.strip()
            kor = kor.strip()
            # 딕셔너리에 저장
            dictionary[eng] = kor
        except ValueError:
            print("입력 오류가 발생했습니다.")
    
    # 검색 명령 처리
    elif command.startswith("> "):
        # "> " 이후의 영어 단어 추출
        eng = command[2:].strip()
        if eng in dictionary:
            print(dictionary[eng])
        else:
            print(f"{eng}가 사전에 없습니다.")
    
    # 잘못된 입력
    else:
        print("입력 오류가 발생했습니다.")