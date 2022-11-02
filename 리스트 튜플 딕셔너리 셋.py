'''# 튜플 : 리스트와 유사, 순서가 존재.
# 리스트와는 달리 [] 대신 ()로 묶어서 표현하며 읽기 전용이다.
# 제공되는 함수는 리스트에 비해 적지만 속도는 그만큼 빠르다.
# 일반적인 경우에 데이터를 묶어서 한번에 전달하거나 여러 개의 값을 묶어서 한번에 반환할 경우에 사용됩니다.
# 자동 완성 기능을 통해서 보면 실제 제공되는 메서드가 count(), index() 정도만 제공되는 것을 볼 수 있습니다

from turtle import color


t = (1, 2, 3)
print(type(t))  # <class 'tuple'>

# 튜플이 주로 사용되는 경우

# 함수에서 하나 이상의 값을 리턴하는 경우


def calc(a, b):
    return a+b, a*b


x, y = calc(5, 4)  # 순서대로 각각 a+b, a*b로 나온다.
print(x, y)  # 9 20

# 문자열 포맷팅
print("id : %s, name : %s" % ("kim", "김유신"))

# 튜플에 있는 값을 함수 인수로 사용하는 경우
args = (3, 4)
print(calc(*args))

# set(세트) - union(), intersection(), difference() : 수학시간에 배운 집합과 동일. 유일한 값의 모임이며 순서는 없다.

a = {1, 2, 3, 4}
b = {3, 4, 4, 5}  # 값이 같은 것이 존재하므로 하나 삭제하고 하나의 값만 들어감. {
print(a)  # {1, 2, 3, 4}
print(b)  # {3, 4, 5}
print(type(a))  # <class 'set'>
print(type(b))  # <class 'set'>

print(a.union(b))  # 합집합. {1, 2, 3, 4, 5}
print(a.intersection(b))  # 교집합. {3, 4}
print(a.difference(b))  # 차집합. {1, 2}

# 집합을 기호로 표시하면
print(a | b)  # {1, 2, 3, 4, 5}
print(a & b)  # {3, 4}
print(a - b)  # {1, 2}

# 리스트, 세트, 튜플은 다음과 같이 생성자 list(), set(), tuple()을 이용해서 서로 변환 가능

# tuple -> set
a = set((1, 2, 3, 2))
print(a)  # {1, 2, 3}
print(type(a))  # <class 'set'>

# set -> list
b = list(a)
print(b)  # [1, 2, 3]
print(type(b))  # <class 'list'>

# list -> tuple
c = tuple(b)
print(c)  # [1, 2, 3]
print(type(c))  # <class 'tuple'>

# DICTIONARY(딕셔너리)

d = dict(a=1, b=2, c=3)
print(d)  # {'a': 1, 'b': 2, 'c': 3}
print(type(d))  # <class 'dict'>

colors = {"apple": "red", "banana": "yellow"}
print(colors)  # {'apple': 'red', 'banana': 'yellow'}

colors["cherry"] = "red"
print(colors)  # {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}

for item in colors.items():
    print(item)  # ('apple', 'red')
    # ('banana', 'yellow')
    # ('cherry', 'red')

for k, v in colors.items():
    print(k, v)  # apple red
    # banana yellow
    # cherry red

print(colors)
del colors["cherry"]
print(colors)  # {'apple': 'red', 'banana': 'yellow'}
colors.clear()
print(colors)  # {}

device = {"아이폰": 5, "아이패드": 10, "윈도우타블렛": 20}
device["아이맥"] = 15
device["아이폰"] = 6
print(device)  # {'아이폰': 6, '아이패드': 10, '윈도우타블렛': 20, '아이맥': 15}
del device["아이폰"]
print(device)  # {'아이패드': 10, '윈도우타블렛': 20, '아이맥': 15}

# 딕셔너리 메서드 - keys(), values()

phone = {"kim": "1111", "lee": "2222", "park": "3333"}
print(phone.keys())  # 키만 찾기

print(phone.values())  # 값만 찾기

print("park" in phone)  # park가 속해있으면 True
print("moon" in phone)  # moon이 속해있지 않기 때문에 False

p = phone  # phone은 딕셔너리
print(p)  # {'kim': '1111', 'lee': '2222', 'park': '3333'}

# 딕셔너리 - for 문으로 참조하기

d = {"a": 100, "b": 200, "c": 300}

for key in d.keys():
    print(key)
    # a
    # b
    # c

for value in d.values():
    print(value)
    # 100
    # 200
    # 300

# bool : 참과 거짓을 나타내는 자료형. 사용 가능한 값은 True, False
isRight = False
print(type(isRight))  # <class 'bool'>
print(1 < 2)  # True
print(1 != 2)  # True
print(1 == 2)  # False
print(True and True and False)  # False
print(True or False or False)  # True

# 수치를 논리연산자에 사용하는 경우
# 0은 False로 간주
# 음수를 포함한 다른 값은 모두 True로 간주
# 문자열을 논리연산자에 사용하는 경우에도 "만 False로 간주
# 값이 없는 상태를 나타내는 None도 False 간주
print(bool(0))  # False
print(bool(-1))  # True
print(bool("test"))  # True
print(bool(None))  # False
print(bool(""))  # False
print(bool(" "))  # True
print(bool(''))  # False
print(bool(' '))  # True
'''
