# 2409 임수민

import random

def func_lotto():
    count = 6
    rand = set()

    while True:
        n = random.randint(1, 45)
        rand.add(n)
        if len(rand) == count:
            break
        
    r = list(rand)
    r.sort()

    return r

for i in range(1, 11, 1):
    print("당첨번호 : ", func_lotto())
