def naruto(a):
    cnt = len(a) - 1
    while cnt > 0:
        if a[cnt] == a[cnt - 1] and a[cnt] == 3 :
            return True
            exit()
        cnt -= 1
    return False
a = list(map(int, input().split()))
print(naruto(a))