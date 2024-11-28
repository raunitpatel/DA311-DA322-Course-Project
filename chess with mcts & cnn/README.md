# Chess AI Repository
## Project Members
- Himanshu Singhal: 220150004
- Raunit Patel : 220150015
- Rishita Agarwal: 220150016
- Arushi Kumar: 220150032
This repository is designed to simulate and experiment with chess-based Artificial Intelligence algorithms, providing implementations for techniques like **Minimax**, **Monte Carlo Tree Search (MCTS)**, and **Convolutional Neural Networks (CNN)**. It also includes a custom hash table and tensor conversion mechanisms for optimized gameplay and data processing.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Folder Structure](#folder-structure)
5. [Detailed Descriptions](#detailed-descriptions)

---

## Features

- **Minimax Algorithm**: Implements a depth-limited adversarial search for evaluating game states.
- **Monte Carlo Tree Search (MCTS)**: Provides a probabilistic approach to decision-making in the chess engine.
- **Convolutional Neural Networks**: Integrates a CNN model for advanced move prediction and evaluation.
- **Custom Hash Table**: Optimized for storing and retrieving game states efficiently.
- **Tensor Conversion**: Translates board states into tensor representations for use in ML models.

---

## Installation

1. Clone the repository or download it as a zip file.
   ```bash
   git clone <repository_url>
   ```
2. Install the following Python Packages:
    Tensorflow 
   
   

---

## Usage

1. Navigate to the main directory.
   ```bash
   cd Chess
   ```
2. If you are running the script for the first time, you will have to train the CNN model. In the CNN folder in the `ConvolutionalNeuralNetwork.py` file add the absolute path of the training set. Then run the script.
 ```bash
   python CNN/ConvolutionalNeuralNetwork.py
   ```
2. Run the `main.py` script to start the chess engine.
   ```bash
   python main.py
   ```
3. in the CNN folder in the  COnvolutionalNeuralNetwork
---

## Folder Structure

- **Chess/**: Core logic and rules for chess.
- **CNN/**: Convolutional Neural Network implementation for move prediction.
- **HashTable/**: Custom implementation for game state storage.
- **MCTS/**: Monte Carlo Tree Search algorithm.
- **Minimax/**: Depth-limited Minimax algorithm implementation.

---

## Detailed Descriptions

### Chess Logic
The core module for implementing chess rules, validating moves, and managing the game state. It handles player turns, piece movement, and checks for checkmate and stalemate conditions.

### Convolutional Neural Networks (CNN)
This module integrates a CNN model for predicting the next best move based on board positions. The board state is converted into tensors, enabling the network to learn and improve over time.

### Game State Handling
Manages the current state of the chessboard and tracks historical states for undo/redo functionality. This is crucial for algorithms like MCTS and Minimax that evaluate multiple scenarios.

### Monte Carlo Tree Search (MCTS)
A probabilistic algorithm that uses simulations to explore potential moves and evaluate the best outcomes. It balances exploration and exploitation using statistical techniques, such as **Upper Confidence Bound for Trees (UCT)** to decide which moves to explore further. The evaluation function used during simulations considers material balance, board control, and king safety as heuristics. By running multiple simulations from a given state, MCTS estimates the probability of success for each potential move, making it suitable for complex decision-making in chess.

### Minimax Algorithm
The Minimax algorithm is a depth-limited adversarial search algorithm that is used to evaluate and rank possible moves in the game. It works by simulating all possible moves for both players (Maximizer and Minimizer) to find the best strategy for the current player. The algorithm assumes that the opponent will always play optimally to minimize the player's advantage. 

- **Depth Limitation**: The depth of the search tree is limited to ensure computational feasibility. The depth limit can be adjusted based on available computational power and time constraints.
- **Evaluation Function**: The leaf nodes of the search tree are evaluated using a heuristic evaluation function that considers factors such as material balance, piece activity, king safety, and control of key squares. This heuristic allows the algorithm to estimate the strength of a given board state.
- **Alpha-Beta Pruning**: Minimax is enhanced with alpha-beta pruning to eliminate branches of the search tree that do not need to be explored because they cannot affect the final decision. This significantly improves the efficiency of the algorithm by reducing the number of nodes that need to be evaluated.
- **Optimal Play**: The algorithm makes a move that maximizes the player's minimum gain, effectively minimizing the opponent's potential advantage. This approach is particularly well-suited for structured games like chess, where each player aims to optimize their chances of winning.

### Chess Pieces
Defines the characteristics and movement rules for each piece (Pawn, Knight, Bishop, Rook, Queen, King). Includes special rules like castling, en passant, and pawn promotion.

### Prime Handling
Optimizes move hashing and board state representation using prime numbers to generate unique identifiers for each game position.

### Custom Hash Table
The custom hash table is used to store previously computed game states to avoid redundant calculations. By caching these states, the system ensures that if a game state has already been evaluated, it does not need to be computed again, significantly improving efficiency, especially in recursive algorithms like Minimax and MCTS.

### Tensor Conversion
Converts board states into tensor formats suitable for machine learning models, enabling faster computations and integration with neural networks.

### User Interface
Provides a minimalistic interface to interact with the chess engine. The interaction is **command-line based**, allowing users to input moves and receive game feedback directly through the terminal.


