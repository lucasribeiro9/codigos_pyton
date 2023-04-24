salario = float(input('Informe seu salário: '))

if salario < 600:
    novoSalario = (salario * 30/100) + salario
    print(f'Seu novo salário é {novoSalario}\n')
else:
    print(f'Você não tem direito pois ganha {salario}\n')