def naruto(a):
    arr = []
    for i in a:
        arr.append(i)
    cnt = len(arr) - 1
    ans = ''
    while cnt >= 0:
        ans += arr[cnt] + ' '
        cnt -= 1
    return ans
a = input().split()
print(naruto(a))