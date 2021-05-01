from unittest.mock import patch

from negocio.game_engine import GameEngine


class TestGameEngine:

    def setup(self):
        self.game_engine = GameEngine()
        self.game_engine.comecar()

    @patch('negocio.game_engine.Fase.comecar')
    def test_should_call_comecar_once(self, mock_comecar):
        self.game_engine.comecar()
        mock_comecar.assert_called_once()

    @patch('negocio.game_engine.Fase.fazendeiro.move')
    def test_should_call_move_with_correct_params(self, mock_move):
        self.game_engine.mover(5, 15)
        mock_move.assert_called_once_with(5, 15)

    @patch('negocio.game_engine.print')
    def test_should_call_print_with_correct_params(self, mock_print):
        self.game_engine.mover(5, 15)
        mock_print.assert_called_once_with(f'Fazendeiro moveu para x=5, y=15')