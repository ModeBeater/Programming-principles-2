import re
file = open('input.txt', 'r')
text = file.read()
ans = r'(\wa\w+b)'
txt = re.findall(ans, text)
print(txt)