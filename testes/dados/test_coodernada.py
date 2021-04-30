from dados.coordenada import Coodernada


class TestCoodernada:

    def test_should_initialize_coordenada_with_correct_params(self):
        self.coordenada = Coodernada()
        assert self.coordenada.x == 0
        assert self.coordenada.y == 0