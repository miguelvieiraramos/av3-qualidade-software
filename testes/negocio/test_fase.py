from negocio.fase import Fase


class TestFase:

    def test_should_gererate_correct_personagem_number(self):
        quantidade_vacas = 5
        quantidade_naves = 3
        quantidade_misseis = 7
        Fase.gerar_personagens(
            quantidade_vacas=quantidade_vacas,
            quantidade_naves=quantidade_naves,
            quantidade_misseis=quantidade_misseis
        )
        assert len(Fase.gados) == quantidade_vacas
        assert len(Fase.naves) == quantidade_naves
        assert len(Fase.misseis) == quantidade_misseis

    def test_comecar_should_generate_correct_personagem_number(self):
        quantidade_vacas = 10
        quantidade_naves = 2
        quantidade_misseis = 4
        Fase.comecar()
        assert len(Fase.gados) == quantidade_vacas
        assert len(Fase.naves) == quantidade_naves
        assert len(Fase.misseis) == quantidade_misseis

    def test_proxima_fase_when_fase_is_2(self):
        Fase.fase = 1
        Fase.proxima_fase()

        quantidade_vacas = 20
        quantidade_naves = 4
        quantidade_misseis = 8

        assert len(Fase.gados) == quantidade_vacas
        assert len(Fase.naves) == quantidade_naves
        assert len(Fase.misseis) == quantidade_misseis

    def test_proxima_fase_when_fase_is_3(self):
        Fase.fase = 2
        Fase.proxima_fase()

        quantidade_vacas = 40
        quantidade_naves = 8
        quantidade_misseis = 16

        assert len(Fase.gados) == quantidade_vacas
        assert len(Fase.naves) == quantidade_naves
        assert len(Fase.misseis) == quantidade_misseis
