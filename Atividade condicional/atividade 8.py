a = float(input('Informe o lado A: '))
b = float(input('Informe o lado B: '))
c = float(input('Informe o lado C: '))

if a < b+c and b < a+c and c < a+b:
    print('TEMOS UM TRIÂNGULO!\n')
else:
    print('Você não encontrou um triângulo :(\n')