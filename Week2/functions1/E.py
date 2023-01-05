import itertools
def naruto(l):
    a = list(itertools.permutations(s))
    for i in a:
        sum = ''
        for j in i:
            sum += j
        print(sum)
s = str(input())
naruto(s)
    