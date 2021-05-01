from unittest.mock import patch

from apresentacao.jogo import Jogo
from negocio.game_engine import GameEngine


class TestJogo:

    def setup(self):
        self.jogo = Jogo()

    def test_should_be_instance_of_game_engine(self):
        assert isinstance(self.jogo.game_engine, GameEngine)

    @patch('apresentacao.jogo.GameEngine.comecar')
    def test_should_call_comecar_once(self, mock_comecar):
        self.jogo.comecar()
        mock_comecar.assert_called_once()

    @patch('apresentacao.jogo.GameEngine.mover')
    def test_should_call_mover_with_correct_params(self, mock_mover):
        self.jogo.mover(5, 3)
        mock_mover.assert_called_once_with(5, 3)