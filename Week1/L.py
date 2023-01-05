def solve(n):
    stack = ''
    k = '([{'
    l = ')]}'
    for a in n:
        if a in k:
            stack += a
        elif a in l:
            if stack == '':
                return False
            elif k[l.index(a)] == stack[-1]:
                stack = stack[:-1]
    return stack == ''
n = input()
if solve(n):
    print("Yes")
else:
    print("No")