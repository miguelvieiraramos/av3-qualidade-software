from dados.personagens import Personagem, Vaca


class TestVaca:

    def setup(self):
        self.vaca = Vaca(40)

    def test_should_be_instance_of_personagem(self):
        assert isinstance(self.vaca, Personagem)

    def test_should_initialize_with_correct_energia(self):
        assert self.vaca.energia == 40