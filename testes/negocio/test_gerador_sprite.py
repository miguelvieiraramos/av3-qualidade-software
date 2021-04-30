from dados.missil import Missil
from dados.personagens import Fazendeiro, Vaca, Nave
from negocio.gerador_sprite import GeradorSprite, TipoSprite


class TestGeradorSprite:

    def setup(self):
        self.gerador_sprite = GeradorSprite()

    def test_should_generate_fazendeiro(self):
        fazendeiro = self.gerador_sprite.new_sprite(TipoSprite.FAZENDEIRO)
        assert isinstance(fazendeiro, Fazendeiro)

    def test_should_generate_vaca(self):
        vaca = self.gerador_sprite.new_sprite(TipoSprite.VACA)
        assert isinstance(vaca, Vaca)

    def test_should_generate_nave(self):
        nave = self.gerador_sprite.new_sprite(TipoSprite.NAVE)
        assert isinstance(nave, Nave)

    def test_should_generate_missil(self):
        missil = self.gerador_sprite.new_sprite(TipoSprite.MISSIL)
        assert isinstance(missil, Missil)