l = list(map(int, input().split()))
a = 1
c = []
if l[1] == 0:
    print(0)
    exit()
while a < len(l) - 1:
    b = l[a]
    c.append(a)
    if b == 0:
        sum0 = 0
        while l[a] == 0:
            a += 1
            sum0 += 1
        a -= sum0
        d = 0 + sum0
        a -= 1
        while l[a] <= d:
            a -= 1
            d += 1
            if a == c[len(c) - 1] or a == 1:
                print(0)
                exit()
        c.append(a)
        b = l[a]
    while b > 0:
        a += 1
        b -= 1
print(1)
