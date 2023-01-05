def naruto(a):
    b = []
    for i in a:
        b.append(i)
    b.reverse()
    if a == b:
        print('palindrome')
    else: print('not palindrome')
a = str(input())
l = []
for i in a:
    l.append(i)
naruto(l)