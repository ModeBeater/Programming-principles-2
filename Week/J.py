a = input().split()
sum = ''
for x in a:
    if len(x) >= 3:
        sum = sum + str(x) + ' '
print(sum)
    