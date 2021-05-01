from negocio.fase import Fase

class GameEngine:

    def comecar(self):
        Fase.comecar()

    def mover(self, x, y):
        Fase.fazendeiro.move(x, y)
        print(f'Fazendeiro moveu para x={Fase.fazendeiro.posicao.x}, y={Fase.fazendeiro.posicao.y}')
