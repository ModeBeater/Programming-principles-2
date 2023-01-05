a = input()
u = 0
l = 0
for i in str(a):
    if i >= 'A' and i <= 'Z':
        u += 1
    if i >= 'a' and i <= 'z':
        l += 1
print('lower letters:', l)
print('upper letters:', u) 