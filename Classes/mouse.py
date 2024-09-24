import pygame
import chess

class Mouse:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.square = None
        self.initialSquare = None
        self.legalMoves = None
        self.piece = None

    def click(self, position, board, interface):
        self.x, self.y = position

        if self.initialSquare == None:
            self.piece = interface.chessBoard.return_piece(self.x//100, self.y//100)

        if (self.piece == None):
            self.initialSquare = None
            return None, None

        self.square = ((str(chr((self.x//100)+97))) + str(8-(self.y//100)))       
        if self.initialSquare != None:
            move = self.getValidMove(self.piece, self.square, self.initialSquare[0], self.initialSquare[1], self.legalMoves)
            if move != None:
                fromSquare = self.initialSquare
                toSquare = self.square
                self.initialSquare = None
                self.square = None
                self.piece = None
                interface.chessBoard.change_piece(fromSquare, toSquare)
                return move, True
            else:
                self.piece = interface.chessBoard.return_piece(self.x//100, self.y//100)    

        initialMove = (7-self.y//100)*8+(self.x//100)
        self.legalMoves = [move for move in board.legal_moves if move.from_square == initialMove]
        for i in range(len(self.legalMoves)):
            self.legalMoves[i] = board.san(self.legalMoves[i])
        print(self.legalMoves)
        self.initialSquare = self.square
        self.square = None
        interface.chessBoard.return_piece(self.x//100, self.y//100)
        return None, False
        
    def getValidMove(self, piece, square, initial_file, initial_rank, legal_moves):
        possibleMoves = [
            square,
            piece + square,                           # Simple move to square
            piece + "x" + square,                     # Capture on square
            piece + initial_file + square,            # Specify file if ambiguity exists
            piece + initial_rank + square,            # Specify rank if ambiguity exists
            piece + initial_file + "x" + square,      # File disambiguation with capture
            piece + initial_rank + "x" + square,      # Rank disambiguation with capture
            piece + initial_file + initial_rank + square,          # File and rank specified
            piece + initial_file + initial_rank + "x" + square,    # Full disambiguation with capture
            piece + square + "=",                     # Promotion (additional character needed)
            piece + "x" + square + "=",               # Promotional capture (additional character needed)
            piece + square + "+",                     # Simple move with check
            piece + "x" + square + "+",                # Capture with check
            initial_file + "x" + square,
            square + "=Q",
            "O-O",
            "O-O-O"
        ]
        print(possibleMoves)
        for move in possibleMoves:
            if move in legal_moves:
                return move

        return None 