def naruto(a):
    for i in range(a):
        if i % 3 == 0 and i % 4 == 0:
            yield(i)

a = int(input())
for i in naruto(a):
    print(i, end = ' ')