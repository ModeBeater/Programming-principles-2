import re
file = open('input.txt', 'r')
text = file.read()
ans = r'(ab{2,3})'
txt = re.findall(ans, text)
print(txt)