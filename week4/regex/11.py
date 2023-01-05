import re
file = open('row.txt', 'r', encoding = 'utf-8')
text = file.read()
n = 1
company = re.findall(r'Филиал (.+)', text)
BIN = re.findall(r'БИН (.+)', text)
print('Name of the company:',company[0])
print('BIN number:',BIN[0])
adress = re.findall(r'Время: .+\n(.+)', text)
data = re.findall(r'Время: (.+)', text)
name = re.findall(r'(.+)\n.+\n.+\nСтоимость', text)
kolvo = re.findall(r'(.+),000', text)
price = re.findall(r'x (.+),00', text)
for i in kolvo:
    print(n, end = '')
    print('. ', end = '')
    print('Title:',name[n - 1])
    print('Cout:',kolvo[n - 1])
    price1 = ''
    for i in price[n - 1]:
        if i >= '0' and i <= '9':
            price1 += i
    sumka = int(price1) * int(kolvo[n - 1])
    print('Unit price:', price1 + ',00')
    print('Total price:', f'{sumka},00')
    print('Date:',data[0])
    print('Adress:', adress[0])
    n += 1
    print('')