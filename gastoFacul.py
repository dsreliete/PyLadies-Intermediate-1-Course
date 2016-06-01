soma = 0
n = 1
while True:
    gasto = float(input('Qual o valor que vc gasta por dia na facul '))
    if gasto == 0:
        break
    soma = soma + gasto
    n = n + 1
print('O total gasto na semana é R$', soma)
