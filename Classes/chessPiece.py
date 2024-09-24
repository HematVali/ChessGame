import os

class ChessPiece:
    def __init__(self, symbol, name, color, texture=None, texture_rect=None):
        self.name = name
        self.symbol = symbol
        self.color = color
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__('P', 'pawn', color)

class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__('N', 'knight', color)

class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__('B', 'bishop', color)

class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__('R', 'rook', color)

class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__('Q', 'queen', color)

class King(ChessPiece):
    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('K', 'king', color, 10000.0)