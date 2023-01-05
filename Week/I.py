a = int(input())
c = '@gmail.com'
d = []
while a > 0:
    b = str(input())
    if b.find(c) != -1:
        e = ''
        for x in b:
            if x == '@':
                d.append(e)
                break
            else: e = e + x
    a = a - 1
for x in d:
    print(x)