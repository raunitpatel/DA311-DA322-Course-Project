from Chess.Board.GameState import GameState
from HashTable.prime_handler import PrimeHandler


class HashTable:
    def __init__(self, initial_size=101):
        
        self.size = initial_size
        self.count = 0
        self.load_factor_threshold = 0.7
        self.table = [[] for _ in range(self.size)]
        self.prime_handler = PrimeHandler()

    def compute_hash(self, fen: str) -> int:
        fen_key = fen.rsplit(' ', 2)[0]
        return hash(fen_key) % self.size

    def lookup(self, fen: str):
        h = self.compute_hash(fen)
        for item in self.table[h]:
            if item[0] == fen:
                return item[1]  # Return the stored value and move
        return None

    def store(self, fen: str, value, move):
        h = self.compute_hash(fen)
        for index, item in enumerate(self.table[h]):
            if item[0] == fen:
                # Replace the existing tuple with a new one that includes the updated value and move
                self.table[h][index] = (fen, (value, move))
                return
        # If the FEN was not found, append a new entry
        self.table[h].append((fen, (value, move)))
        self.count += 1
        if self.count / self.size > self.load_factor_threshold:
            self.resize()

    def resize(self):
        self.size = self._next_prime()
        old_table = self.table
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for entry in old_table:
            for fen, data in entry:
                self.store(fen, *data)

    def _next_prime(self) -> int:
       
        return self.prime_handler.generate_prime(2 * self.size)
