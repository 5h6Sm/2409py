# 2409 임수민

def isPrimeNumber(num):
    count = 0

    value = 0
    for i in range(2, num, 1):
        if num % i == 0:
            value = 1

    if value == 0:
        return True
    else:
        return False

count = 0

print("1 ~ N 까지의 소수와 그 갯수를 구하는 프로그램")

num = int(input("N 입력 : "))
print("소수 : ", end="")

for i in range(2, num):
    result = isPrimeNumber(i)
    if result == True:
        print(i," ", end="")
        count = count+1

print()
print(f"1 ~ {num}까지 소수의 갯수 : {count}")

# print("소수 : ", end="")
# for i in range(2, num+1, 1):
#     isPrimeNumber(num)
