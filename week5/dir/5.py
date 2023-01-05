file = open('input.txt', 'w')
a = list(input())
file.writelines(a)
file.close()