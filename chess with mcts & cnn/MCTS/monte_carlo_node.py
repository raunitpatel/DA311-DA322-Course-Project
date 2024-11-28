import math
from typing import Tuple
from Chess.Board.GameState import GameState


class MCTSNode:
    """ This is a node in the Monte Carlo Search Tree. """

    def __init__(self, state: GameState, parent=None, move=None, alpha=-float("inf"), beta=float("inf"), cnn = None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0
        self.alpha = alpha
        self.beta = beta
        self.cnn = cnn

    def not_fully_expanded(self) -> bool:
        """ Check if the node has been fully expanded"""
        return len(self.children) < len(self.state.possible_moves())

    def ucb1(self, exploration_constant: float) -> float:
        """ Apply the UCT formula (Upper Confidence Bound applied to Trees)"""

        if self.visits == 0:
            return float('inf')
        if self.cnn is not None:
            [predicted_result] = self.cnn.predict(self.state.fen())
            print(predicted_result)
            if predicted_result[0 if self.state.get_turn() == "b" else 2] > 0.5:
                return float('inf')
            else:
                return self.wins / self.visits + exploration_constant * math.sqrt(math.log(self.parent.visits) / self.visits)
        else:
            return self.wins / self.visits + exploration_constant * math.sqrt(math.log(self.parent.visits) / self.visits)