from dados.missil import Missil
from dados.sprite import Sprite


class TestMissil:

    def test_missil_is_instance_of_sprite(self):
        self.missil = Missil()
        assert isinstance(self.missil, Sprite)