g = 1


def testScope(a):
    global g
    g = 2
    return g + a


print(testScope(1))
print(g)
