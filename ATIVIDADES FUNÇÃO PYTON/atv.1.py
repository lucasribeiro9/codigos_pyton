import os
idade = int(input('Informe sua idade: '))

def categoria(idade):
    if idade >= 5 and idade <= 7:
        return('INFANTIL A')
    elif idade >= 8 and idade <= 10:
        return('INFANTIL B')
    elif idade >= 11 and idade <= 13:
        return('JUVENIL A')
    elif idade >= 14 and idade <= 17:
        return('JUVENIL B')
    elif idade >= 18:
        return('ADULTO')
os.system('cls') 
print(categoria(idade))
       
    
    