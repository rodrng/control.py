# 문제 혼자 하다가 실패
# from math import pi
#
#
# class Circle:
#     def __init__(self, radius, x, y):
#         self.radius = radius
#         self.x = x
#         self.y = y
#
#     area = radius * radius * pi
#     def area_print(self):
#         print("원의 넓이:", self.area)
#
# radius = int(input("radius의 값을 입력하세요:"))
# x = int(input("x의 값을 입력하세요:"))
# y = int(input("y의 값을 입력하세요:"))
#
#
# print(area)


# 텍스트 파일 쓰기
# f = open("data/test.txt","w")
# f.write("hello world!")
# f.close()

# 텍스트 파일 내용 불러오기
# try:
#     f = open("data/test.txt","r")
#     txt = f.read()
#     f.close()
#
#     txt = txt[5:10]
#     print(txt)
#     if txt == "12345":
#         print("비밀번호 체크 완료")
#     else:|
#         print("비밀번호가 다릅니다. 확인해주세요")
#
# except:
#     print("불려오려는 파일이 없습니다.")