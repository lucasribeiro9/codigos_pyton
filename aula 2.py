nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

#Isso é um comentário de uma linha
"""
Isso é um comentário de várias linhas
"""
# Primeira forma de concatenar
print("Olá ",nome," sua idade é ",idade)
print("Olá {} sua idade é {}".format(nome,idade))
print(f"Olá {nome} sua idade é {idade}")