from dicionarios import mostra_chaves, mostra_valores, mostra_pares_chave_valor

coordenadas = {(1,1):'cafeteria', (300,990): 'pet shop ',
(2,4): { '1 andar ': None, '2 andar ': [ 'restaurante ',
'bar ', 'banheiros '], '3 andar ': 'estacionamento '},
(5, 100, 400000): 'topo da colina '}

mostra_chaves(coordenadas)
mostra_valores(coordenadas)
mostra_pares_chave_valor(coordenadas)
