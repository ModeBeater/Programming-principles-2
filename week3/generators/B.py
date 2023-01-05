def naruto(a):
    for i in range(a):
        if i % 2 == 0:
            yield(i)

a = int(input()) + 1

print(','.join(str(i) for i in naruto(a)))