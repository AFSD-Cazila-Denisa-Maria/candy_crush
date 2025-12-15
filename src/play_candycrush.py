from board import Board
from engine import Engine
from gui import GameGUI

if __name__ == "__main__":
    board = Board()
    engine = Engine(board)
    GameGUI(engine).run()
