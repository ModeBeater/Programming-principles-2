a = str(input())
b = len(a)
c = 1
sum = 0
while b > 1:
    c = c * 2
    b = b - 1
for x in a:
    if str(x) == '1':
        sum = sum + c
    c = c / 2
print(int(sum))