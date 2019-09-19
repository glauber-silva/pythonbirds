from typing import List


class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome: str = None, idade: int = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá {id(self)}"


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
