import calculator as cal

n1 = int(input("첫 번째 수는? "))
n2 = int(input("두 번재 수는? "))

print(n1, "+", n2, "=", cal.add(n1, n2))
print(n1, "-", n2, "=", cal.sub(n1, n2))
print(n1, "*", n2, "=", cal.mul(n1, n2))
print(n1, "/", n2, "=", cal.div(n1, n2))
