from dados.pontuacao import Pontuacao


class TestPontuacao:

    def setup(self):
        self.pontuacao = Pontuacao()

    def test_should_initialize_with_correct_pontos(self):
        assert self.pontuacao.pontos == 0
