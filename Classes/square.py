class Square:
    def __init__(self, row, col, location, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.location = location

    def initializePiece(self, piece):
        self.piece = piece

    def has_piece(self):
        return self.piece != None