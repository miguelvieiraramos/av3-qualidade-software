from negocio.game_engine import GameEngine


class Jogo:

    def __init__(self):
        self.game_engine = GameEngine()

    def comecar(self):
        self.game_engine.comecar()

    def mover(self, x, y):
        self.game_engine.mover(x, y)
