a = str(input()) # Вводим строку
sum = '' # создаем пустую строку
for x in a: # цикл для проверки строки
    if ord(str(x)) >= 65 and ord(str(x)) <= 90: # условие для нахождения заглавных букв и перевод в строчные
        b = ord(str(x)) + 32
        c = chr(b)
        sum = sum + str(c)
    else: sum = sum + x # условие если нет заглавных букв
print(sum) 