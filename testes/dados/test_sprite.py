from dados.sprite import Sprite
from dados.coordenada import Coodernada


class TestSprite:

    def setup(self):
        self.sprite = Sprite()

    def test_should_change_x_value(self):
        self.sprite.move(x=4, y=7)
        assert self.sprite.posicao.x == 4

    def test_should_change_y_value(self):
        self.sprite.move(x=4, y=7)
        assert self.sprite.posicao.y == 7

    def test_posicao_is_instance_of_coordenada(self):
        assert isinstance(self.sprite.posicao, Coodernada)
