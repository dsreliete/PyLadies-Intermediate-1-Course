coord_gatos = {'pompom': (1,1), 'Mingau': (4,0), 'Fifi':(2,4), 'Fofona': (4,0)}

def achei_uns_gatos(dicio, coord):
    for chave, valor in dicio.items():
       if valor == coord:
           return print(chave)
       else:
           return print('não há gato com essa coordenada')
    
achei_uns_gatos(coord_gatos, (2,4))                  
achei_uns_gatos(coord_gatos, (4,0))
achei_uns_gatos(coord_gatos, (10,0))


