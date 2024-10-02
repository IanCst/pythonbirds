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
