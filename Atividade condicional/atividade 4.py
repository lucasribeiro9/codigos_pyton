salario = float(input('Informe seu salário: '))
financiamento = float(input('Qual o valor do financiamento? '))

valor5x = financiamento * 5

if valor5x <= salario:
    print('Financiamento CONCEDIDO\n')
else:
    print('Financiamento NÃO concedido\n')
    
print('OBRIGADO POR NOS CONSULTAR\n')