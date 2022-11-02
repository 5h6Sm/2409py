'''a = 5
if a > 5:
    print("test입니다.")
    print("a가 10입니다.")
else:
    print("else문입니다")'''

'''x = int(input("숫자 입력 : "))  # 입력하는 함수 input()
print(x)
print(type(x))

if x % 2 == 0:
    print("짝수")
else:
    print("홀수")

password = input("암호를 입력하세요 : ")

if password == "암호":
    print("암호이다.")
else:
    print("암호가 아니다.")'''

'''money = 1
if money:
    print("택시를")
print("타고")
print("가라")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")'''

'''# pocket에 money가 있으면
pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# 주머니에 돈이 있으면 아무 것도 하지 말고, 돈이 없으면 카드를 꺼내라

# 1번째 방법
pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
print("수행완료")

# 2번재 방법
pocket = ['paper', 'cellphone', 'money', 'card']
if 'money' not in pocket:
    print("카드를 꺼내라")
print("수행완료")'''

# 만약 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라

# pocket = ['paper', 'cellphone', 'money', 'card']
# if 'money' in pocket : print("택시를 타라 - money") 한 문장이면 한 줄에 써도 된다
# if 'money' in pocket:
#     print("택시를 타라 - money")
# elif 'card' in pocket:
#     print("택시를 타라 - card")
# else:
#     print("걸어가라")

# saying = "Life is too short, you need python"

# if "wife" in saying:
#     print("wife")
# elif "python" in saying and "you" not in saying:
#     print("python")
# elif "shirt" not in saying:
#     print("shirt")
# elif "need" in saying:
#     print("need")
# else:
#     print("none")

# print(bool(True))
# print(bool(False))
# print(bool(0))
# print(bool(3))
# print(bool(""))
# print(bool("test"))
# print(bool([]))
# print(bool([1, 2, 3]))

# x = int(input("숫자를 입력하세요 : "))

# if x < 0:
#     print("minus")
#     if x % 2 != 0:
#         print("odd")
#     else:
#         print("even")
# else:
#     print("plus")
#     if x % 2 != 0:
#         print("odd")
#     else:
#         print("even")

# for ch in "LOVE":
#     print(ch, end='')


# v = int(input("수 입력 : "))
# if v % 3 == 0:
#     print("{}은(는) 3의 배수이다.".format(v))
# if v % 5 == 0:
#     print("{}은(는) 5의 배수이다.".format(v))
# if v % 8 == 0:
#     print("{}은(는) 8의 배수이다.".format(v))
# if v % 3 != 0 and v % 5 != 0 and v % 8 != 0:
#     print("어느 배수도 아니다.")


# if v % 3 == 0 or v % 5 == 0 or v % 8 == 0:
#     if v % 3 == 0:
#         print("{}은(는) 3의 배수이다.".format(v))
#     if v % 5 == 0:
#         print("{}은(는) 5의 배수이다.".format(v))
#     if v % 8 == 0:
#         print("{}은(는) 8의 배수이다.".format(v))
# else:
#     print("어느 배수도 아니다.")

# n = int(input("근로소득 입력 : "))

# if n <= 20000000:
#     tax = n * 0.05
# elif n <= 40000000:
#     tax = n * 0.15
# elif n <= 80000000:
#     tax = n * 0.25
# else:
#     tax = n * 0.4

# print("근로소득 ", n, "원에 대한 소득세는 ", int(tax), "원입니다.")

# m = int(input("현 연봉을 입력하세요 : "))
# rk = input("근무평가등급을 입력하세요 : ")

# if rk == '우수':
#     up = m * 1.06
# elif rk == '보통':
#     up = m * 1.04
# else:
#     up = m * 1.02

# print("연봉인상액 : ", int(up-m))
# print("새 연봉인상액 :", int(up))
