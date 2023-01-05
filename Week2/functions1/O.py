import random
def naruto(b, name):
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
print('Hello! What is your name?')
name = str(input())
print('Well,',name, end = '')
print(', I am thinking of a number between 1 and 20.')
print('Take a guess.')
b = random.randint(1,20)
naruto(b, name)
    