from Classes.square import Square
from Classes.chessPiece import *

class ChessBoard:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(8)]
        self.create()
        self.add_pieces('white')
        self.add_pieces('black')

    def create(self):
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = Square(row, col, (str(chr(row+97)) + str(col)))

    def add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        for col in range(8):
            self.squares[row_pawn][col].initializePiece(Pawn(color))

        self.squares[row_other][1].initializePiece(Knight(color))
        self.squares[row_other][6].initializePiece(Knight(color))

        self.squares[row_other][2].initializePiece(Bishop(color))
        self.squares[row_other][5].initializePiece(Bishop(color))

        self.squares[row_other][0].initializePiece(Rook(color))
        self.squares[row_other][7].initializePiece(Rook(color))

        self.squares[row_other][3].initializePiece(Queen(color))

        self.squares[row_other][4].initializePiece(King(color))

    def return_piece(self, x, y):
        if (self.squares[y][x].piece != None):
            return (self.squares[y][x].piece.symbol)
        return None
    
    def change_piece(self, fromSquare, toSquare):
        fromS = (8-int(fromSquare[1]), self.file_to_index(fromSquare[0]))
        toS = (8-int(toSquare[1]) ,self.file_to_index(toSquare[0]))
        self.squares[toS[0]][toS[1]].piece = self.squares[fromS[0]][fromS[1]].piece
        self.squares[fromS[0]][fromS[1]].piece = None
        
    
    def file_to_index(self, file):
        file_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return file_map[file]

    
