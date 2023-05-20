class Pessoa:
    #atributos
    nome = 'Jow'
    idade = 31
    altura = 1.75

    #métodos
    def falar(self, texto): # self é um parâmetro obrigatório do python obrigatório que informa que o método pertence a própria classe
        print(texto)

pessoa1 = Pessoa()
pessoa1.nome = 'Lucas'
print(f'Seu nome é: {pessoa1.nome}') 
print(f'Sua idade é: {pessoa1.idade}')
print(f'Sua altura é: {pessoa1.altura}')

pessoa1.falar('Olá mundo')