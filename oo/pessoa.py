from __future__ import annotations
from typing import List


class Pessoa:
    olhos = 2

    def __init__(self, *filhos:Pessoa, nome: str = None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self) -> str:
        return f'Ola {id(self)}'


    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls.olhos} - olhos'


if __name__ == '__main__':
    ulisses = Pessoa(nome='Ulisses')
    glauber = Pessoa(ulisses ,nome='Glauber')
    print(Pessoa.cumprimentar(glauber))
    print(id(glauber))
    print(id(ulisses))
    print(glauber.cumprimentar())
    print(glauber.nome)
    print(glauber.idade)
    print(glauber.filhos)

    for filho in glauber.filhos:
        print(filho.nome)

    ulisses.sobrenome = "Nogueira"
    print(glauber.__dict__)
    print(ulisses.__dict__)
    del ulisses.sobrenome
    print(ulisses.__dict__)
    print(Pessoa.nome_e_atributos_de_class(), glauber.nome_e_atributos_de_class())