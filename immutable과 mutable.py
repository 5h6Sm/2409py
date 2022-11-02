# mutable(변하기 쉬운), immutable(불변) 객체
# mutable : 변경되는 객체(객체의 상태를 변경할 수 있음)
# 종류 : list, set, dictionary
# immutable : 변경되지 않는 객체(객체의 상태를 변경할 수 없음)
# 종류 : int, float, str, bool, tuple

# immutable 객체(상태 변경 X)
'''print("immutable 객체")
a = 99
b = 99
c = 99
d = 99
e = 99
print(hex(id(a)))  # 0x1d1ead00d30
print(hex(id(b)))  # 0x1d1ead00d30
print(hex(id(c)))  # 0x1d1ead00d30
print(hex(id(d)))  # 0x1d1ead00d30
print(hex(id(e)))  # 0x1d1ead00d30

# immutable 객체는 모두 같은 주소로 출력됨. 99가 들어가는 방을 만들고 99의 값을 가진 모든 변수가 99가 들어있는 방을 가르키는 것.
# 하나의 immutable 값에 여러 개의 참조가 붙게 됨. 99라는 값이 존재하는

# mutable 객체
print("\nmutable 객체")
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
arr3 = [1, 2, 3]
arr4 = [1, 2, 3]
print(hex(id(arr1)))
print(hex(id(arr2)))
print(hex(id(arr3)))
print(hex(id(arr4)))

# mutable 객체는 데이터가 같아도 다른 방을 잡음.
# arr1, append 와 같이 mutable한 리스트는 값이 자유롭게 바뀔 수 있기 때문에, 각각의 메모리를 할당해주는게 관리가 더 용이하다고 판단

# immutable 객체 - int 값 변경시
# mutable 객체
print("=" * 50)
print("immutable 객체 예제.")
print("=" * 50)
print("1. int 값이 변경되면?")
num1 = 99
num2 = 99
num3 = 99
num4 = 99
print(f"num1 값: {num1} \t주소: {hex(id(num1))}")
print(f"num2 값: {num2} \t주소: {hex(id(num2))}")
print(f"num3 값: {num3} \t주소: {hex(id(num3))}")
print(f"num4 값: {num4} \t주소: {hex(id(num4))}")
num1 += 1  # num1 값 증가
num3 += 1  # num3 값 증가
num4 += 1  # num4 값 증가
print(f"num1 값: {num1} \t주소: {hex(id(num1))}")
print(f"num2 값: {num2} \t주소: {hex(id(num2))}")
print(f"num3 값: {num3} \t주소: {hex(id(num3))}")
print(f"num4 값: {num4} \t주소: {hex(id(num4))}")

# immutable 객체 - str 값 변경시
print("\n2. str  값이 변경되면?")
s1 = "BlockDmasak"
s2 = "BlockDmasak"
s3 = "BlockDmasak"
s4 = "BlockDmasak"
print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")
s1 = s1.replace('D', 'ZZZ')  # replace 로 값을 변경하고, 새로운 문자열을 s1에 대입하게 됨
s2 = "BlockZZZMask"  # replace 로 변경한 문자열과 동일한 문자열로 변경함
s4 = s3.upper()
print(f"s1 값 : {s1} \t주소 : {hex(id(s1))}")
print(f"s2 값 : {s2} \t주소 : {hex(id(s2))}")
print(f"s3 값 : {s3} \t주소 : {hex(id(s3))}")
print(f"s4 값 : {s4} \t주소 : {hex(id(s4))}")'''

# immutable  객체는 거의 대부분 같은 값을 참조한다.(같은 값이면 보통 같은 주소값을 가짐)(동일한 메모리를 참조하는 것이 특징, 항상 값이 동일하다고 주소값이 같은게 아님)

# mutable 객체(상태 변경 가능) - list, set, dicitionary...
# mutable 객체(아래 예제는 list로 사용)
'''print("=" * 50)
print("mutable 객체 예제")
print("=" * 50)
print("1. list 값이 변경되면?")
arr1 = ['a', 'b', 77]
arr2 = ['a', 'b', 77]
arr3 = ['a', 'b', 77]
print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
print(f"arr3 값 : {arr3} \t주소 : {hex(id(arr3))}")
arr1.append(10)  # ['a', 'b', 77, 10']
arr2.append(10)  # ['a', 'b', 77, 10']
print(f"arr1 값 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 값 : {arr2} \t주소 : {hex(id(arr2))}")
print(f"arr3 값 : {arr3} \t주소 : {hex(id(arr3))}")

# mutable에서 볼 것은 두 가지
# arr1, arr2, arr3의 값이 설사 같다 하더라도 메모리에 각각 값들이 생성되고 참조를 각각 하기 때문에 다들 주소가 다르게 나온다,
# arr1, arr2, arr3에서 내부의 값이 변한다 하더라도 최초 참조 메모리 주소가 변경되지 않는다.

# mutable 객체(아래 예제는 dictionary로 사용)
print("\n2. dictionary 값이 변경되면?")
d1 = {'a': 11, 'b': 22, 'c': 33}
d2 = {'a': 11, 'b': 22, 'c': 33}
d3 = {'a': 11, 'b': 22, 'c': 33}
print(f"d1 값 : {d1} \t주소 : {hex(id(d1))}")
print(f"d2 값 : {d2} \t주소 : {hex(id(d2))}")
print(f"d3 값 : {d3} \t주소 : {hex(id(d3))}")
d1['a'] = 99
d2['d'] = 44
print(f"d1 값 : {d1} \t주소 : {hex(id(d1))}")
print(f"d2 값 : {d2} \t주소 : {hex(id(d2))}")
print(f"d3 값 : {d3} \t주소 : {hex(id(d3))}")'''

# 얕은 복사, 깊은 복사를 하기 위해서 mutable, immutable이 필요한 것.

# mutable 객체 안에 있는 immutable
# mutable 객체
'''print("=" * 50)
print("mutable 객체 요소로 존재하는 immutable, mutable")
print("=" * 50)
arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']
# 리스트(immutable)객체의 주소
print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

# 리스트 내부의 mutable 요소
print("=" * 50)
print('리스트 내부의 mutable 요소들')
print(f"arr1[0] : {arr1[0]} \t 주소 : {hex(id(arr1[0]))}")
print(f"arr2[0] : {arr2[0]} \t 주소 : {hex(id(arr2[0]))}")
print(f"arr1[1] : {arr1[1]} \t 주소 : {hex(id(arr1[1]))}")
print(f"arr2[1] : {arr2[1]} \t 주소 : {hex(id(arr2[1]))}")
print(f"arr1[3] : {arr1[3]} \t 주소 : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]} \t 주소 : {hex(id(arr2[3]))}")
print(f"arr1[4] : {arr1[4]} \t 주소 : {hex(id(arr1[4]))}")
print(f"arr2[4] : {arr2[4]} \t 주소 : {hex(id(arr2[4]))}")

print(f"arr1[2] : {arr1[2]} \t 주소 : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]} \t 주소 : {hex(id(arr2[2]))}")'''

'''arr1 = [55, 66, [11, 22], 'a', 'b']
arr2 = [55, 66, [11, 22], 'a', 'b']

arr1 = [1, 2, 3]
arr2 = arr1

print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")

arr1.append(4)

print(f"arr1 : {arr1} \t주소 : {hex(id(arr1))}")
print(f"arr2 : {arr2} \t주소 : {hex(id(arr2))}")'''
