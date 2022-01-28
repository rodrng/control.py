

# 예외처리
a = int(input("a의 값을 입력하세요:"))

try:
    b = 10/a
    print(b)
    try:
        c = a/b
    except:
        print("a나누기 b 에러 발생!!!")

except:
    print("모든 에러")

finally:
    print("에러 발생여부와 상관없이 출력!!!")





# 초기화자 상속
# class Person:
#     def __init__(self, name, job): # 초기화자 -> 인스턴스를 생성할때 자동으로 호출되는 함수
#         self.name = name
#         self.job = job
#
#     # 클래스 속성(초기값)
#     company = "삼성"
#     # 메서드(멤버 함수)
#     def name_print1(self): # self 초기값 객체 // 클래스가 선언 될 때 속성들을 가지고 이름 없는 객체를 만든다
#         print("내 이름 출력1:", self.name) # 필드 속성
#
# class Student(Person): # 상속 : 상속받을 부모클래스명을 ()안에 넣는다
#     def __init__(self, name, job, phoneNumber, studentID):
#         self.name = name
#         self.job = job
#         self.phoneNumber = phoneNumber
#         self.studentID = studentID
#
#     def name_print2(self):
#         print("내 이름 출력2:", self.name)
#
# st1 = Student("권율", "회사원", "1234-123", "1234567")
#
# st1.name_print2()
# st1.name_print1()
# print(st1.company)
# print(st1.job)


# per1 = Person('김유신') # 인스턴스(객체) 생성
# print(per1.name)
# per2 = Person("오오경경민민", "무적")
# print(per2.name)
# print(per2.job)
# print(per2.company)

# per1.name_print() # name_print 메서드 호출
