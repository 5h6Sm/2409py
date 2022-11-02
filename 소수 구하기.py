# 입력 받은 수가 소수인지 판별하는 프로그램을 작성하라

n = int(input("숫자를 입력하세요 : "))
c = 1
if n == 1:
    c = 0
for i in range(2, int(n/2), 1):
    if n % i == 0:
        c = 0
        break

if c == 0:
    print("소수가 아닙니다.")
else:
    print("소수입니다.")
