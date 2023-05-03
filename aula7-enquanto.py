# While funcionando como loop contado
contador = 1
while contador <=5:
    print(contador)
    contador = contador+1
    
# While funcionando como loop condicional
'''

senha = ''
while senha != '999':
    senha = input('Digite sua senha:')
    
print('Obrigado por usar nossos serviços\n')
'''
# While como se fosse o FAÇA - ENQUANTO
while True:
    senha = input('Digite sua senha: ')
    
    if senha == '999':
        break
print('Senha correta!') 