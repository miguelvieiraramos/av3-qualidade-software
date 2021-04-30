from enum import Enum
from dados.personagens import Fazendeiro, Vaca, Nave
from dados.missil import Missil

TipoSprite = Enum('Sprite', 'FAZENDEIRO VACA NAVE MISSIL')


class GeradorSprite:

    def new_sprite(self, tipo_sprite: TipoSprite):
        if tipo_sprite == TipoSprite.FAZENDEIRO:
            return Fazendeiro(30)
        elif tipo_sprite == TipoSprite.VACA:
            return Vaca(30)
        elif tipo_sprite == TipoSprite.NAVE:
            return Nave(30)
        elif tipo_sprite == TipoSprite.MISSIL:
            return Missil()
