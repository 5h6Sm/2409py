def func_sum(p):
    sum = 0
    li = p.split(" ")
    list(li)
    for i in li:
        sum += int(i)
    return sum


in_list = input("데이타 입력 : ")
print("합 : ", func_sum(in_list))
