import repeater
s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")
repeater.repeat(s, int(n))
print()
repeater.repeat(s)
print()
repeater.once(s)
