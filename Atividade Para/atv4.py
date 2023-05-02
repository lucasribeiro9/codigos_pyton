inicial = int(input('informe um valor inicial: '))
final = int(input('informe um valor inicial: '))
soma = 0

for contador in range(inicial, final+1):
    soma = soma + inicial
    
print(f'A soma de {inicial} + {final} é {soma}\n')              