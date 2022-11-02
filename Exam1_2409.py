# 2409 임수민

# 1
# n1 = int(input("점수 1 입력 : "))
# n2 = int(input("점수 2 입력 : "))
# n3 = int(input("점수 3 입력 : "))
# n4 = int(input("점수 4 입력 : "))
# n5 = int(input("점수 5 입력 : "))

# s = f'입력된 정수 {n1}, {n2}, {n3}, {n4}, {n5}'
# print(s)

# sum = n1 + n2 + n3 + n4 + n5
# print("합계 :", sum)

# avg = sum / 5
# s1 = '평균 : {0:0.2f}'.format(avg)
# print(s1)

# if avg >= 60.0:
#     print('{0:0.2f}점으로 합격입니다.'.format(avg))
# else:
#     print('{0:0.2f}점으로 불합격입니다.'.format(avg))

# 2

# x = int(input("정수 1 입력 : "))
# y = int(input("정수 2 입력 : "))
# print()

# if x > y:
#     x, y = y, x

# for i in range(x, y+1, 1):
#     print(f'{i}단')
#     for j in range(1, 9, 1):
#         print(f'{i} * {j} = {i*j}')
#     print()

# 3
value = {"메로나": [1000, 20], "비비빅": [700, 3], "바밤바": [850, 100]}

# 3-1
print("상품 조회")
st = '{0:^5}{1:^5}{2:^5}'.format('상품명', '가격', '수량')
print(st)
for i in value:
    s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
    print(s)
print()

# 3-2
print("1. 신규 상품 등록")
name = input("상품명 입력 : ")
price = int(input("가격 입력 : "))
num = int(input("수량 입력 : "))

value[name] = [price, num]

print(st)
for i in value:
    s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
    print(s)
print()

# 3-3
print("2. 상품 수정")
name = input("상품명 입력 : ")
print("1. 가격 수정\n2. 수량 수정")
n1 = int(input("메뉴 입력 : "))
if n1 == 1:
    n2 = int(input("가격 입력 : "))
    value[name][0] = n2
elif n1 == 2:
    n2 = int(input("수량 입력 : "))
    value[name][1] = n2

print(st)
for i in value:
    s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
    print(s)
print()

# 3-4
print("3. 상품 삭제")
name = input("상품명 입력 : ")
del value[name]
print(st)
for i in value:
    s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
    print(s)
print()

# 3-5
print("""1. 신규 상품 등록
2. 상품 수정
3. 상품 삭제
4. 상품 조회
0. 종료""")
inp = int(input("메뉴 입력 : "))

if inp == 0:
    print("\n프로그램을 종료합니다.\n")

# 3-6

print("""1. 신규 상품 등록
2. 상품 수정
3. 상품 삭제
4. 상품 조회
0. 종료""")
inp = int(input("메뉴 입력 : "))
print()

while True:
    if inp == 1:
        print("1. 신규 상품 등록")
        name = input("상품명 입력 : ")
        price = int(input("가격 입력 : "))
        num = int(input("수량 입력 : "))

        value[name] = [price, num]
        print(st)
        for i in value:
            s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
            print(s)
        print()

    if inp == 2:
        print("2. 상품 수정")
        name = input("상품명 입력 : ")
        print("1. 가격 수정\n2. 수량 수정")
        n1 = int(input("메뉴 입력 : "))
        if n1 == 1:
            n2 = int(input("가격 입력 : "))
            value[name][0] = n2
        elif n1 == 2:
            n2 = int(input("수량 입력 : "))
            value[name][1] = n2

        print(st)
        for i in value:
            s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
            print(s)
        print()

    if inp == 3:
        print("3. 상품 삭제")
        name = input("상품명 입력 : ")
        del value[name]

        print(st)
        for i in value:
            s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
            print(s)
        print()

    if inp == 4:
        print("상품 조회")
        print(st)
        for i in value:
            s = '{0:<5} {1:>5} {2:>5}'.format(i, value[i][0], value[i][1])
            print(s)
        print()

    if inp == 0:
        print("프로그램을 종료합니다.")
        break

    print("""1. 신규 상품 등록
2. 상품 수정
3. 상품 삭제
4. 상품 조회
0. 종료""")
    inp = int(input("메뉴 입력 : "))
    print()
