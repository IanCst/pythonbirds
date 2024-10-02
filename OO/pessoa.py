class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

if __name__ == '__main__':
    Ian = Pessoa(nome='Ian')
    Italia = Pessoa(Ian, nome='Italia')
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