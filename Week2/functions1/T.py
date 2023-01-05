def histogram(a):
    for i in a:
        while i > 0:
            print('*', end = '')
            i -= 1
        print('')
a = list(map(int, input().split()))
histogram(a)