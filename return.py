# return 값이 없는 경우
# def setValue(newValue):
#     x = newValue


# retValue = setValue(10)
# print(retValue)

# # return 값이 있는 경우


# def swap(x, y):
#     return y, x


# print(swap(1, 2))
# retValue = swap(1, 2)
# print(retValue[0], retValue[1])

# def sum(*nums):
#     result = 0
#     for i in nums:
#         result += i
#     return result

# result = sum(1, 3)
# print("1 + 3 = ", result)

# print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))

# min retrun
# def min(*args):
#     result = args[0]
#     for i in args:
#         if i < result:
#             result = i
#     return result


# result = min(1, 3)
# print("min(1, 3) = ", result)
# print("min(0, 3, -11) = ", min(0, 3, -11))

# 리스트로 여러 값을 리턴
# def multi_num(multi, start, end):
#     result = []
#     for n in range(start, end):
#         if n % multi == 0:
#             result.append(n)
#     return result


# multi2 = multi_num(17, 1, 200)
# print("multi_num(17,1,200) : ", multi2)
# print()
# multi3 = multi_num(3, 1, 100)
# print("multi_num(3,1,100) : ", multi3)

# print()


# def min_max(*args):
#     min = args[0]
#     max = args[0]
#     for arg in args:
#         if min > arg:
#             min = arg
#         if max < arg:
#             max = arg
#     return min, max


# print(min_max(52, -3, 23, 89, -21))
# min_value, max_value = min_max(52, -3, 23, 89, -21)
# print("최젓값 :", min_value)
# print("최곳값 :", max_value)

# 혼자 해 보기
def div_name(fullname):
    return fullname[0], fullname[1:]


surname, name = div_name("임수민")
print("성 :", surname, "\n이름 :", name)
