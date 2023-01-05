def naruto(l):
    d = dict()
    for i in l:
        if i not in d.keys():
            d[i] = 1
        else: d[i] += 1
    for k,v in d.items():
        if v == 1:
            print(k)
a = map(str, list(input().split()))
naruto(a)