n = int(input())
c = []
for i in range(n):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    l = str(input())
    for j in l:
        if j >= 'A' and j <= 'Z':
            sum1 += 1
        if j >= 'a' and j <= 'z':
            sum2 += 1
        if j >= '0' and j <= '9':
            sum3 += 1
    if sum1 >= 1 and sum2 >= 1 and sum3 >= 1:
        if l not in c:
            c.append(l)
print(len(c))
for i in sorted(c):
    print(i)