a = list(map(str, input().split()))
c = []
for i in a:
    l = ''
    for j in i:
        if j >= 'A' and j <= 'Z':
            l += j
            continue
        if j >= 'a' and j <= 'z':
            l += j
            continue
        else: break
    if l not in c:
        c.append(l)
print(len(c))
for i in sorted(c):
    print(i)