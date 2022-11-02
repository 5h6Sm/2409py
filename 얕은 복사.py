# shallow Copy

# [:] 를 사용한 얕은 복사
# 전체적인 리스트는 깊은 복사 처럼 보이지만, 리스트의 내부 리스트는 같은 주소값을 참조하고 있으므로 깊은 복사 같지만 얕은 복사이다.
'''print('=' * 50)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1[:]
print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)
print('arr.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}') '''


# copy 메서드를 이용한 얕은 복사
# [:] 과 비슷함. arr1과 arr2는 다른 주소를 가지고 있지만 리스트 내부의 리스트는 주소값이 동일함.
'''print('=' * 50)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1.copy()  # 여기서 복사 copy 메서드 이용
print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2에 값 추가
print('arr.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')'''

# copy 모듈의 copy 함수를 이용한 얕은 복사
# copy.copy(값) 마찬가지로 내부 리스트만 주소값이 동일함.
'''import copy
print('=' * 50)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = copy.copy(arr1)  # 여기서 복사 copy 함수 이용
print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2에 값 추가
print('arr.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')'''

# copy모듈의 copy 함수를 이용한 얕은 복사 - dictionary
import copy
print('=' * 50)
d1 = {'a': 'Mirim', 'b': [1, 2, 3]}
d2 = copy.copy(d1)  # dopy 모듈 얕은 복사
print("1. 전체 출력")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd1 : {d2}, address : {hex(id(d2))}')

print("\n2. 딕셔너리에 새 key, value 추가")
d2['c'] = 'Kimchi'
print("d2['c'] = 'Kimchi")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd1 : {d2}, address : {hex(id(d2))}')
# 딕셔너리 내부에 리스트 value
print("\n3. 딕셔너리 내부 리스트")
print(f"d1['b']: {d1['b']}, address: {hex(id(d1['b']))}")
print(f"d2['b']: {d2['b']}, address: {hex(id(d2['b']))}")

print("\n4. 딕셔너리 내부 리스트에 값 추가")
d1['b'].append('NO')
print("d1['b'].append('NO')")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d1['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n5. 리스트 전체 다시 확인")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd1 : {d2}, address : {hex(id(d2))}')
