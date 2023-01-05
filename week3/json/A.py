import json
with open('sample.json', 'r') as txt:
    data = json.loads(txt.read())
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU')
print('-------------------------------------------------- --------------------  ------  ------')
max = 0
for i in data['imdata']:
    cnt = 0
    for j in i['l1PhysIf']['attributes']['dn']:
        print(j,end = '')
        cnt += 1
    if cnt > max:
        max = cnt
    while cnt < max:
        print(' ', end = '')
        cnt += 1
    print('        ', end = '')
    for k in i['l1PhysIf']['attributes']['descr']:
        print('        ', end = '')
        print(k,end = '',)
    print('                      ', end = '')
    for k in i['l1PhysIf']['attributes']['speed']:
        print(k,end = '')
    print('   ', end = '')
    for k in i['l1PhysIf']['attributes']['mtu']:
        print(k,end = '')
    print('')