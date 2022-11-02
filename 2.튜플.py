t = ()
print(t)
xy = (2560, 1440)
print(xy)
color = 129, 247, 216
print(color)
print(xy + color)
print(xy * 2)

# 2. 패킹과 언패킹 : 괄호를 생량해도 하나로 묶어서 대입되고, 여러 개로 대입할 때도 하나씩 들어간다.
color = 129, 247, 216
red, green, blue = color
print(red)
print(green)
print(blue)

x, y = 1920, 1080
print(x)
print(y)

# 3. 튜플 활용
x = 2560
y = 1440
x, y = y, x
print(x)
print(y)


a = (123, "abc", True, 123)
print(a[1])
#a[1] = 2
# 'tuple' object does not support item assignment 튜플은 값을 수정할 수 없다, 오류 발생
print(a.index("abc"))
print(a.count(123))

t = (1, 2, 3)
t += (4,)  # 추가하는 방법. ,(콤마)를 찍어줘야하낟.
print(t)
