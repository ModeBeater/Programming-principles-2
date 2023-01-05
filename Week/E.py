import math
a,b = map(int, input().split())
c = 2
if a <= 500 and (b % 2 == 0):
    while c < math.sqrt(a):
        if(a % c == 0):
            print("Try next time!")
            exit()
        c = c + 1
    print("Good job!")    
else:
    print("Try next time!")