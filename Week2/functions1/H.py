def naruto(a):
    ans = ''
    sum = 0
    for i in a:
        if i == 0 and sum == 0:
            ans += '0'
            sum += 1
        if i == 0 and sum == 1:
            ans += '0'
            sum += 1
        if i == 7 and sum == 2:
            ans += '7'
            sum += 1
    if ans == '007':
        return True
    else: return False
a = list(map(int, input().split()))
print(naruto(a))