from negocio.gerador_sprite import GeradorSprite, TipoSprite


class Fase:

    fase = 1
    gados = []
    naves = []
    misseis = []
    fazendeiro = None
    gerador_sprite = GeradorSprite()

    @staticmethod
    def resetar():
        Fase.gados = []
        Fase.naves = []
        Fase.misseis = []

    @staticmethod
    def gerar_personagens(quantidade_vacas, quantidade_naves, quantidade_misseis):
        Fase.resetar()
        for i in range(quantidade_vacas):
            Fase.gados.append(Fase.gerador_sprite.new_sprite(TipoSprite.VACA))

        for i in range(quantidade_naves):
            Fase.naves.append(Fase.gerador_sprite.new_sprite(TipoSprite.NAVE))

        for i in range(quantidade_misseis):
            Fase.misseis.append(Fase.gerador_sprite.new_sprite(TipoSprite.MISSIL))

    @staticmethod
    def comecar():
        Fase.fazendeiro = Fase.gerador_sprite.new_sprite(TipoSprite.FAZENDEIRO)
        if Fase.fase == 1:
            Fase.gerar_personagens(quantidade_naves=2, quantidade_misseis=4, quantidade_vacas=10)

    @staticmethod
    def proxima_fase():
        Fase.fase += 1
        print(Fase.fase)
        if Fase.fase == 2:
            Fase.gerar_personagens(quantidade_naves=4, quantidade_misseis=8, quantidade_vacas=20)
        elif Fase.fase == 3:
            Fase.gerar_personagens(quantidade_naves=8, quantidade_misseis=16, quantidade_vacas=40)


