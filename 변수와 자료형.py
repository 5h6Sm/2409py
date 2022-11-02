'''
strA = "Hello python"
x = 5
y = 3.14

print(type(strA))
print(type(x))
print(type(y))
'''

# 파이썬 키워드 소개
'''
import keyword
print(keyword.kwlist) 
'''
'''
print("py""thon")
print("py" + "thon")
print("py"*3)
'''
'''
strA = "python"
print(strA[0:1])  # p
print(strA[1:3])  # yt
print(strA[:2])  # py
print(strA[-2:])  # on
print(strA[:])  # python

strB = "python is powerful"
print(strB[0])  # p
print(strB[0:6])  # python
print(strB[:6])  # python

strC = "python is powerful"
print(strB[-1])  # l
print(strB[-2])  # u
print(strB[-3:])  # ful
print(strB[-8:])  # powerful

strD = "python is powerful"
print(strD[7:18])  # is powerful
print(strD[:])  # python is powerful
print(strD[::2])  # pto spwru


print(strB[-11:-9])  # is
print(strB[-18:-11])  # python
'''

# 리스트(list)
# 값의 나열. 데이터를 모아 놓은 목록. 순서가 존재하며 여러 가지 자료형을 담을 수 있다. 다른 프로그래밍 언어의 배열 대신 사용


from pkgutil import extend_path
colors = ["red", "green", "blue"]
print(colors)  # ['red', 'green', 'blue']
print(type(colors))  # <class 'list'>

# 리스트 메서드 - append(), insert(), index(), count(), pop(), remove(), extend(), sort(), reverse()

# append() 메서드 : 기존 리스트에 값을 추가
print(colors)  # ['red', 'green', 'blue']
colors.append("blue")
print(colors)  # ['red', 'green', 'blue', 'blue']

# insert() 메서드 : 원하는 위치에 추가
print(colors)  # ['red', 'green', 'blue', 'blue']
colors.insert(1, "black")
print(colors)  # ['red', 'black', 'green', 'blue', 'blue'] : 인덱스 시작은 0부터 시작.

# index() : 어떤 값이 어디에 있는지 확인. 2번째 인자를 지정하지 않으면 처음부터 검색을 하고, 지정을 하면 지정된 방 번호 이후의 아이템의 방 번호 리턴
print(colors)  # ['red', 'black', 'green', 'blue', 'blue']
print(colors.index("red"))  # 0
colors += ["red"]
print(colors)  # ['red', 'black', 'green', 'blue', 'blue', 'red']
print(colors.index("red", 1))  # 5
colors += "red"
# ['red', 'black', 'green', 'blue', 'blue', 'red', 'r', 'e', 'd']
print(colors)

# count() 메서드 : 현재 해당 값의 개수를 반환
# pop() 메서드 : 값을 뽑아내서 반환(pop된걸 반환(return)함)
print(colors)
print(colors.count("red"))
print(colors.pop())
print(colors.pop())
print(colors.pop(1))  # 1번 위치가 pop됨(반환) -> 그걸 출력함
print(colors)
print()

# remove() 메서드 : 단순히 해당 값을 삭체(반환하지않음)
print(colors)
print(colors.remove("blue"))  # blue가 없어짐
print(colors)

# 같은 값이 있을 때
print(colors)
print(colors.remove("red"))  # 앞쪽 red가 없어짐
print(colors)

# extend() 메서드 : 데이터(리스트) 추가
print(colors)
colors.extend(["blue", "yellow", "white"])
print(colors)

# sort() 메서드 : 오름차순 정렬
# reverse() : 내림차순 정렬
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)
