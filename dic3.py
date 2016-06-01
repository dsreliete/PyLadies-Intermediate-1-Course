cat = {'nome': 'Filoca', 'mãe': True, 'filhotes':9, 'idade': 4,
'raça': 'indefinida', 'cor': ['preta','branca'], 'localização': (15,20)}
print(cat)

print('values\n')
for valor in cat.values():
    print(valor)

print('*************************************************')
print('keys\n')
for chave in cat.keys():
    print(chave)

print('*************************************************')
print('chave - valor\n')
for chave, valor in cat.items():
    print('chave: ' + str(chave) + '\t valor: ' + str(valor))
