#2409 임수민

def star(li):
    num = [0, 0, 0, 0, 0]
    mx = max(li)
    mn = min(li)
    for i in li:
        if i >= 90:
            num[0] = num[0]+1
        elif i >= 80:
            num[1] = num[1]+1
        elif i >= 70:
            num[2] = num[2]+1
        elif i >= 60:
            num[3] = num[3]+1
        else:
            num[4] = num[4]+1

    str_star = "*"
    s = '{0:<19}   :  {1:<5}'.format('90점 이상',str_star*num[0])
    print(s)
    s = '{0:<20}   :  {1:<5}'.format('80점 대',str_star*num[1])
    print(s)
    s = '{0:<20}   :  {1:<5}'.format('70점 대',str_star*num[2])
    print(s)
    s = '{0:<20}   :  {1:<5}'.format('60점 대',str_star*num[3])
    print(s)
    s = '{0:<19}   :  {1:<5}'.format('60점 미만',str_star*num[4])
    print(s)
    s = '{0}  :  {1:<5}'.format('최고점수',mx)
    print(s)
    s = '{0}  :  {1:<5}'.format('최저점수',mn)
    print(s)

str = input("점수 입력 : ")
li = str.split(" ")

li2 = []
for i in li:
    li2.append(int(i))

star(li2)
