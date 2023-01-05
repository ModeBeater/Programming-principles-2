a = str(input())
b = str(input())
c = []
cnt = 0
sum = 0
summ = 0
for x in a:
    if b == x:
        sum = sum + 1
for x in a:
    if b == x and summ == 0:
        c.append(cnt)
    if b == x:
        summ = summ + 1
    if b == x and summ == sum:
        c.append(cnt)
    cnt = cnt + 1
if sum > 1:
    d = str(c[0]) + ' ' + str(c[1])
    print(d)
if sum == 1:
    print(c[0])