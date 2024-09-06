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
        legal_moves = []
        direction = -1 if self.color == 'white' else 1
        start_row, start_col = self.row, self.col

        # One step forward
        if 0 <= start_row + direction < 8 and board[start_row + direction][start_col] is None:
            legal_moves.append((start_row + direction, start_col))

        # Two steps forward for the first move
        if not self.moved and 0 <= start_row + 2 * direction < 8 and \
           board[start_row + direction][start_col] is None and board[start_row + 2 * direction][start_col] is None:
            legal_moves.append((start_row + 2 * direction, start_col))

        # Capture diagonally
        if start_col - 1 >= 0 and 0 <= start_row + direction < 8 and \
           board[start_row + direction][start_col - 1] is not None and board[start_row + direction][start_col - 1].color != self.color:
            legal_moves.append((start_row + direction, start_col - 1))
        if start_col + 1 < 8 and 0 <= start_row + direction < 8 and \
           board[start_row + direction][start_col + 1] is not None and board[start_row + direction][start_col + 1].color != self.color:
            legal_moves.append((start_row + direction, start_col + 1))

        return legal_moves


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
