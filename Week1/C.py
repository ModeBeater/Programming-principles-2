n = int(input())
arr = [[0] * n for i in range(n)]
a = 0
for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = a * a
            a += 1
i = 0
j = 0
a = 0
while j < n:
    arr[i][j] = a
    a += 1
    j += 1
j = 0
a = 0
while i < n:
    arr[i][j] = a
    a += 1
    i += 1
for r in arr:
    print(' '.join([str(e) for e in r]))
