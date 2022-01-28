import datetime

now = datetime.datetime.now() # 현재시간 불러오기
print(now)
now1 = now.strftime("%y-%m-%d") # 소문자랑 대문자랑 다름 2022년이아니라 22년 이런식으로 출력됨
print(now1)
now2 = now.strftime("%H:%M:%S") # 시간 분 초 출력 # 헐 소문자는 오류뜸 뭐야
print(now2)
now3 = now.strftime("%Y-%m-%d %H:%M:%S")
print(now3)