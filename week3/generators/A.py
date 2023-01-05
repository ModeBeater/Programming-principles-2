def naruto(a):
    for i in range(a):
        yield(i * i)


a = int(input()) + 1
for i in naruto(a):
    print(i, end = ' ')