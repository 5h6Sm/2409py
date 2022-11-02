from calculator import add
from calculator import sub
from calculator import mul
from calculator import div

n1 = int(input("첫 번째 수는? "))
n2 = int(input("두 번재 수는? "))

print(n1, "+", n2, "=", add(n1, n2))
print(n1, "-", n2, "=", sub(n1, n2))
print(n1, "*", n2, "=", mul(n1, n2))
print(n1, "/", n2, "=", div(n1, n2))
