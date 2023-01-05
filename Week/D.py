import math
a = int(input())
b = str(input())
if b == 'k':
    ans = a / 1024
    c = int(input())
    d = round(ans,c)
    print(d)
if b == 'b':
    ans = a * 1024
    print(ans)