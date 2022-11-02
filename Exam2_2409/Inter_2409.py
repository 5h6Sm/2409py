# 2409 임수민

def intersect(a, b):
    s1 = set(a)
    s2 = set(b)
    s3 = set()
    for i in s1:
        for j in s2:
            if i == j:
                s3.add(i)

    return s3


a1 = input("첫 번째 문자열 입력 : ")
b1 = input("두 번째 문자열 입력 : ")

result = list(intersect(a1, b1))
result.sort()
print(result)
