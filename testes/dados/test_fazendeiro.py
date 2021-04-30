from dados.personagens import Fazendeiro, Personagem


class TestFazendeiro:

    def setup(self):
        self.fazendeiro = Fazendeiro(40)

    def test_should_be_instance_of_personagem(self):
        assert isinstance(self.fazendeiro, Personagem)

    def test_should_initialize_with_correct_energia(self):
        assert self.fazendeiro.energia == 40