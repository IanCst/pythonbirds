class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return'Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    Ian = Mutante(nome='Ian')
    Italia = Homem(Ian, nome='Italia')
    print(Pessoa.cumprimentar(Italia))
    print(id(Italia))
    print(Italia.cumprimentar())
    print(Italia.nome)
    print(Italia.idade)
    for filho in Italia.filhos:
        print(filho.nome)
    Italia.sobrenome = 'franca'
    print(Italia.sobrenome)
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Homem))
    print(Ian.olhos)
    print(Mutante.olhos)
    print(Ian.cumprimentar())
    print(Italia.cumprimentar())