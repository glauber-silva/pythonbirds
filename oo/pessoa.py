from typing import List


class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome: str = None, idade: int = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls.__name__} - olhos {Pessoa.olhos}'

if __name__ == '__main__':
    dylan = Pessoa(nome='Dylan')
    glauber = Pessoa(dylan, nome='Glauber')
    print(Pessoa.cumprimentar(glauber))
    glauber.nome = "Glauber"
    print(glauber.nome)
    print(glauber.idade)
    for filho in glauber.filhos:
        print(filho.nome)
    glauber.sobrenome = 'Silva'
    del(glauber.filhos)
    print(glauber.__dict__)
    print(dylan.__dict__)
    print(Pessoa.olhos)
    glauber.olhos = 1
    print(Pessoa.olhos)
    print(glauber.olhos)
    print(dylan.olhos)
    print(Pessoa.metodo_estatico(), glauber.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), glauber.nome_e_atributos_de_classe())