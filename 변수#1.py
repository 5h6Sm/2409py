a = b = [1, 2, 3]
print(hex(id(a)))
print(hex(id(b)))
a[1] = 4
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))
