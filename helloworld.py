def triangel_area(x,y):
    return x * y / 2

def square_area(x,y):
    return x * y

def circle_area(r):
    pi = 3.14
    return r * r * pi

number=0
while number != 4:
    number = int(input("삼각형은 1번, 사각형은 2번, 원은 3번, 종료는 4번 입력하시오:"))

    if number == 1:
        x = int(input("가로값:"))
        y = int(input("세로값:"))
        print("**삼각형의 넓이는", triangel_area(x, y))

    elif number == 2:
        x = int(input("가로값:"))
        y = int(input("세로값:"))
        print("사각형의 넓이는", square_area(x, y))

    elif number == 3:
        r = int(input("반지름값:"))
        print("원의 넓이는", circle_area(r))

    elif number == 4:
       print("종료되었습니다")

    else:
        print("잘못입력하셨습니다")