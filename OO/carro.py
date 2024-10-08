class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def turn_right(self):
        return self.direcao.turn_right()
    def turn_left(self):
        return self.direcao.turn_left()


NORTH = 'Norte'
SOUTH = 'Sul'
EAST = 'East'
WEST = 'Oeste'
class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    rotation_right_dct = {NORTH: EAST, EAST: SOUTH,SOUTH: WEST}
    rotation_left_dct = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST}
    def __init__(self):
        self.valor = NORTH

    def turn_right(self):
        self.valor = self.rotation_right_dct[self.valor]
    def turn_left(self):
        self.valor = self.rotation_left_dct[self.valor]
