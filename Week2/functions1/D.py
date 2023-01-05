import math
def filter_prime(l):
    a = []
    for i in l:
        ok = 0
        if i == 2:
            a.append(i)
        if i > 2:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    ok = 1
            if ok == 0:    
                a.append(i)
    return a
a = list(map(int, input().split()))
print(filter_prime(a))