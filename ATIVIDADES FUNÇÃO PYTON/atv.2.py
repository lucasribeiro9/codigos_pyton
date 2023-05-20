'''
while True:
    numA = int(input('Informe o valor de A: '))
    numB = int(input('Informe o valor de B: '))
    if numA != numB:
        break

def somaImpar(a,b):
    acumuladora = 0
    for contador in range(a,b+1):
        if contador % 2 == 1:
            acumuladora = acumuladora + contador
    print(acumuladora)

somaImpar(numA,numB)
'''
#CORREÇÃO DA QUESTÃO
while True:
    A = int(input('Informe um valor qualquer: '))
    B = int(input('Informe um outro valor qualquer diferente: '))
    if A != B:
        break

def somaImpar(inicial,final):
    soma = 0
    for contador in range(inicial,final+1):
        if contador % 2 == 1:
            soma += contador

    return soma

def mediaMultiplo3(inicial,final):
    total = 0
    contDivisores = 0
    for contador in range(inicial,final+1):
        if contador % 3 == 0:
            total += contador # isto é para somar todos os divisores
            contDivisores += 1 # isto é para contar todos os divisores
    
    return total / contDivisores

if A < B:
    print(f'A soma dos ímpares é: {somaImpar(A,B)}')
else:
    print(f'A média dos multiplos de 3 é: {mediaMultiplo3(B,A)}')