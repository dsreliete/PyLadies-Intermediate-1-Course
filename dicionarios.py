def mostra_chaves(d):
    for chave in d.keys():
        print(chave)

def mostra_valores(d):
    for valor in d.values():
        print(valor)

def mostra_pares_chave_valor(d):
    for item in d.items():
        chave, valor = item
        print(chave)
        print(valor)
