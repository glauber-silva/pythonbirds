"""Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

    Motor
    Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

    Atributo de dado velocidade
    Método acelerar, que deverá incremetar a velocidade de uma unidade
    Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

    Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
    Método girar_a_direita
    Método girar_a_esquerda


       N
    O     L
       S

Exemplo:

    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade+=1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade-=2
        else:
            self.velocidade-=1


class Direcao:

    def __init__(self):
        self.direcoes = {1: 'Norte', 2: 'Leste', 3: 'Sul', 4: 'Oeste'}
        self.valor = 'Norte'

    def girar_a_direita(self):
        for key, value in self.direcoes.items():
            if value == self.valor:
                if key == 4:
                    self.valor = self.direcoes[1]
                else:
                    self.valor = self.direcoes[key+1]
                return

    def girar_a_esquerda(self):
        for key, value in self.direcoes.items():
            if value == self.valor:
                if key == 1:
                    self.valor = self.direcoes[4]
                else:
                    self.valor = self.direcoes[key-1]
                return


class Carro:
    def __init__(self, direcao: Direcao, motor: Motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
