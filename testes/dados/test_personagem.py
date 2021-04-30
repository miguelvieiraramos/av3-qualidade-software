from dados.personagens import Personagem
from dados.sprite import Sprite


class TestPersonagem:

    def setup(self):
        self.personagem = Personagem(30)

    def test_should_be_instance_of_sprite(self):
        assert isinstance(self.personagem, Sprite)

    def test_should_initialize_with_correct_energia(self):
        assert self.personagem.energia == 30