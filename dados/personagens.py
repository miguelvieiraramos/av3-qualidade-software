from dados.sprite import Sprite


class Personagem(Sprite):

    def __init__(self, energia):
        super().__init__()
        self.energia = energia


class Fazendeiro(Personagem):

    def __init__(self, energia):
        super().__init__(energia)


class Vaca(Personagem):

    def __init__(self, energia):
        super().__init__(energia)


class Nave(Personagem):

    def __init__(self, energia):
        super().__init__(energia)
