import calculator

n1 = int(input("첫 번째 수는? "))
n2 = int(input("두 번재 수는? "))

print(n1, "+", n2, "=", calculator.add(n1, n2))
print(n1, "-", n2, "=", calculator.sub(n1, n2))
print(n1, "*", n2, "=", calculator.mul(n1, n2))
print(n1, "/", n2, "=", calculator.div(n1, n2))
