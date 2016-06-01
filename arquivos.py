import os
from collections import Counter

arq1 = '/Users/eliete/Desktop/PyLadiesSP/interm/intermediario1/zen.txt'
arq2 = '/Users/eliete/Desktop/PyLadiesSP/interm/intermediario1/zen2.txt'

def continua_escrevendo_novo_zen(arq, novoArq, palavra):
    with open(arq, 'r') as l:
        for linha in l:
            if not palavra in linha:
                with open(novoArq, 'a') as e:
                    e.write(linha)

def ler(a):
    with open(a, 'r') as l:
        conteudo = l.read()
        print(conteudo)

continua_escrevendo_novo_zen(arq1, arq2, 'is')
ler(arq2)

texto = 'eliete eliete eliete eliete renan renan renan sheldon sheldon felipe mariana'
nome = texto.split( )
cont = Counter(nome)
print(cont)

def contador_palavras(arq):
    with open(arq, 'r') as l:
        conteudo = l.read()
        palavra = conteudo.split()
        quantidade = Counter(palavra)
        for pal, qtd in quantidade.items():
            print('Palavra %s : %s x' %(pal, qtd))

contador_palavras(arq1)



