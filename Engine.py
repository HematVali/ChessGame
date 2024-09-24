import chess as ch
import random as rd

class Engine:

    def __init__(self, board, maxDepth, color):
        self.board = board
        self.color = color
        self.maxDepth = maxDepth

    def getBestMove(self):
        return self.engine(None, 1)

    def evalFunct(self):
        compt = 0
        # Sums up the material values and adds additional positional factors
        for i in range(64):
            compt += self.squareResPoints(ch.SQUARES[i])
            compt += self.pieceMobility(ch.SQUARES[i])
            compt += self.kingSafety(ch.SQUARES[i])
            compt += self.centerControl(ch.SQUARES[i])
        compt += self.mateOpportunity() + self.openning() + 0.001 * rd.random()
        return compt

    def mateOpportunity(self):
        if self.board.legal_moves.count() == 0:
            if self.board.turn == self.color:
                return -999  # Engine's side loses
            else:
                return 999  # Engine wins (opponent is mated)
        else:
            return 0

    def openning(self):
        # Give a bonus for the opening phase (first 10 moves)
        if self.board.fullmove_number < 10:
            if self.board.turn == self.color:
                return 1 / 30 * self.board.legal_moves.count()
            else:
                return -1 / 30 * self.board.legal_moves.count()
        else:
            return 0

    def squareResPoints(self, square):
        pieceValue = 0
        if self.board.piece_type_at(square) == ch.PAWN:
            pieceValue = 1
        elif self.board.piece_type_at(square) == ch.ROOK:
            pieceValue = 5.1
        elif self.board.piece_type_at(square) == ch.BISHOP:
            pieceValue = 3.33
        elif self.board.piece_type_at(square) == ch.KNIGHT:
            pieceValue = 3.2
        elif self.board.piece_type_at(square) == ch.QUEEN:
            pieceValue = 8.8

        if self.board.color_at(square) != self.color:
            return -pieceValue
        else:
            return pieceValue

    # New mobility factor: Reward pieces with more mobility
    def pieceMobility(self, square):
        piece = self.board.piece_at(square)
        if piece and piece.color == self.color:
            return 0.1 * len(list(self.board.attacks(square)))  # Reward piece mobility
        return 0

    # King safety: Penalize if the king is exposed
    def kingSafety(self, square):
        if self.board.piece_type_at(square) == ch.KING:
            # Penalize if the king is too exposed (for simplicity)
            if self.board.color_at(square) == self.color:
                king_position = self.board.king(self.color)
                return -0.2 * len(list(self.board.attackers(not self.color, king_position)))
        return 0

    # Control of the center squares (e4, d4, e5, d5)
    def centerControl(self, square):
        center_squares = [ch.E4, ch.D4, ch.E5, ch.D5]
        if square in center_squares:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.color:
                return 0.2  # Reward for controlling the center
        return 0

    # Improved engine with Quiescence Search
    def engine(self, candidate, depth):
        if depth == self.maxDepth or self.board.legal_moves.count() == 0:
            return self.evalFunct()

        moveListe = self.orderMoves(list(self.board.legal_moves))  # Ordered move list
        newCandidate = float("-inf") if depth % 2 != 0 else float("inf")

        for i in moveListe:
            self.board.push(i)
            value = self.quiescence_search(newCandidate, depth + 1) if depth == self.maxDepth else self.engine(newCandidate, depth + 1)

            if value > newCandidate and depth % 2 != 0:
                if depth == 1:
                    move = i
                newCandidate = value
            elif value < newCandidate and depth % 2 == 0:
                newCandidate = value

            if candidate is not None:
                if value < candidate and depth % 2 == 0:
                    self.board.pop()
                    break
                elif value > candidate and depth % 2 != 0:
                    self.board.pop()
                    break

            self.board.pop()

        if depth > 1:
            return newCandidate
        else:
            return move

    # Quiescence search: Extends search in tactical positions (captures)
    def quiescence_search(self, candidate, depth):
        stand_pat = self.evalFunct()
        if candidate is not None and stand_pat >= candidate:
            return stand_pat

        legal_moves = list(self.board.legal_moves)
        for move in legal_moves:
            if self.board.is_capture(move):
                self.board.push(move)
                score = -self.quiescence_search(-candidate, depth + 1)
                self.board.pop()
                if score >= candidate:
                    return score
        return stand_pat

    # Order moves to improve search efficiency (captures first)
    def orderMoves(self, legal_moves):
        captures = []
        non_captures = []
        for move in legal_moves:
            if self.board.is_capture(move):
                captures.append(move)
            else:
                non_captures.append(move)
        return captures + non_captures
