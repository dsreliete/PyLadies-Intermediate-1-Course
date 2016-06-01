print ('Soma de números ímpares')
lista = [1,2,3,4,5,6,7,8,9,10]
tam = len(lista)
i = 0
somaImpar = 0
while i < tam:
    if (lista[i] % 2) != 0:
        somaImpar = somaImpar + lista[i]
        print ('Somando o n. ímpar: %d' %lista[i])
    i+= 1
print('A soma dos ímpares da lista é %d' %somaImpar)

somaImpar = 0
for x in lista:
    if (x % 2)!= 0:
        somaImpar = somaImpar + x
        print ('Somando o n. ímpar: %d' %x)
print('A soma dos ímpares da lista é %d' %somaImpar)
