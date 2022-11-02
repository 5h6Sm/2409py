'''
number = "881120-1068234"
print("연월일 : " + number[0:6])
print("숫자 : " + number[7:14])
# split을 사용하는 방법도 있음(나누기)

print("성별 : " + number[7])

list1 = [1, 3, 5, 4, 2]
print("원본 : ", list1)
list1.sort()
list1.reverse()
print("결과 : ", list1)'''

list1 = ['Life', 'is', 'too', 'short']

list2 = list(range(len(list1)))
print(list2)
