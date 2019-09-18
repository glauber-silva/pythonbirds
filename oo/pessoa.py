class Pessoa:
    def __init__(self, nome: str = None, idade: int = 35):
        self.idade = idade
        self.nome = nome


    def cumprimentar(self):
        return f"Olá {id(self)}"


if __name__ == '__main__':
    p = Pessoa('Lucio')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Glauber"
    print(p.nome)
    print(p.idade)