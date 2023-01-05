def naruto1(grams):
    ounces = 28.3495231 * grams
    return ounces
def naruto2(F):
    C = (5 / 9) * (F - 32)
    return C
import math
import random
def naruto3(l):
    a = []
    for i in l:
        ok = 0
        if i == 2:
            a.append(i)
        if i > 2:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    ok = 1
            if ok == 0:    
                a.append(i)
    return a
import itertools
def naruto4(l):
    a = list(itertools.permutations(s))
    for i in a:
        sum = ''
        for j in i:
            sum += j
        print(sum)
def naruto5(numheads, numlegs):
    x = (numlegs / 2) - numheads
    y = numheads - x
    ans = "chickens: " + str(y) + " rabbits: " + str(x)
    return ans
def naruto6(a):
    arr = []
    for i in a:
        arr.append(i)
    cnt = len(arr) - 1
    ans = ''
    while cnt >= 0:
        ans += arr[cnt] + ' '
        cnt -= 1
    return ans
def naruto7(a):
    cnt = len(a) - 1
    while cnt > 0:
        if a[cnt] == a[cnt - 1] and a[cnt] == 3 :
            return True
            exit()
        cnt -= 1
    return False
def naruto8(a):
    ans = ''
    sum = 0
    for i in a:
        if i == 0 and sum == 0:
            ans += '0'
            sum += 1
        if i == 0 and sum == 1:
            ans += '0'
            sum += 1
        if i == 7 and sum == 2:
            ans += '7'
            sum += 1
    if ans == '007':
        return True
    else: return False
def naruto9(r):
    return (4/3) * math.pi * (r * r * r)
def naruto10(l):
    d = dict()
    for i in l:
        if i not in d.keys():
            d[i] = 1
        else: d[i] += 1
    for k,v in d.items():
        if v == 1:
            print(k)
def naruto11(a):
    b = []
    for i in a:
        b.append(i)
    b.reverse()
    if a == b:
        print('palindrome')
    else: print('not palindrome')
def naruto12(a):
    for i in a:
        while i > 0:
            print('*', end = '')
            i -= 1
        print('')
def naruto13(b,name):
    cnt = 0
    while True:
        a = int(input())
        if a == b:
            cnt += 1
            print('Good job,', name, end = '')
            print('! You guessed my number in ', cnt, end = '')
            print(' guesses!')
            exit()
        if a < b:
            cnt += 1
            print('Your guess is too low.')
        if a > b:
            cnt += 1
            print('Your guess is too big.')
print("What function do you want to use?")
print("grams per ounce \n"
      "Fahrenheit to Celsius \n"
      "Check Prime \n"
      "Permutation in string"
      "Chicken and Rabbits"
      "reverse words in string \n"
      "check if 33 contains \n"
      "check if 007 contains \n"
      "find volume sphere \n"
      "unique elements"
      "make a histogram \n"
      "check if the palindrome is a string \n"
      "Guess the number \n")
task = input()
if task == 'grams per ounce':
    a = int(input())
    print(naruto1(a))
if task == 'Fahrenheit to Celsius':
    a = int(input())
    print(naruto2(a))
if task == 'Check Prime':
    a = list(map(int, input().split()))
    print(naruto3(a))
if task == 'Permutation in string':
    s = str(input())
    naruto4(s)
if task == 'Chicken and Rabbits':
    print(naruto5(35,94))
if task == 'reverse words in string':
    a = input().split()
    print(naruto6(a))
if task == 'check if 33 contains':
    a = list(map(int, input().split()))
    print(naruto7(a))
if task == 'check if 007 contains':
    a = list(map(int, input().split()))
    print(naruto8(a))
if task == 'find volume sphere':
    a = int(input())
    print(naruto9(a))
if task == 'unique elements':
    a = map(str, list(input().split()))
    naruto10(a)
if task == 'check if the palindrome is a string':
    a = str(input())
    l = []
    for i in a:
        l.append(i)
    naruto11(l)
if task == 'make a histogram':
    a = list(map(int, input().split()))
    naruto12(a)
if task == 'Guess the number':
    print('Hello! What is your name?')
    name = str(input())
    print('Well,',name, end = '')
    print(', I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    b = random.randint(1,20)
    naruto13(b, name)
#from (namefile) import (namefunc)