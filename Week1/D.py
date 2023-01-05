n = int(input())
arr = [['.'] * n for i in range(n)]
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i >= j:
                arr[i][j] = '#'
if n % 2 == 1:
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                arr[i][j] = '#'
for r in arr:
    print(''.join([str(e) for e in r]))