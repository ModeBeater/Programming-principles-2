import re
file = open('input.txt', 'r')
text = file.read()
ans = r'([A-Z]+[a-z]*)'
txt = re.findall(ans, text)
print(' '.join(str(i) for i in txt))