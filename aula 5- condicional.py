nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))

media = (nota1 + nota2)/2
'''

se media >= 7 entao

fimse;
'''
print(f'Sua média é {media}')
if media >= 7:
    print('Você passou :)')
    
elif media == 6:
    print('Você está de recuperação meu jovem :/')
else:
    print('Você ficou reprovado:(')
    