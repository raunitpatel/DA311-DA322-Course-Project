import io

import dill
import pstats
import math
from collections import deque
from datetime import time

from CNN.ConvolutionalNeuralNetwork import ConvolutionalNeuralNetwork
from MCTS.Exceptions.LosingState import LosingState
from MCTS.monte_carlo_node import MCTSNode
from Chess.Repository.ChessRepository import ChessRepository
from Chess.Board.GameState import GameState
from Chess.utils.move_handlers import print_board
from Chess.Exceptions.Checkmate import Checkmate
import time
import cProfile

from HashTable.hash_table import HashTable


class MCTS:
    def __init__(self, state: GameState, iterations: int, exploration_constant: float = math.sqrt(2),
                 depth_limit: int | None = None, use_opening_book: bool = False,
                 cnn: ConvolutionalNeuralNetwork = None):
        
        self.iterations = iterations  # The number of iterations to perform
        self.exploration_constant = exploration_constant  # The exploration constant, sqrt(2) by default
        self.root = MCTSNode(state)
        self.hashtable = HashTable()  # The hashtable to store the results of the simulations
        self.current_node = self.root
        self.depth_limit = depth_limit
        self.use_opening_book = use_opening_book
        self.cnn = cnn
        # TODO: Create a stronger opening book
        self.opening_book = {
            # 6 moves of exchange QGD
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR": "d2d4",
            "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR": "c2c4",
            "rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR": "b1c3",
            "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR": "c4d5",
            "rnbqkb1r/ppp2ppp/5n2/3p4/3P4/2N5/PP2PPPP/R1BQKBNR": "c1g5",
            "rnbqkb1r/pp3ppp/2p2n2/3p2B1/3P4/2N5/PP2PPPP/R2QKBNR": "e2e3",

            # 4 moves of the Catalan
            "rnbqkb1r/pppppppp/5n2/8/3P4/8/PPP1PPPP/RNBQKBNR": "c2c4",
            "rnbqkb1r/pppp1ppp/4pn2/8/2PP4/8/PP2PPPP/RNBQKBNR": "g2g3",
            "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/6P1/PP2PP1P/RNBQKBNR": "c1d2",
            "rnbqk2r/ppppbppp/4pn2/8/2PP4/6P1/PP1BPP1P/RN1QKBNR": "g1d3"
        }

    def set_current_node(self, state: GameState):
       
        # First look in the children of the current node
        for child in self.current_node.children:
            if child.state == state:
                self.current_node = child
                print_board(self.current_node.state.get_board())
                return
        # If it's not in the children of the node, look in the entire tree
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.state == state and node != self.root and node != self.current_node:
                self.current_node = node
                print_board(self.current_node.state.get_board())
                return
            queue.extend(node.children)
        if not self.current_node.state == state:
            self.current_node = MCTSNode(state)

    def _select(self, node: MCTSNode, depth: int) -> MCTSNode:
        
        while not node.state.board.game_over:
            if node.not_fully_expanded():
                return node
            if self.depth_limit and depth >= self.depth_limit:
                return node
            hashtable_result = self.hashtable.lookup(node.state.fen())
            if hashtable_result:
                value, move = hashtable_result
                if node.state.board.turn == "w":
                    if value >= node.beta:
                        return node
                else:
                    if value <= node.alpha:
                        return node
            children = node.children
            children = [child for child in children if child.alpha <= node.beta]
            if len(children) == 0:
                return node
            node = max(children, key=lambda c: c.ucb1(self.exploration_constant))
            depth += 1
        return node

    def _expand(self, node: MCTSNode) -> MCTSNode:
        next_state = dill.copy(node.state)
        try:
            next_state.play_random_move()
        except Checkmate:
            return node
        new_node = MCTSNode(next_state, parent=node, alpha=node.alpha, beta=node.beta,
                            move=next_state.board.history[-1], cnn=self.cnn)
        node.children.append(new_node)
        return new_node

    def _simulate(self, node: MCTSNode) -> int:
        state = dill.copy(node.state)
        # start = time.time()
        while not state.board.game_over:
            hashtable_result = self.hashtable.lookup(state.fen())
            if hashtable_result:
                value, move = hashtable_result
                if state.board.turn == "w":
                    if value >= node.beta:
                        return -1
                    node.alpha = max(node.alpha, value)
                else:
                    if value <= node.alpha:
                        return 1
                    node.beta = min(node.beta, value)
            else:
                try:
                    state.play_random_move()
                except Checkmate as e:
                    # print(e)
                    # end = time.time()
                    # print(end - start)
                    return state.board.result
        # end = time.time()
        # print(end - start)
        return state.board.result

    def _backpropagate(self, node: MCTSNode, result: int):
       
        while node is not None:
            node.visits += 1
            node.wins += result
            node = node.parent

    def select_move(self, state: GameState) -> str:
       
        self.set_current_node(state)

        if self.use_opening_book:
            fen = self.root.state.fen().split(" ")[0]
            if fen in self.opening_book:
                return self.opening_book[fen]

        for _ in range(self.iterations):
            node = self._select(self.current_node, 0)
            try:
                if node.not_fully_expanded():
                    node = self._expand(node)
            except LosingState:
                pass
            result = self._simulate(node)
            self._backpropagate(node, result)

        best_child = max(self.current_node.children, key=lambda c: c.ucb1(self.exploration_constant))
        self.current_node = best_child
        return best_child.move


if __name__ == "__main__":
    chess_repository = ChessRepository()
    chess_repository.initialize_board()
    chess_state = GameState(chess_repository)
    mcts = MCTS(chess_state, iterations=2)
    start = time.time()
    while not chess_state.board.game_over:
        pr = cProfile.Profile()
        pr.enable()
        move = mcts.select_move(chess_state)
        pr.disable()
        s = io.StringIO()
        sortby = 'tottime'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        print(move)
        print(f"\nTime taken on average/game: {(time.time() - start)/20}")
        chess_state.make_move(move)
        mcts.set_current_node(chess_state)
        print_board(chess_state.get_board())
