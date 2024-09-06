import copy

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def __str__(self):
        return self.__class__.__name__[0] + ('W' if self.color == 'white' else 'B')

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.moved = False

    def get_legal_moves(self, board):
        # Implement pawn movement logic here
        pass

# Other piece classes (Rook, Knight, Bishop, Queen, King)

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        # Initialize pieces on the board

    def move(self, start_row, start_col, end_row, end_col):
        # Implement move logic, including capturing, pawn promotion, castling, en passant
        pass

    def is_check(self, color):
        # Implement check detection
        pass

    def is_checkmate(self, color):
        # Implement checkmate detection
        pass

    def is_stalemate(self, color):
        # Implement stalemate detection
        pass
