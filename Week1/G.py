n = int(input())
d = dict()
demons = 0
for i in range(n):
    l = input().split()
    if l[1] not in d.keys():
        d[l[1]] = 1
    else: d[l[1]] += 1
m = int(input())
v = dict()
for i in range(m):
    l = input().split()
    if l[1] not in v.keys():
        v[l[1]] = int(l[2])
    else: v[l[1]] += int(l[2])
for key, value in sorted(d.items()):
    if key not in v.keys():
        demons += value
for key, value in sorted(d.items()):
    for key1, value1 in sorted(v.items()):
        if key1 == key:
            sum = value - value1
            if sum > 0:
                demons += sum
            break
print('Demons left:', demons)