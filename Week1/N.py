c = []
while(True):
    a = int(input())
    if a == 0:
        break
    c.append(a)
d = 0
e = len(c) - 1
while d < e:
    sum = int(c[d]) + int(c[e])
    if sum > 0:
        print(sum, end = ' ')
    d += 1
    e -= 1
if len(c) % 2 == 1:
    print(c[e])