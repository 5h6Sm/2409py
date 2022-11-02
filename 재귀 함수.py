# recursive
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)


print(factorial(5))

# help 함수

help(print)
