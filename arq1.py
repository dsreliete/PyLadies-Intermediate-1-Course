import os

path = '/Users/eliete/Desktop/PyLadiesSP/interm/intermediario1/zen.txt'
if os.path.isfile(path):
    with open(path, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

path2 = '/Users/eliete/Desktop/PyLadiesSP/interm/test/teste1.txt'
with open (path2, 'a') as arq:
    arq.write('teste')

with open(path2, 'r') as a:
    conteudo = a.read()
    print(conteudo)

path3 = '/Users/eliete/Desktop/PyLadiesSP/interm/test/teste2.txt'
#open(path3, 'a')
if os.path.exists(path):
    with open (path3, 'a') as arq:
        arq.write('\nlulululuuu')

    with open(path3, 'r') as a:
        conteudo = a.read()
        print(conteudo)
        
