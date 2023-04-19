texto = 'Técnico em Desenvolvimento de Sistemas'
print('******* Título *******')
print('*'*100)
print(texto)
print(int)
idade = int(input('Qual é a sua idade? '))
print('#'*idade)

#Manipulando Textos(String)
print(f'O total de letras é {len(texto)}') #len vem de length, que significa total de caracteres

print(texto.upper())# upper() coloca todo o texto em maiúsculo
print(texto.lower())# lower() coloca todo o texto em minúsculo
print(texto.capitalize())# capitalize() coloca a 1ª letra em maiúsculo
print(texto.replace('Sistemas','web'))# replace troca um texto por outro
#1- texto procurar
#2- vai ser trocado

#TRABALHANDO COM FATIAMENTO

print('Fatiando a variável texto')
print(texto[:3])#Vai exibir todo o texto até a posição 2, no caso a posição 3 não conta.
print(texto[3:])#Vai exibir todo o texto a partir da posição 3.
print(texto[3:10])#Vai exibir todo o texto que está na posição 3 até 10.