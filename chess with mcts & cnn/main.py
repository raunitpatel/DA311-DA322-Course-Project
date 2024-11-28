from CNN.ConvolutionalNeuralNetwork import ConvolutionalNeuralNetwork
from MCTS.monte_carlo_tree_search import MCTS
from Minimax.minimax import Minimax
from Chess.Board.GameState import GameState
from Chess.Repository.ChessRepository import ChessRepository
from Chess.UI.console import UI

if __name__ == "__main__":
    use_gui = True
    chess_repository = ChessRepository()
    chess_repository.initialize_board()
    game_state = GameState(chess_repository)
    cnn = ConvolutionalNeuralNetwork()
    cnn.load("CNN/TrainedModels/cnn.h5")
    
    ui = UI(game_state, cnn)
    ui.start()
