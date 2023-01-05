import math

a = input().split()
x = int(a[0])
y = int(a[1])
n = int(input())
d = []
for i in range(n):
    b = input()
    c = b.split()
    x1 = int(c[0])
    y1 = int(c[1])
    sum = math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))
    d.append((b,sum))
    d.sort(key = lambda x:x[1])

for i in d:
    print(i[0])
        
