

# 이너머레이터 (아이템값 과 인덱스번호를 동시에출력할수있다?)
list7 = list(range(11,30,2))
print(list7)
for num, item in enumerate(list7):
    # print("num=",num)
    # print("item", item)
    print(f"{num+1}회전: value={item}")


# # 리스트 내장2 (if 조건식 + len 문자 길이를 설정해서 출력)
# list4 = ["apple", "orange", "banana"]
# # list5 = [len(i) for i in list4]
# # print(list5)
#
# list6 = [i for i in list4 if len(i)>=6]
# print(list6)


# # 리스트 내장 (새로운 리스트 객체를 생성)
# list3 = list(range(1,6)) # 1~5 리스트 생성
# list4 = [i**2 for i in list3]
# # print(list4)


# # continue문
# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(i)


# a = 10
# while a < 20:
#     a = a+1
#     print(a)
#     if a > 15:
#         break


# # 구구단 만들기
# for i in range(2,10):
#     print("구구단수:", i)
#     for j in range(1,10): # 1~9까지 반복
#         print(f"{i}*{j} = {i*j}") # 1 * 1 = 1, 1 * 2 = 2, 1 * 3 = 3 ~ 1 * 9 = 9


# 구구단 만들기 전에 잠깐 배우기
# a = 10.123456
# b = '10000'
# c = 1000
# print("a={0}, b={1}, c={2}".format(a, b, c)) # 포멧
# print(f"a={a:.3f}, b={b}, c={c:,}원") # 에프스트링?


# range 함수 관련
# for i in range(1,6): # for i in [1,2,3,4,5]: # 파이썬에서 직접넣는건 권장하지 않는다 대신 range 함수를 쓴다
#     print(i)
#
# list2 = list(range(5,11,2)) # 5~10까지 숫자 중 2를 step으로 출력 (2씩 건너띔)
# print(list2)
# tup1 = tuple(range(1,11)) # 1~10까지 튜플로 출력
# print(tup1)


# 이건 머지
# list1 = [10, 100, 1000, 2000]
#
# iter1 = iter(list1)
#
# for i in iter1:
#     print(i)

# for문 연습2
# dic1 ={"apple":100, "orange":200, "banana":300} # 시퀀스형 객체(사전타입)
#
# for i,j in dic1.items():
#     print(i, j)

# for문 연습
# list1 = [10, 100, 1000, 2000] # 시퀀스형 객체(리스트)
#
# for i in list1: # 시퀀스 객체인 list1의 원소를 순서대로 하나씩 빼서 i에 저장
#     print(i)


# while 문 연습
# a = 10
# while a >= 5:
#     print(a)
#     a = a-1 # a -= 1, a=a+1 -> a += 1