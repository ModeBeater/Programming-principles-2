def naruto(a):
    m = a 
    for i in range(a + 1):
        yield(m)
        m -= 1
a = int(input())
for i in naruto(a):
    print(i, end = ' ')