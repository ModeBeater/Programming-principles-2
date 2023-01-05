a = int(input())
c = []
max = 0 
b = list(map(int, input().split()))
for x in b:
    if x > max:
        max = x
    c.append(x)
if b.count(max) >= 2:
    d = max * max
    print(d)
    exit()
maxx = 0
for x in c:
    if x > maxx and x != max:
        maxx = x
d = maxx * max
print(d)