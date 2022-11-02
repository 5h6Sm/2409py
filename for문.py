# table = [["월", "화", "수"], [100, 200, 300]]
# for row in table:
#     for col in row:
#         print(str(col) + " ")
#     print()

# lst = ["apple", 100, 3.14]
# for ty in lst:
#     print(str(ty) + " " + str(type(ty)))
#     print(ty, type(ty))

# d = {"apple": 100, "orange": 200, "banana": 300}
# for v in d:
#     print(str(v) + " " + str(d[v]))

# for k, v in d.items():
#     print(k, v)

# a = [(1, 2), (3, 4), (5, 6)]

# for (first, last) in a:
#     print("first:", first, "last:", last)
#     print(first+last)

# for i in range(1, 11):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print("*" * i)

# for i in range(1, 11):
#     print("*" * i)

# for dan in range(2, 5+1):
#     for i in range(1, 9+1):
#         print("{} x {} = {}".format(dan, i, dan*i))

# for i in range(1, 5+1):
#     print(" "*(5-i), end="")
#     print("*"*(2*i-1))

# table = [["월", "화", "수"], [100, 200, 300]]
# for row in table:
#     for col in row:
#         print(str(col) + " ")
#     print()

# for i in range(1, 9+1):
#     if i == 7:
#         break
#     print("2 x {} = {}".format(i, 2*i))

# print()

# for i in range(1, 9+1):
#     if i % 2 == 0:
#         continue
#     print("2 x {} = {}".format(i, 2*i))


# array = []
# for i in range(1, 10, 2):
#     array.append(i*i)

# array = [i*i for i in range(1, 10, 2)]

# aray = [i*i for i in range(1, 10, 2) if i*i > 30]

# x = 3
# while x < 6:
#     print(x)


# echo = input("hello")
# while echo != "exit":
#     print(echo)
#     echo = input()

# echo = input()
# while True:
#     if echo == "exit":
#         break
#     print(echo)
#     echo = input()

# print(list(range(10)))
# print(list(range(5, 10)))
# print(list(range(10, 0, -1)))
# print(list(range(10, 20, 2)))

# lst = [1, 2, 3, 4, 5]
# print(lst)
# lst = [i**2 for i in lst]
# print(lst)

# test = ("apple", "banana", "ornage")
# test_len = [len(i) for i in test]
# print(test_len)

# d = {100: "apple", 200: "banana", 300: "orange"}
# d_upper = [v.upper() for v in d.values()]
# print(d_upper)

# lst = [10, 25, 30]
# itel = filter(None, lst)
# for item in itel:
#     print("item:{0}}", format(item))

#     def getBoggerThan20(i):
#         return i < 20

# lst =[10, 25, 30]
# itel = filter(getBiggerThan20, lst)
# for item in itel:
#     print("item:{0}".format(item))


# 입력 받은 수가 소수인지 판별하는 프로그램을 작성하라
# 소수는 어떻게 구할까?

# n = int(input("숫자를 입력하세요 : "))
# c = 1
# if n == 1:
#     c = 0
# for i in range(2, int(n/2), 1):
#     if n % i == 0:
#         c = 0
#         break

# if c == 0:
#     print("소수가 아닙니다.")
# else:
#     print("소수입니다.")

# star 함수 정의

def star():
    print("*"*5)


star()
star()
star()

# our_post = {"김민영": 1, "김예진": 5, "박예진": 9, "신유림": 3, "양서영": 4, "오나현": 11,
#             "유정은": 9, "윤성현": 12, "임수민": 3, "최가을": 5, "최승빈": 6, "최원서": 2, "황채민": 8}

# for문을 이용하여 our_post에 저장되어 있는 학생 이름 전체를 출력해 보자.
# for i in our_post:
#     print(i)

# our_post에 "{학생 이름}의 집에는 {냄비의 수}개의 냄비가 있다." 형식으로 출력하시오
# for i in our_post:
#     print(i, "의 집에는", our_post[i],"개의 냄비가 있다.")

# our_post에서 냄비 수가 세개 이상인 학생의 이름을 모두 출력하시오.
# for i in our_post:
#     if our_post[i] >= 3:
#         print(i)

# 처음 세개 이상인 학생이 나오면 그 학생의 이름만 출력하고 출력을 멈추시오
# for i in our_post:
#     if our_post[i] >= 3:
#         print(i)
#         break

# 구구단 2~9단을 출력하는 프로그램을 for문을 이용하여 작성하시오.
# for i in range(2, 10, 1):
#     print(i,"단")
#     for j in range(1, 10, 1) :
#         print(i, "*", j, "=", i*j)
#     print()

# 구구단 2~9단을 출력하는 프로그램을 while문을 이용하여 작성하시오.
# gugu = 2
# while gugu < 10:
#     value = 1
#     print(gugu,"단")
#     while value < 10:
#         print(gugu,"*",value,"=",gugu*value)
#         value += 1
#     print()
#     gugu += 1

# 1~100까지 홀수만 출력하는 프로그램을 작성하시오
# for i in range(1, 101, 1) :
#     if i % 2 == 1:
#         print(i)

# 100 ~ 200까지 3으로 나누어 떨어지는 수를 출력하는 프로그램을 작성하시오.
# for i in range(100, 201, 1):
#     if i % 3 == 0:
#         print(i)

# 소수인지 아닌지 판별하는 프로그램을 작성하시오.
# n = int(input("숫자를 입력하세요 : "))
# c = 1
# if n == 1:
#     c = 0
# for i in range(2, int(n/2), 1):
#     if n % i == 0:
#         c = 0
#         break

# if c == 0:
#     print("소수가 아닙니다.")
# else:
#     print("소수입니다.")

# 1~100 중에서 소수가 몇 개인지 세는 프로그램을 작성하시오
# count가 0일 때 : 소수, 1일 때 : 소수가 아님
# cnt = 0
# for i in range(2, 101):
#     count = 1
#     for j in range(2, i):
#         if i != j and i % j == 0:
#             count = 0
#             break
#     if count == 0:
#         continue
#     else:
#         cnt += 1

# print(cnt)
