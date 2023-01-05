txt = input().split()
n = int(txt[0])
if len(txt) == 2:
    x = int(txt[1])
else: x = int(input())
i = 0
arr = []
while i < n:
    ans = x + 2 * i
    i += 1
    arr.append(ans)
i = 1
sum = arr[0]
while i < n:
    sum = sum ^ arr[i]
    i += 1
print(sum)    