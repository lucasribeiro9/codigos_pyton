esporte = input('Informe um esporte: ')

def categoria(esporte):
    if esporte == 'Natação' or esporte == 'Vôlei':
        return('Ginásio 1')
    elif esporte == 'Dança' or esporte == 'Futebol':
        return('Ginásio 2')
    elif esporte == 'Corrida' or esporte == 'Ballet':
        return('Ginásio 3')
 
print(categoria(esporte))