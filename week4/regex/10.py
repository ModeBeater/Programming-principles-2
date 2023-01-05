import re
file = open('input.txt', 'r')
text = file.read()
ans = r'([A-Z]+[a-z]*)'
txt = re.findall(ans, text)
print('_'.join(str(i).lower() for i in txt))