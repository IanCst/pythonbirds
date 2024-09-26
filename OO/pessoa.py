class Pessoa:
    def __init__(self,*filhos, nome = None, idade = 23):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

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