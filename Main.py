import Engine as ce
import chess as ch
import pygame
import sys
from Classes.interface import Interface
from Classes.mouse import Mouse

class Main:
    def __init__(self, board=ch.Board):
        self.board=board
        self.Interface = Interface()
        self.mouse = Mouse()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('chess')      

    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        bestMove = engine.getBestMove()
        self.board.push(bestMove)
        bestMove = str(bestMove)
        self.Interface.chessBoard.change_piece(bestMove[0]+bestMove[1],bestMove[2]+bestMove[3])

    def show(self):
        flag = False
        humanMove = None
        screen = self.screen
        Interface = self.Interface
        while (self.board.is_checkmate()==False):
            Interface.showBoard(screen)
            Interface.showPieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    humanMove, flag = self.mouse.click(event.pos, self.board, self.Interface)
                    if flag == True:
                        self.board.push_san(humanMove)
                        self.playEngineMove(2, ch.BLACK)
                        flag = False
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

newBoard= ch.Board()
game = Main(newBoard)
bruh = game.show()