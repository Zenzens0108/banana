import datetime as dt

date = dt.datetime(2019, 2, 14)
today = dt.datetime.now()
plus_day = today - date

print(f"춘향이와 몽룡이의 연애 시작일 : {date.year}년 {date.month}월 {date.day}일")
print(f"연애 시작일로부터 경과한 날짜 : {plus_day.days}일")