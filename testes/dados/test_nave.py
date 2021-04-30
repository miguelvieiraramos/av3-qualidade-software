from dados.personagens import Personagem, Nave


class TestNave:

    def setup(self):
        self.nave = Nave(40)

    def test_should_be_instance_of_personagem(self):
        assert isinstance(self.nave, Personagem)

    def test_should_initialize_with_correct_energia(self):
        assert self.nave.energia == 40