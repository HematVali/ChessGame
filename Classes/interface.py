import pygame
from Classes.chessBoard import ChessBoard
# from Classes.dragger import Dragger

class Interface:
    def __init__(self):
        self.chessBoard = ChessBoard()

    def showBoard(self, surface):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 ==0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)
                rect = (col * 100, row * 100, 100, 100)

                pygame.draw.rect(surface, color, rect)

    def showPieces(self, surface):
        for row in range(8):
            for col in range(8):

                if self.chessBoard.squares[row][col].has_piece():
                    piece = self.chessBoard.squares[row][col].piece
                
                    piece.set_texture(size=80)
                    img = pygame.image.load(piece.texture)
                    img_center = col * 100 + 100 // 2, row * 100 + 100 // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)