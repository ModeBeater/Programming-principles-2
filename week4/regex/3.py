import re
file = open('input.txt', 'r')
text = file.read()
ans = r'(.*[a-z]_[a-z])'
txt = re.findall(ans, text)
print(txt)