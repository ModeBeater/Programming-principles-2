text=input()
text=text.replace('+',' ')
text=text.split()
thi=""
d={}
d['ONE']='1'
d['TWO']='2'
d['THR']='3'
d['FOU']='4'
d['FIV']='5'
d['SIX']='6'
d['SEV']='7'
d['EIG']='8'
d['NIN']='9'
d['ZER']='0'
def first(text,d):
    b = 0
    c = 3
    s = text[0]
    sum1 = ''
    # print(s)
    while c <= len(s):
        a = ''
        for i in range(b,c):
            a += s[i]
        for key,value in d.items():
            if a == key:
                sum1 += value
                break
        b += 3
        c += 3
    return sum1
def second(text,d):
    b = 0
    c = 3
    s = text[1]
    sum2 = ''
    # print(s)
    while c <= len(s):
        a = ''
        for i in range(b,c):
            a += s[i]
        for key,value in d.items():
            if a == key:
                sum2 += value
                break
        b += 3
        c += 3
    return sum2
# print(first(text,d))
# print(second(text,d))
sum = int(first(text,d)) + int(second(text,d))
ans = str(sum)
answer = ''
for i in ans:
    for key,value in d.items():
        if i == value:
            answer += key
print(answer)
# print(sum1)