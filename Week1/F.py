d = dict()
for i in range(int(input())):
    inp = input().split()
    if inp[0] not in d.keys(): 
        d[inp[0]] = 0
    d[inp[0]] += int(inp[1])
mx = max(d.values())
d = sorted(d.items(), key = lambda x:x[0])

for i in d:
    if mx - i[1] > 0:
        e = mx - i[1]
        print(i[0], 'has to receive',e, 'tenge')
    if mx - i[1] == 0:
        print(i[0], 'is lucky!')