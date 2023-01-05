n = int(input())
c = []
d = []
e = 0
for i in range(n):
    b = input().split()
    if int(b[0]) == 1:
        c.append(b[1])
    if int(b[0]) == 2:
        d.append(c[e])
        e += 1
for i in d:
    print(i, end = ' ')
