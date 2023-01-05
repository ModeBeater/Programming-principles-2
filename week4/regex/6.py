import re
file = open('input.txt', 'r')
text = file.read()
ans = r'([., ])'
txt = re.sub(ans, ':', text)
print(txt)