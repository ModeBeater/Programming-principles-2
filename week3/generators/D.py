def naruto(a,b):
    for i in range(a,b):
        yield(i * i)
a = int(input())
b = int(input())
for i in naruto(a,b):
    print(i, end = ' ')