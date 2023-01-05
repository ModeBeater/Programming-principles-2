import re
file = open('input.txt', 'r')
text = file.read()
ans = r'(a.*b)'
txt = re.findall(ans, text)
print(txt)