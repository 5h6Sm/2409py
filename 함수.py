# def times(a, b):
#     return a*b


# myTimes = times
# print(times)
# print(myTimes)
# print(times(10, 5))
# print(myTimes(10, 5))

# # 절댓값
# print(10, "의 절댓값 : ", abs(10))
# print(-10, "의 절댓값 : ", abs(-10))

# # 10진수 -> 2진수 변환
# print(128, "의 2진수 : ", bin(128))
# print(255, "의 2진수 : ", bin(255))
# # 10진수 -> 8진수 변환
# print(7, "의 8진수 : ", oct(7))
# print(8, "의 8진수 : ", oct(8))
# # 10진수 -> 16진수
# print(15, "의 16진수 : ", hex(15))
# print(16, "의 16진수 : ", hex(16))

# # 연산
# numbers = [1, 5, -2, 0, 6]
# print(numbers, "중 가장 큰 값은 ", max(numbers))
# print(numbers, "중 가장 작은 값은 ", min(numbers))
# print(numbers, "합계는", sum(numbers))
# print("2의 10승은", pow(2, 10))

# #반올림 : round()
# pi = 3.56789
# print(pi, "의 소수점 1자리 반올림은", round(pi))
# print(pi, "의 소수점 1자리 반올림은", round(pi, 0))
# print(pi, "의 소수점 2자리 반올림은", round(pi, 1))
# print(pi, "의 소수점 3자리 반올림은", round(pi, 2))
# print(pi, "의 소수점 4자리 반올림은", round(pi, 3))

# # 문자열 관련 내장 함수와 문자열 형 변환 함수
# user_name = input("이름은? ")
# user_age = input("나이는? ")
# print(user_name + "님! 나이는 " + str(user_age) + "세군요!")
# say = "{0}님! 나이는 {1}세군요! {1}세라니 놀라워요!"
# print(say.format(user_name, user_age))

# pi = "3.14159"
# print("문자열 출력 : ", pi)
# print("실수 변환 출력 : ", float(pi))
# print(float(pi) + 100)
# year = "2018"
# print("올해 연도 : ", year)
# print("100년 뒤는", int(year) + 100, "년입니다.")
# print("숫자를 문자열로 변환하려면 str()을 이용합니다.")
# print("올해는 " + str(year) + "년입니다")

# # 리스트 관련 내장 함수(활용도 높음)
# list = ['d', 'c', 'a', 'b']
# list.reverse()
# print("리스트 항목 순서 뒤집기", list)
# list.sort(reverse=True)
# print("리스트 항목 역정렬하기", list)
# for index, value in enumerate(list):
#     print("인덱스", index, "위치의 값은 ", value)

# # 내장 함수와 똑같은 이름의 변수 사용
# str1 = "나는 문자열"
# print(str1)
# n = 3
# print(str(n))

# import random  # 임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다.


# def rolling_dice(pip, repeat):
#     for r in range(1, repeat+1):
#         n = random.randint(1, pip)
#         print(pip, "면 주사위 굴린 결과 :", n, ":", n)

# # 처음 시작
# # n = random.randint(1, 6)    #1에서 6까지의 정수 중에 하나를 뽑는다.
# # print("결과 :" ,n )
# # n = random.randint(1, 6)
# # print("결과 :" ,n )
# # n = random.randint(1, 6)
# # print("결과 :" ,n )


# rolling_dice(4, 3)
# rolling_dice(6, 2)
# rolling_dice(10, 4)

# 데이터를 입력하여 합ㅇ르 구하는 함수 정의
# def func_sum(p):
#     sum = 0
#     li = p.split(" ")
#     list(li)
#     for i in li:
#         sum += int(i)
#     return sum


# in_list = input("데이타 입력 : ")
# print("합 : ", func_sum(in_list))

# 매개 변수에 가변 인수가 있는 함수
# varg1
# print("♡")
# print("♡", "♪")
# print("♡", "♪", "♣")
# print("♡", "♪", "♣", "♠")
# print("♡", "♪", "♣", "♠", "★")

# varg2

# def p(*args):
#     str = ""
#     for a in args:
#         str = str + a
#     print(str)


# print("♡")
# print("♡", "♪")
# print("♡", "♪", "♣", "♠")

# varg3
# def p(space, space_num, *args):
#     str = args[0]
#     for i in range(1, len(args)):
#         str = str + (space * space_num) + args[i]
#     print(str)


# print(",", 3, "♡", "♪")
# print("☆", 2, "♡", "♪", "♣")
# print("_", 3, "♡", "♪", "♣", "♠")

# star 함수 정의
# def star(s, *args):
#     for i in range(len(args)):
#         print((s+" ") * args[i])

# star("♬", 3)
# star("♡", 1, 2, 3)

# 키워드 인자를 사용한 함수

# 위치 인자
# keyfn3

# def fn(a, b, c, *d):
#     print(a, b, c, d)


# # 다음 코드 모두 실행되지 않음
# fn(c=3, b=2, a=1, 4, 5)
# fn(1, 2, c=3, 4, 5)
# fn(4, 5, a=1, b=2, c=3)

# 매개 변수에 가변 인수가 있는 함수 실습
# 여러 문자열의 합집합 문자를 구하여 다음과 같이 출력되도록 함수 union()을 작성하시오.

# def union(*ar):
#     result = []
#     for item in ar:
#         for x in item:
#             if x not in result:
#                 result.append(x)
#     return result


# print(union("HAM", "EGG"))
# print(union("HAM", "EGG", "SPAM"))

# 가변인자도 키워드 인자보다 앞으로 위치해야한다.

# def str(a,  * c, b):
#     print(a, b)
#     for i in c:
#         print(c)


# str(1, "ham", "spam", b=5)

# 디폴트 값을 갖는 함수

# def hello(msg="안녕하세요"):
#     print(msg + "!")

# hello("오랜만이에요")
# hello("이영희")
# hello()

# 기본 인자 같이 가변 객체인 함수

# def fn(a, b=[]):
#     b.append(a)
#     print(b)


# fn(3)
# fn(5)
# fn(10)
