from MCTS.monte_carlo_tree_search import MCTS
from Minimax.minimax import Minimax
from Chess.Board.GameState import GameState
from Chess.Exceptions.IllegalMoveException import IllegalMove
from Chess.Exceptions.WrongColor import WrongColor
from Chess.Repository.ChessRepository import ChessRepository


class UI:
    def __init__(self, game_state, cnn):
        self.ai = None
        self.state = game_state
        self.cnn = cnn

    def handle_algorithm_selection(self):
        commands = {"minimax": "Minimax",
                    "mcts": "MCTS"
                    }

        while True:
            algorithm = input("Please select algorithm: minimax, mcts\n> ")
            if algorithm in commands:
                return commands[algorithm]
            else:
                print("Invalid algorithm")

    def handle_color_selection(self):
        commands = {"white": "w",
                    "black": "b"
                    }

        while True:
            color = input("Please select color: white, black\n> ")
            if color in commands:
                return commands[color]
            else:
                print("Invalid color")

    def handle_difficulty_selection(self):
        commands = {"easy": 2,
                    "medium": 5,
                    "hard": 10
                    }

        while True:
            difficulty = input("Please select difficulty: easy, medium, hard\n> ")
            if difficulty in commands:
                return commands[difficulty]
            else:
                print("Invalid difficulty")

    def print_board(self, board):
        for i in range(len(board.board)):
            string = []
            for j in range(len(board.board[i])):
                if board.board[i][j] is not None:
                    string.append(board.board[i][j])
                else:
                    string.append("")
            print(string)
        print("\n")

    def start(self):
        algorithm = self.handle_algorithm_selection()
        difficulty = self.handle_difficulty_selection()
        color = self.handle_color_selection()
        if algorithm == "MCTS":
            self.ai = MCTS(self.state, iterations=difficulty, depth_limit=None, use_opening_book=True, cnn=self.cnn)
        else:
            self.ai = Minimax(self.state, difficulty, color)

        while not self.state.board.game_over:
            if self.state.board.turn == color:
                move = self.ai.select_move(self.state)
                self.state.make_move(move)
                self.print_board(self.state.board)
            else:
                move = input("Your move: ")
                try:
                    self.state.make_move(move)
                    self.print_board(self.state.board)
                except IllegalMove as e:
                    print(e)
                except WrongColor as e:
                    print(e)
                except IndexError:
                    print("Invalid input")

if __name__ == "__main__":
    game_repository = ChessRepository()
    game_repository.initialize_board()
    game_state = GameState(game_repository)
    ui = UI(game_state)
    ui.start()