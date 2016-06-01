linguas={'portugues':'gato', 'ingles':'cat', 'alemao':'katse', 'espanhol':'gato', 'frances':'chat'}
print(linguas)
linguas['finlandes'] = 'kissa'
linguas['italiano'] = 'gatto'
print(linguas.items())
print(linguas.keys())
print(linguas.values())

list = linguas.items()
print('list = ', list)

print('linguas.get(portugues, desconhecido)' + linguas.get('portugues', 'desconhecido'))
print(linguas.get('dfudf', 'desconhecido'))

print('******************************************************')
for key in linguas.keys():
    print(key)
print('******************************************************')
for value in linguas.values():
    print(value)
print('******************************************************')
for key, value in linguas.items():
    #print(value)
    #print(key)
    if 'a' in key:
        print('tem A')
        print('\n')
print('******************************************************')
for item in linguas.items():
    print(item)
    chave, valor = item
    print(chave)
    print(valor)
print('******************************************************')        
print(sorted(linguas.keys()))
print(sorted(linguas.values()))
print('******************************************************')
for k in sorted(linguas.keys()):
    print(k)
    print(linguas.get(k))
print('******************************************************')
print(sorted('eliete', reverse=True))
print('******************************************************')
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3

for key in d:
    print(key, d[key])

    
    
