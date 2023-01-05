c = []
while(True):
    s = str(input())
    if s == '0':
        break
    d,m,y = s.split()
    e = [d,m,y]
    c.append(e)
c.sort(key = lambda x:x[0])
c.sort(key = lambda x:x[1])
c.sort(key = lambda x:x[2])
for i in c:
    print(i[0], i[1], i[2])
