from dados.coordenada import Coodernada


class Sprite:

    def __init__(self):
        self.posicao = Coodernada()

    def move(self, x, y):
        self.posicao.x = x
        self.posicao.y = y
