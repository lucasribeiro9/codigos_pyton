percurso = float(input('Informe o percurso em km: '))
tipoCarro = int(input('Informe o tipo do carro 1, 2 ou 3: '))

if tipoCarro == 1:
    total = percurso/8
    
elif tipoCarro == 2:
    total = percurso/9
    
elif tipoCarro == 3:
    total = percurso/12
    
else:
    total = 0
    print('Escolha um valor válido: \n')
print(f'O tipo do carro é {tipoCarro} e vai precisar de {total} litros de gasolina\n')

