from abc import abstractmethod


class Piece:
    def __init__(self, type, color, position):
        self.type: str = type
        self.color: str = color
        self._position: tuple[int, int] = position

    def get_legal_moves(self, board, move_history, pieces):

        pass

    @abstractmethod
    def get_value(self, *args):
        pass

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    def __repr__(self):
        return self.color + self.type
