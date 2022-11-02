import random
origin = [0, 0, 0]
# 데이터 생성
for i in range(0, 3):
    # origin[i] = int(random.randint(0, 9)*10)
    # origin[i] = int(random.random(0, 9)*10)
    # origin[i] = random.choice([0,1,2,3,4,5,6,7,8,9])
    origin[i] = random.randrange(0, 10)

    for j in range(0, i):
        while origin[i] == origin[j]:
            origin[i] = random.randint(0, 9)
    print(origin[i], end=" ")
print()

cnt = 1
while True:
    # 유저 데이터 입력
    myData = [0, 0, 0]
    myData = input(f"{cnt}회 숫자 입력 : ").split(" ")
    myData = list(map(int, myData))
    cnt = cnt+1

    # 판정
    strike = 0
    for i in range(0, 3):
        if(origin[i] == myData[i]):
            strike = strike+1
    print(strike, "strike")

    # ball
    ball = 0
    for i in range(0, 3):  # origin의 방번호
        for j in range(0, 3):  # myData의 방번호
            if (i != j):  # ball 처리 i==j strike에서 처리됨
                if (origin[i] == myData[j]):
                    ball = ball+1
    print(ball, " ball")

    if(strike == 3):
        print(f"축하합니다.{cnt}회만에 맞추었습니다.")
        break
    elif(cnt == 0):
        print(f"실패했습니다.{cnt}회가 되었습니다.")
        break
